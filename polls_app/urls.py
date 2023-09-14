from django.urls import path

from . import views
app_name = "polls_app"
urlpatterns = [
    path("", views.index, name="index"),
    # path("sayone/", views.redirect_to_sayone, name="sayone"),
    # ex: /polls/5/
    # path('sign_up/',views.SighUp, name = 'signup'),
    path('company/',views.company, name = 'company'),
    # path('logout/',views.logout_user, name = 'logout'),
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/\d4+/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]