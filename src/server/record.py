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

from google.appengine.ext import webapp

import time
import json

class RecordUser(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    count = 0;
    
    def get(self):
        name = self.request.get('name')
        email = self.request.get('email')
        
        # Add User add code here
        time.sleep(2);
        if RecordUser.count % 5 == 0:
            resultdata = {'status': 'error'}
        else:
            resultdata = {'status': 'success'}

        resultjson = json.dumps(resultdata)
        self.response.out.write(resultjson)
        RecordUser.count += 1;
