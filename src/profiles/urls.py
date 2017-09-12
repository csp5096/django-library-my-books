from django.conf.urls import url
from django.views.generic import TemplateView
from profiles import views

urlpatterns = [
    url(r'^profile/$', TemplateView.as_view ( template_name="profile" )),
]
