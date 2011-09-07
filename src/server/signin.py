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

import datetime as datetimefuncs
import hashlib

from server import datetime_format_py as dtformat
from models import Event


class SignInPage(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def post(self):
        org = self.request.get('organization')
        eventname = self.request.get('event')
        date_str = self.request.get('datetime')
        datetime = datetimefuncs.datetime.strptime(date_str, dtformat)
        
        key_name = '.'.join([org, eventname, date_str])
        key = db.Key.from_path('Event', key_name)
        
        action = self.request.get('action')
        event = Event.get(key)
        if action == 'create':
            newpassword = hashlib.sha256(self.request.get('newpassword')).hexdigest()
            
            if event is None:                
                event = Event(key=key,
                              name=eventname, 
                              organization=org, 
                              datetime=datetime,
                              password=newpassword)
                event.put()
                
                path = '../static/html/signin.html'
                template_values = {'organization': org, 'event': eventname, 
                                   'datetime': date_str}
                self.response.out.write(template.render(path, template_values, True))
            else:
                self.response.out.write('Event already exist. \nDid you mean to login to the event?')
        elif action == 'login':
            password = hashlib.sha256(self.request.get('password')).hexdigest()
            
            if event is None: # Event does not exist
                header = ('Event does not exist. \nDid you mean to create it?'+
                          ' Did you type in all the information correctly:\n')
                eventinfo = ('\nOrganization: %s \nEvent: %s \nDate/Time: %s' 
                             %(org, eventname, date_str))
                
                self.response.headers.add_header('Content-Type', 'text/plain')
                self.response.out.write(header+eventinfo)
            elif password == event.password: # Event exist; correct password
                path = '../static/html/signin.html'
                template_values = {'organization': org, 'event': eventname, 
                                   'datetime': date_str, 'users': event.user_set}
                self.response.out.write(template.render(path, template_values, True))
            else: # Event exist; wrong password
                self.response.out.write('Bad Event/Password Combination.')
                
        else: #action malformed, show error
            self.response.out.write('Server Error. Please try again. (Invalid '+
                                    'value for "action": %s' % action)