from django.urls import path
from . import views

urlpatterns=[
    path('addlap/', views.AddLaptopView, name='add_lap'),
    path('showlap/', views.ShowLaptopView, name='show_lap'),
    path('update/<int:i>', views.UpdateLaptopView, name='update'),
    path('delete/<int:i>', views.DeleteLaptopView, name='delete')
]
