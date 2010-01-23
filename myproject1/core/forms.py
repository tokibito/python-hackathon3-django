from django import forms

from models import Person, Book

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
