   

from django.urls import path, include
from a_users.views import *

    
urlpatterns = [
    path('',profile_view, name='profile'),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    path('usernamechange/', profile_usernamechange, name="profile-usernamechange"),
    path('<username>/', profile_view,name='userprofile'),
    path('profile/edit/',profile_edit_view, name='profile-edit'),
    path('profile/delete/',profile_delete_view, name='profile-delete'),
    path('profile/onboarding/',profile_edit_view, name="profile-onboarding"),
]


    