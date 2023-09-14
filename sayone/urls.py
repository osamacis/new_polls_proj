from django.urls import path
from django.contrib.auth import views 

from . import views
app_name = "sayone"
urlpatterns = [
    # path("", views.Index_view.as_view()),
    path('',views.Index_view.as_view(),name='Index'),
    path("home/", views.Home_view.as_view(), name="home"),
    path('index/',views.RedirectView.as_view(url='/sayone/')),
    path('details/',views.Details_ListView.as_view(),name='details'),
    path('details/<str:slug>/',views.Details_DetailView.as_view(),name='details'),
    path('about/',views.About_templateview.as_view(),name='about'),
    path('pdf/',views.PDF_view.as_view(),name='pdf'),
    path('sendmail/',views.Send_mail.as_view(),name='sendmail'),
    # -----------------------------------------------------------------
    #auth
    
    path('login/', views.Login_user.as_view(), name='login'),
    path('logout/', views.Logout_user.as_view(), name='logout'),
    path('sign_up/', views.sign_up.as_view(), name='signup'),

    # ---------------------------------------------------------------
    # CRUD
    path('booklist/', views.BookList.as_view(), name='book_listt'),
    path('booklist/view-book-detail/<int:pk>/', views.BookView.as_view(), name='book_view'),
    path('booklist/create/', views.BookCreate.as_view(), name='book_new'),
    # path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('booklist/edit-book-detail/<int:pk>/', views.BookUpdate.as_view(), name='book_edit'),
    path('booklist/delete-book-detail/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    # -------------------------------------------------------------------------

    path('new_login/',views.New_login.as_view(), name='new_login')
]