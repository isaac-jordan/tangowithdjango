from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from registration.backends.simple.views import RegistrationView
from rango import views as rangoViews

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/rango/add_profile/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/password/change/done/$', rangoViews.passwordChangeDone, name='auth_password_change_done'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
    'django.views.static',
    (r'^media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
