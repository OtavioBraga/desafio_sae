from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Purchase, Product, Task
from .forms import NewProductForm, NewPurchaseForm


# Mixins-----------------------------------------------------------------------
class UserObjectsMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
# -----------------------------------------------------------------------------


# Views------------------------------------------------------------------------
class ListPurchasesView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'list_purchases.html'
    context_object_name = 'purchases'
    model = Purchase
    paginate_by = 12


class ListProductsView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'list_products.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 30


class NewProductView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    template_name = 'new_product.html'
    success_url = '/manage/products/'
    form_class = NewProductForm


class NewPurchaseView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    template_name = 'new_purchase.html'
    success_url = '/manage/purchases/'
    form_class = NewPurchaseForm

    def get_initial(self):
        return {'product': self.kwargs['pk']}


class TasksView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name = 'list_tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context