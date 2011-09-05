#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        models.event
# Purpose:     
#
# Author:      Andre
#
# Created:     Sep 4, 2011
# Copyright:   (c) Andre 2011
# License:     <your license>
#-------------------------------------------------------------------------------

from google.appengine.ext import db


class Event(db.Model):
    name = db.StringProperty(verbose_name="Name", required=True)
    organization = db.StringProperty(verbose_name="Organization", required=True)
    datetime = db.DateTimeProperty(verbose_name="DateTime", required=True)
    password = db.StringProperty(verbose_name="Password", required=True)