from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.generic import FormView
from django.views.generic.base import TemplateResponseMixin
from .forms import SeleniumForm

class SeleniumView(FormView,TemplateResponseMixin):
  template_name = "selenium/index.html"
  success_url = '.'
  form_class = SeleniumForm

  def get(self, request, *args, **kwargs):
    print("SeleniumView.get()")
    form = SeleniumForm(request.user)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    print("SeleniumView.post()")
    form = SeleniumForm(request.user, request.POST)
    if form.is_valid():
      form.screenshot()
      return HttpResponseRedirect(request.path)
    else:
      return render(request, self.template_name, {'form': form})
