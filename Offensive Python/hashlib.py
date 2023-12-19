#!/usr/bin/python

import hashlib

hash_sha256 = input("Istalgan so'zni kiriting: ")

print("\n md5")
hash_sha256_next1 = hashlib.md5()
hash_sha256_next1.update(hash_sha256.encode())
print(hash_sha256_next1.hexdigest())

print("\n sha1")
hash_sha256_next2 = hashlib.sha1()
hash_sha256_next2.update(hash_sha256.encode())
print(hash_sha256_next2.hexdigest())

print("\nsha224")
hash_sha256_next3 = hashlib.sha224()
hash_sha256_next3.update(hash_sha256.encode())
print(hash_sha256_next3.hexdigest())


print("\n sha256")
hash_sha256_next = hashlib.sha256()
hash_sha256_next.update(hash_sha256.encode())
print(hash_sha256_next.hexdigest())


print("\n sha512")
hash_sha256_next4 = hashlib.sha512()
hash_sha256_next4.update(hash_sha256.encode())
print(hash_sha256_next4.hexdigest())

