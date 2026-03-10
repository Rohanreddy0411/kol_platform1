from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def pricing(request):
    return render(request,'pricing.html')

def explore_kols(request):
    return render(request,'explore_kols.html')

def explore_campaigns(request):
    return render(request,'explore_campaigns.html')

def forgot_password(request):
    return render(request,'forgot_password.html')


# KOL PAGES

def kol_dashboard(request):
    return render(request,'kol_dashboard.html')

def kol_profile(request):
    return render(request,'kol_profile.html')

def social_accounts(request):
    return render(request,'social_accounts.html')

def kol_collaborations(request):
    return render(request,'kol_collaborations.html')

def kol_messages(request):
    return render(request,'kol_messages.html')

def kol_wallet(request):
    return render(request,'kol_wallet.html')


# COMPANY PAGES

def company_dashboard(request):
    return render(request,'company_dashboard.html')

def create_campaign(request):
    return render(request,'create_campaign.html')

def browse_kols(request):
    return render(request,'browse_kols.html')

def company_messages(request):
    return render(request,'company_messages.html')

def company_wallet(request):
    return render(request,'company_wallet.html')

def kol_wallet(request):
    return render(request,"kol_wallet.html")

def kol_messages(request):
    return render(request,"kol_messages.html")        