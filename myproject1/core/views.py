from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django import forms

from models import Person, Book

class Views(object):
    default_name = ''
    
    def __init__(self, name=None, app_name=None):
        if name is None:
            self.name = self.default_name
        else:
            self.name = name
        if app_name is None:
            self.app_name = self.default_name
        else:
            self.app_name = app_name

    def get_urls(self):
        return patterns('')

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.name

class AddListViews(Views):
    def __init__(self, modelclass, template_name='', name=None, app_name=None):
        super(AddListViews, self).__init__(name, app_name)
        self.modelclass = modelclass
        self.template_name = template_name
        self.name = modelclass.__name__.lower()
        self.app_name = self.name

    def get_urls(self):
        return patterns('',
            url(r'^$', self.list_obj, name='list'),
            url(r'^add$', self.add_obj, name='add'),
        )

    def list_obj(self, request):
        return direct_to_template(request, 'list%s.html' % self.template_name, {
          'objects': self.modelclass.objects.all(),
          'title': self.modelclass._meta.verbose_name,
        })

    def make_form(self):
        class ObjectForm(forms.ModelForm):
            class Meta:
                model = self.modelclass
        return ObjectForm

    def add_obj(self, request):
        form = self.make_form()(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('%s:list' % self.name)
        return direct_to_template(request, 'add%s.html' % self.template_name, {
          'form': form,
          'title': self.modelclass._meta.verbose_name,
        })

def index(request):
    return direct_to_template(request, 'index.html')
