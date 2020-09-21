from django.views.generic import ListView
from . models import ServicesProduct
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404


def services_product(request):
    services_prod = ServicesProduct.objects.all()
    context = {
        'services_prod': services_prod,
    }
    return render(request,'servlist.html',context)



def services_detail(request, id):

    servicesprod = get_object_or_404(ServicesProduct, id=id)
    context ={
        'servicesprod' : servicesprod,
    }
    return render(request,'servdetail.html',context)


class ServicesCreateView(CreateView):
    model = ServicesProduct
    fields = ['name','image1','image2','image3','image4','image5','description', 'price_range']
    success_url = reverse_lazy('shop:home')
    template_name = 'services-new.html'

    def get_form(self, form_class=None):
        form = super(ServicesCreateView, self).get_form(form_class)
        return form

    def get_initial(self):
        return {
            'owner': self.request.user,
        }

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ServicesCreateView, self).form_valid(form)
