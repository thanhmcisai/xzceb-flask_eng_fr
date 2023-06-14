"""
Author: ThanhMC
Description: Translate English to French and from French to English
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English to French
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French to English
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

if __name__ == "__main__":
    GREETING = "Bonjour"
    print(french_to_english(GREETING))
    print(english_to_french(GREETING))
