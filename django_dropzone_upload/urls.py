from django.conf.urls import url
from fileupload.views import PictureCreateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', PictureCreateView.as_view(), name='home'),
#    url(r'^admin/', include(admin.site.urls)),
]
