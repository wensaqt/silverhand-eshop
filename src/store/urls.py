from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import CustomLoginView, CustomLogoutView, SignUpView

urlpatterns = [
    path('', home, name="home"),
    path('best-sellers/', best_sellers, name="best_sellers"),
    path('categories/', categories, name="categories"),
    path('collections/', collections, name="collections"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

# Serve les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)