from django.contrib.auth.models import *
from rest_framework import viewsets
from ballots.serializers import *

class MethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Method.objects.all()
    serializer_class = MethodSerializer

class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class BallotBoxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BallotBox.objects.all()
    serializer_class = BallotBoxSerializer

class BallotOptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BallotOption.objects.all()
    serializer_class = BallotOptionSerializer

class BallotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ballot.objects.all()
    serializer_class = BallotSerializer
     
class DecisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializer