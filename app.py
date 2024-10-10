from flask import Flask
from flask_restful import Resource,Api,reqparse
from flask_cors import CORS
import json
from modules.function import *
# import Synonym

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Synonym(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument('word',
                            required = True,
                            help='word arg cannot be empty')
        parser.add_argument('lan',
                            required=True,
                            help='lang arg cannot be empty')


        arguments = parser.parse_args()
        word_arg = arguments['word']
        lang_arg = arguments['lan']
        print(word_arg)
        print(lang_arg)
        print('----')
        try:
            # output = get_synonyms_edu(word_arg,lang_arg)
            output = syno_multiple_language_offline(word_arg,lang_arg)
            print(output)
        except:
            return { 'message':'check your internet connection' }  , 404
        return output, 200

class Grammer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word',
                            required=True,
                            help='word arg cannot be empty')

        arguments = parser.parse_args()
        word = arguments['word']
        list = grammer_check(word)

        print(list)
        filtered_list = sorted(list, key=lambda x: x['offset'], reverse=False)

        # list.sorted(key=lambda x: x['offset'], reverse=False)
        # filtered_list = []
        # for item in list:
        #     print(item['issue_type'])
        #     if item['issue_type'] == 'misspelling':
        #         item['replacements'] = []
        #     filtered_list.append(item)

        print()
        ###########################
        # global tempWord
        # tempWord = word
        #
        # sentence = ""
        #
        # for item in list:
        #
        #     sub = word[item['offset']:item["offset"] + item['error_length']]
        #     new = tempWord.replace(sub,"<span [class.underlined]='underlined'>"+sub+"</span>")
        #     tempWord = new
        #     sentence = new
        #     item['html'] = sentence
        #
        # print(sentence)
        # print(tempWord)
        ###########################

        # for index,item in enumerate(list):
        #     item['index'] = index

        return filtered_list,200
class SpellChecker(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word',
                            required=True,
                            help='word arg cannot be empty')

        arguments = parser.parse_args()
        word = arguments['word']
        output = spellcheck(word)

        for alt in output:
            if word == alt['word']:
                output.remove(alt)
        print(output)

        return output


api.add_resource(Synonym, '/syn')
api.add_resource(Grammer,'/grammer')
api.add_resource(SpellChecker,'/spellcheck')
app.run(host='0.0.0.0')
