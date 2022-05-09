from flask import Flask, redirect, url_for

# __name__ 表示当前的模块名字(就是当前py文件),flask以这个模块所在的目录为根目录
#   在这个文件执行的， 那么 __name__ == "__main__"  如果是其它模块导进来的，__name__的值就是其所在py文件的名字

# app = Flask(__name__,
#             static_url_path="/python",  # 同Django中的STATIC_URL，指定访问静态资源的url前缀，默认值是static
#             static_folder="static",   # 静态文件的目录，默认就是static
#             template_folder="templates"  # 模板文件的目录，默认就是templates
#             )

app = Flask(__name__)


# 1、从文件中导入配置文件
# app.config.from_pyfile("settings.py")
# app.config.from_pyfile("config.cfg")  # 文件什么后缀不重要，都是一样的结果


# 2、使用类对象配置参数
class MyConfig(object):
    DEBUG = True  # 把需要配置的参数都写成类属性
    My_IP = "127.0.0.1"  # 这样好像有些问题，以后用到再说吧


# app.config.from_object(MyConfig)


# 3、把app.config理解为一个字典，然后配置参数比较少的时候，可以直接新增
app.config["DEBUG"] = True


# app.config["My_IP"] = "127.0.0.123"


# 读取配置文件
# 所以如果配置文件中写了一个自己要的参数而不是Flask使用的话，可以直接  app.config.get("my_key") 拿到值
# print(app.config.get("My_IP"))

# # 教程里写，如果在别的模块里没有app这个对象，如果要获取参数呢
# from flask import current_app  # 这个current_app就相当于是app的引用吧，这么理解
# print(current_app.config.get("DEBUG"))


@app.route("/", methods=["POST", "GET"])
def index():
    return "hello.html"


@app.route("/login")
def login():
    # 使用uel_for函数，通过视图名字(这里是index)找到UI应的url路径
    url = url_for("index")
    return redirect(url)
    # return redirect("https://www.baidu.com/")    # 重定向，这就写死了


if __name__ == '__main__':
    print(app.url_map)  # 查看所有路由
    app.run()
