import webapp2
from google.appengine.ext import db

class A(db.Model):
  a = db.BooleanProperty()
  n = db.IntegerProperty()

class MainHandler(webapp2.RequestHandler):

  def get(self):  # pylint:disable-msg=invalid-name
    messages = []
    
    a = A(a = True)
    b = A(a = True)

    messages.append('hello')
    messages.append(a == b)
    messages.append(dir(a))
    messages.append(db.to_dict(a))
    messages.append(db.model_to_protobuf(a))
    messages.append(db.model_to_protobuf(a).ByteSize())
    messages.append(db.model_to_protobuf(a).Encode())
    messages.append(len(db.model_to_protobuf(a).Encode()))

    messages.append(db.model_to_protobuf(a) == db.model_to_protobuf(b))
    messages.append(type(db.model_to_protobuf(a)).__name__)
    messages.append(dir(type(db.model_to_protobuf(a))))

    self.response.write('<br/>'.join(map(str,messages)))

APP = webapp2.WSGIApplication([
    ('/.*', MainHandler),
], debug=True)

