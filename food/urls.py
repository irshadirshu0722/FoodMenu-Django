
from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    #food/hallo
    path('hallo/',views.index,name="index"),
    path('',views.ListClassViews.as_view(),name="list"),

    path('detail/<int:pk>',views.detail,name="detail"),
    #add item
    path('add/',views.CreateItemClassView.as_view(),name="add-item"),
    #edit
    path('edit/<int:pk>' ,views.UpdateItemClassView.as_view(),name="edit-item"),
    #delete
    path('delete/<int:pk>' ,views.DeleteItemClassView.as_view(),name="delete-item")
]
