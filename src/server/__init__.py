#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        __init__.py (for src/server/ package)
# Purpose:     Contains all code for serving webpages to clients
#
# Author(s):   Andre Wiggins
#
# Created:     08/22/2011
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

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

datetime_format_py = "%m/%d/%Y %I:%M %p"
date_format_js = "mm/dd/yy"
time_format_js = "hh:mm tt"
sepr_format_js = " "

from setup import SetupPage
from signin import SignInPage
from record import RecordUser


def main():
    run_wsgi_app(app)


app = webapp.WSGIApplication([('/?', SetupPage), #@UndefinedVariable - for Eclipse
                              ('/event/?', SignInPage),
                              ('/signin/?', RecordUser)],
                              debug=True)


if __name__ == "__main__":
    main()