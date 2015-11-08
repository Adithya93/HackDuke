import sys
import time
import datetime
import requests
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
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

def encrypt_data(originStr,pubKeyString):  #uuid,amount,tokenID,st
    # encrypt_list=[]
    # uuid=res[0]
    # amount=res[1]
    # tokenid=int(res[2])
    # toEncrypt = uuid + amount
    print "key used to encrypt data method is"+ pubKeyString
    keyDER = b64decode(pubKeyString)

    keyPub = RSA.importKey(keyDER)

    cipher = PKCS1_OAEP.new(keyPub)
    # enc_uuid = cipher.encrypt(uuid)
    # enc_amount = cipher.encrypt(amount)
    enc_toEncrypt = cipher.encrypt(originStr)
    # encrypt_list.append(tokenid)
    # encrypt_list.append(enc_uuid)
    # encrypt_list.append(enc_toEncrypt)
    # encrypt_list.append(enc_amount)
    return enc_toEncrypt

def decrypt_data(encryptStr, privKeyString):

    # decrypt_list=[]
    # tokenid=encrypt[0]
    # uuid=encrypt[1]
    # amount=encrypt[2]
    keyDERs = b64decode(privKeyString)
    keyPriv = RSA.importKey(keyDERs)

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
    return res

if __name__ == "__main__":
    # priv="MIIEpAIBAAKCAQEA5fUre3eH0Jgk5xJSxgysP03LtO5Zabmfcx+wUIfCiGQ9nAifXLTK1YRcztAX2dITtUVXLdqExH6HlmQZbAcrufcXWxF1x7UBgQ4l1FDdqNerXb6JcwOKu9TPbQUFeiSXMUlnQsn5v27LscQL5jvQ6MdjfV+RZ1jQkr2wL+hYUn9WXZx9VTMf+UuAzhutjZ8jfjKgh/NoWMHhB0xPQd1RsCy2gTbjP3QFpmkz5K0Gb5ugE1MyeWF/cugU0MrR3vDjBXVf2JO8599v1uToEBWRdzeaptOL6ot5ruZrJAa0Lx/sLEwH58TVIHKWzK9ZHjIYbWniZTqV+jHcZgRT1Dv9PQIDAQABAoIBAQCOiQ7wssBeTU/iYnsoA0bo3iG7/lkxrTrmMugool20CN4fT0DoR6/J9QdJsbZ27z4EB/znkSDmYr9MOrN/QFqcJEo3ynTE2q8Z/Vj5Zz5dn4C61JWB0to1Xs1Ld+dTNEb659K3lVXWkKh1gV0W0lDFWIGUfp4z/tsZebYxm8TTLKmxJzTPn4HPFNy6uItbzPBfJi/xzJgEWu1HFvuZUkxMomlHARLQbxnYM/U7C6yYk1n9AhLGLGK5gWWPBbEeUbH807ijJc6adAn3dOMDbsq7kovXHR6KM1d0EHapKLcrvpFhPDiYMWFWkI8CcDZmdKrhL0nP/gr3mjcadJjd2YSJAoGBAPuy5HkwM607OivEONZRkJdGqX1+/QzrFr2qS50VgMRuLZDZ2wHw1pSo4t/vw3jAuwpJ18I5EvjRWuvX8MzPKCdCce7VZXEif58fWvfLG05I3XTdOpMci/QGGr5VlEadEy+BhQAbzZ4M5ypjdO7R7Wzgb7LSu2KlZ5sOo/6eHcxLAoGBAOnjKp/ph7a2T9/cnfjSdWU0/HTl63frie3L0MVuJ7SgeMn2mRyMjTfflC7usV32d+e/ppId2kk81P8F9ut88TpqiP80krntqk1mIwLiMEg7pCy1kFCr57CrAHf5CjQRcKrFSUTMKuHF1Dbc6aS51AHQPmrqnMasnrQ1w2eV0VeXAoGABOl92fud1pCkVvxSW6Rl3P3tCtzylVD1NahgJ2WnCK5Zx0zpIEWR+n69Rr+IIhAo1k+QnWK9wwta6eVh9q1ITFPYo1+Yxjd1JCbZgKJ/Gu0DHWe/3+UbuhxwYyyKY0JngHLXpKPmRGJeFI6yVoLUTl6m72d7brZpqjYD71EopbcCgYEAj/xzz0KbdBZEkhJlhjs6XnYCPY0WKxtsLGLfQcwQ0ZhBBES1+edlQNJ5jXMQ6kHDi35m82lBavjyP5XSbyLZ9xaDBGm/Motn3oJUZ4AMLUvaRFP6Zk+OMSr0/ObqKyfZbqhJ9PqkI54AiU3y4KAuLnefFX8dyQmYImU+yNRorj0CgYBu5H+CqfEZZHP5yUO42rXnYX08sYgvFCZ1iqjuaD8BxSFaoeOny2N8qbYG8+sWInM/8rhhZk0fcaGwQED9WXEhsTvjLwKZcgpiMd5ZNNoJRoxAKomBfGikPAFNrQb+4M4dbExce0egIP/p+n5nH0CwKM88TuVaEybawrqGFYN2cw=="
    # pub ="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5fUre3eH0Jgk5xJSxgysP03LtO5Zabmfcx+wUIfCiGQ9nAifXLTK1YRcztAX2dITtUVXLdqExH6HlmQZbAcrufcXWxF1x7UBgQ4l1FDdqNerXb6JcwOKu9TPbQUFeiSXMUlnQsn5v27LscQL5jvQ6MdjfV+RZ1jQkr2wL+hYUn9WXZx9VTMf+UuAzhutjZ8jfjKgh/NoWMHhB0xPQd1RsCy2gTbjP3QFpmkz5K0Gb5ugE1MyeWF/cugU0MrR3vDjBXVf2JO8599v1uToEBWRdzeaptOL6ot5ruZrJAa0Lx/sLEwH58TVIHKWzK9ZHjIYbWniZTqV+jHcZgRT1Dv9PQIDAQAB"
    priv="MIIEowIBAAKCAQEAg9xWfydchUJ5sDoyARXdtx1GsTvx+liCtERiA62AKt9pD4f2\nS0fklgsPEc522fa2FUqkfcfEb21EmYN2371CRmwatTaYfJ4LdIyhC3vrRB7NLV70\nx/I+pcGmKAZupeMbC71mZguinVKRHGMOfSYpjSwN74MPPoFHkxIe8QSI15Fpf+3X\nGMP2d+iZIfZILzB9pgdO3Iel91TosCCJyopPdIHVGHvyFpsTPPUmBqiSruPT/jKW\niqjvoCyb08Wjyhkitj0MtdbZ3LO1waFbqiTjN5XeqSnumH6FrauGk3c2SL7V7av7\nZS0jyqo6XvDd81HbxVPYWWSwrmwIGoUiQJPMhQIDAQABAoIBAH6tgoeb1/3KFEAi\nWIHEcQGHZa/FiD3bJI5sl8EywMvvX+5kz1AZXFhtfWe881+I7frcf9S6w1PNJLda\nnixqlS40kx/+uFYYO6cXp2vx+96wvKrW69DfQCJcPPV84HYMDaKkrahhizMa7H/a\nBkRjEk4mwaiVP2LsLkfzg7hGg/SbxBUiOWE+CamvZgFsbfDAOvqUjWM4cdEoSTa1\ntZnNMKy3mtsumHycROta/3HfL8S7qrllUWqRdUSXgOdeISWOxeZqFDzTiA9sWogk\n+THLVnfkSPvZxEEujGK2pSB//NmFQr/13QJwbvD994R7Cb2HbOzh5jxzw2FImb1T\nLE9ZPSECgYEAvR1kHFgqABRTpYuWNnJF16p3JggXZquQCUk9NNAXv2TSi79sDZcF\npd4BZWz/vcBx3HVMnZnI3zDLdpNMsy8bOFMQGDOKDAvd7FvYt2/vDqe79L9UzfRx\nwNDLknjtn1e+SjB7RrbqAd4NBfOqaXjS+rvocu6BwiKp0MYIhWMnnBkCgYEAsn8c\n2ABWpmpw4hmoJFKs1ocLn72/Kxf1o4zecX7G0Q+U+RkSziBYuDUToGkAyPpJpo1C\nz/fcdVQtxgbEeeEWC6R87UJ6ECxX0FUJsj94Mt8/ysqnx2RiloNm9C0faqPiwMuk\ndgvzDQkTlq89iIR+RoLMechhWUpp9ZETITgzwU0CgYEAtKGPDnezXjIMFzH1fvm0\n9iKO/Zd66ojx4by/pmMgW6IsbGihB3X5Yg1jngH3X8Ghv6WWUW4i6/OKUy6scvWK\ndUj5NXR85bar+OddXxCd8IyLvWDG2pUh1b5YwwWYSbsgOXKHPOrXJoN2QvoTCfzq\n36x9gNGIxOog8xVD7Evh+HkCgYBnshLWpXOxYBrOL2uQFnuUcYXeOkRpy5SHfBnq\nQ2VLJMs930QefYotEaCiSv4Kw+SvnlcXLH5lpw6kgV/5EjtVbiypRTpWVPx66jwk\n0lyI6UtNC2hnHLltiU7xQZmDwUvFB0k2zwBXLVO08X9E5PvbCLezdCah0eo2oB5F\n6Tmf7QKBgENjvXIjw0n1LmoAryIQ7eqr3MWdv5JyT7+Nuwcp+xCYkiXkvVyORWR2\nphkEcIxl0FRAgYTbN76i4bOoXyGQZCYCwfWOV5WmnZvzUWVk2YlU/Si9uTPB8ujs\nQPP5X/X9R6WZheYgIRkpiMkQ0RhEgJRLZKWq+aVNVIQkYAAlzGsr"
    pub ="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg9xWfydchUJ5sDoyARXd\ntx1GsTvx+liCtERiA62AKt9pD4f2S0fklgsPEc522fa2FUqkfcfEb21EmYN2371C\nRmwatTaYfJ4LdIyhC3vrRB7NLV70x/I+pcGmKAZupeMbC71mZguinVKRHGMOfSYp\njSwN74MPPoFHkxIe8QSI15Fpf+3XGMP2d+iZIfZILzB9pgdO3Iel91TosCCJyopP\ndIHVGHvyFpsTPPUmBqiSruPT/jKWiqjvoCyb08Wjyhkitj0MtdbZ3LO1waFbqiTj\nN5XeqSnumH6FrauGk3c2SL7V7av7ZS0jyqo6XvDd81HbxVPYWWSwrmwIGoUiQJPM\nhQIDAQAB"
    rs = getInputs()
    toEncrypt = rs[0] + rs[1]
    # es = encrypt_data(toEncrypt,pub)
    # print "toEncrypt"
    # print toEncrypt
    # print "\n\n decrypt"
    # ds = decrypt_data(es,priv)
    # print ds
    result = requests.post("http://still-scrubland-1100.herokuapp.com/users/new",{"uuid" : rs[0],"amount" : rs[1],"tokenID":rs[2],"timestamp":rs[3]})
    res = result.json()
    pub = res["Key"].encode("utf-8")
    privkeyid = res["ID"]
    en_total = encrypt_data(toEncrypt,pub)
    #load = {"tokenid": rs[2],"encrypt_total":en_total,"timestamp":rs[3]}
    load = {"tokenid": privkeyid,"encrypt_total": b64encode(en_total),"timestamp":rs[3]}

    result = requests.post("http://still-scrubland-1100.herokuapp.com/deposits",json=load)
    if result.status_code == 200:
        print "Successful"
    else:
        print "ggxx.. " + str(result.status_code)
