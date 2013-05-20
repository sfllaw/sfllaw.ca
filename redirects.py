#!/usr/bin/env python2.7

from collections import OrderedDict

import webapp2


PERMANENT_REDIRECTS = OrderedDict([
    ('/~sfllaw/', '/'),
    ('/programs/index.html', '/freesoftware.html'),
])

app = webapp2.WSGIApplication(
    [webapp2.Route(src, webapp2.RedirectHandler, defaults={'_uri': dst,
                                                           '_code': 301})
     for src, dst in PERMANENT_REDIRECTS.iteritems()],
    debug=False
)
