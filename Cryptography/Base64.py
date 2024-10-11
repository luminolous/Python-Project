import base64

mode = input().upper()
text = input()

if mode == 'ENCODE':
# Encode
    base64_encode = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print(base64_encode)
elif mode == 'DECODE':
#Decode
    base64_decode = base64.b64decode(base64_encode).decode('utf-8')
    print(base64_decode)

