from flask import Flask, render_template
from car import app_car

app = Flask(__name__)

# 3、注册蓝图路由
app.register_blueprint(app_car, url_prefix="/car")  # 这里的前缀自己随意写


@app.route("/index")
def index():
    return render_template("index.html")

print(app.url_map)
if __name__ == '__main__':
    # app.run(host="192.168.108.147", port=5000, debug=False)
    app.run(host="0.0.0.0", port=5001, debug=False)
