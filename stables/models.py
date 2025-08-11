from django.db import models

class Horse(models.Model):
    name = models.CharField('الاسم', max_length=255)
    breed = models.CharField('السلالة', max_length=100, blank=True, null=True)
    birth_date = models.DateField('تاريخ الميلاد', blank=True, null=True)
    color = models.CharField('اللون', max_length=50, blank=True, null=True)
    photo = models.ImageField('الصورة', upload_to='horses/photos/', blank=True, null=True)

    class Meta:
        verbose_name = 'حصان'
        verbose_name_plural = 'الخيول'

    def __str__(self):
        return self.name
