from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Basket
from .forms import BasketForm


class CreateBasketView(generic.CreateView):
    template_name = "basket/create_basket.html"
    form_class = BasketForm
    success_url = '/basket/' 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


@method_decorator(cache_page(60 * 15), name='dispatch') 
class BasketListView(generic.ListView):
    template_name = "basket/basket_list.html"
    context_object_name = "basket_list" 
    
    def get_queryset(self):
        basket = cache.get("basket")
        if not basket:
            basket = Basket.objects.all().order_by('-id')
            cache.set("basket", basket, 60 * 15) 
        return basket


class BasketDetailView(generic.DetailView):
    template_name = "basket/basket_detail.html"
    context_object_name = "basket"

    def get_object(self):
        basket_id = self.kwargs.get("id")
        return get_object_or_404(Basket, id=basket_id)


class UpdateBasketView(generic.UpdateView):
    template_name = "basket/update_basket.html"
    form_class = BasketForm
    success_url = '/basket/' 

    def get_object(self):
        basket_id = self.kwargs.get("id")
        return get_object_or_404(Basket, id=basket_id)


class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket/'  

    def get_object(self):
        basket_id = self.kwargs.get("id")
        return get_object_or_404(Basket, id=basket_id)


def clear_cache(sender, **kwargs):
    cache.delete("basket")