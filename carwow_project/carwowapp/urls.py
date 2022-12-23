
from django.urls import path
from carwowapp import views
app_name='carwowapp'

urlpatterns = [

    path('',views.index,name="index"),
    path('cars/<int:cars_id>/',views.details,name='details'),
    path('add/',views.add_car,name='add_car'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]