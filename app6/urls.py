from django.urls import path
from . import views
app_name='app6'
urlpatterns = [
    path('hello',views.hello,name='index'),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('showusers',views.showusers,name='showusers'),
    path('logout',views.logout,name='logout'),
    path('image',views.image,name='image'),
    path('showimages',views.showimages,name='showimages'),
]
    




