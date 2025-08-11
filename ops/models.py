from django.db import models

class Booking(models.Model):
    BOOKING_TYPES = [
        ('training', 'تدريب'),
        ('boarding', 'إيواء'),
        ('vet', 'بيطري'),
        ('competition', 'منافسة'),
    ]

    type = models.CharField('نوع الحجز', max_length=20, choices=BOOKING_TYPES)
    date = models.DateField('التاريخ')
    time = models.TimeField('الوقت')
    notes = models.TextField('ملاحظات', blank=True, null=True)

    class Meta:
        verbose_name = 'حجز'
        verbose_name_plural = 'الحجوزات'

    def __str__(self):
        return f"{self.get_type_display()} - {self.date}"
