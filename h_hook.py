from flask import Flask, request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/index")
def index():
    print("index视图函数运行！")
    print("path: ", request.path)
    print("url: ", request.url)
    return "hello world!"

from flask import request, url_for
@app.before_first_request
def my_first_handle():
    print("第一次")

@app.before_request
def my_before_handle():
    print("视图函数处理前运行")


@app.after_request
def my_after_handle(resp):
    print("视图函数正常运行后，这里执行（有异常就不会执行）")
    return resp

"""注意后面这两个需要一个参数，这个参数内容就是上一个处理完返回的内容"""

@app.teardown_request
def my_teardown_handle(resp):
    print("每次请求完后，即便有未处理的异常抛出，这也会执行")
    return resp


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
