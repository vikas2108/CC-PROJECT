from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource
class Lcm(Resource): 
	def get(self, num1, num2):
		num1 = int(num1)
		num2 = int(num2)
		if num1 == 0 or num2 == 0:
			lcm = 0
			return{'result': lcm}
		for i in range(max(num1, num2), 1 + (num1 * num2)):
			if i % num1 == i % num2 == 0:
				lcm = i
				break
		return{'result': lcm}	

app = Flask(__name__)
api = Api(app)
api.add_resource(Lcm, '/<num1>/<num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5057,
		host="0.0.0.0"
	)
