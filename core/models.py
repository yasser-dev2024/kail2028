from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField('اسم الموقع', max_length=255)
    logo = models.ImageField('الشعار', upload_to='site/logo/', blank=True, null=True)
    updated_at = models.DateTimeField('آخر تحديث', auto_now=True)

    class Meta:
        verbose_name = 'إعدادات الموقع'
        verbose_name_plural = 'إعدادات الموقع'

    def __str__(self):
        return self.site_name
