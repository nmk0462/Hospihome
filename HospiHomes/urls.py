from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("login1",views.login_view1,name="login1"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register1",views.register1,name="register1"),
    path("reg",views.reg,name="reg"),
    path("go",views.go,name="go"),
    path("srh",views.srh,name="srh"),
    path("hosp/<str:nm>",views.hosp,name="hosp"),
    path("update",views.update,name="update"),
    path("list1/<str:mn>",views.list1,name="list1"),
    path("appoint/<str:re>",views.appoint,name="appoint"),
    path("apsub/<str:re>",views.apsub,name="apsub"),
    path("check",views.check,name="check"),
    path("approved/<int:num>",views.approved,name="approved"),
    path("your",views.your,name="your"),
    path("back",views.back,name="back"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("rate/<str:mk>",views.rating,name="rate")
]