from google.appengine.ext import ndb


class Person(ndb.Model):
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    email = ndb.StringProperty()

    @property
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email
        }
