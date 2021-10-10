from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

# Create your views here.
def index(request):

    # home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profile = Profile.objects.filter(about=about)

    # skills
    categories = Category.objects.all()

    # Portfolios
    portfolios = Portfolio.objects.all()


    context = {
        'home': home,
        'about':about,
        'profile':profile,
        'categories': categories,
        'portfolios' : portfolios,
        
        }

    

    return render(request, 'index.html',context)