from ballots.models import *
from rest_framework import serializers

class MethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Method
        fields = ('id','name')
        
class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ('id','name','decision','url')
        
class BallotBoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BallotBox
        fields = ('id','name','decision')
        
class BallotOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BallotOption
        fields = ('id','option_id','ballot','value')
        
class BallotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ballot
        fields = ('id','ballot_box','decision','voting')
        
class DecisionSerializer(serializers.HyperlinkedModelSerializer):
    votes = BallotSerializer(many=True)
    class Meta:
        model = Decision
        fields = ('id','title','type','date','method','votes_count','votes_valid','votes')