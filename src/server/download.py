#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        server.download
# Purpose:     
#
# Author:      Andre
#
# Created:     Sep 6, 2011
# Copyright:   (c) Andre 2011
# License:     <your license>
#-------------------------------------------------------------------------------

from google.appengine.ext import db
from google.appengine.ext import webapp

import StringIO

from models import Event

class DownloadCSV(webapp.RequestHandler): #@UndefinedVariable - for Eclipse
    
    def get(self):
        org = self.request.get('organization')
        eventname = self.request.get('event')
        date = self.request.get('datetime')
        key_name = '.'.join([org, eventname, date])
        key = db.Key.from_path('Event', key_name)
        
        event = Event.get(key)
        users = event.user_set
        
        output = StringIO.StringIO()
        output.write('%s,%s,%s\n' % (org, eventname, date))
        output.write('%s, %s\n' % ('Name', 'Email'))
        for user in users:
            output.write("%s, %s\n" % (user.name, user.email))
        
        filename = "%s - %s.csv" % (org.title(), eventname.title())
        self.response.headers['Content-Type'] = 'text/csv'
        self.response.headers['Content-Disposition'] = 'attachment; filename="%s"' % filename
        
        self.response.out.write(output.getvalue())