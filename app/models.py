from django.db import models
import uuid
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from user.models import CustomUser


class BigDepartment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False, unique=False)
    description = models.TextField()
    image = models.ImageField(upload_to='media/big_department', blank=True, null=True)

    def __str__(self):
        return f"{self.name} -- {self.user.username}"

    def get_units(self):
        return self.unit_set.all()


class Unit(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    department = models.ForeignKey(BigDepartment, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False, unique=False)
    description = models.TextField()
    image = models.ImageField(upload_to='media/big_department', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return f"{self.title} - from - {self.department}"


class Vocabulary(models.Model):
    TYPE = [
        ('WORD', 'Word'),
        ('PHRASE', 'Phrase'),
    ]
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=150, blank=False, null=False)
    title_uz = models.CharField(max_length=150, blank=False, null=False)
    type = models.CharField(choices=TYPE, max_length=10)
    definition = models.TextField(blank=True, null=True)
    audiofile = models.FileField(blank=True, null=True, upload_to='vocabulary/audio')

    def __str__(self):
        return f"{self.title_en} - to - {self.title_uz}"
