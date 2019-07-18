import sys, os, requests

#this file gets imported by djserver
import djhelpers as dj

HOST="mongodb://127.0.0.1:27017"
DB="local"
dj.mongo_set(HOST, DB)

djangle_endpoints=["proxy0"]

#
# Create endpoint /version
#
def proxy0_version():
    return dj.json({'version': "0.0.001"})

#
# Create endpoint /api?search=abcdef123
#
# http://localhost/example/testy/arg1?arg2=3
def proxy0_testargs(*args, **kw):
    return dj.json({"args": args, "keywords": kw})

def proxy0_get(url):
    resp = requests.get(url)
    return dj.json({"response": resp.status_code, "size": len(resp.content), "type": resp.headers['Content-Type']})