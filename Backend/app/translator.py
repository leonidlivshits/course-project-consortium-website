from translate import Translator

def translate_to_english(text, translator=Translator(from_lang="ru", to_lang="en")):
    if not text or not isinstance(text, str):
        return text

    try:
        translated_text = translator.translate(text)
        if "MYMEMORY WARNING" in translated_text:
            raise Exception(translated_text)
        return translated_text
    except Exception as e:
        return text
    
def translate_to_russian(text, translator=Translator(from_lang="en", to_lang="ru")):
    if not text or not isinstance(text, str):
        return text

    try:
        translated_text = translator.translate(text)
        if "MYMEMORY WARNING" in translated_text:
            raise Exception(translated_text)
        return translated_text
    except Exception as e:
        return text