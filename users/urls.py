from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import UserProfile

urlpatterns = [
    url(r'^profile/$', login_required(UserProfile.as_view()), name="profile"),
]