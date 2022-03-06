
from django.urls import path

from . import views

urlpatterns = [
    # urls padrao
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("following", views.following, name="following"),

    # essas urls sao mais detalhadas 
    path("profile/<str:owner>", views.profile, name="profile"),

    # like e deslike
    path("edit/<str:post_id>", views.edit, name="edit"), 
    path("like/<str:post_id>", views.like, name="like")
]
