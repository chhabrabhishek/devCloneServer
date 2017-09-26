"""
	models for the devClone Server,
	Currently supports Rants and Actions
"""
from peewee import Model
from peewee import *

def getModels(db):
	"""
		cook the models connected
		to a given db
	"""

	class Rant(Model):
		time = IntegerField(null=False, default=0)
		tags = CharField(max_length=30, null=False)
		user = CharField(max_length=12, null=False)
		post = TextField(null=False, constraints=[Check("LENGTH(POST) > 8")])
		votes = IntegerField(null=False, default=0, constraints=[Check("votes >= 0")])

		class Meta:
			database = db

	class Action(Model):
		post = IntegerField(null=False)
		upvoted = CharField(max_length=12)
		downvoted = CharField(max_length=12)

		class Meta:
			database = db

	return Rant, Action
