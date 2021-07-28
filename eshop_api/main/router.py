from rest_framework import routers
from ..cart.views import CartViewSet

router = routers.SimpleRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = []
urlpatterns += router.urls
