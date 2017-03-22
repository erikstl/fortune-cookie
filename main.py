import webapp2


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
