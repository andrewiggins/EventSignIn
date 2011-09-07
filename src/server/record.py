#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        server.record
# Purpose:     RequestHandler for the RecordUserPage
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
from django.utils import simplejson as json #@UnresolvedImport - for Eclipse

import logging
import traceback

from models import User

class RecordUser(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def get(self):
        org = self.request.get('organization')
        event = self.request.get('event')
        datetime = self.request.get('datetime')
        
        name = self.request.get('name')
        email = self.request.get('email')
        
        user_key_name = name+':'+email
        userkey = db.Key.from_path('User', user_key_name)
        
        event_key_name = '.'.join([org, event, datetime])
        logging.warning(event_key_name)
        eventkey = db.Key.from_path('Event', event_key_name)
        
        try:
            user = User(key=userkey,
                        name=name,
                        email=email,
                        event=eventkey)
            user.put()
        except db.Error:
            resultdata = {'status': 'error'}
            logging.error(traceback.format_exc())
        else:
            resultdata = {'status': 'success'}

        resultjson = json.dumps(resultdata)
        self.response.out.write(resultjson)
