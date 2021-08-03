from django.db import models
from lib.models import BaseModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(BaseModel):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='phone number', max_length=11, null=True, blank=True)
    bio = models.TextField(verbose_name='bio', max_length=200, null=True, blank=True)
    avatar = models.ImageField(verbose_name='avatar', upload_to='images/account/user_avatar/', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True, blank=True)
    gender = models.CharField(verbose_name='gender', max_length=6, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profile'


def save_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile(user=kwargs['instance'])
        profile.save()


post_save.connect(save_profile, sender=User)
