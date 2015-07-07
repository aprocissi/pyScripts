#!/usr/bin/python
from urllib2 import Request, urlopen, URLError, HTTPError
from xml.dom.minidom import parse
from sys import argv

numErrors = 0
dom = parse(argv[1])

loc = dom.getElementsByTagName('loc')
for index, line in enumerate(loc):
    url = loc[index].firstChild.nodeValue
    
    try:
        response = urlopen(url)
    except HTTPError as e:
        print '\n%d Error: Not found' %e.code
        print '%s\n' %url
        numErrors += 1
    except URLError as e:
        print '\n', e.reason
        print '%s Could not be reached.\n' %url
        numErrors += 1
    else:
        print response.getcode(), url

print '\n%d bad urls found' %numErrors
