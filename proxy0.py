#
# Dead-simple proxy-ish code to take a URL as a parameter, fetch the content thereof,
# and return the content
#
# Why would one need this, you may ask?
#
# Well the use case that initiated this project was as follows:
#
# A website has a static image link
# We want to serve that link from another site
# But the link is http://
# And the server's headers are whatevs
# And oftentimes these days, browsers are adamant to the point of obsession about cross-site links
# Typically they just refuse to serve http:// requests from within an https:// session
# Irregardless of CORS, CSFR etc
# So,
#
# Proxy0
#
# usage:
#
# proxy0hostOrIP?url=http://www.acme.com/random-image.jpg
#

