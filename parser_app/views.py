from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import generic


class KnigoGidListView(generic.ListView):
    template_name = "parser/knigogid_list.html"
    context_object_name = "knigogid"
    model = models.KnigoGid
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
        
        
class KnigoGidFormView(generic.FormView):
    template_name = "parser/knigogid_form.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()  # Исправлено: вызов правильного метода
            return HttpResponse("STATUS 200")
        else:
            return super(KnigoGidFormView, self).post(request, *args, **kwargs)

