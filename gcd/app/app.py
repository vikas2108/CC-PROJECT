from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource
class Gcd(Resource): 
	def get(self, num1, num2):
		num1 = int(num1)
		num2 = int(num2)
		while num1!=num2:
			if num1>num2:
				num1,num2 = num1-num2,num2
			else:
				num1,num2 = num1,num2-num1
		return {'result': num1}

app = Flask(__name__)
api = Api(app)
api.add_resource(Gcd, '/<num1>/<num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5055,
		host="0.0.0.0"
	)
