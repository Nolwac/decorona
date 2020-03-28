from django.db import models
from django.urls import reverse # access to creating links that can easily be referenced as an attribute
from django.contrib.auth.models import User
from .operations import *

# Create your models here.

class Question(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	question = models.TextField()
	magnitude = models.IntegerField()
class Operation(models.Model):
	execution_choices = EXECUTION_CHOICES
	description = models.TextField()
	title = models.CharField(max_length=50, null=False, blank=False)
	execution = models.CharField(max_length=50, null=False, blank=False)
	execution_info = models.TextField()

class DecisionBox(models.Model):
	description = models.TextField()
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	questions = models.ManyToManyField(Question)
	threshold = models.IntegerField(default=1)

	@property
	def get_api_url(self):
		return reverse('test_kit_api:decision_box', kwargs={'id':self.id})

	@property	
	def get_absolute_url(self):
		return reverse('test_kit:decision_box', kwargs={'id':self.id})


	def is_threshold_true(self, value):
		if value >= self.threshold:
			return True
		else:
			return False

	def next(self, value):
		"""This method returns the next connector object in the teskit algorithm sequence after this very object if any"""
		if self.is_threshold_true(value): #testing if the threshold condition is met
			try: #trying to be sure that such connector even exist before attempting to return it
				connector = self.connector_set.filter(connector_type=True)
				return connector
			except:
				return None
		else:
			try: #trying to be sure that such connector even exist before attempting to return it
				connector = self.connector_set.filter(connector_type=False)
				return connector
			except:
				return None

	def next_absolute_url(self, value):
		"""This method returns the absolute url for the next connector object in the testkit algorithm sequence after this very object if any"""
		if self.next(): #checking if there is a next in the first place
			return self.next().get_absolute_url
		else:
			return None

	def next_api_url(self, value):
		"""This method returns the api url for the next connector object in the testkit algorithm sequence after this very object if any"""
		if self.next(): #checking if there is a next in the first place
			return self.next().get_api_url
		else:
			return None


class ConnectorToDecisionBox(models.Model):
	decision_box = models.ForeignKey(DecisionBox, null=True, on_delete=models.SET_NULL)

class Connector(models.Model):
	connector_type = models.BooleanField(default=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	connect_from = models.ForeignKey(DecisionBox, null=True, on_delete=models.SET_NULL)
	connect_to = models.OneToOneField(ConnectorToDecisionBox, null=True, on_delete=models.SET_NULL)
	operation = models.ManyToManyField(Operation)

	@property
	def get_api_url(self):
		return reverse('test_kit_api:connector', kwargs={'id':self.id})

	@property	
	def get_absolute_url(self):
		return reverse('test_kit:connector', kwargs={'id':self.id})

	@property
	def get_decision_box(self):
		return self.connect_to.decision_box
	@property
	def get_decision_box_absolute_url(self):
		if self.connect_to:
			return self.connect_to.decision_box.get_absolute_url
		else:
			return None

	@property
	def get_decision_box_api_url(self):
		if self.connect_to:
			return self.connect_to.decision_box.get_api_url
		else:
			return None


class Algorithm(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=50, null=False, blank=False)
	description = models.TextField()
	initial_decision_box = models.ForeignKey(DecisionBox, on_delete=models.CASCADE)

	@property
	def get_api_url(self):
		return reverse('test_kit_api:algorithm', kwargs={'id':self.id})

	@property	
	def get_absolute_url(self):
		return reverse('test_kit:algorithm', kwargs={'id':self.id})