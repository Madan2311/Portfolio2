from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombEtni


class TipoDocu(models.Model):
    NombTipo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTipo

class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombEsCi

class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiEs

class TipoLogro(models.Model):
    NombTiLo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiLo