from django.db import models

class Policy(models.Model):
    POLICY_TYPES = (
        ('life' , ' بیمه عمر'),
        ('third_party','بیمه شخص ثالث'),
        ('health' , 'بیمه درمان '),

    )

    Policy_number = models.CharField(max_length=20, unique=True, verbose_name=" شماره بیمه نامه " )
    holder_name = models.CharField(max_length=100, verbose_name=" name bime gozar")
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES, verbose_name=" nooe bime")
    issue_date = models.DateField(verbose_name=" tarikh sodoor")
    is_active = models.BooleanField(default=True, verbose_name=" vaziat faaal boodan")


    def __str__(self):
        return f"{self.Policy_number} - {self.holder_name}"