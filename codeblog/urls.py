from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addpost/', views.AddCode, name='add'),
    path('addcontent/<str:post>', views.addCodeContent, name="content"),
    path('viewpost/<str:pk>', views.ViewPost, name="view"),
    path('editpost/<str:pk>', views.EditPost, name="edit"),
    path('deletepost/<str:pk>', views.DeletePost, name='delete'),
    path('genrepage/', views.GenrePage, name='genrepage')
]