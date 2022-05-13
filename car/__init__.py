from flask import Blueprint

app_car = Blueprint("app_car", __name__,
                    # 这个的默认值是空，必须要指定
                    template_folder="templates",
                    )

# 要把这个视图函数导进来，让代码看到，不然视图函数get_car就没出现，也没被导包什么的
from .views import get_car     # 一定要写成 .view 点代表这个包，不加的话会报找不到views这个包
