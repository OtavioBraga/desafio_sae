from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


from .models import Purchase


# Mixins-----------------------------------------------------------------------
class UserObjectsMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
# -----------------------------------------------------------------------------


# Views------------------------------------------------------------------------
class ListPurchasesView(LoginRequiredMixin, generic.ListView):
    template_name = 'list_purchases.html'
    context_object_name = 'purchases'
    model = Purchase
    paginate_by = 20
