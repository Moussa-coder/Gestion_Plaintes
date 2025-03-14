
from django.urls import path
from problemes_urbains import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 
    path('', views.home, name='home'),  
    path('liste-problemes/', views.liste_problemes, name='liste_problemes'),
    path('problemes/<int:probleme_id>/', views.detail_probleme, name='detail_probleme'),  # Détail d'un problème
    path('signaler/', views.signaler_probleme, name='signaler_probleme'),  
     path('nouveau_probleme/', views.nouveau_probleme, name='nouveau_probleme'),
     path('traitement_probleme/',views.traitement_probleme,name='traitement_probleme'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
