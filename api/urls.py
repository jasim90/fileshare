from rest_framework import routers
from django.conf.urls import patterns, include, url
from views import UserViewSet, FileViewSet, SharedFileViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'files', FileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/$',UserViewSet.as_view(),name="userlist"),
    url(r'^files/$', FileViewSet.as_view(), name="file_list"),
    url(r'^shared/files/$', SharedFileViewSet.as_view(), name="shared_files_list")
]