#!/usr/bin/python

from urllib.request import urlopen
import hashlib

sha1_hash = input("[*] sha1 kodni kiriting: ")
parol_list = str(urlopen("https://raw.githubusercontent.com/iryndin/10K-Most-Popular-Passwords/master/passwords.txt").read(), 'utf-8')

for parol in parol_list.split('\n'):
    hash_tahmin = hashlib.sha256(bytes(parol, 'utf-8')).hexdigest()
    if hash_tahmin == sha1_hash:
        print("[%%] parol topildi: " + parol)
        quit()
    else:
        print("[%%] sha1 parol togri kelamadi: " + hash_tahmin)
    print("sha1 parolga oxshash parol topilmadi")