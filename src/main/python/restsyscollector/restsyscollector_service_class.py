#!/usr/bin/env python3

# See: http://flask.pocoo.org/
# See: http://flask.pocoo.org/docs/0.11/quickstart/#a-minimal-application
# See: http://blog.luisrei.com/articles/flaskrest.html

import sys
sys.path.append("../python")
sys.path.append("src/main/python")
from flask import Flask, render_template, json, request, Response, jsonify

class RestSysCollectorService():

    app = Flask(__name__)

    @staticmethod
    @app.route('/')
    def hello_world():
        return "Hello World!"

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)
        # Test: curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/hello/Kay

    @staticmethod
    @app.route('/helloapi', methods=['GET'])
    def api_hello():
        data = {
            'hello': 'api',
            'number': 3
        }
        if 'firstname' in request.args:
            data['firstname'] = str(request.args['firstname'])
        if 'lastname' in request.args:
            data['lastname'] = str(request.args['lastname'])

        # Test: curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/helloapi?firstname=John
        #js = json.dumps(data)
        #resp = Response(js, status=200, mimetype='application/json')
        resp = jsonify(data)
        resp.status_code = 200

        resp.headers['Link'] = 'http://wwww.onlinetech.de'

        return resp

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @staticmethod
    @app.route('/messages', methods=['POST'])
    def api_message():

        if request.headers['Content-Type'] == 'text/plain':
            return "Text Message: " + request.data

        elif request.headers['Content-Type'] == 'application/json':
            return "JSON Message: " + json.dumps(request.json)
            # Test: curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/messages -d '{"message":"Hello Data"}'

        elif request.headers['Content-Type'] == 'application/octet-stream':
            f = open('./binary', 'wb')
            f.write(request.data)
            f.close()
            return "Binary message written!"

        else:
            return "415 Unsupported Media Type ;)"

    def run_app(self, debug=False):
        self.app.run(debug=debug)


if __name__ == '__main__':
    RestSysCollectorService().run_app()