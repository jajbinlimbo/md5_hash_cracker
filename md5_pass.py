import hashlib
import time as t

#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'


print("\n ==================================================================================")

print(r"""
               _ _____   _               _                                     _             
              | |  ___| | |             | |                                   | |            
 _ __ ___   __| |___ \  | |__   __ _ ___| |__   ___  ___    ___ _ __ __ _  ___| | _____ _ __ 
| '_ ` _ \ / _` |   \ \ | '_ \ / _` / __| '_ \ / _ \/ __|  / __| '__/ _` |/ __| |/ / _ \ '__|
| | | | | | (_| /\__/ / | | | | (_| \__ \ | | |  __/\__ \ | (__| | | (_| | (__|   <  __/ |   
|_| |_| |_|\__,_\____/  |_| |_|\__,_|___/_| |_|\___||___/  \___|_|  \__,_|\___|_|\_\___|_| by Jajbin Limbu  
                                                                                             
                                                                                             
""")

print("\n ==================================================================================")


flag = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print(color.PURPLE + "No file found")
    quit()
    
for word in pass_file:
    
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    
    t.sleep(0)
    print (color.GREEN + '[x] ' + color.CWHITE + word + color.CWHITE)
    t.sleep(0)
    print(color.GREEN + '[+] ' + color.CWHITE + digest + color.CWHITE)
    t.sleep(0)
    print(color.GREEN + '[+] ' + color.CWHITE + pass_hash + color.CWHITE)
    t.sleep(0)
    
    
    if digest == pass_hash:

        t.sleep(1)
        print(color.GREEN + '[!] ' + color.CWHITE + "password found" + color.CWHITE)
        print(color.GREEN + '[√] ' + color.CWHITE + "password is " + word + color.CWHITE)
        flag = 1
        break

if flag == 0:
    t.sleep(0.1)
    print(color.RED + '[!] ' + "password/passphrase is not in the list" + color.CWHITE)