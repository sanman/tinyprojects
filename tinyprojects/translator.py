#import goslate
from translate import Translator
from textblob import TextBlob

'''def from_goslate(text_to_translate, lang):
    new_gs = goslate.Goslate()
    print(new_gs.translate(text_to_translate, lang))'''
    
def from_translate(from_lan, to_lan, text):
    translator = Translator(from_lang=from_lan, to_lang=to_lan)
    print(translator.translate(text))
    
def from_textblob(text_to_translate, from_lang, to_lang):
    adding_blob = TextBlob(text_to_translate)
    adding_blob.translate(from_lang = from_lang, to_lang = to_lang)


#from_goslate("Python is so powerful", 'es')
from_translate("english", "french", "This is a useful library")
from_textblob("Easy way to translate text in Python", 'en', 'ar')