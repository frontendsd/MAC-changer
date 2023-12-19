#!/usr/bin/python

# import re
#
# pattern = r'\b\d+\b'  # Example pattern to match one or more digits
# text = 'There are 123 apples and 456 oranges.'
# matches = re.findall(pattern, text)
# print(matches)


# import requests
#
# url = 'https://www.example.com'
# response = requests.get(url)
# print(response.text)


# import os
#
# current_directory = os.getcwd()
# print(f'Current directory: {current_directory}')
#
# # List files in the current directory
# files = os.listdir(current_directory)
# print(f'Files in the directory: {files}')





import re, requests, os
import hashlib

banner = """"
#########################################################################
            Kriptor dastur      author Shukrullo Zaylobidinov
#########################################################################

            _[1]___ Hash kodlash --
                                        sha1//sha224//sha256//sha512//md5
                                        
            _[2]___ Dehash sha1 --->
            
            _[3]___ Dehash md5 --->
            
            _[4]__ Chiqish --->
            
##########################_______________################################
            
"""

os.system("clear")
print(banner)


while True:
    buyruq = input("\n\n  -----------------<[*] Iltimos xos raqamni tanlang! ---> ")

    if buyruq == "1":
        os.system("python3 hashlib.py")
    elif buyruq == "2":
        os.system("python3 dehash_sha1.py")
    elif buyruq == "3":
        os.system("python3 dehash_md5.py")
    elif buyruq == "4":
        break
    else:
        os.system("clear")
        print(banner)
        print("\n\n\n           OGOHLANTIRISH\n\n\n   ---> Iltimos to'g'ri raqam kiriting")

exit()

