
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include

# 使用django 能支持 http 和 websocket
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        # path('admin/', admin.site.urls),
    ])
})