from django.urls import path
from useraccount.views import user_login,user_logout,UserLoginView,SignupView,profile_view,profile_update_view

app_name='user'
urlpatterns = [
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name='logout'),
    path('register/',SignupView.as_view(),name='register'),
    path('profile/<str:username>/',profile_view, name='profile'),
    path('profile-edit/',profile_update_view,name="profile_update"),
]
