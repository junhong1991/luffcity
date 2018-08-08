本程序软件环境：
python 3.5.4
django 1.11.11

ORM查询语句详见app01/views.py文件
输入http://127.0.0.1:8000/app01/select/

测试路径
查看所有课程以及详细课程（示例）：
http://127.0.0.1:8000/api/course/
http://127.0.0.1:8000/api/course/1/

查看所有学位课并打印学位课名称以及授课老师
http://127.0.0.1:8000/api/v1/degreecourse/teachers/

查看所有学位课并打印学位课名称以及学位课的奖学金
http://127.0.0.1:8000/api/v1/degreecourse/scholarship/

展示所有的专题课
http://127.0.0.1:8000/api/v1/courses/special/