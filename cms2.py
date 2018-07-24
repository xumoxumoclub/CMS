import requests
import re
from xml.etree import ElementTree as ET
f = open('domain.txt','r')
d = f.readlines()

ht = 'http://'




def chkUrl(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	try:
		response = requests.get(url, headers=headers)
	#code = (response.status_code)
		response.connection.close()	
		return response
	except:
		print  url + " not found"
	
	

				
for i in d:
	v = {'/joomla.xml','/language/en-GB/en-GB.xml','/readme.html','/CHANGELOG.txt','/'}
	for a in v:
		c = chkUrl(ht + i.strip() + a)
		if c.status_code == 302:
			print ht + i.strip() + " Redirecting"
		if c.status_code == 200:
			#print ht + i.strip() + a + " " + str(c.status_code)
			if a == '/joomla.xml':
				try:
					rawdata=ET.fromstring(c.content)
					result= rawdata.find('version').text
				except:
					break
				
				
		#root = ET.fromstring('version')
				print ht + i.strip() + a + " joomla " + result
				break
			elif a == '/language/en-GB/en-GB.xml':
				try:
					rawdata=ET.fromstring(c.content)
					result= rawdata.find('version').text
				except:
					break
				
		
				print ht + i.strip() + a + " joomla " + result
				break
			elif a == '/readme.html':
				rawdata = c.content
				for line in rawdata.split("\n"):
					if 'Version' in line:
						print ht + i.strip() + a + " wordpress " + line.split(">")[1]
						break
			elif a == '/CHANGELOG.txt':
				#print a
				rawdata = c.content
			
				v = rawdata.split("-",1)[0]
				#print line
				if 'Drupal' in v.strip():		
					print ht + i.strip() + a + "  " + v.strip()
				break
			elif a == '/':
				#print a
				rawdata = c.content
			
				for line in rawdata.split("\n"):
					if 'content="WordPress' in line:
						vers = line.split('content="')[1]
						fn = vers.strip('" />')
						
						if re.match(r"^\w+ \d+\.\d+\.\d+",fn):
							
							print ht + i.strip() + " " +fn
						
		
	
#print(response.status_code)

	
	
			

		
		
	
