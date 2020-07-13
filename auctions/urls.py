from django.urls import path

from . import views

urlpatterns = [
    path("",views.start,name="start"),
    path("active", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("created",views.created,name="created"),
    path("lst/<int:mk1>",views.bid,name="bid"),
    path("nx/<str:mk2>",views.bid1,name="bid1"),
    path("cmnt/<str:mm>",views.comm,name="comm"),
    path("win/<int:mk3>",views.win,name="win"),
    path("watchlist/<str:mk4>",views.watchlist,name="watchlist"),
    path("remwatchlist/<str:mkk>",views.remwatchlist,name="remwatchlist"),
    path("my",views.my,name="my"),
    path("categories",views.cate,name="cate"),
    path("lists/<str:jj>",views.lists,name="lists"),
    path("winners",views.winnerlist,name="winnerlist")
    
]
