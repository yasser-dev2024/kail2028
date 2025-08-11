from django.db import models

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('draft', 'مسودة'),
        ('unpaid', 'غير مدفوعة'),
        ('paid', 'مدفوعة'),
        ('cancelled', 'ملغاة'),
    ]

    invoice_number = models.CharField('رقم الفاتورة', max_length=50, unique=True)
    issue_date = models.DateField('تاريخ الإصدار')
    due_date = models.DateField('تاريخ الاستحقاق')
    status = models.CharField('الحالة', max_length=20, choices=STATUS_CHOICES, default='draft')
    total_amount = models.DecimalField('الإجمالي', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'فاتورة'
        verbose_name_plural = 'الفواتير'

    def __str__(self):
        return self.invoice_number
