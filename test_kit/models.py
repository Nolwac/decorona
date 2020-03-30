from django.db import models
from django.urls import reverse # access to creating links that can easily be referenced as an attribute
from django.contrib.auth.models import User
from .operations import EXECUTION_CHOICES, EXECUTION_DEFINITIONS
import json

# Create your models here.

class Algorithm(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=50, null=False, blank=False)
	description = models.TextField()

	@property
	def get_api_url(self):
		return reverse('test_kit_api:algorithm', kwargs={'id':self.id})

	@property	
	def get_absolute_url(self):
		return reverse('test_kit:algorithm', kwargs={'id':self.id})

class Question(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	question = models.TextField()
	magnitude = models.IntegerField()

class DecisionBox(models.Model):
	description = models.TextField()
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	questions = models.ManyToManyField(Question)
	threshold = models.IntegerField(default=1)
	algorithm = models.ForeignKey(Algorithm, null=False, on_delete=models.CASCADE)

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
				connector = self.connector_set.get(connector_type=True)
				return connector
			except:
				return None
		else:
			try: #trying to be sure that such connector even exist before attempting to return it
				connector = self.connector_set.get(connector_type=False)
				return connector
			except:
				return None

	def next_absolute_url(self, value):
		"""This method returns the absolute url for the next connector object in the testkit algorithm sequence after this very object if any"""
		if self.next(value): #checking if there is a next in the first place
			return self.next(value).get_absolute_url
		else:
			return None

	def next_api_url(self, value):
		"""This method returns the api url for the next connector object in the testkit algorithm sequence after this very object if any"""
		if self.next(value): #checking if there is a next in the first place
			return self.next(value).get_api_url
		else:
			return None


class ConnectorToDecisionBox(models.Model):
	decision_box = models.ForeignKey(DecisionBox, null=True, on_delete=models.SET_NULL)

class Connector(models.Model):
	connector_type = models.BooleanField(default=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	connected_from = models.ForeignKey(DecisionBox, null=False, on_delete=models.CASCADE)
	connect_to = models.OneToOneField(ConnectorToDecisionBox, null=True, blank=True, on_delete=models.SET_NULL)

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

	def execute_first_operation(self, request):
		"This method implements the operations that accompany a connector starting with the first operation in the list"
		first_operation = self.operation_set.first()
		return first_operation.execute(request)

class Operation(models.Model):
	execution_choices = EXECUTION_CHOICES
	description = models.TextField()
	connector = models.ForeignKey(Connector, null=False, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, null=False, blank=False)
	execution = models.CharField(max_length=50, null=False, blank=False, choices=execution_choices)
	execution_info = models.TextField()

	def execute(self, request):
		"""This method implements and operation then moves to implement the next operation that follows it if any"""
		operation_model = EXECUTION_DEFINITIONS.get(self.execution)
		try:
			params = json.loads(self.execution_info) #converts the execution info to a python dictionary
		except:
			params = None
		if operation_model:
			if params:
				operation_instance = operation_model(request, self, **params)
			else:
				operation_instance = EXECUTION_DEFINITIONS.get("Default")(request, self)
			return operation_instance.execute()
		else:
			operation_instance = EXECUTION_DEFINITIONS.get("Default")(request, self)
			return operation_instance.execute()

	def get_next_operation_of_same_instance(self):
		instance = self.connector
		operations = instance.operation_set.all()
		next_object_index = 0
		current_obj = None
		for i, obj in enumerate(operations):
			current_obj = obj
			if next_object_index >0:
				break
			if obj == self:
				next_object_index = i + 1
		print(self, "is the self")
		print(current_obj, "is the next")
		if not current_obj == self:
			return current_obj
		else:
			return None

		
