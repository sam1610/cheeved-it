#!/usr/bin/env python

import jinja2
import os
import datetime
import webapp2

from google.appengine.api import users


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class _BaseHandler(webapp2.RequestHandler):
  def initialize(self, request, response):
    super(_BaseHandler, self).initialize(request, response)
    self.user = users.get_current_user()
    if self.user:
      self.template_values = {
          'user': self.user,
          'is_admin': users.is_current_user_admin(),
          'logout_url': users.create_logout_url('/')}
    else:
      self.template_values = {'login_url': users.create_login_url(self.request.url)}

class AchievementsPage(_BaseHandler):
  def get(self):
    template = jinja_environment.get_template('achievements.template')
    self.response.out.write(template.render(self.template_values))

class CheeversPage(_BaseHandler):
  def get(self):
    template = jinja_environment.get_template('cheevers.template')
    self.response.out.write(template.render(self.template_values))    

class ProfilePage(_BaseHandler):
  def get(self):
    template = jinja_environment.get_template('profile.template')
    self.response.out.write(template.render(self.template_values))      

class HomePage(_BaseHandler):
  def get(self):
    template = jinja_environment.get_template('home.template')
    self.response.out.write(template.render(self.template_values))

app = webapp2.WSGIApplication([
  ('/achievements', AchievementsPage),
  ('/cheevers', CheeversPage),  
  ('/profile', ProfilePage),
  ('/', HomePage)],
  debug=True)
