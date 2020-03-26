from __future__ import unicode_literals
from django.db import models
import uuid # access to uuid for generating reference id
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

User._meta.local_fields[4].__dict__['_unique'] = True
User._meta.local_fields[4].__dict__['_required'] = True

class Profile(models.Model):
	"""this class is responsible for the profile of each user in the website."""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	reference_id = models.UUIDField(max_length=50, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	class Meta:
		unique_together = ('reference_id',)

		#making reference key unique will allow each user to have his or her own key unique to him or her.
@receiver(post_save, sender=User)
def create_userprofile(sender, **kwargs):
     if kwargs['created']:
         user = Profile.objects.create(user=kwargs['instance'])
         user.save()
# Create your models here.
