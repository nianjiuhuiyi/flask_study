from flask import Flask

app = Flask(__name__)

from flask import abort, Response
@app.route("/index")
def index():
    if True:
        abort(400)
        # resp = Response("登陆失败！")
        # abort(resp)
    return "login success"

@app.errorhandler(400)     # 重写其它标准页面，就把对应的状态码放这里
def my_error_hand(err):  # 一定要接受一个参数，里面是错误信息，可以不用
    return "这是我的400错误：%s" % err


if __name__ == '__main__':
    app.run()

