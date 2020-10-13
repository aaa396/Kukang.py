#--coding: utf-8 --
import os
import sys
os.system('clear')
os.system('figlet kukang')
print "---------------------------"
print ":      🔥 Welcome 🔥      :"
print ":-------------------------:"
print ":      Author:aaa         :"
print ":-------------------------:"
print ":    silahkan digunakan   :"
print ":-------------------------:"
print ":[1] Socialsploit         :"
print ":-------------------------:"
print ":[2] Metasploit           :"
print ":-------------------------:"
print ":[3] RED HAWK             :"
print ":-------------------------:"
print ":[4] Osif                 :"
print ":-------------------------:"
print ":[5] hammer               :"
print ":-------------------------:"
print ":[6] Weeman               :"
print ":-------------------------:"
print ":[7] DARK FB 1.8          :"
print ":-------------------------:"
print ":[8] Exit                 :"
print ":-------------------------:"
pilih = raw_input("pilih:")
if pilih == "1":
   os.system('pkg update && pkg upgrade -y')
   os.system('pkg install -y git')
   os.system('git clone https://github.com/Cesar-Hack-Gray/SocialSploit')
   print "pengintallan selesai"
   print " selanjutnya ketik cd SocialSploit"
   print " dan ./Sploit perhatikan hurufnya"
   print "script ini digunakan untuk phising"
elif pilih == "2":
   os.system('pkg update && pkg upgrade -y')
   os.system('pkg install curl -y')
   os.system('curl -LO https://raw.githubusercontent.com/Techzindia/Metasploit_For_Term>')
   os.system('sh metasploitTechzindia.sh')
   print "pengintallan selesai"
   print " selanjutnya ketik cd metasploit-framework"
   print " dan ketik ./msfconsole "
elif pilih == "3":
   os.system('apt update && apt upgrade -y')
   os.system('apt install git && apt install php -y')
   os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
   os.system('chmod +x rhawk.php')
   print "pengintallan selesai"
   print " selanjutnya ketik cd RED_HAWK "
   print "lalu ketik php rhawk.php"
elif pilih == "4":
   os.system('apt update && apt upgrade -y')
   os.system('apt install git -y')
   os.system('git clone https://github.com/CiKu370/OSIF.git')
   os.system('pip2 install -r requirements.txt')
   print "pengintallan selesai"
   print "selanjutnya ketik cd OSIF "
   print "lalu ketik python2 osif.py "
   print "dan ketik token untuk memasukan akun facebook kalian"
elif pilih == "5":
   os.system('apt update -y')
   os.system('apt upgrade -y')
   os.system('apt install python -y')
   os.system('apt install git -y')
   os.system('apt install dnsutils -y')
   os.system('git clone https://github.com/Pavithran-R/Hammer/')
   print "pengintallan selesai"
   print "selanjutnya ketik cd Hammer"
   print "lalu ketik python hammer.py "
elif pilih == "6":
   os.system('apt update &&  apt upgrade -y')
   os.system('pkg install git')
   os.system('git clone https://github.com/evait-security/weeman')
   os.system('chmod 777 weeman.py')
   print "selanjutnya ketik cd weeman"
   print "lalu ketik python2 weeman.py"
   print "untuk membuat web phising nya ketik set url [nama web tersebut]"
   print "contoh set url http://www.facebook.com lalu ketik set port 8080"
   print "lalu ketik set action_url [nama web tersebut] contoh set action_url https://facebook.com"
   print "dan untuk menjalankan nya ketik run"
elif pilih == "7":
   os.system('pkg install python2')
   os.system('pkg install git')
   os.system('git clone https://github.com/Mr-xDODOL/1.8')
   os.system('pip2 install -r requirements.txt')
   print "lalu ketik cd 1.8 "
   print "dan ketik python2 dark.pyc"
elif pilih == "8":
   os.system('exit')

