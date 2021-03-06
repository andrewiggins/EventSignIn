#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        server.setup
# Purpose:     RequestHandler for the SetupPage
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

from server import date_format_js as dformat, time_format_js as tformat, sepr_format_js as sep


class SetupPage(webapp.RequestHandler): #@UndefinedVariable - for Eclipse

    def get(self):        
        path = '../static/html/setup.html'
        template_values = {'dformat': dformat, 'tformat': tformat, 'sep':sep}
        self.response.out.write(template.render(path, template_values, True))