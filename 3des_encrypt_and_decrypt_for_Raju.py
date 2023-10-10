#
# from Crypto.Cipher import DES3
# import array
#
# key = '8FB3952CE339F6F8900ACCCF4ABDB797'
# encryptedvalue = '8E5B15974B5ABA894E94B1E36D23EEC5'
# keyarray = array.array('B', key.encode("utf-8"))
# des = DES3.new(keyarray)
# value = des.decrypt(encryptedvalue.decode('base64'))
#
# value.decode('utf-8') # Gives me an error

import base64
import os
from Crypto.Cipher import DES3
import binascii

# password = '\xAA\xEE\xFF\x00\x00\x00\x00\x00'
password = binascii.unhexlify(16*"00")
# print(password)

# password_bytes = password.encode("utf-8")
# padded_password = DES3.pad(password_bytes, DES3.block_size)
# master_key = b'\x54\x9B\x6E\x13\xB5\x45\xA8\x7F\xA4\x32\x13\xF8\xE5\xBC\x85\x0D'
raju_key = binascii.unhexlify('C1D0F8FB4958670DBA40AB1F3752EF0D')
cipher_DES3 = DES3.new(raju_key, DES3.MODE_CBC, IV=b'00000000')
enc_pass = cipher_DES3.encrypt(password)

print((enc_pass))

de_cipher = DES3.new(raju_key, DES3.MODE_CBC, IV=b'00000000')
test2 = de_cipher.decrypt(enc_pass)
print(test2)
print("The recovered plaintext is what we expected:", test2 )

