import urllib
import urllib2

model = """
Name
    attr
    ---
    method
"""

url = "http://www.diagramadeclases.com.ar"
post = {'diagram_code': model}
data_post = urllib.urlencode(post)
response = urllib2.urlopen(url + '/draw', data_post)

if response.code == 200:
    print "Creando el digrama, acceda a la siguiente URL:"
    print "%s/%s" %(url, response.read())
else:
    print "Imposible acceder al recurso '%s'" %(url)
