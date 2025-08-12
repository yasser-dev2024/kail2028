from django.db import models

class Horse(models.Model):
    name = models.CharField('الاسم', max_length=255)
    breed = models.CharField('السلالة', max_length=100, blank=True, null=True)
    birth_date = models.DateField('تاريخ الميلاد', blank=True, null=True)
    color = models.CharField('اللون', max_length=50, blank=True, null=True)
    photo = models.ImageField('الصورة', upload_to='horses/photos/', blank=True, null=True)

    # الحقول الجديدة
    contact_phone = models.CharField('رقم التواصل', max_length=30, blank=True, null=True)
    price = models.DecimalField('السعر (ريال)', max_digits=10, decimal_places=2, blank=True, null=True)
    specs = models.TextField('المواصفات', blank=True, null=True)
    location = models.CharField('الموقع', max_length=120, blank=True, null=True)

    class Meta:
        verbose_name = 'حصان'
        verbose_name_plural = 'الخيول'

    def __str__(self):
        return self.name
