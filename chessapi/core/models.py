from django.db import models


# only one of this model can be created
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)


    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj