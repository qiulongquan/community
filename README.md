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

- 首先分析代码<br>
然后添加自己喜欢的功能  尽量实用化<br>

- django ImageField使用
  - 不能更新图片的原因 
  - profile = form.save(commit=False)
我推测是表格更新图片后，form里面没有跟新 cleaned_data字段 为什么form的cleaned_data字段没有更新？
所以profile里面也没有更新  数据库里面也没有更新

- 加入djcelery 功能<br>
python+django+djcelery 入门级踩坑
https://blog.csdn.net/michael_lbs/article/details/74923367