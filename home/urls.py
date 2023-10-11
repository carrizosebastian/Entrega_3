from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

app_name = "home"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home/index.html"), name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html", next_page="home:index"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
]


urlpatterns += staticfiles_urlpatterns()

