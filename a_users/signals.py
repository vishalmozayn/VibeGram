from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.models import EmailAddress

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user= instance
    if created:
        Profile.objects.create(
            user = user,
            email = user.email
        )
    else:
         try:
             email_address = EmailAddress.objects.get_primary(user)
             if email_address.email != user.email:
                 email_address.email = user.email
                 email_address.verified = False
                 email_address.save()
        
         except:
             EmailAddress.objects.create(
                 user= user,
                 email = user.email,
                 primary = True,
                 verified = False
             )
    
        
@receiver(post_save,sender=Profile)
def update_user(sender,instance,created,**kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            
           user.email = profile.email
           user.save()
        
        
