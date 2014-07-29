import urllib2
import json
query = raw_input ( 'Query: ' )
query = urllib.urlencode ( { 'q' : query } )
response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query + '+site%3Awww.icd10data.com').read()
list1 = json.loads(response)

#print list1
results = list1['responseData'] ['results']

for result in results:
    title = result['title']
    code = title.split()
    url = result['url']   # was URL in the original and that threw a name error exception
    print code[4]
    print (title + url)
