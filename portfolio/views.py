from django.shortcuts import render
from .models import Photo, Category

def portfolio_view(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'portfolio/portfolio.html', context)
