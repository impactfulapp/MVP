from social_core.backends.facebook import FacebookOAuth2
#from social_core.backends.twitter import TwitterOAuth
#from social_core.backends.google import GoogleOAuth2

import urllib2
import json
from urllib2 import urlopen
from django.core.files.base import ContentFile
from models import Profile

def connect_to_profile(strategy, *args, **kwargs):
    user = kwargs['user']
    profile_list = Profile.objects.all()
    for profile in profile_list:
        if profile.user.username == user.username:
            return #HttpResponseRedirect('/donations/')
    new_profile = Profile(user=user, email='', phone='')
    new_profile.save()
    #return HttpResponseRedirect('/donations/')

# get profile information from social logins
def update_user_social_data(strategy, *args, **kwargs):

    backend = kwargs['backend']
    user = kwargs['user']
    
    #Set only if is new.
    if not kwargs['is_new']:
        return

    #get full name
    full_name = ''
    full_name = kwargs['response'].get('name')
    user.full_name = full_name

    #get avatar
    fbuid = kwargs['response']['id']
    image_name = 'fb_avatar_%s.jpg' % fbuid
    image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
    image_stream = urlopen(image_url)

    user.profile.avatar.save(
        image_name,
        ContentFile(image_stream.read()),
    )

    #get email
    fbuid = kwargs['response']['id']
    access_token = kwargs['response']['access_token']

    url = u'https://graph.facebook.com/{0}/' \
          u'?fields=email' \
          u'&access_token={1}'.format(
        fbuid,
        access_token,
    )

    request = urllib2.Request(url)
    email = json.loads(urlopen(request).read()).get('email')
    user.email = email
    print '2 email is: ', email

    #get birthday - not working, returning none (facebook review?)
    #birthday = kwargs['response'].get('birthday')
    #user.birthday = birthday
    #print 'birthday is ', birthday

    #gender = kwargs['response'].get('gender')
    #print 'asdf gender is ', gender


    """
    if (
        isinstance(backend, FacebookOAuth2)
        #or isinstance(backend, GoogleOAuth2)
    ):
        full_name = kwargs['response'].get('name')
    
    elif (
        isinstance(backend, TwitterOAuth)
    ):
        if kwargs.get('details'):
            full_name = kwargs['details'].get('fullname')
    
    user.full_name = full_name
    
    if isinstance(backend, GoogleOAuth2):
        if response.get('image') and response['image'].get('url'):
            url = response['image'].get('url')
            ext = url.split('.')[-1]
            user.avatar.save(
               '{0}.{1}'.format('avatar', ext),
               ContentFile(urllib2.urlopen(url).read()),
               save=False
            )
    elif isinstance(backend, FacebookOAuth2):
        fbuid = kwargs['response']['id']
        image_name = 'fb_avatar_%s.jpg' % fbuid
        image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
        image_stream = urlopen(image_url)

        user.avatar.save(
            image_name,
            ContentFile(image_stream.read()),
        )
    elif isinstance(backend, TwitterOAuth):
        if kwargs['response'].get('profile_image_url'):
            image_name = 'tw_avatar_%s.jpg' % full_name
            image_url = kwargs['response'].get['profile_image_url']
            image_stream = urlopen(image_url)

            user.avatar.save(
                image_name,
                ContentFile(image_stream.read()),
            ) """

    #save all
    user.save()
