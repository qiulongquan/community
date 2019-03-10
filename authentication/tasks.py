# coding=utf-8
from celery import task


@task  #appname为当前app注册的名字
def celery_test():
    print('------- celery_test--------')


# # coding=utf-8
# from celery import app
#
# @app.task
# def test(sss):
#     f = open('/celery/a.txt','a+')
#     f.write(sss)
#     f.close()
#
# if __name__=="__main__":
#     test('bas')


