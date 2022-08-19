"""language translator"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def connect(apikey, url):
    """translator instance"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator

language_translator = connect(apikey, url)

def englishToFrench(english_text):
    """english to french translation"""
    #write the code here
    if english_text == '':
        french_text = ''
    else:
        output = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        french_text = output['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """french to english translation"""
    #write the code here
    if french_text == '':
        english_text = ''
    else:
        output = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        english_text = output['translations'][0]['translation']
    return english_text
