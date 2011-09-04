#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/server/ package)
# Purpose:     Contains all code for serving webpages to clients
#
# Author(s):   Andre Wiggins
#
# Created:     08/22/2011
# Copyright:   (c) Andre Wiggins 2011
# License:
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import time
import json


class HomePage(webapp.RequestHandler):

    def get(self):
        path = '../static/html/setup.html'
        template_values = {}
        self.response.out.write(template.render(path, template_values, True))


class SignInPage(webapp.RequestHandler):
    
    def get(self):
        path = '../static/html/signin.html'
        template_values = {'organization': 'Phi Sigma Pi', 'event': 'Rush Event'}
        self.response.out.write(template.render(path, template_values, True))


class RecordUser(webapp.RequestHandler):
    count = 0;
    
    def get(self):
        name = self.request.get('name')
        email = self.request.get('email')
        
        time.sleep(2);
        if RecordUser.count % 5 == 0:
            resultdata = {'status': 'error'}
        else:
            resultdata = {'status': 'success'}

        resultjson = json.dumps(resultdata)
        self.response.out.write(resultjson)
        RecordUser.count += 1;


def main():
    run_wsgi_app(app)


app = webapp.WSGIApplication([('/?', HomePage),
                              ('/event/?', SignInPage),
                              ('/signin/?', RecordUser)],
                              debug=True)


if __name__ == "__main__":
    main()