
from time import time
import jwt
from secrets import zoom_access_key, zoom_secret_key

'''
The Zoom Meeting SDKs use an SDK Key and Secret to generate an SDK JWT for authorized use of the SDK. 
This is a SDK App Signature Generation Python 3 script using PyJWT to sign signature.

Install: 
* pip3 install pyjwt

Documentation : 
* https://marketplace.zoom.us/docs/sdk/native-sdks/auth/#generate-the-sdk-jwt
* https://pyjwt.readthedocs.io/en/latest/
* https://jwt.io/
'''

def generate_signature(meeting_number, role, sdk_key, sdk_secret):

      # The current timestamp. Required.
      iat = round(time())
      print("Time iat :", iat)
      
      # JWT expiration date. Required for Web, optional for Native. 
      # Values: Min = 1800 seconds greater than iat value, 
      # max = 48 hours greater than iat value. In epoch format.
      exp = iat + 60 * 60 * 2

      token = jwt.encode({
        "sdkKey": sdk_key, # Optional for Web.
        "appKey": sdk_key,  # Optional for Web.
        "mn": meeting_number, # Required for Web, optional for Native.
        "role": role, # Required for Web, optional for Native.
        "iat": iat, #  Required.
        "exp": exp, # Required for Web, optional for Native.
        "tokenExp": iat + 60 * 60 * 2 # Required for Native, optional for Web.
        }, sdk_secret, algorithm="HS256", headers={ 'alg': 'HS256', 'typ': 'JWT' })
      
      return token

# Decode PyJWT to signed the signature
def decode_signature(token, sdk_secret):

      return jwt.decode(token,sdk_secret, algorithms=["HS256"])

if __name__ == '__main__':
    mn = '94995306902'
    role = 0
    SDK_Key = "4ASmoeC9qV2BAcj8XFNPD9GK9uTrg60582Fm"
    SDK_Secret= "ZuX1Zz0KDVAPhshIlEgPguZGxY4gcoPP93RD"
    encoded_token = generate_signature(mn,role, SDK_Key, SDK_Secret)
    payload = decode_signature(encoded_token,SDK_Secret)

    print("Encoded Signature: " + str(encoded_token) + '\n')
    print("Decoded Signature: " + str(payload))
    
    #run sciprt : python3 gensignature.py
    
