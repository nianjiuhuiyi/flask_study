from flask import Flask, request

app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
def index():
    name = request.form.get("name")
    age = request.form.get("age")
    # print(request.data)
    # print(request.data.decode())  # 记得去解析出来
    print(request.headers)
    print(request.headers.get("Host"))
    print(request.method)
    return "hello name={} age={} aa={}".format(name, age, request.form.getlist("name"))


# 文件上传
@app.route("/upload", methods=["POST"])
def upload():
    img_data = request.files.get("my_pic")
    # # 方法一：
    # with open("demo.png", "wb") as fp:
    #     fp.write(img_data.read())
    # 方法二：
    img_data.save("demo1.png")
    print(img_data.filename)

    return "upload ok"


if __name__ == '__main__':
    app.run(DEBUG=True)
