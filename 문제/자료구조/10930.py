# sha- 256
# 문자열 s의 해시값 

import hashlib

S = input()
m = hashlib.sha256(S.encode())
print(m.hexdigest())