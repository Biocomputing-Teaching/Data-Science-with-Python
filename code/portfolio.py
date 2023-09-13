import sys
import urllib
from WebParser import *
# baixa la web resum de la borsa
temp=urllib.quote("0#MCE.MC")
data=urllib.urlencode({"Page":"VAN_HOME", "Group1":temp, "Symbol1":"010060.IBEX",\
                       "APP":"VAN","LANGUAGE":"ES"})
f = urllib.urlopen("http://finanzas.lavanguardia.es/index.xhtml?"+data)
# llegeix el contingut
s = f.read()
# Try and process the page.
# The class should have been defined first, remember.
myparser = MyParser()
myparser.parse(s)

# Get the hyperlinks.
print myparser.get_hyperlinks()
print myparser.get_descriptions()
