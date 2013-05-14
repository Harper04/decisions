# -*- coding: utf-8 -*-
from django.db import models
from datetime import date

    
class Method(models.Model):
    name = models.CharField(max_length = 255)
    def __unicode__(self):
        return "{0}".format(self.name)
    
class Option(models.Model):
    name = models.CharField(max_length = 255)
    decision = models.ForeignKey("Decision", related_name="options")
    url = models.URLField()
    def __unicode__(self):
        return "{0}".format(self.name)
    
class BallotBox(models.Model):
    name = models.CharField(max_length = 255)
    decision = models.ForeignKey("Decision", related_name="ballot_boxes")
    def __unicode__(self):
        return "{0}".format(self.name)
    
class BallotOption(models.Model):
    option_id = models.ForeignKey("Option")
    ballot = models.ForeignKey("Ballot", related_name="voting")
    value = models.IntegerField()
    def __unicode__(self):
        return "Ballot option {0} with {1}".format(self.option_id.pk, self.value)
    
class Ballot(models.Model):
    ballot_box = models.ForeignKey("BallotBox", related_name="ballots")
    decision = models.ForeignKey("Decision", related_name="votes")
    def __unicode__(self):
        return "Ballot from {0}".format(self.decision.title)
    
class Decision(models.Model):
    title = models.CharField(max_length = 255)
    type = models.CharField(max_length = 255)
    date = models.DateField(max_length = 255)
    method = models.ForeignKey("Method", related_name="decisions")
    votes_count = models.IntegerField()
    votes_valid = models.IntegerField()
    def __unicode__(self):
        return "{0}".format(self.title)