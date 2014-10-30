from google.appengine.ext import ndb

class Project(ndb.Model):
	datetime_created = ndb.DateTimeProperty(auto_now_add=True)
	project_type = ndb.StringProperty()
	project_desc = ndb.StringProperty()
	project_scale = ndb.StringProperty()
	contact_name = ndb.StringProperty()
	contact_email = ndb.StringProperty()
	started_at = ndb.DateTimeProperty()
	finished_at = ndb.DateTimeProperty()