#!/usr/bin/env python

import jinja2
import os
import datetime
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class HomePage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('home.template')
    self.response.out.write(template.render(self.template_values))

app = webapp2.WSGIApplication([
  ('/', HomePage)],
  debug=True)
