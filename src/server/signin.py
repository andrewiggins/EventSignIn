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

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import datetime
import hashlib

from models import Event

class SignInPage(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def post(self):
        org = self.request.get('organization')
        eventname = self.request.get('event')
        date_str = self.request.get('date')
        date = datetime.datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")
        password = hashlib.sha256(self.request.get('password')).hexdigest()
        
        key_name = '.'.join([org, eventname, date_str])
        key = db.Key.from_path('Event', key_name)
        
        action = self.request.get('action')
        if action == 'create':
            event = Event(key=key,
                          name=eventname, 
                          organization=org, 
                          datetime=date,
                          password=password)
            event.put()
            
            path = '../static/html/signin.html'
            template_values = {'organization': org, 'event': eventname, 
                               'datetime': date.strftime("%m/%d/%Y %I:%M %p")}
            self.response.out.write(template.render(path, template_values, True))
        elif action == 'login':
            event = Event.get(key)
            if event is None: # Event does not exist
                self.response.out.write('Event Does Not Exist')
            elif password == event.password: # Event exist; correct password
                path = '../static/html/signin.html'
                template_values = {'organization': org, 'event': eventname}
                self.response.out.write(template.render(path, template_values, True))
            else: # Event exist; wrong password
                self.response.out.write('wrong password')
        else: #action malformed, show error
            self.response.out.write('no action')