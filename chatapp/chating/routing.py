from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<int:id>/', consumers.PersonalChatConsumer.as_asgi())

]

# websocket_urlpatterns = [
#     re_path(r'', consumers.ChatConsumer.as_asgi()),
# ]