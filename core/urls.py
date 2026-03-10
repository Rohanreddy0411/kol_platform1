from django.urls import path
from . import views

urlpatterns = [

# PUBLIC PAGES
path('', views.home),
path('login/', views.login),
path('register/', views.register),
path('about/', views.about),
path('pricing/', views.pricing),
path('explore-kols/', views.explore_kols),
path('explore-campaigns/', views.explore_campaigns),
path('forgot-password/', views.forgot_password),

# KOL
path('kol/dashboard/', views.kol_dashboard),
path('kol/profile/', views.kol_profile),
path('kol/social-accounts/', views.social_accounts),
path('kol/collaborations/', views.kol_collaborations),
path('kol/messages/', views.kol_messages),
path('kol/wallet/', views.kol_wallet),

# COMPANY
path('company/dashboard/', views.company_dashboard),
path('company/create-campaign/', views.create_campaign),
path('company/kols/', views.browse_kols),
path('company/messages/', views.company_messages),
path('company/wallet/', views.company_wallet),

]