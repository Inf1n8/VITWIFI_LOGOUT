import requests
r=requests.post('http://phc.prontonetworks.com/cgi-bin/authlogout')
if(r.status_code==200):
    print('Successfully logged out')
else:
    print('Logout not successfull!')