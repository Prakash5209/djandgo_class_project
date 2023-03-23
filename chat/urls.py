from django.urls import path
from chat.views import message_view,message_to_user,delete_message

app_name = "chat"
urlpatterns = [
    path('messages/',message_view,name="messages"),
    path('messages/<str:username>/',message_to_user,name="message_user"),
    path('delete-message/',delete_message,name="delete_message"),
]