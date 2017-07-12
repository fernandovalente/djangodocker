from django.conf.urls import url
from django.contrib import admin

from tmp import views as tmp_vw

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tmp/$', tmp_vw.test_vw),
]
