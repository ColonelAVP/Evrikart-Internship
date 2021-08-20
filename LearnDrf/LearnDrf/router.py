from rest_framework import routers
from store.viewset import StoreViewset


router = routers.DefaultRouter()
router.register('store', StoreViewset)
