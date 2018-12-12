from django.shortcuts import render
from xadmin.views import CommAdminView, BaseAdminView
# Create your views here.
class TestView(CommAdminView):
    def get(self, request):
        context = super().get_context()
        title = "会员延期"
        context["title"] = title
        return render(request, 'login.html', context)