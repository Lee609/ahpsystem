# Welcome

> 本案例使用的环境：Ubuntu18.0.4 + python3.7.1
>
> 建议使用python虚拟环境，方便自我管理

## 安装

 进入Terminal，输入`git clone git://github.com/Lee609/ahpsystem.git`就可以把clone到你的电脑了

## 运行

> 本案例是在env虚拟环境上跑的，输入`. env/bin/activate`以激活环境

使用*PyCharm*打开此项目，相关库如下

```python
Click==7.0
Flask==1.1.1
Flask-Login==0.4.1
Flask-SQLAlchemy==2.4.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
numpy==1.18.1
python-dotenv==0.10.3
SQLAlchemy==1.3.12
Werkzeug==0.16.0
```

输入`pip install -r requirements.txt`即可配置好这些库

**一切环境配置好后**

进入Terminal输入`flask run`，并进入浏览器输入`127.0.0.1:5000`就可以运行起来了
