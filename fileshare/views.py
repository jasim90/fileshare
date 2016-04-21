from django.shortcuts import render
from django.views.generic import View


class Login(View):
    template_name = "login.html"

    def get(self, request):
    	return render(request, self.template_name)
