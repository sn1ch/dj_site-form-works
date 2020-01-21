from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()
    context = {
        'product_list': products,
    }
    return render(request, template, context)


class ProductView(View):
    def get(self, request, pk):
        template = 'app/product_detail.html'
        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product=product)
        form = ReviewForm
        context = {
            'form': form,
            'product': product,
            'reviews': reviews
        }
        return render(request, template, context)

    def post(self, request, pk):
        template = 'app/product_detail.html'
        product = get_object_or_404(Product, id=pk)
        form = ReviewForm
        context = {
            'form': form,
            'product': product,
            'is_review_exist': False
        }

        if 'reviewed_products' not in request.session.keys():
            request.session['reviewed_products'] = []

        if pk not in request.session['reviewed_products']:
            request.session['reviewed_products'].append(pk)
            print(request.session['reviewed_products'])
            text = request.POST.get('text')
            Review.objects.create(text=text, product=product)
            request.session.modified = True
            context['is_review_exist'] = True
        else:
            context['is_review_exist'] = True

        reviews = Review.objects.filter(product=product)
        context['reviews'] = reviews
        return render(request, template, context)
