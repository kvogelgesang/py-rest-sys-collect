#!/usr/bin/env python3

import sys
sys.path.append("../python")
sys.path.append("src/main/python")
from flask import Flask

class RestSysCollectorService():

    app = Flask(__name__)

    @staticmethod
    @app.route('/')
    def hello_world():
        return "Hello World!"

    def run_app(self, debug=False):
        self.app.run(debug=debug)


if __name__ == '__main__':
    RestSysCollectorService().run_app()