from django.db import models

# Create your models here.
class Proyectos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    link = models.URLField(verbose_name="Enlace del proyecto")
    img = models.ImageField(upload_to='projects/', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']
        db_table = 'proyectos'