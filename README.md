### 这个是一个采用python+django框架的社区提问回答系统

- 实现功能有:
  - 提问
  - 回答
  - 站内搜索
  - 新用户注册
  - 登录 退出
  - 修改注册用户信息

- 本地环境下已经可以运行程序<br>
数据库采用的aws的rds

- 首先分析代码   ok<br>
然后添加自己喜欢的功能  尽量实用化<br>

- django ImageField使用
  - 不能更新图片的原因 
  - profile = form.save(commit=False)
我推测是表格更新图片后，form里面没有跟新 cleaned_data字段 为什么form的cleaned_data字段没有更新？
所以profile里面也没有更新  数据库里面也没有更新
  - 为什么上传文件的表单需要设置enctype="multipart/form-data"
  - https://blog.csdn.net/mazhibinit/article/details/49667511
  - 已经解决
```  
            {#enctype="multipart/form-data"文件编码方式，必须设置，否则文件无法上传#}
            <form method="post" enctype="multipart/form-data">
```
 - 加入djcelery 功能<br>
python+django+djcelery 入门级踩坑
https://blog.csdn.net/michael_lbs/article/details/74923367
djcelery（django、celery）实现定时任务
https://blog.csdn.net/weixin_33127753/article/details/84836885
  - 已经解决
    - 基本功能实现
	- 先安装celery 然后安装redis（2.10）版本，不要安装高版本会有问题。
	- 然后安装redis-server  3.2.100
	- https://github.com/MicrosoftArchive/redis/releases
	- 安装方法参考下面的链接
	- http://www.runoob.com/redis/redis-install.html
	- 然后就是settings里面的设定
	- 最后是建立tasks.py文件 里面写需要执行的程序任务
	- celery beat会把新增的task加入到数据库的periodictask表里面，如果没有新增的task可以不启动celery beat。
	- celery worker会按照预定好的时间定期执行periodictask表中的task任务。需要一直打开。
	- redis-server是不能关闭的要一直打开。
  