from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views import View


def algorithm(request, id):
	return HttpResponse("well done")

class DecisionBoxView(View):
	"""This implements the algorithm for a user"""

	def get(self, request, id, **kwargs):
		# self.instance = get_object_or_404(Algorithm, id=id)
		# self.decision_box = self.instance.initial_decision_box
		# self.questions = self.decision_box.questions.all()
		# context = {
		# "decision_box":self.decision_box,
		# "questions": self.questions,
		# "instance": self.instance,
		# }
		decision_box = get_object_or_404(DecisionBox, id=id)
		instance = decision_box.algorithm
		questions = decision_box.questions.all()
		context = {
		"decision_box":decision_box,
		"questions": questions,
		"instance": instance,
		}
		return render(request, 'test_kit/algorithm.html', context)

	def post(self, request, id):
		print(request.POST)
		print(dir(request.POST))
		data = request.POST
		decision_box = get_object_or_404(DecisionBox, id=id)
		instance = decision_box.algorithm
		questions = decision_box.questions.all()

		value = 0
		for q in questions:#here is a hack to add the sum magnitude of checked questions
			question = data.get("question"+str(q.id))
			if question:
				value = value + q.magnitude

		context = {
		"decision_box":decision_box,
		"questions": questions,
		"instance": instance,
		}
		if decision_box.next(value):
			return HttpResponseRedirect(decision_box.next_absolute_url(value))
		else:
			return render(request, 'test_kit/test_completed_message.html', context)

class AlgorithmView(DecisionBoxView):
	"""This implements the Decision box of the algorithm"""
	def get(self, request, id, **kwargs):
		instance = get_object_or_404(Algorithm, id=id)
		id = instance.decisionbox_set.first().id
		return DecisionBoxView.get(self, request, id, **kwargs)

	def post(self, request, id, **kwargs):
		instance = get_object_or_404(Algorithm, id=id)
		id = instance.decisionbox_set.first().id
		return DecisionBoxView.post(self, request, id, **kwargs)

class ConnectorView(View):
	def get(self, request, id):
		connector = get_object_or_404(Connector, id=id)
		first_operation = connector.operation_set.first()
		if first_operation:
			return connector.execute_first_operation(request)
		else:
			if connector.connect_to:
				return HttpResponseRedirect(connector.connect_to.decision_box.get_absolute_url)
			else:
				context = {
				"decison_box":connector.connected_from,
				"instance":connector.connected_from.algorithm,
				"questions":connector.connected_from.questions,
				}
				return render(request, 'test_kit/test_completed_message.html', context)

	def post(self, request, id):
		connector = get_object_or_404(Connector, id=id)
		next_operation_id = request.POST.get("next")
		print(next_operation_id)
		if next_operation_id:
			print("the code implementation got here")
			next_operation = get_object_or_404(Operation, id=int(next_operation_id))
			return next_operation.execute(request)
		else:
			print("the code did not get where we want it to be")
			if connector.connect_to:
				return HttpResponseRedirect(connector.connect_to.decision_box.get_absolute_url)
			else:
				context = {
				"decison_box":connector.connected_from,
				"instance":connector.connected_from.algorithm,
				"questions":connector.connected_from.questions,
				}
				return render(request, 'test_kit/test_completed_message.html', context)