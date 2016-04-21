from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class UserProfile(View):
	template_name = "profile.html"

	def get(self, request):
		return render(request, self.template_name)