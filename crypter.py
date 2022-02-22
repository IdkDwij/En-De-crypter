import os
import base64


content = ""


crypt = input("Decrypt(d) or Encrypt(e): ")
level = input("Binary encrypter/decrypter[b] or base64 encrypter/decrypter[base]")
getpath = input("enter file path: ")

if os.path.isfile(getpath) == True:
  if level == "b":
    if crypt == "d":
      with open(getpath) as f:
        content = f.read()
      f.close()
      decrypted = "".join([chr(int(binary, 2)) for binary in content.split(" ")])
      with open('decryptedfile.txt', 'w') as e:
        e.write(decrypted)
      e.close()

    elif crypt == "e":
      with open(getpath) as f:
        content = f.read()
        f.close()
      binaryencrypt = ' '.join(format(ord(x), 'b') for x in content) 
      with open('cryptedfile.encrypt', 'w') as r:
        r.write(binaryencrypt)
      r.close()

  if level == "base":
    if crypt == "d":
      with open(getpath) as f:
        content = f.read()
      f.close()
      decodedBytes = base64.b64decode(content)
      decodedStr = str(decodedBytes, "utf-8")
      with open('decryptedfile.txt', 'w') as e:
        e.write(decodedStr)
      e.close()

    elif crypt == "e":
      with open(getpath) as f:
        content = f.read()
        f.close()
      urlSafeEncodedBytes = base64.urlsafe_b64encode(content.encode("utf-8"))
      urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8") 
      with open('cryptedfile.encrypt', 'w') as r:
        r.write(urlSafeEncodedStr)
      r.close()
else:
  print("invalid file path")
