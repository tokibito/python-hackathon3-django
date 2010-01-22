# coding:utf-8
from django.db import models

class Person(models.Model):
    first_name = models.CharField(u'名', max_length=20)
    last_name = models.CharField(u'姓', max_length=20)

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)

class Book(models.Model):
    title = models.CharField(u'タイトル', max_length=50)
    author = models.ForeignKey(Person)

    def __unicode__(self):
        return self.title
