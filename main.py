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

def getRandomFortune():

    fortunes = [
        "You will do well.",
        "You will do bad.",
        "Eh."
                ]
    return random.choice(fortunes)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = getRandomFortune()
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = random.choice(range(1,100))
        number_sentence = 'Your lucky number is: ' + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"

        button_label = "Get a new number."
        button = "<button>" + "<a href='.'>" + button_label + "</a>"+ "</button>"

        content = header + fortune_paragraph + number_paragraph + button

        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for tryign to log in!")

routes = [
    ('/', MainHandler),
    ('/login', LoginHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
