from django.urls import path

from . import views

urlpatterns = [
path("<int:id>",views.index,name="index"),
path("home/",views.home,name="home"),
path("",views.home,name="home"),
path("create/",views.create,name="create"),
path("view/",views.show_all,name="view"),
path("deleteitem/<int:id>",views.deleteitem,name="delete_item"),
path("deleteobject/<int:id>",views.deleteobject,name="delete_object"),
path("mywishlists/",views.my_wish_list,name="mywishlists"),
]

