from django.contrib      import admin
from django.contrib.auth import views as auth_views
from django.urls         import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    # Includes
    path('producto/', include('apps.productos.urls'))
]



