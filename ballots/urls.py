from django.conf.urls import patterns, url, include
from rest_framework import routers
from ballots import views

router = routers.DefaultRouter()
router.register(r'methods', views.MethodViewSet)
router.register(r'options', views.OptionViewSet)
router.register(r'ballotboxes', views.BallotBoxViewSet)
router.register(r'ballotoptions', views.BallotOptionViewSet)
router.register(r'ballots', views.BallotViewSet)
router.register(r'decisions', views.DecisionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)