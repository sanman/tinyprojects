import goslate
from translate import Translator

def from_goslate(text_to_translate, lang):
    new_gs = goslate.Goslate()
    print(new_gs.translate(text_to_translate, lang))
    
def from_translate(from_lan, to_lan, text):
    translator = Translator(from_lang=from_lan, to_lang=to_lan)
    print(translator.translate(text))


from_goslate("Python is so powerful", 'es')
from_translate("english", "french", "This is a useful library")
