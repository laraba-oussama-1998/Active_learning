from django.apps import AppConfig
from django.conf import settings
import pickle
import os

class CharAlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'char_al'
    
    path = os.path.join(settings.MLMODELS, 'models.pickle')
    
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled) 
        
    headers = data['headers']
    labelEncoder = data['labelEncoder']
    classifier = data['classifier']
