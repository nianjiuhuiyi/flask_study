from flask import Flask, make_response

app = Flask(__name__)

@app.route("/index")
def index():
    # 第一种：
    #       返回的数据    状态码，可以自己写      后面这是返回到header中的响应头(2种写法)
    # return "index page", 200, [("name", "zhangsan"), ("age", 18)]
    # return "index page", 400, {"name": "zhangsan", "age": 19}
    # return "index page", 600   # 甚至返回一个非标准的http状态码 （响应头、状态码都可以不要）
    # return "index page", "600 my_status", {"name": "zhangsan", "age": 19}  # 状态码加注释

    # 第二种：
    resp = make_response("index page 2")
    resp.status_code = "999 rand_my_status"
    resp.headers["city"] = "sc"


"""返回json数据集格式"""
import json
from flask import jsonify
@app.route("/login")
def login():
    data = dict(
        name="zhangsan",
        age=18
    )
    # 第一种，直接返回json的字符串
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}  # 好像一定需要后面这个header的设定

    # 第二种：jsonify （用这个）
    return jsonify(data)   # 这个会自动帮我们设定"Content-Type"这个header
    # 或者 return jsonify(name="zhangsna", age=18)  # 直接以关键字参数传进去也行



if __name__ == '__main__':
    app.run()

