from django.urls import path
from django.contrib.auth import views 

from . import views
app_name = "booksystem"
urlpatterns = [
    # path("", views.Index_view.as_view()),
    path('',views.Header.as_view(),name='Index'),

    # -----------------------------------------------------------------
    #auth
    
    # path('login/', views.Login_user.as_view(), name='login'),
    # path('logout/', views.Logout_user.as_view(), name='logout'),
    # path('sign_up/', views.sign_up.as_view(), name='signup'),

    # ---------------------------------------------------------------
    # CRUD
    # path('booklist/', views.BookList.as_view(), name='book_listt'),
    # path('booklist/view-book-detail/<int:pk>/', views.BookView.as_view(), name='book_view'),
    # path('booklist/create/', views.BookCreate.as_view(), name='book_new'),
    # # path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    # path('booklist/edit-book-detail/<int:pk>/', views.BookUpdate.as_view(), name='book_edit'),
    # path('booklist/delete-book-detail/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    # -------------------------------------------------------------------------
]