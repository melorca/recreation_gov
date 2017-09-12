from __future__ import print_function

import urllib2
import re
import time
import smtplib
import datetime
import winsound
import my_mail

def send_mail(text = "Testing e-mail", subject = "Hello!"):
	"""Use a dummy account  and allow
	account to be accessed by 'less secure appps'
	https://www.google.com/settings/security/lesssecureapps.
	
	my_mail.py:
	
		fromaddr = "sender@gmail.com"
		toaddrs  = ["user@gmail.com"]
		username = "sender@gmail.com"
		password = "password"
		
	"""

    fromaddr = my_mail.fromaddr
    toaddrs  = my_mail.toaddrs
    msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s

                """ % (fromaddr, ", ".join(toaddrs), subject, text)

    username = my_mail.username
    password = my_mail.password
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    #server.quit()
    server.close()

PARK_IDS = {
    #'north pines': ('70927',80),  #yosemite
    #'lower pines': ('70928',73),  #yosemite
    #'upper pines': ('70925',235), #yosemite
	#'dry gulch': ('73750',2),  #yosemite
	#'big meadow': ('151140',10), # test
	#'sunset': ('110283', 150), #kings
	#'dorst creek': ('70940', 177), #sequoia
	#'lodgepole': ('70941', 181) #sequoia
	#'camp sherman': ('72099', 9), #Eclipse
	#'whispering falls': ('127540', 16), #Eclipse
	#'humbug': ('127940', 22), #Eclipse
	#'santiam flats': ('131440', 32) #Eclipse
	# 'PLASKETT CREEK': ('70161',10), #BigSur  Out, false positive with group camp
	# 'KIRK CREEK': ('71993',10), #BigSur
	'Kirby Cove': ('70972',10), #Golden Gate
	# 'Point Reyes': ('72393', 10), #Point reyes
	# "Meeks Bay": ('71664', 10), #Tahoe
	# "Fallen Leaf": ('71531', 10), #Tahoe
	# "Kaspian": ('71663', 10), #Tahoe	
	# "Nevada Beach": ('71530', 10), #Tahoe
	# "William Kent": ('71662', 10), #Tahoe
	# "Prosser Family": ('75053', 10), #Outer Tahoe
	# "South Shore": ('74125', 10), #Outer Tahoe
	# "Wolf Creek": ('70757', 10), #Outer Tahoe
	# "Yellow Jacket": ('70359', 10), #Outer Tahoe
	# "Sunset Union": ('70310', 10), #Outer Tahoe
	# "Fashoda" : ('74162', 10) #Outer Tahoe
	
}

Dates = ['09/22/2017']#, '06/23/2017']


url = "https://www.recreation.gov/campsiteCalendar.do?page=matrix&calarvdate=%s&contractCode=NRSO&parkId=%s&sitepage=true&startIdx=%s"

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

flag = False
message = "Camping Available:\n"

for i in range(168): #14 hours
	print("Checking Campgrounds:", i+1, '(' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')')
	
	for p_name, p_info in PARK_IDS.iteritems():
		p_id,sites = p_info
		
		for date in Dates:
			for s in [0]:#range(sites/25):
				raw = opener.open(url%(date, p_id, str(s*25)))
				page = raw.read()
				
				pat = re.compile("<div class='loopName' title=.*</td>\n<td class='status a") # 1 day
				#pat = re.compile("<div class='loopName' title=.*</td>\n<td class='status a.*</td>\n<td class='status a") # 2 days
				#pat = re.compile("<div class='loopName' title=.*</td>\n<td class='status a.*</td>\n<td class='status a.*</td>\n<td class='status a") # 3 days
				
				l = pat.findall(page)			


				if l:
					flag = True
					print(p_name,date)
					print(url%(date, p_id, str(s*25)))
					message += p_name + "\n" + url%(date, p_id, str(s*25)) + "\n"
				
				
	if flag:
		winsound.PlaySound("C:\\Windows\\Media\\tada.wav", winsound.SND_FILENAME)
		print("e-mail sent!\n\n" + message)
		send_mail(message,  "Camping Available")
		message = "Camping Available:\n"
		flag = False
		
	print('sleep')
	time.sleep(300)
	
# send_mail("test message","test subject") #It works!

##############
# Sample text follows
##############


"""
<div id='maplinkicon_205068_816044415'><a href='/camping/Upper_Pines/r/campgroundMap.do?camparea=82267466&amp;selectedSiteRb=205068&amp;contractCode=NRSO&amp;parkId=70925' class='sitemarker'  id='205068_816044415'  onclick='showProgressBar("contentProgressBar","Retrieving facility maps ...", null, "contentArea"); return true;'  >Map
<img src='/images/type_rv.gif'  id='i_205068_816044415' width='28' height='28' alt='003, STANDARD NONELECTRIC' title='003, STANDARD NONELECTRIC'></a></div>
<div class='siteListLabel'><a href='/camping/Upper_Pines/r/campsiteDetails.do?siteId=205068&amp;contractCode=NRSO&amp;parkId=70925'   onclick='showProgressBar("contentProgressBar","Retrieving site details ...", null, "contentArea"); return true;'  onmouseover='showKeyAttr(this, "205068", "false");'  onmouseout='closeKeyAttr();'>003</a></div></td>
<td >
<div class='loopName' title='UPPER PINES '>UPPER PINES </div></td>
<td class='status r' >R</td>
<td class='status r sat' >R</td>
<td class='status r sun' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r sat' >R</td>
<td class='status r sun' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td>
<td class='status r' >R</td></tr>
<tr class='separator'>
<td colspan='16' ></td></tr>

<tr>
<td class='sn' >
"""

"""<td class='status a' ><a href='/camping/Lower_Pines/r/campsiteDetails.do?siteId=203378&amp;contractCode=NRSO&amp;parkId=70928&amp;offset=0&amp;arvdate=9/27/2017&amp;lengthOfStay=1' class='avail'  id='avail_203378_13'  onclick='showProgressBar("contentProgressBar","Retrieving site details ...", null, "contentArea"); return true;'  >A</a></td>"""