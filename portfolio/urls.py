from django.urls import path
from .views import portfolio_view, category_photos

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('category/<int:category_id>/', category_photos, name='category_photos'),
]