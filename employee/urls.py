from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<str:pk>/', views.edit_employee, name='edit-employee'),
    path('delete/<str:pk>/', views.delete_employee, name='delete-employee'),
    
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)