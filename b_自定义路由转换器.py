from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1、定义自己的转换器
class MyRegexConverter(BaseConverter):
    def __init__(self, url_map, my_regex):
        super(MyRegexConverter, self).__init__(url_map)
        self.regex = my_regex  # 重写BaseConverter继承下来的regex这个类属性

    def to_python(self, value):
        # return "abcd"
        return value


# 2、将自定义的转换器添加到flask的应用中去
app.url_map.converters["my_re"] = MyRegexConverter  # "my_re"名字随意起


@app.route("/send/<my_re(r'1[37]\d{9}'):phone_num>")
def send_mgs(phone_num):
    return "send message to {}".format(phone_num)


# 127.0.0.1:5000/send/13512345678  可以访问，

@app.route("/login")
def login():
    # phone_num一定要与send_mgs视图函数参数名字想同
    url = url_for("send_mgs", phone_num="13512345678")
    return redirect(url)


@app.route("/goods/<int:good_id>")
def goods(good_id):
    return "hello world {}".format(good_id)


if __name__ == '__main__':
    app.run()
