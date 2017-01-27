#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, random

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        lucky_number = random.choice(range(1,100))
        number_sentence = 'Your lucky number is: ' + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"
        button_label = "Get a new number."
        button = "<button>" + button_label + "</button>"
        self.response.write(header + number_paragraph + button)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for tryign to log in!")

routes = [
    ('/', MainHandler),
    ('/login', LoginHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
