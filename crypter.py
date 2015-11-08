import sys
import time
import datetime
import requests
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
from Crypto.Util import asn1
#buildMap code
# pub={}
# priv={}
# 
# def buildMap():
#     for i in range(32):
#         key = RSA.generate(1024)
#         binPrivKey = key.exportKey('DER')
#         binPubKey =  key.publickey().exportKey('DER')
#         public_key =  RSA.importKey(binPubKey)
#         priv_key = RSA.importKey(binPrivKey)
#         if i not in pub:
#             pub[i] =[];
#             priv[i] =[];
#         if i in pub:
#             pub[i].append(public_key)
#             priv[i].append(priv_key)
# 
# def getPub(num):
#     req = pub.get(num)[0]
#     return req
# 
# def getPriv(num):
#     req = priv.get(num)[0]
#     return req

def encrypt_data(res,pubKeyString):  #uuid,amount,tokenID,st
    encrypt_list=[]
    uuid=res[0]
    amount=res[1]
    tokenid=int(res[2])
    keyDER = b64decode(pubKeyString)
    keyPub = RSA.importKey(keyDER)
    
    cipher = PKCS1_OAEP.new(keyPub)
    enc_uuid = cipher.encrypt(uuid)
    enc_amount = cipher.encrypt(amount)
    encrypt_list.append(tokenid)
    encrypt_list.append(enc_uuid)
    encrypt_list.append(enc_amount)
    return encrypt_list

def decrypt_data(encrypt, privKeyString):
    
    decrypt_list=[]
    tokenid=encrypt[0]
    uuid=encrypt[1]
    amount=encrypt[2]
    keyDERs = b64decode(privKeyString)
    keyPriv = RSA.importKey(keyDERs)
    
    cipher = PKCS1_OAEP.new(keyPriv)
    de_uuid = cipher.decrypt(uuid)
    de_amount = cipher.decrypt(amount)
    
    decrypt_list.append(tokenid)
    decrypt_list.append(de_uuid)
    decrypt_list.append(de_amount)
    return decrypt_list

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
    return res

# receive a public key, encrypt the message and post back encrypted message
def retrieve_and_post(res,pub,urlname):
    es = encrypt_data(res, pub)
    load = {"tokenid": es[0],"encrypt_uuid":es[1],"encrypt_amount":es[2],"timestamp":res[3]}
    print es[0]
    print es[1]
    print es[2]
    print res[3]
#     requests.post(urlname,json=load)
    print "Success"
    
if __name__ == "__main__":
#     priv="MIIEpAIBAAKCAQEA5fUre3eH0Jgk5xJSxgysP03LtO5Zabmfcx+wUIfCiGQ9nAifXLTK1YRcztAX2dITtUVXLdqExH6HlmQZbAcrufcXWxF1x7UBgQ4l1FDdqNerXb6JcwOKu9TPbQUFeiSXMUlnQsn5v27LscQL5jvQ6MdjfV+RZ1jQkr2wL+hYUn9WXZx9VTMf+UuAzhutjZ8jfjKgh/NoWMHhB0xPQd1RsCy2gTbjP3QFpmkz5K0Gb5ugE1MyeWF/cugU0MrR3vDjBXVf2JO8599v1uToEBWRdzeaptOL6ot5ruZrJAa0Lx/sLEwH58TVIHKWzK9ZHjIYbWniZTqV+jHcZgRT1Dv9PQIDAQABAoIBAQCOiQ7wssBeTU/iYnsoA0bo3iG7/lkxrTrmMugool20CN4fT0DoR6/J9QdJsbZ27z4EB/znkSDmYr9MOrN/QFqcJEo3ynTE2q8Z/Vj5Zz5dn4C61JWB0to1Xs1Ld+dTNEb659K3lVXWkKh1gV0W0lDFWIGUfp4z/tsZebYxm8TTLKmxJzTPn4HPFNy6uItbzPBfJi/xzJgEWu1HFvuZUkxMomlHARLQbxnYM/U7C6yYk1n9AhLGLGK5gWWPBbEeUbH807ijJc6adAn3dOMDbsq7kovXHR6KM1d0EHapKLcrvpFhPDiYMWFWkI8CcDZmdKrhL0nP/gr3mjcadJjd2YSJAoGBAPuy5HkwM607OivEONZRkJdGqX1+/QzrFr2qS50VgMRuLZDZ2wHw1pSo4t/vw3jAuwpJ18I5EvjRWuvX8MzPKCdCce7VZXEif58fWvfLG05I3XTdOpMci/QGGr5VlEadEy+BhQAbzZ4M5ypjdO7R7Wzgb7LSu2KlZ5sOo/6eHcxLAoGBAOnjKp/ph7a2T9/cnfjSdWU0/HTl63frie3L0MVuJ7SgeMn2mRyMjTfflC7usV32d+e/ppId2kk81P8F9ut88TpqiP80krntqk1mIwLiMEg7pCy1kFCr57CrAHf5CjQRcKrFSUTMKuHF1Dbc6aS51AHQPmrqnMasnrQ1w2eV0VeXAoGABOl92fud1pCkVvxSW6Rl3P3tCtzylVD1NahgJ2WnCK5Zx0zpIEWR+n69Rr+IIhAo1k+QnWK9wwta6eVh9q1ITFPYo1+Yxjd1JCbZgKJ/Gu0DHWe/3+UbuhxwYyyKY0JngHLXpKPmRGJeFI6yVoLUTl6m72d7brZpqjYD71EopbcCgYEAj/xzz0KbdBZEkhJlhjs6XnYCPY0WKxtsLGLfQcwQ0ZhBBES1+edlQNJ5jXMQ6kHDi35m82lBavjyP5XSbyLZ9xaDBGm/Motn3oJUZ4AMLUvaRFP6Zk+OMSr0/ObqKyfZbqhJ9PqkI54AiU3y4KAuLnefFX8dyQmYImU+yNRorj0CgYBu5H+CqfEZZHP5yUO42rXnYX08sYgvFCZ1iqjuaD8BxSFaoeOny2N8qbYG8+sWInM/8rhhZk0fcaGwQED9WXEhsTvjLwKZcgpiMd5ZNNoJRoxAKomBfGikPAFNrQb+4M4dbExce0egIP/p+n5nH0CwKM88TuVaEybawrqGFYN2cw=="
#     pub ="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5fUre3eH0Jgk5xJSxgysP03LtO5Zabmfcx+wUIfCiGQ9nAifXLTK1YRcztAX2dITtUVXLdqExH6HlmQZbAcrufcXWxF1x7UBgQ4l1FDdqNerXb6JcwOKu9TPbQUFeiSXMUlnQsn5v27LscQL5jvQ6MdjfV+RZ1jQkr2wL+hYUn9WXZx9VTMf+UuAzhutjZ8jfjKgh/NoWMHhB0xPQd1RsCy2gTbjP3QFpmkz5K0Gb5ugE1MyeWF/cugU0MrR3vDjBXVf2JO8599v1uToEBWRdzeaptOL6ot5ruZrJAa0Lx/sLEwH58TVIHKWzK9ZHjIYbWniZTqV+jHcZgRT1Dv9PQIDAQAB"
#     es = encrypt_data(rs,pub)
#     print es
#     ds = decrypt_data(es,priv)
#     print ds
    reload(sys)
    rs = getInputs()
    result = requests.post("http://still-scrubland-1100.herokuapp.com/users/new",{"uuid" : rs[0],"amount" : rs[1],"tokenID":rs[2],"timestamp":rs[3]})
    res = result.json()

    pub = res["Key"].encode("utf-8")
    print type(pub)
    print pub
    retrieve_and_post(rs,pub,"http://still-scrubland-1100.herokuapp.com/deposits")
    