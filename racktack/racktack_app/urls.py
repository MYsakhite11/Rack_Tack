from django.urls import path, include

from . import views

app_name = 'racktack_app'

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('conection/', views.login_view, name="conection"),
    path('deconection/', views.logout_view, name="deconection"),
    path('inscription/', views.register_view, name="inscription"),
    path('list/<int:id>/detail/', views.detail, name="detail"),
    path('list/', views.list, name ='list'),
    path('aft/', views.aft, name="after"),
    path('<int:id>/delete', views.delete_task, name ='delete'),
    path('<int:id>/update/', views.update_task, name ='update'),
    path('register/', views.saver_task, name="saver_task")
]