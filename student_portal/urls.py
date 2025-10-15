from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root URL → registration form page
    path('', views.register_student, name='register_student'),

    # After submitting the form → success/home page
    path('success/', views.success, name='success'),
]
