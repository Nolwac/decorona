from django.urls import path # access to the django url path
from .views import * # access to all the url views available
from rest_framework.routers import DefaultRouter # access to routers
from django.conf.urls import include # access to the url inclusion class

router = DefaultRouter()
router.register('userprofile', UserProfileViewset)


urlpatterns = [
    path('userprofile/get_user_profile/', GetUserProfile.as_view(), name="userprofile"), #this is to get userprofile from the users user token and session
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name="login"),
    path('authentication/logout_one/', LogoutView.as_view(), name="logout"), #this is to make sure that all the user is logged out only in that particular device
    path('userprofile/user/<int:id>/', GetUserDetails.as_view(), name="profile") #this is to get userprofile from the users models
    # and not in all the devices he has logged into
]
