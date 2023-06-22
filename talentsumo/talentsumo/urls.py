from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_note/', views.create_note, name='create_note'),
    path('view_note/<int:note_id>/', views.view_note, name='view_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('share_note/<int:note_id>/', views.share_note, name='share_note'),
    path('accounts/profile/', views.profile, name='profile'),
    path('view_all_notes/', views.view_all_notes, name='view_all_notes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
