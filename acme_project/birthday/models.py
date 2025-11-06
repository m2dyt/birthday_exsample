from django.db import models
from .validators import real_age
from django.urls import reverse

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,)) 
    image = models.ImageField('Фото', blank=True, upload_to='birthdays_images')


    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
    
    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})
    
