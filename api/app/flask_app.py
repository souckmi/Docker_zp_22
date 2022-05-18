from flask import Flask
from flask_restful import Resource, Api
from utils import *

app=Flask(__name__)
api=Api(app)

class IndexPage(Resource):
    def get(self):
        message="Vitejte v mem zapoctovem programu."
        return message

class Generate(Resource):
    def get(self,filename,max):
        return save_txt(filename, max)

class GetFile(Resource):
    def get(self,filename):
        return get_data(filename)

api.add_resource(Generate,'/generate/<string:filename>,<int:max>')
api.add_resource(GetFile,'/getfile/<string:filename>')
api.add_resource(IndexPage,"/")

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)