from binascii import hexlify, unhexlify

def GetDataKeyVariant(ksn, ipek):
    key = GetDUKPTKey(ksn, ipek)
    key = bytearray(key)
    key[5] ^= 0xFF
    key[13] ^= 0xFF
    return str(key)

def TDES_Dec(data, key):
    t = triple_des(key, CBC, padmode=None)
    res = t.decrypt(data)
    return res

def decrypt_card_info(ksn, data):
    BDK = unhexlify("0123456789ABCDEFFEDCBA9876543210")
    ksn = unhexlify(ksn)
    data = unhexlify(data)
    IPEK = GenerateIPEK(ksn, BDK)
    DATA_KEY_VAR = GetDataKeyVariant(ksn, IPEK)
    print (hexlify(DATA_KEY_VAR))
    res = TDES_Dec(data, DATA_KEY_VAR)
    return hexlify(res)

decrypt_card_info('00000332100300E0000A', '744B8A95FF1982CD63FB24D581FCD1A0590E7F6DD12B86ED1B1D26E687EA853A128598C16BE14964A34607452511C4B6CBDCACD72BEB566E32094937C18C2424')