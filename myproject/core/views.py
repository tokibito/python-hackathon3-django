from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template

from models import Person
from forms import PersonForm

def index(request):
    return direct_to_template(request, 'index.html')

def list_person(request):
    return direct_to_template(request, 'list.html', {
      'objects': Person.objects.all(),
      'title': Person._meta.verbose_name,
    })

def add_person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('list_person'))
    return direct_to_template(request, 'add.html', {
      'form': form,
      'title': Person._meta.verbose_name,
    })
