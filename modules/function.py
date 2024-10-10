from educalingoDictionary import EducalingoDictionary
from nltk.corpus import wordnet

#grammer check
import language_check as lc
import collections
from model.Replacement import Replacement


#SpellCheck
import textblob as tb

import json,ast

# requires internet connection
# en / fr
def get_synonyms_edu(word,lang):
    my_dictionary = EducalingoDictionary()
    my_dictionary.set_language(lang)
    my_dictionary.search_word(word=word)
    synonyms = my_dictionary.get_synonyms()
    return synonyms

# requires internet connection
# en / fra / arb
def get_synonums_multilang_2(word):

    synonyms = []

    wordset = wordnet.synsets(word)
    for word in wordset:
        for ls in word.lemma_names(lang='fra'):

            synonyms.append(ls)
    synonym = list(dict.fromkeys(synonyms))
    # print("get_synonums_multilang_2()")
    return synonym

#  multiple language synonyms except irish
#  nltk.download_gui()
#  nltk.download9('all')
def syno_multiple_language_offline(word,lang):
    # Getting list of similar word in given lang to english
    syno = []
    for lm in wordnet.lemmas(word, lang=lang):
        syno.append(lm.synset().name().split('.')[0])
    syno = list(dict.fromkeys(syno))

    synonyms = []
    if len(syno) != 0:
        wordset = wordnet.synsets(syno[0])
        for syno[0] in wordset:
            for ls in syno[0].lemma_names(lang=lang):
                print(ls)
                synonyms.append(ls.replace('_',' '))

        result =  list(dict.fromkeys(synonyms))
        return result
    else:
        return synonyms

def to_dict(data):
    str = json.dumps(data)
    str_eval = ast.literal_eval(str)
    dict = json.loads(str_eval)
    return dict

def grammer_check(text):
    tool = lc.LanguageTool('en-US')
    # text = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
    matches = tool.check(text)
    # text_list = list(text)

    list = []
    for match in matches:
        replacement = Replacement(match)
        replacement_dict = replacement.to_dict()

        print(f'Replacement for text : {text}')
        replacement.print_details()

        list.append(replacement_dict)

    return list



def spellcheck(word):
    text = tb.Word(word)
    output = text.spellcheck()

    list = []

    for out in output:

        word = out[0]
        confidence = out[1]

        item = {
            'word':word,
            'confidence':confidence
        }
        list.append(item)
        print()

    # print(list)
    return list