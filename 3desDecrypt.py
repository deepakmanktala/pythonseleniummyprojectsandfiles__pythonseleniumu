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


import os
from Crypto.Cipher import DES3

des3 = DES3.new('ABC', DES3.MODE_CBC, '21232527292B2D2F20222426282A2C2E')

print (des3)

decrypt_data= des3.decrypt('8E5B15974B5ABA894E94B1E36D23EEC5')