from django.shortcuts import render, get_object_or_404
from .models import Photo, Category

def portfolio_view(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'portfolio/portfolio.html', context)


def category_photos(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    photos = Photo.objects.filter(category=category)
    context = {
        'category': category,
        'photos': photos,
    }
    return render(request, 'portfolio/category_photos.html', context)