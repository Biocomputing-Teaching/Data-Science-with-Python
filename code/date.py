import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:
        print line

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('jvf666@gmail.com','jordi.villafreixa@gmail.com',
                """To: jordi.villafreixa@gmail.com
From: jvf666@gmail.com

Hola perola
""")
server.quit()
