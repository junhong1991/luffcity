import json
import redis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
# from rest_framework.parsers import JSONParser
from django.conf import settings

from api import models
from api.utils.response import BaseResponse

CONN = redis.Redis(host='192.168.37.131', port=6379)
USER_ID = 1


class ShoppingCarView(ViewSetMixin, APIView):
    # parser_classes = [JSONParser, ]

    def list(self, request, *args, **kwargs):
        """
        查看购物车信息
        """
        ret = {'code': 10000, 'data': None, 'error': None}
        try:
            shopping_car_course_list = []
            pattern = 'shopping_car_%s_*' % (USER_ID,)
            user_key_list = CONN.keys(pattern)
            for key in user_key_list:
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8')),
                }
                shopping_car_course_list.append(temp)
            ret['data'] = shopping_car_course_list
        except Exception as e:
            ret['code'] = 10005
            ret['error'] = '获取购物车数据失败'
        # print(user_key_list)
        return Response(ret)

    def create(self, request, *args, **kwargs):
        """
        1. 接受用户选中的课程ID和价格策略ID
        2. 判断合法性
            - 课程是否存在？
            - 价格策略是否合法？
        3. 把商品和价格策略信息放入购物车 SHOPPING_CAR
        """
        course_id = request.data.get('coursed')
        policy_id = request.data.get('policyid')
        # 课程是否存在？
        course = models.Course.objects.filter(id=course_id, status=0).first()
        if not course:
            return Response({'code': 10001, 'error': '课程不存在'})
        # 价格策略是否合法？
        price_policy_queryset = course.price_policy.all()
        price_policy_dict = {}
        for item in price_policy_queryset:
            temp = {
                'id': item.id,
                'price': item.price,
                'valid_period': item.valid_period,
                'valid_period_display': item.get_valid_period_display()
            }
            price_policy_dict[item.id] = temp
        if policy_id not in price_policy_dict:
            return Response({'code': 10002, 'error': '傻x，价格策略别瞎改'})
        # print(price_policy_dict)
        # 把商品和价格策略信息加入购物车SHOPPING_CAR
        """
        shopping_car_2_3: {
            id: 课程ID
            name: 课程名称
            img: 课程图片
            default: 默认选中的价格策略
            price_list: 所有价格策略
        }
        """
        # CONN.flushall()
        pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*',)
        keys = CONN.keys(pattern)
        if keys and len(keys) >= 1000:
            return Response({'code': 10009, 'error': '购物车东西太多，先去结算再进行购买...'})
        key = 'shopping_car_%s_%s' % (USER_ID, course_id)
        CONN.hset(key, 'id', course_id)
        CONN.hset(key, 'name', course.name)
        CONN.hset(key, 'img', course.course_img)
        CONN.hset(key, 'default_price_id', policy_id)
        CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))
        # print(CONN.hget('shopping_car_1_1', 'id').decode('utf-8'))
        # print(CONN.hget('shopping_car_1_1', 'name').decode('utf-8'))
        # print(CONN.hget('shopping_car_1_1', 'img').decode('utf-8'))
        # print(CONN.hget('shopping_car_1_1', 'default_price_id').decode('utf-8'))
        # print(json.loads(CONN.hget('shopping_car_1_1', 'price_policy_dict').decode('utf-8')))
        # print('要加入购物车了...', request.data)
        return Response({'code': 10000, 'data': '购买成功'})

    def destroy(self, request, *args, **kwargs):
        """
        删除购物车中的课程
        """
        response = BaseResponse()
        try:
            courseid = request.GET.get('courseid')
            print('要删除的课程ID', courseid)
            key = 'shopping_car_%s_%s' % (USER_ID, courseid)
            CONN.delete(key)
            response.data = '删除成功'
        except Exception as e:
            response.code = 10006
            response.error = '删除失败'
        return Response(response.dict)

    def update(self, request, *args, **kwargs):
        """
        修改用户选中的价格策略
        1. 获取课程ID、要修改的价格策略ID
        2. 校验合法性
        """
        response = BaseResponse()
        try:
            course_id = request.data.get('coursed')
            policy_id = str(request.data.get('policyid')) if request.data.get('policyid') else None
            key = 'shopping_car_%s_%s' % (USER_ID, course_id)
            if not CONN.exists(key):
                response.code = 10007
                response.error = '该课程不存在'
                return Response(response.dict)
            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            if policy_id not in price_policy_dict:
                response.code = 10008
                response.error = '价格策略不存在'
                return Response(response.dict)
            CONN.hset(key, 'default_price_id', policy_id)
            response.date = '修改成功'
        except Exception as e:
            response.code = 10009
            response.error = '修改失败'
        return Response(response.dict)
