from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import SimpleRouter
from books.views import BooksView, FavoriteToggleView
from audio.views import AudioView
from genres.views import GenresView
from selections.views import SelectionsView
from users.views import RegisterUserView, LoginUserView, ProfileView
from reviews.views import ReviewCreateView

router = SimpleRouter()

router.register('books', BooksView)
router.register('audio', AudioView)
router.register('genres', GenresView)
router.register('selections', SelectionsView)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("api/", include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/jwt/register/', RegisterUserView.as_view(), name='register'),
    path('api/auth/jwt/login/', LoginUserView.as_view(), name='login'),
    path('api/favorites/toggle/', FavoriteToggleView.as_view(), name='favorite-toggle'),
    path('api/profile/', ProfileView.as_view(), name='user-profile'),
    path('api/reviews/', ReviewCreateView.as_view(), name='review_create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()