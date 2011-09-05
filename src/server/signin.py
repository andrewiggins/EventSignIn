#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        server.signin
# Purpose:     RequestHandler for the SignInPage
#
# Author:      Andre Wiggins
#
# Created:     Sep 4, 2011
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


from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class SignInPage(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def get(self):
        path = '../static/html/signin.html'
        template_values = {'organization': 'Phi Sigma Pi', 'event': 'Rush Event'}
        self.response.out.write(template.render(path, template_values, True))