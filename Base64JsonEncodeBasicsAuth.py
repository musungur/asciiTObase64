import base64
import json

# Basic authentication process
username = str(input('Username$ '))
password = str(input('Password$ '))

#authentication in Text
auth = f'{username}:{password}'

print(f'printing authText:\n{auth}\n***end Of AuthText***')

# Conversion of authText To String Using encode()
authtoString = auth.encode()
print(f"\n***printing AuthTextToStringEncoded***\n{authtoString}\n**End of AuthTextToStringEncoded***\n")

# # Conversion of AuthText TO string Using Json.dumps
authtTexttoStringbyJson = json.dumps(auth)
print(f"**\nText to String conversion by Json**\n{authtTexttoStringbyJson}\n**End of Json conv from Text to String\n")

'''Conversion of Auth To Base64: Base64 converts binary(8bits) represantation of Data in ascii to 6bits(binary) -
represantation of Data, then to text for. Base64 transpforms ascii binary(8bits) to base64 binary(6bits)then converts to texts
'''
#Json string to binary represantation
print('**Json string to binary**')
JsonStringTObinary = authtTexttoStringbyJson.encode()
print(f'Json binary\n{JsonStringTObinary}')
print('\nend of Json String to bynary\n')

#json binary to base64
print('jsons binary to base64\n')
jsonbase64 = base64.b64encode(JsonStringTObinary)
print(jsonbase64)
print('\ndecode back json from base64 to ascii\n')
jsondecodedfrombase64 = base64.b64decode(jsonbase64)
print(f'{jsondecodedfrombase64}\n***end of Json back  to ascii***\n')

#Auth TextBinary to base64
authtoBase64 = base64.b64encode(authtoString)
print(f'\n*****Printing Auth to Base64*****\n{authtoBase64}')

decoded = base64.b64decode(authtoBase64)
print(f"decoded to ascii format:\n{decoded} \n")