"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from req import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/', views.base, name='base'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    # Password reset url's
    # path('password-reset/', auth_views.password_reset, name="password_reset"),
    # path('password-reset/done/', auth_views.password_reset_done, name="password_reset_done"),
    # path('password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/', auth_views.password_reset_confirm, name="password_reset_confirm"),
    # path('password-reset/complete/', auth_views.password_reset_complete, name="password_reset_complete"),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 4 views для сброса пароля:

# - password_reset отправляет почту
# - password_reset_done показывает сообщение об успехе для вышеупомянутого
# - password_reset_confirm проверяет ссылку
# запрашивает новый пароль
# - password_reset_complete показывает сообщение об успехе для вышеупомянутого
