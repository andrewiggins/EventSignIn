#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        models.user
# Purpose:     
#
# Author:      Andre
#
# Created:     Sep 4, 2011
# Copyright:   (c) Andre 2011
# License:     <your license>
#-------------------------------------------------------------------------------

from google.appengine.ext import db
from event import Event

class User(db.Model):
    name = db.StringProperty(verbose_name="Name", required=True);
    email = db.EmailProperty(verbose_name="Email", required=True);
    event = db.ReferenceProperty(reference_class=Event, verbose_name="Event", required=True);