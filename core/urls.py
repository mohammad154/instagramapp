from django.urls import path
from . import views
from . import searcher

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.Login.as_view(), name="login"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('home/', views.Home.as_view(), name="home"),
    path('logout/', views.logout_user, name="logout"),

    path('like_post/', views.like_post, name="like_post"),
    path('remove_like/', views.remove_like, name="remove_like"),

    path('profilepage/<int:personid>/', views.profile, name="profile"),

    # profile updates
    path('update/pic/', views.pic_update, name="update-pic"),
    path('update/profession/', views.pro_update, name="update-pro"),
    path('update/bio/', views.bio_update, name="update-bio"),
    path('update/city-country/', views.cc_update, name="update-cc"),

    # commenting
    path('showcomments/', views.show_comments, name="showcomments"),
    path('addcomment/', views.add_comment, name="addcomment"),
    # follow-unfollow
    path('follow/', views.follow, name="follow"),
    path('unfollow/', views.unfollow, name="unfollow"),

    # searching
    path('search/', searcher.Searcher.as_view(), name="search"),

    # liked
    path('liked/', searcher.liked_page, name="liked"),

    # delete post
    path('delete/<int:postid>/', searcher.delete_post, name="deletepost"),

]
