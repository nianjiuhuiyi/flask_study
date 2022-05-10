from flask import Flask, make_response, request

app = Flask(__name__)

"""设置cookie"""
@app.route("/set_cookie")
def set_cookie():
    # 设置cookie需要 make_response 函数来创建
    resp = make_response("成功设置cookie")
    # 设置cookie，默认是临时cookie，浏览器关闭就失效
    resp.set_cookie("my_cookie1", "a_num1")  # 前面试key，后面是value
    resp.set_cookie("my_cookie2", "a_num2")  # 可以设置多个cookie
    # max_age：设置过期时间，以秒为单位
    resp.set_cookie("new_cookie", "flask_study", max_age=3600)
    # 也可以通过这样的方式添加header
    resp.headers["Set-Cookie"] = "other_cookie=my_123; Expires=Tue, 10 May 2022 15:25:10 GMT; Max-Age=3600; Path=/"
    return resp


"""获取cookie"""
@app.route("/get_cookie")
def get_cookie():
    value = request.cookies.get("new_cookie")
    return value


"""删除cookie"""
@app.route("/delete_cookie")
def delete_cookie():
    # 也是需要 make_response 来创建
    resp = make_response("cookie 删除成功")
    # 删除cookie
    resp.delete_cookie("my_cookie1")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
