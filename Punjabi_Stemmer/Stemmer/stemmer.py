import os
import collections
import re

class PunjabiStemmer:
    def __init__(self):
        # Define the base path relative to this script
        base_path = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        # Load the data files
        self.pronouns = self.load_words(os.path.join(base_path, 'Punjabi_Pronouns.txt'))
        self.adverbs = self.load_words(os.path.join(base_path, 'Punjabi_Adverbs.txt'))
        self.postpositions = self.load_words(os.path.join(base_path, 'Punjabi_Postpositions.txt'))
        self.vocabulary = self.load_words(os.path.join(base_path, 'Punjabi_Vocabulary.txt'))
        self.names = self.load_words(os.path.join(base_path, 'Punjabi_Boys_Girls_Name.txt'))
        self.suffix = self.load_words(os.path.join(base_path, 'Suffix.txt'))

        # In the development of the PunjabiStemmer, one of our core objectives was to create a highly accurate
        # and versatile tool capable of navigating the rich morphological landscape of the Punjabi language. To
        # achieve this, we have meticulously developed and implemented an expansive set of rules that serve as
        # the foundation of our stemming process.
        #
        # The PunjabiStemmer incorporates over 300 specific rules, designed to accurately process a wide array
        # of grammatical scenarios. These rules are meticulously categorized to address different aspects of the
        # language, including but not limited to, proper nouns and names, pronouns, verbs, adverbs, and adjectives.
        # This structured approach allows the stemmer to precisely identify and handle the morphological nuances
        # of Punjabi, significantly reducing errors related to overstemming and understemming.
        #
        # The rules are thoughtfully crafted and arranged from longest to smallest, optimizing both accuracy and
        # efficiency in stemming. This organization reflects our meticulous approach to handling the complexities
        # of Punjabi morphology.
        
        self.rules = [
{"match": "ਪੂਰਵਕ", "strip": "ਪੂਰਵਕ", "add": ""},
{"match": "ਉਦਿਆਂ", "strip": "ਉਦਿਆਂ", "add": ""},
{"match": "ਉਂਦੀਆਂ", "strip": "ਉਂਦੀਆਂ", "add": ""},
{"match": "ਉਦੀਆਂ", "strip": "ਉਦੀਆਂ", "add": ""},
{"match": "ਉਣੀਆਂ", "strip": "ਉਣੀਆਂ", "add": ""},
{"match": "ਅਈਆ", "strip": "ਅਈਆ", "add": ""},
{"match": "ਅਤਣ",  "strip": "ਣ", "add": ""},
{"match": "ਆਵਣ", "strip": "ਵਣ", "add": ""},
{"match": "ਆਵਣੀ", "strip": "ਆਵਣੀ", "add": ""},
{"match": "ਊਗੜਾ", "strip": "ਊਗੜਾ", "add": ""},
{"match": "ਕਰਣ", "strip": "ਕਰਣ", "add": ""},
{"match": "ਕਾਰਕ", "strip": "ਕਾਰਕ", "add": ""},
{"match": "ਜਨਕ", "strip": "ਜਨਕ", "add": ""},
{"match": "ਗਰਦੀ", "strip": "ਗਰਦੀ", "add": ""},
{"match": "ਤੰਤਰ", "strip": "ਤੰਤਰ", "add": ""},
{"match": "ਦਾਇਕ", "strip": "ਦਾਇਕ", "add": " "},
{"match": "ਦਾਰਨੀ", "strip": "ਦਾਰਨੀ", "add": "ਦਾਰਨੀ"},
{"match": "ਨਵੀਸ", "strip": "ਨਵੀਸ", "add": " "},
{"match": "ਪ੍ਰਸਤ", "strip": "ਪ੍ਰਸਤ", "add": " "},
{"match": "ਪਾਤਰ", "strip": "ਪਾਤਰ", "add": " "},
{"match": "ਪੂਰਣ", "strip": "'ਪੂਰਣ", "add": " "},
{"match": "ਸ਼ਕਤੀ", "strip": "ਸ਼ਕਤੀ", "add": " "},
{"match": "ਸ਼ੀਲਤਾ", "strip": "ਸ਼ੀਲਤਾ", "add": " "},
{"match": "ਵਾਂਗੀਆ", "strip": "ਵਾਂਗੀਆ", "add": ""},
{"match": "ਾਵਾਂਗਾ", "strip": "ਵਾਂਗਾ", "add": ""},
{"match": "ਾਵਾਂਗੀ", "strip": "ਵਾਂਗੀ", "add": ""},
{"match": "ਾਵਾਂਗੇ", "strip": "ਵਾਂਗੇ", "add": ""},
{"match": "ੀਕਰਨ", "strip": "ੀਕਰਨ", "add": " "},
{"match": " ੀਕਰਨ", "strip": " ੀਕਰਨ", "add": ""},
{"match": "ਉਂਦਾ", "strip": "ਉਂਦਾ", "add": ""},
{"match": "ਉਂਦੀ", "strip": "ਉਂਦੀ", "add": ""},
{"match": "ਉਂਦੇ", "strip": "ਉਂਦੇ", "add": ""},
{"match": "ਉਣਾ", "strip": "ਉਣਾ", "add": ""},
{"match": "ਉਣੀ", "strip": "ਉਣੀ", "add": ""},
{"match": "ਉਣੇ", "strip": "ਉਣੇ", "add": ""},
{"match": "ਓਣ", "strip": "ਓਣ", "add": ""},
{"match": "ਓਗੇ", "strip": "ਓਗੇ", "add": ""},
{"match": "ਅਈ", "strip": "ਅਈ", "add": ""},
{"match": "ਅਣ", "strip": "ਅਣ", "add": ""},
{"match": "ਅਤ", "strip": "ਅਤ", "add": ""},
{"match": "ਆਈ", "strip": "ਆਈ", "add": ""},
{"match": "ਆਉ", "strip": "ਆਉ", "add": ""},
{"match": "ਆਉਂ", "strip": "ਆਉਂ", "add": ""},
{"match": "ਆਕ", "strip": "ਆਕ", "add": ""},
{"match": "ਆਣੀ", "strip": "ਆਣੀ", "add": ""},
{"match": "ਆਨੀ", "strip": "ਆਨੀ", "add": ""},
{"match": "ਆਰ", "strip": "ਆਰ", "add": ""},
{"match": "ਆਰਾ", "strip": "ਆਰਾ", "add": ""},
{"match": "ਆਰੀ", "strip": "ਆਰੀ", "add": ""},
{"match": "ਆਲ", "strip": "ਆਲ", "add": ""},
{"match": "ਆਲਾ", "strip": "ਆਲਾ", "add": ""},
{"match": "ਆਲੂ", "strip": "ਆਲੂ", "add": ""},
{"match": "ਐਲ", "strip": "ਐਲ", "add": ""},
{"match": "ਆੜੀ", "strip": "ਆੜੀ", "add": ""},
{"match": "ਇਕ", "strip": "ਇਕ", "add": ""},
{"match": "ਇਤ", "strip": "ਇਤ", "add": ""},
{"match": "ਈਆਂ", "strip": "ਈਆਂ", "add": ""},
{"match": "ਇਆ", "strip": "ਇਆ", "add": ""},
{"match": "ਇਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਇਆਂ", "strip": "ਇਆਂ", "add": ""},
{"match": "ਈਆ", "strip": "ਆ", "add": ""},
{"match": "ਈਆ", "strip": "ਈਆ", "add": ""},
{"match": "ੲੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਈਨ", "strip": "ਈਨ", "add": ""},
{"match": "ਇਏ", "strip": "ਇਏ", "add": ""},
{"match": "ਈਏ", "strip": "ਈਏ", "add": ""},
{"match": "ਏਟਾ", "strip": "ਏਟਾ", "add": ""},
{"match": "ਏਟੀ", "strip": "ਏਟੀ", "add": ""},
{"match": "ਏਰਾ", "strip": "ਏਰਾ", "add": ""},
{"match": "ਏਲੀ", "strip": "ਏਲੀ", "add": ""},
{"match": "ਈਲਾ", "strip": "ਈਲਾ", "add": ""},
{"match": "ਏਗਾ", "strip": "ਏਗਾ", "add": ""},
{"match": "ਏਗੀ", "strip": "ਏਗੀ", "add": ""},
{"match": "ਕਾਰ", "strip": "ਕਾਰ", "add": ""},
{"match": "ਕਾਰੀ", "strip": "ਕਾਰੀ", "add": ""},
{"match": "ਕੁਸ਼ੀ", "strip": "ਕੁਸ਼ੀ", "add": ""},
{"match": "ਖੋਰਾਂ", "strip": "ਖੋਰਾਂ", "add": ""},
{"match": "ਖ਼ੋਰ", "strip": "ਖ਼ੋਰ", "add": ""},
{"match": "ਖੋਰ", "strip": "ਖੋਰ", "add": ""},
{"match": "ਖ਼ਾਨਾ", "strip": "ਖ਼ਾਨਾ", "add": ""},
{"match": "ਗਾਰ", "strip": "ਗਾਰ", "add": ""},
{"match": "ਗਿਰੀ", "strip": "ਗਿਰੀ", "add": ""},
{"match": "ਗੀਰ", "strip": "ਗੀਰ", "add": ""},
{"match": "ਗਰ", "strip": "ਗਰ", "add": "ਗਰ"},
{"match": "ਗ਼ਰ", "strip": "ਗ਼ਰ", "add": "ਗ਼ਰ"},
{"match": "ਘਰ", "strip": "ਘਰ", "add": ""},
{"match": "ਘਣੀ", "strip": "ਘਣੀ", "add": "ਘਣੀ"}, #ਸਿੰਘਣੀ
{"match": "ਘਾਤ", "strip": "ਘਾਤ", "add": ""},
{"match": "ਚਾਰੀ", "strip": "ਚਾਰੀ", "add": ""},
{"match": "ਤਣ", "strip": "ਣ", "add": ""},
{"match": "ਤਰ", "strip": "ਤਰ", "add": ""},
{"match": "ਤਾਈ", "strip": "ਤਾਈ", "add": ""},
{"match": "ਤੇਰਾ", "strip": "ਤੇਰਾ", "add": ""},
{"match": "ਦਾਨ", "strip": "ਦਾਨ", "add": ""},
{"match": "ਦਾਰੀ", "strip": "ਦਾਰੀ", "add": ""},
{"match": "ਦਿਲ", "strip": "ਦਿਲ", "add": ""},
{"match": "ਦੀਆਂ", "strip": "ਆਂ", "add": ""}, # ਕੈਦੀਆਂ
{"match": "ਦੀਆਂ", "strip": "ਦੀਆਂ", "add": ""},
{"match": "ਂਦੀਆ", "strip": "ਂਦੀਆ", "add": ""},
{"match": "ਦਿਆ", "strip": "ਦਿਆ", "add": ""},
{"match": "ਦੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਧਰ", "strip": "ਧਰ", "add": ""},
{"match": "ਧਾਰ", "strip": "ਧਾਰ", "add": ""},
{"match": "ਧਾਰੀ", "strip": "ਧਾਰੀ", "add": ""},
{"match": "ਨਾਕ", "strip": "ਨਾਕ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ੀਆਂ", "add": ""},
{"match": "ਨੀਆਂ", "strip": "ਨੀਆਂ", "add": ""},
{"match": "ਪਣ", "strip": "ਪਣ", "add": ""},
{"match": "ਪਨ", "strip": "ਪਨ", "add": ""},
{"match": "ਪੁਣਾ", "strip": "ਪੁਣਾ", "add": ""},
{"match": "ਪੁੱਣਾ", "strip": "ਪੁੱਣਾ", "add": ""},
{"match": "ਪੁਰ", "strip": "ਪੁਰ", "add": "ਪੁਰ"},
{"match": "ਪੋਸ਼", "strip": "ਪੋਸ਼", "add": ""},
{"match": "ਪੰਥੀ", "strip": "ਪੰਥੀ", "add": ""},
{"match": "ਬਾਜ਼ੀ", "strip": "ਬਾਜ਼ੀ", "add": ""},
{"match": "ਬਾਜੀ", "strip": "ਬਾਜੀ", "add": ""},
{"match": "ਬਾਨ", "strip": "ਬਾਨ", "add": ""},
{"match": "ਬਾਜ", "strip": "ਬਾਜ", "add": ""},
{"match": "ਬੱਧ", "strip": "ਬੱਧ", "add": ""},
{"match": "ਬਾਜ਼", "strip": "ਬਾਜ਼", "add": ""},
{"match": "ਮਾਨ", "strip": "ਮਾਨ", "add": ""},
{"match": "ਮਾਰ", "strip": "ਮਾਰ", "add": ""},
{"match": "ਮੁਖੀ", "strip": "ਮੁਖੀ", "add": ""},
{"match": "ਮੰਦੀ", "strip": "ਮੰਦੀ", "add": ""},
{"match": "ਮੰਦ", "strip": "ਮੰਦ", "add": ""},
{"match": "ਣਗੇ", "strip": "ਣਗੇ", "add": ""},
{"match": "ਣੀਆਂ", "strip": "ਣੀਆਂ", "add": ""},
{"match": "ਯੋਗ", "strip": "ਯੋਗ", "add": ""},
{"match": "ਵਾਂਗਾ", "strip": "ਵਾਂਗਾ", "add": ""},
{"match": "ਵਾਂਗੇ", "strip": "ਵਾਂਗੇ", "add": ""},
{"match": "ਵਾਂਗੀ", "strip": "ਵਾਂਗੀ", "add": ""},
{"match": "ਵੋਗੇ", "strip": "ਵੋਗੇ", "add": ""},
{"match": "ਵੇਗਾ", "strip": "", "add": ""},
{"match": "ਵੇਗੀ", "strip": "ਵੇਗੀ", "add": ""},
{"match": "ਵਟ", "strip": "ਵਟ", "add": ""},
{"match": "ਵਰ", "strip": "ਵਰ", "add": ""},
{"match": "ਵਾਦ", "strip": "ਵਾਦ", "add": ""},
{"match": "ਵਾਨ", "strip": "ਵਾਨ", "add": ""},
{"match": "ਵਾਲਾ", "strip": "ਵਾਲਾ", "add": ""},
{"match": "ਾਵਲੀ", "strip": "ਾਵਲੀ", "add": "ਾਵਲੀ"},
{"match": "ਾਵਟ", "strip": "ਾਵਟ", "add": ""},
{"match": "ਵਟ", "strip": "ਵਟ", "add": ""},
{"match": "ਵਟੀ", "strip": "ਵਟੀ", "add": ""},
{"match": "ਾਵਣ", "strip": "ਵਣ", "add": ""},
{"match": "ਾਵਣੀ", "strip": "ਵਣੀ", "add": ""},
{"match": "ਾਵਣੀ", "strip": "ਣੀ", "add": ""},
{"match": "ਵਾਲ", "strip": "ਵਾਲ", "add": ""},
{"match": "ਵੰਤੀ", "strip": "ਵੰਤੀ", "add": ""},
{"match": "ਵੰਤ", "strip": "ਵੰਤ", "add": ""},
{"match": "ਵੰਦ", "strip": "ਵੰਦ", "add": ""},
{"match": "ਸ਼ਾਹੀ", "strip": "ੀ", "add": ""},
{"match": "ਸ਼ੀਲ", "strip": "ਸ਼ੀਲ", "add": ""},
{"match": "ਸਾਜ", "strip": "ਸਾਜ", "add": ""},
{"match": "ਸਾਜ਼", "strip": "ਸਾਜ਼", "add": ""},
{"match": "ਸਾਰ", "strip": "ਸਾਰ", "add": ""},
{"match": "ਸ਼ਾਲਾ", "strip": "ਸ਼ਾਲਾ", "add": "ਸ਼ਾਲਾ"}, # ਗਊਸ਼ਾਲਾ if we don't remove or add same suffix then stemmmer will continue steming
                                                  # because input word is valid but now we are adding same suffix and converting it to stem word output 
                                                   # which is now stemmed valid output so no further stemming take place so
{"match": "ਸਾਲ", "strip": "ਸਾਲ", "add": ""},
{"match": "ਸਾਲ", "strip": "ਸਾਲ", "add": "ਸਾਲ"},
{"match": "ਹਾਰੀ", "strip": "ਹਾਰੀ", "add": ""},
{"match": "ਹਾਰਾ", "strip": "ਹਾਰਾ", "add": ""},
{"match": "ਹਾਰ", "strip": "ਹਾਰ", "add": ""},
{"match": "ਹੀਣ", "strip": "ਹੀਣ", "add": ""},
{"match": "ਹਟ", "strip": "ਹਟ", "add": ""},
{"match": "ਾਹਟ", "strip": "ਾਹਟ", "add": ""},
{"match": "ਿਉਂ", "strip": "ਿਉਂ", "add": "ਾ"},
{"match": "ਿਓਂ", "strip": "ਿਓਂ", "add": "ੇ"},
{"match": "ੀਓ", "strip": "ਓ", "add": ""},
{"match": "ਿਓ", "strip": "ਿਓ", "add": "ੀ"},
{"match": "ਿਓ", "strip": "ਿਓ", "add": "ਾ"},
{"match": "ਿੳ", "strip": "ਿੳ", "add": "ੀ"},
{"match": "ਿੳ", "strip": "ਿੳ", "add": "ਾ"},
{"match": "ਊ", "strip": "ਊ", "add": ""},
{"match": "ਉ", "strip": "ਉ", "add": ""},
{"match": "ਓ", "strip": "ਓ", "add": ""},
{"match": "ੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ੀਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਿਆਂ", "strip": "ਿਆਂ", "add": "ਾ"}, #ਜਾਗਦਿਆਂ
{"match": "ਿਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਿਆਂ", "strip": "ਿਆਂ", "add": ""}, #ਮੰਗਿਆਂ
{"match": "ੀਆ", "strip": "ਆ", "add": ""},
{"match": "ਿਆ", "strip": "ਿਆ", "add": "ਾ"},
{"match": "ੂਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ੋਆਂ", "strip": "ਆਂ", "add": ""},
{"match": "ਆਂ", "strip": "ਆਂ", "add": ""},# ਨਹੁੰਆਂ
{"match": "ਆ", "strip": "ਆ", "add": ""},
{"match": 'ਜੇ', "strip": 'ਜੇ', "add": ""},
{"match": 'ਾਈ', "strip": 'ਈ', "add": ""}, #ਗਹਿਰਾਈ
{"match": 'ਾਈ', "strip": 'ਾਈ', "add": ""},
{"match": 'ਾਈ', "strip": 'ਾਈ', "add": "ਾਈ"}, #ਅਸਥਾਈ
{"match": " ਾਈ", "strip": "ਈ", "add": ""},
{"match": " ਾਈ", "strip": " ਾਈ", "add": ""},
{"match": "ਿਏ", "strip": "ਿਏ", "add": "ੀ"},
{"match": "ਿਏ", "strip": "ਿਏ", "add": ""},
{"match": "ੀਏ", "strip": "ਏ", "add": ""},
{"match": "ੀਏ", "strip": "ਏ", "add": "ਆ"},# ਏਰੀਏ , ਮੀਡੀਏ 
{"match": "ੀਏ", "strip": "ੀਏ", "add": ""}, #ਦੇਖੀਏ
{"match": "ਈਂ", "strip": "ਈਂ", "add": ""},
{"match": "ਈ", "strip": "ਈ", "add": ""},
{"match": "ਿਆਈ", "strip": "ਿਆਈ", "add": "ਾ"}, #ਚੰਗਿਆਈ
{"match": "ਏ", "strip": "ਏ", "add": ""},
{"match": "ਕਾ", "strip": "ਕਾ", "add": ""},
{"match": "ਕੀ", "strip": "ਕੀ", "add": ""},
{"match": "ਕ", "strip": "ਕ", "add": ""},
{"match": "ਕੇ", "strip": "ਕੇ", "add": ""},
{"match": "ਕੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ਕੇ", "strip": "ਕੇ", "add": "ਕੇ"}, #ਜਾਣਕੇ , ਕਰਕੇ, ਮਿਲਕੇ,  ਕੜਾਕੇ ,ਆਕੇ, ਬਣਾਕੇ, ਬੰਨਕੇ
{"match": "ੇਗੀ", "strip": "ੇਗੀ", "add": ""},
{"match": "ੇਗਾ", "strip": "ੇਗਾ", "add": ""},
{"match": "ੋਗੇ", "strip": "ੋਗੇ", "add": ""},
{"match": "ਾਂਗਾ", "strip": "ਾਂਗਾ", "add": ""},
{"match": "ਾਂਗੀ", "strip": "ਾਂਗੀ", "add": ""},
{"match": "ਾਂਗੇ", "strip": "ਾਂਗੇ", "add": ""},
{"match": "ੋਗੀ", "strip": "ੋਗੀ", "add": ""},#ਕਰੋਗੀ
{"match": "ੋਗੀ", "strip": "ੀ", "add": ""}, #ਯੋਗੀ
{"match": "ਗੀ", "strip": "ਗੀ", "add": ""},
{"match": "ਚੀ", "strip": "ੀ", "add": ""}, #ਸੋਚੀ
{"match": "ਚੀ", "strip": "ਚੀ", "add": "ਚੀ"}, #ਖਜਾਨਚੀ
{"match": "ਾਣੀ", "strip": "ਾਣੀ", "add": "ਾਣੀ"},#ਮਹਾਰਾਣੀ, ਪੁਰਾਣੀ ਪਾਣੀ ਢਾਣੀ ਹਾਣੀ ਖਾਣੀ ਕਹਾਣੀ ਨੌਕਰਾਣੀ
{"match": "ੈਣੀ", "strip": "ਣੀ", "add": ""}, #ਸੈਣੀ
{"match": "ੂਣੀ", "strip": "ੂਣੀ", "add": "ੂਣੀ"}, #ਧੂਣੀ
{"match": "ੁਣੀ", "strip": "ੀ", "add": ""}, #ਸੁਣੀ, ਚੁਣੀ, ਦੋਗੁਣੀ, ਨਿਗੁਣੀ, ਅਣਸੁਣੀ, ਚੌਗੁਣੀ,
{"match": "ੋਣੀ", "strip": "ੀ", "add": ""},
{"match": "ਣੀ", "strip": "ਣੀ", "add": ""},#ਭੁਗਤਣੀ, ਭੇਜਣੀ, ਪੀਣੀ
{"match": "ਣੀ", "strip": "ੀ", "add": ""}, #ਬਣੀ
{"match": "ਣੀ", "strip": "ਣੀ", "add": "ਣੀ"}, #ਕਾਣੀ ਗਿਣੀ
{"match": "ਾਣੇ", "strip": "ੇ", "add": "ਾ"}, #ਥਾਣੇ ਗਾਣੇ ਟਿਕਾਣੇ ਦਾਣੇ
{"match": "ੂਣੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ੁਣੇ", "strip": "ੇ", "add": ""},
{"match": "ੇਣੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ੈਣੇ", "strip": "ੇ", "add": ""},
{"match": "ਣੇ", "strip": "ੇ", "add": "ਾ"}, # ਜਾਣੇ, ਸਾਮਣੇ,  ਲਾਣੇ, ਛਣਕਣੇ
{"match": "ਣੇ", "strip": "ਣੇ", "add": ""}, #ਉਠਣੇ
{"match": "ਣਾ", "strip": "ਣਾ", "add": ""},
{"match": "ਣ", "strip": "ਣ", "add": ""},
{"match": "ਤੀ", "strip": "ੀ", "add": ""},
{"match": "ਤੀ", "strip": "ਤੀ", "add": "ਤੀ"},
{"match": "ਤਾ", "strip": "ਤਾ", "add": ""},
{"match": "ਤ", "strip": "ਤ", "add": ""},
{"match": "ਜੀ", "strip": "ਜੀ", "add": ""},
{"match": "ੇ", "strip": "ੇ", "add": "ਾ"},
{"match": "ਾਂਦਾ", "strip": " ਂਦਾ", "add": "ਾ"},
{"match": "ਾਂਦੀ", "strip": "ਾਂਦੀ", "add": "ਾ"},
{"match": " ਾਂਦੇ", "strip": "  ਾਂਦੇ", "add": "ਾ"},
{"match": "ਂਦੇ", "strip": "ਂਦੇ", "add": ""},
{"match": "ਂਦੀ", "strip": "ਂਦੀ", "add": ""},
{"match": "ਂਦਾ", "strip": "ਂਦਾ", "add": ""},
{"match": "ੰਦਾ", "strip": "ੰਦਾ", "add": ""},
{"match": "ੰਦੀ", "strip": "ੰਦੀ", "add": ""},
{"match": "ੰਦੇ", "strip": "ੰਦੇ", "add": ""},
{"match": "ੀਦਾ", "strip": "ੀਦਾ", "add": ""},
{"match": "ਦਾ", "strip": "ਦਾ", "add": ""},
{"match": "ਦੀ", "strip": "ਦੀ", "add": ""},
{"match": "ਦੇ", "strip": "ਦੇ", "add": ""},
{"match": "ਨੀ", "strip": "ਨੀ", "add": "ਨੀ"},
{"match": "ਨਾ", "strip": "ਨਾ", "add": ""},
{"match": "ਨੇ", "strip": "ਨੇ", "add": ""},
{"match": "ਨਾਂ", "strip": "ਨਾਂ", "add": ""},
{"match": "ਨ", "strip": "ਨ", "add": ""},
{"match": "ਪਾ", "strip": "ਪਾ", "add": ""},
{"match": "ਪ", "strip": "ਪ", "add": ""},
{"match": 'ੀਲਾ', "strip": 'ੀਲਾ', "add": ""},
{"match": " ੀਲਾ", "strip": " ੀਲਾ", "add": ""},
{"match": 'ੂਲ਼ਾ', "strip": 'ੂਲ਼ਾ', "add": ""},
{"match": " ੂਲਾ", "strip": " ੂਲਾ", "add": ""},
{"match": " ੂਲਾ", "strip": " ੂਲਾ", "add": ""},
{"match": 'ੇਲੂ', "strip": 'ੇਲੂ', "add": ""},
{"match": "ੈਲ", "strip": "ੈਲ", "add": ""},
{"match": "ਲੂ", "strip": "ਲੂ", "add": ""},
{"match": "ਲਾ", "strip": "ਲਾ", "add": ""},
{"match": "ਲ", "strip": "ਲ", "add": ""},
{"match": "ਵੀ", "strip": "ਵੀ", "add": ""},
{"match": "ਵਾਂ", "strip": "ਵਾਂ", "add": ""},
{"match": "ਵਾ", "strip": "ਵਾ", "add": ""},
{"match": "ਵ", "strip": "ਵ", "add": ""},
{"match": "ਵੇਂ", "strip": "ਵੇਂ", "add": ""},
{"match": "ੜੀ", "strip": "ੜੀ", "add": ""},
{"match": "ੜਾ", "strip": "ੜਾ", "add": ""},
{"match": "ੜ", "strip": "ੜ", "add": ""},
{"match": "ਸ", "strip": "ਸ", "add": "ਸ"},
{"match": "ਸ", "strip": "ਸ", "add": ""},
{"match": " ਾ", "strip": " ਾ", "add": ""},
{"match": 'ਾ', "strip": 'ਾ', "add": ""},
{"match": "ੀਂ", "strip": "ੀਂ", "add": ""},
{"match": " ਿ", "strip": " ਿ", "add": ""},
{"match": "ੀ", "strip": "ੀ", "add": ""},
{"match": "ੀ", "strip":"ੀ", "add": "ੀ"},
{"match": 'ਿ', "strip": 'ਿ', "add": ""},
{"match": 'ੀ', "strip": 'ੀ', "add": ""},
{"match": 'ੁ', "strip": 'ੁ', "add": ""},
{"match": 'ੂ', "strip": 'ੂ', "add": ""},
{"match": " ੂ", "strip": " ੂ", "add": ""},
{"match": "ਾਂ", "strip": "ਾਂ", "add": ""},
{"match": "ੋ", "strip": "ੋ", "add": ""},
{"match": "ੋਂ", "strip": "ੋਂ", "add": ""},
{"match": "ੋ ਂ", "strip": "ੋ ਂ", "add": ""}
        ]
        self.dictionary_cache = {}
        self.rules_application_success = collections.defaultdict(int)
        self.rules_application_attempts = collections.defaultdict(int)
        

    def load_words(self, filename):
    """
    Loads words from a given file into a set. This method is primarily used
    for loading lists of pronouns, adverbs, postpositions, vocabulary, names,
    and suffixes from text files.
    
    Parameters:
    - filename (str): The path to the file containing the words.
    
    Returns:
    - set: A set of words loaded from the file.
    
    If the file is not found, it returns an empty set and prints an error message.
    """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return set(line.strip() for line in file)
        except FileNotFoundError:
            print(f"Error: File not found {filename}")
            return set()

    def load_dictionary(self, char):
    """
    Loads a dictionary of words starting with a specific character from a file.
    This method supports caching to avoid reloading the same dictionary multiple
    times.
    
    Parameters:
    - char (str): The first character of the words to be loaded.
    
    Returns:
    - set: A set of words starting with the specified character.
    """
        if char in self.dictionary_cache:
            return self.dictionary_cache[char]
        dictionary_path = os.path.join(os.path.dirname(__file__), '..', 'dictionaries', f"{char}.txt")
        try:
            with open(dictionary_path, "r", encoding="utf-8") as file:
                words = set(file.read().splitlines())
                self.dictionary_cache[char] = words
                return words
        except FileNotFoundError:
            return set()

    def is_valid_word(self, word):
        """
    Determines if a given word is valid by checking if it exists in the
    dictionary loaded for its starting character.
    
    Parameters:
    - word (str): The word to check.
    
    Returns:
    - bool: True if the word is valid, False otherwise.
    """
        if not word:
            return False
        first_char = word[0]
        dictionary = self.load_dictionary(first_char)
        is_valid = word in dictionary
        return is_valid

    def apply_rules(self, word):
    """
    Applies stemming rules to a given word. The rules are designed to handle
    various grammatical structures in Punjabi, such as suffix stripping and
    replacements, based on the morphological characteristics of the word.
    
    Parameters:
    - word (str): The word to be stemmed.
    
    Returns:
    - str: The stemmed word.
    """
        for rule in self.rules:
            if word.endswith(rule["match"]):
                new_word = word[:-len(rule["strip"])] + rule["add"]
                if self.is_valid_word(new_word) or not self.is_valid_word(word):
                    return new_word
        return word

    def preprocess_text(self, text):
    """
    Cleans the input text by removing punctuation, special characters, and
    emojis, while preserving Punjabi characters, numbers, and words from
    other languages. Underscores are replaced with spaces to prevent word
    merging.
    
    Parameters:
    - text (str): The text to be cleaned.
    
    Returns:
    - str: The cleaned text.
    """
        text = text.replace('_', ' ')
        regex_pattern = r"[^\u0A00-\u0A7F0-9a-zA-Z\s]+"
        cleaned_text = re.sub(regex_pattern, '', text)
        return cleaned_text

    def stem_file(self, input_file_path, output_file_path):
        """
    Stems the content of a given input file and writes the stemmed text to an
    output file. This method allows processing of larger texts or entire documents
    stored in files.
    
    Parameters:
    - input_file_path (str): Path to the input file containing original text.
    - output_file_path (str): Path where the stemmed text will be saved.
    """
    
      try:
        # Open and read the input file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
        
        # Process (stem) the text
        stemmed_text = self.stem_text(input_text)
        
        # Write the stemmed text to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(stemmed_text)
        
        print(f"Processed text has been saved to {output_file_path}")
      except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
      except Exception as e:
        print(f"An error occurred: {e}")

    def stem_word(self, word):
    """
    Stems a single word after preprocessing it to remove any noise. This
    is a comprehensive method that combines cleaning and stemming for
    individual words.
    
    Parameters:
    - word (str): The word to be stemmed.
    
    Returns:
    - str: The stemmed word.
    """
        cleaned_word = self.preprocess_text(word)
        if cleaned_word in self.pronouns or cleaned_word in self.adverbs or cleaned_word in self.postpositions or cleaned_word in self.vocabulary or cleaned_word in self.names or cleaned_word in self.suffix:
            return cleaned_word
        return self.apply_rules(cleaned_word)

    def stem_text(self, text):
    """
    Stems a body of text, such as sentences or paragraphs, after preprocessing
    to remove noise. This method is suitable for text analysis and processing
    tasks that require stemming of multiple words in context.
    
    Parameters:
    - text (str): The text to be stemmed.
    
    Returns:
    - str: The stemmed text.
    """
        cleaned_text = self.preprocess_text(text)
        words = cleaned_text.split()
        stemmed_words = [self.stem_word(word) for word in words]
        return ' '.join(stemmed_words)

# Add your stemming rules in the `self.rules` list as needed.
