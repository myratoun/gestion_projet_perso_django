from django.urls import path
from projects.views import home
from django.contrib.auth import views

app_name = "projects"

urlpatterns = [
                  path("", home, name="home"),
                  path(
                      "login/",
                      views.LoginView.as_view(template_name='projects/login.html', redirect_authenticated_user=True),
                      name="login-page"
                  ),
                  path(
                      "logout/",
                      views.LogoutView.as_view(template_name='projects/logout.html', next_page='projects:login-page'),
                      name="logout-page"
                  )
              ]
