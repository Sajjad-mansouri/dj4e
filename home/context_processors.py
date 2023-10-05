from django.conf import settings as dj_settings

def  title(request):
	return {
	'settings':dj_settings
	}