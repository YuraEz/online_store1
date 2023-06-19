from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    img = models.ImageField(blank=True)
    price = models.IntegerField()
    # slug = models.SlugField(unique=True)


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    goods_list = models.ManyToManyField(to=Good)


# class GoodGroup(Group):
good_group = Group.objects.create(name='Good Group')
