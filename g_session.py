from flask import Flask

app = Flask(__name__)

# 要设置session，必须要配置一下(key的名字是固定的，值随便给的)
app.config["SECRET_KEY"] = "abcdefg_dasdw"
"""
如果不设置这行，就会得到这样的错误：RuntimeError: The session is unavailable because no secret key was set. 
"""


"""设置session"""
from flask import session
@app.route("/login")
def login():
    session["name"] = "zhnagsan"
    session["age"] = 18
    return "login success"


@app.route("/index")
def index():
    name = session.get("name")
    return "拿到的session中的值是：%s" % name


from flask import g
@app.route("/show")
def show():
    # 假设这个视图函数要调用 do_something 这个函数，同时还要传很多参数
    g.my_name = "hui"      # 这样存进去
    g.age = [18, 23]
    do_something()
    return "hello show"


def do_something():
    """假设这个函数需要show视图函数传进来很多参数，写到定义里就很繁琐"""
    name = g.my_name
    print("这就相当于传进来的参数：%s" % name)


if __name__ == '__main__':
    app.run()
