from rest_framework import routers

from detektor_suhu.views import StatsViewSet

router = routers.DefaultRouter()
router.register('Stats', StatsViewSet)

urlpatterns =[]
urlpatterns += router.urls
