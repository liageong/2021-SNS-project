from django.urls import path
from django.urls.conf import include
from main.views import *

app_name="main"
urlpatterns=[
    path('',showmain, name="showmain"),
    path('first/',first, name="first"),
    path('second/',second, name="second"),
    path('<str:id>',detail, name="detail"),
    path('new/',new,name="new"),
    path('create/',create, name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    path('<str:blog_id>/create_comment', create_comment, name="create_comment"),
    path('cdelete/<str:id>',cdelete,name="cdelete"),
    path('cedit/<str:id>',cedit,name="cedit"),
    path('cupdate/<str:id>',cupdate,name="cupdate"),
    
]
