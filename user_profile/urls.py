from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import ProfileDetailView, UpdateProfileView

app_name = 'user_profile'

urlpatterns = [
    path('user/', include(([
        path('<int:user_id>/', ProfileDetailView.as_view(), name='profile'),
        path('<int:user_id>/edit', UpdateProfileView.as_view(), name='update_profile'),
    ])))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
