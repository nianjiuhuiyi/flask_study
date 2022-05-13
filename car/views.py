from . import app_car   # 注意这个写法,.好像就代表这个包，那就代表__init__.py
from flask import render_template

@app_car.route("get_car")
def get_car():
    return render_template("123.html")
