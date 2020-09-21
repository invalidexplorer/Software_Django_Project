from django.views.generic import ListView
from . models import Tendorsmod,Applypdf
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .forms import ApplyForm
def TendorListView(request):

    tendorsmod = Tendorsmod.objects.all()
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('tendor_list')
    else:
        form = ApplyForm()

    context={
        'form':form,
        'tendorsmod':tendorsmod,
    }
    return render(request,'Tendors_list.html',context)


class TendorCreateView(CreateView):
    model = Tendorsmod
    fields = ['requirements','body','description_pdf']
    success_url = reverse_lazy('shop:home')
    template_name = 'Tendors_new.html'

    def get_form(self, form_class=None):
        form = super(TendorCreateView, self).get_form(form_class)
        return form

    def get_initial(self):
        return {
            'author': self.request.user,
        }

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TendorCreateView, self).form_valid(form)
