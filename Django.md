# Django

## cookie

```python
from django.shortcuts import render,redirect
from functools import wraps
# Create your views here.
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="s10nb")
        if ret == "1":
            # 已经登陆过的 继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            # 获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/login/?next={}".format(next_url))
    return inner
def  login(request):
    if request.method == "POST":
        user =request.POST.get("user")
        pwd=request.POST.get("pwd")

        next_url = request.GET.get("next")
        if next_url:
            rep = redirect(next_url)  # 得到一个响应对象
        else:
            rep = redirect("/index/")  # 得到一个响应对象
            rep.set_signed_cookie("is_login","1",salt="s10nb")
            return rep
    return  render(request,"login.html")
@check_login
def  home(request):
    return  render(request,"home.html")
@check_login
def index(request):
    return  render(request,"index.html")
# 在form表单  action=‘’ 当前路径  或者 action=｛｛request.get_full_path｝｝
```