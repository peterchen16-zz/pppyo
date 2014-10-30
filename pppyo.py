import webapp2
from google.appengine.ext.webapp import template
from webapp2_extras import json
from models import *
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):
    def get(self):
        html = template.render('onepage/templates/index.html', {})
        self.response.out.write(html)

class StartProject(webapp2.RequestHandler):

    def post(self):
        data_str = self.request.get('json')
        data_str = data_str.replace('%40', '@')
        data = data_str.split('&')
        data_dict = {}
        for info in data:
            info = info.split('=')
            data_dict[info[0]] = info[1]
        project = Project(project_type = data_dict['project_type'], project_desc = data_dict['project_description'], project_scale = data_dict['project_scale'], contact_name = data_dict['contact_name'], contact_email = data_dict['email'])
        project.put()
        sender = data_dict['contact_name'] + " <" + data_dict['email'] + ">"
        try:
            mail.send_mail(sender=sender,
                  to="PPPYO pppyo@pppyo.co",
                  subject="New Project",
                  body=data_str)
            self.response.content_type = 'application/json'
            obj = {
                'success': 'success',
              } 
            self.response.write(json.encode(obj))
        except:
            self.error(500)


app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/start_project', StartProject)
                               ],
                              debug=True)