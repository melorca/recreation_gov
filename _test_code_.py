import camping
import winsound
import time
import datetime
import smtplib
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


parks = ["234039", "234040", "234041"] #, "234156"]

# :: Lassen Campgrounds
# rem 234039 Manzanita Lake
# rem https://www.recreation.gov/camping/campgrounds/234039
# rem 234041 SUMMIT LAKE NORTH
# rem https://www.recreation.gov/camping/campgrounds/234041
# rem 234040 SUMMIT LAKE South
# rem https://www.recreation.gov/camping/campgrounds/234040
# Bute Lake, test park 234156

message = ""

for i in range(100): #168 at 300 sec = 14 hours
    print("Checking Campgrounds:", i+1, '(' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')')
    
    flag = False

    for park_id in parks:
        #print(camping.get_park_information(park_id, camping.valid_date("2021-06-11"), camping.valid_date("2021-06-14")),)
        
        output = camping.check_park(park_id, camping.valid_date("2021-06-11"), camping.valid_date("2021-06-14"), None, nights=2)
        print(park_id, output)
        if output[0] > 0: 
            flag = True
            message += str(output) + "\n"
            message += "\n https://www.recreation.gov/camping/campgrounds/" + park_id
    if flag:
        winsound.PlaySound("C:\\Windows\\Media\\tada.wav", winsound.SND_FILENAME)
        send_mail(message,  "Camping Available")
    
    print('sleep')
    time.sleep(300)

#flag = True




