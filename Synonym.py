from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from modules.function import *

# app = Flask(__name__)
# api = Api(app)

#
# class Synonym(Resource):
#     def post(self):
#
#         parser = reqparse.RequestParser()
#         parser.add_argument('word',
#                             required = True,
#                             help='word arg cannot be empty')
#         parser.add_argument('lan',
#                             required=True,
#                             help='lang arg cannot be empty')
#
#
#         arguments = parser.parse_args()
#         word_arg = arguments['word']
#         lang_arg = arguments['lan']
#
#         output = get_synonyms_edu(word_arg,lang_arg)
#
#         return output, 200