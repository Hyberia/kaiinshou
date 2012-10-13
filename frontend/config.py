#!/usr/bin/python
# -*- coding: utf-8 *-*
#
#       Filename: config.py
#       Date:     2012-08-14
#       author:   Mathieu Charron <mathieu@hyberia.ca>
#       Project:  Kaiinshou
#
#       Copyright 2012 Hyberia Inc.
#
#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above copyright
#         notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the Hyberia Inc. nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import web
from pymongo import Connection

# Database configuration
#mongoURI = "mongodb://ganime:2EKY7BSN@127.0.0.1/registration-dev"
mongoURI = "mongodb://ganime:2EKY7BSN@127.0.0.1/registration"

# For testing puposes
#paypalAccount = "mathie_1345421600_biz@hyberia.ca"
#paypalUrl = "https://www.sandbox.paypal.com"
#paypalId = "9B3P56RWHB85Q"
paypalAccount = "finance@ganime.ca"
paypalUrl = "https://www.paypal.com"
paypalId = "SP2X3RHPES2HU"

cookieName = "ganime_cartid"
salt = "+828497786499849"
email = {
    "debug_from": "noreply@ganime.ca",
    "debug": "mathieu.charron@ganime.ca",
    "notice_from": "inscription@ganime.ca",
    }

# Web.py stuff
web.config.debug = True
#web.ctx.home = "https://secure.sajg.net/inscription"
web.ctx.home = "http://localhost/frontend/"
cache = False

# Initialize the MongoDB connection
connection = Connection(mongoURI)
DB = connection.registration