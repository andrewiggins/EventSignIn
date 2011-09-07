#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        server.download
# Purpose:     Handles request to download an event's signin.
#
# Author:      Andre Wiggins
#
# Created:     Sep 6, 2011
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

import StringIO

from models import Event

class DownloadCSV(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def get(self):
        org = self.request.get('organization')
        eventname = self.request.get('event')
        datetime = self.request.get('datetime')
        key_name = '.'.join([org, eventname, datetime])
        key = db.Key.from_path('Event', key_name)
        
        event = Event.get(key)
        users = event.user_set
        
        output = StringIO.StringIO()
        output.write('%s,%s,%s\n' % (org, eventname, datetime))
        output.write('%s, %s\n' % ('Name', 'Email'))
        for user in users:
            output.write("%s, %s\n" % (user.name, user.email))
        
        filename = "%s - %s SignIn.csv" % (org.title(), eventname.title())
        self.response.headers['Content-Type'] = 'text/csv'
        self.response.headers['Content-Disposition'] = 'attachment; filename="%s"' % filename
        
        self.response.out.write(output.getvalue())