from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, FormView
from django.views.generic.list import ListView
from products.forms import Reviewform
from products.models import Color, Product, ProductCategory, Review, Size
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# def ProductDetail(request):
#     return render(request, 'product-detail.html')


class Productdetailview(FormView):
    template_name = "product-detail.html"
    form_class = Reviewform
    
    def get_success_url(self):
        return reverse_lazy('product_detail', args = [self.kwargs['pk']])

    def get_object(self):
        return Product.objects.filter(id=self.kwargs['pk']).first()

    def update_view_count(self):
        obj = self.get_object()
        obj.view_count += 1
        obj.save()


    def get_context_data(self, **kwargs):
        self.update_view_count()
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'object': self.get_object(),
                'product_reviews': self.get_object().product_reviews.all(),
                'form': self.get_form,
                'product_images': self.get_object().product_image.all(),
            }
        )
        return context

    def create_review(self, **kwargs):
        product = self.get_object()
        return Review.objects.create(
            product=product,
            value_rate=kwargs.get('value_rate'),
            quality_rate=kwargs.get('quality_rate'),
            price_rate=kwargs.get('price_rate'),
            nickname=kwargs.get('nickname'),
            summary=kwargs.get('summary'),
            review=kwargs.get('review')
        )

    def form_valid(self, form):
        if form.is_valid():
            self.create_review(
                product=self.kwargs.get('pk'),
                value_rate=form.cleaned_data.get('value_rate'),
                quality_rate=form.cleaned_data.get('quality_rate'),
                price_rate=form.cleaned_data.get('price_rate'),
                nickname=form.cleaned_data.get('nickname'),
                summary=form.cleaned_data.get('summary'),
                review=form.cleaned_data.get('review')
            )
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    





class Productlistview(ListView):
    template_name = 'product-list.html'
    model = Product
    paginate_by = 5
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        return context
