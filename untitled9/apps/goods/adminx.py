from xadmin import  views
import xadmin
from django.forms import ModelForm
from django import forms
from  .models import *
from django.db.models import Max
from django.http import HttpResponse
from django.utils.safestring import mark_safe
# class OrderForm(ModelForm):
#     muchs = forms.IntegerField(
#         min_value=8,
#         error_messages={
#             "min_value": "用户名最长为16位",
#             "required": "用户名不能为空"
#         },)
class Shopline():
    exclude = ["bianma"]
    model=Shop
    extra=0



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)
class GlobalSettings(object):
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"

    def get_site_menu(self):
        return (
            {'title': 'ERP管理系统',
             # 'perm': self.get_model_perm(Goods, 'view'),
             'menus': (
                 {
                     'title': '会员延期',
                     'url': '/xadmin/test_view/',
                     # 'perm': self.get_model_perm(ZVipbalanceList, 'view'),
                 },
             )
             },
        )
xadmin.site.register(views.CommAdminView, GlobalSettings)

class Goodsdmin(object):
    def imgs(self,request):
        a=request.image
        return mark_safe("<a href = 'https:www.baidu.com' target='_blank'><img src=/media/" + request.image.name + " class='field_img'></a>")
    list_display=["id","good_id","user_id","add_time","imgs"]
    list_filter = ["good_id", "add_time"]

    inlines = [Shopline]
    import_excel=True
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(Goodsdmin, self).post(request, args, kwargs)

xadmin.site.register(Goods,Goodsdmin)

class Shopdmin(object):
    list_display=["good_id","color","size","shangjia_time","image","bianma"]
    list_filter = ["good_id__user_id"]
    search_fields = ["good_id__user_id"]
    exclude=["bianma"]
    show_detail_fields =["good_id"]


    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.bianma = str(obj.good_id) + str(obj.color) + str(obj.size)
        obj.save()

xadmin.site.register(Shop,Shopdmin)

class Orderdmin(object):
    list_display=["id","bianma","muchs","pici"]
    exclude = ["pici"]
    list_filter = ["bianma__bianma"]
    search_fields = ["bianma__bianma"]
    list_editable=["bianma"]

    # form=OrderForm

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        pici_new=Order.objects.filter(bianma=obj.bianma).aggregate(Max('pici'))['pici__max']
        if pici_new:
            obj.pici = pici_new + 1
        else:
            obj.pici = 1
        obj.save()
xadmin.site.register(Order,Orderdmin)
import xadmin

from .views import TestView

xadmin.site.register_view(r'test_view/$', TestView, name='for_test')