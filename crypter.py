import sys
import time
import datetime
import requests
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
from Crypto.Util import asn1
import rsa

def encrypt_data(originStr,pubKeyString):
    start = "-----BEGIN RSA PUBLIC KEY-----\n"
    end = "-----END RSA PUBLIC KEY-----"
    print pubKeyString
    middle = pubKeyString[59:-24]
    pubKeyString = start + middle + end
    print pubKeyString

    pubkey = rsa.PublicKey.load_pkcs1(pubKeyString)
    return rsa.encrypt(originStr, pubkey)

def decrypt_data(encryptStr, privKeyString):

    # decrypt_list=[]
    # tokenid=encrypt[0]
    # uuid=encrypt[1]
    # amount=encrypt[2]
    # keyDERs = b64decode(privKeyString)
    keyPriv = RSA.importKey(privKeyString)

    cipher = PKCS1_OAEP.new(keyPriv)
    # de_uuid = cipher.decrypt(uuid)
    # de_amount = cipher.decrypt(amount)
    de_toEncrypt = cipher.decrypt(encryptStr)
    # decrypt_list.append(tokenid)
    # decrypt_list.append(de_uuid)
    # decrypt_list.append(de_amount)
    return de_toEncrypt

def getInputs():
    res=[]
    uuid = str(raw_input("Please type in your UUID:"))
    amount = str(raw_input("amount: "))
    tokenID = int(raw_input("tokenID: "))
    ts= time.time()         #timestamp in gibberish
    st= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    res.append(uuid)
    res.append(amount)
    res.append(tokenID)
    res.append(st)
    print "output of getInputs"
    print res
    return res

if __name__ == "__main__":
    rs = getInputs()
    amt = rs[1] + '.'+((4-len(rs[1]))*'0')


    toEncrypt = rs[0] + amt
    result = requests.post("http://still-scrubland-1100.herokuapp.com/twilio",{"uuid" : rs[0],"amount" :
    rs[1],"tokenID":rs[2],"timestamp":rs[3]})
    res = result.json()
    pub = res["Key"]
    privkeyid = res["ID"]
    en_total = encrypt_data(toEncrypt.encode('utf8'),pub)
    load = {"tokenid": privkeyid,"encrypt_total": b64encode(en_total),"timestamp":rs[3]}
    result = requests.post("http://still-scrubland-1100.herokuapp.com/deposits",json=load)
    if result.status_code == 200:
        print "Successful"
    else:
        print "ggxx.. " + str(result.status_code)
