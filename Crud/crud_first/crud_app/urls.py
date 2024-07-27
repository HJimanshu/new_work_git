from django.urls import path
from .views import InsertPageView,InsertData,ShowPage,Editpage,UpdateData,DeleteData


urlpatterns = [
    # path('',cru),
    path('',InsertPageView,name='InsertPage'),
    path('insert/',InsertData,name='insert'),
    path('showpage/',ShowPage,name='showpage'),
    path('editPage/<int:pk>',Editpage,name='editPage'),
    path('update/<int:pk>',UpdateData,name='update'),
    path('delete/<int:pk>',DeleteData,name='delete'),
]