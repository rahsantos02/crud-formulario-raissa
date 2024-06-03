"""
URL configuration for projeto_receita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from receitas_app.views import home, cadastrar_receita, create, view, minhas_receitas



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastrar_receita/', cadastrar_receita, name='cadastrar_receita'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('minhas_receitas/', minhas_receitas, name='minhas_receitas')
]
