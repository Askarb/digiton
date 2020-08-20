from django.views.generic import CreateView, TemplateView
from .forms import RequestMCreateForm
from .models import RequestM


class IndexView(CreateView):
    template_name = 'index.html'
    model = RequestM
    form_class = RequestMCreateForm

    def get_success_url(self):
        return "/"
