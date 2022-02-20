try:
  import base64
except:
  print("Base 64 Package not installed")

contents = ""
content = ""


crypt = input("Decrypt(d) or Encrypt(e): ")
level = input("Binary encrypter/decrypter[b] or base64 encrypter/decrypter[base]")
if level == "b":
  if crypt == "d":
    getpath = input("enter file path: ")
    with open(getpath) as f:
      contents = f.read()
    f.close()
    decrypted = "".join([chr(int(binary, 2)) for binary in contents.split(" ")])
    with open('decryptedfile.txt', 'w') as e:
      e.write(decrypted)
    e.close()

  elif crypt == "e":
    getfilepath = input("enter file path: ")
    with open(getfilepath) as f:
      content = f.read()
      f.close()
    binaryencrypt = ' '.join(format(ord(x), 'b') for x in content) 
    with open('cryptedfile.binary', 'w') as r:
      r.write(binaryencrypt)
    r.close()

if level == "base":
  if crypt == "d":
    getpath = input("enter file path: ")
    with open(getpath) as f:
      contents = f.read()
    f.close()
    decodedBytes = base64.b64decode(contents)
    decodedStr = str(decodedBytes, "utf-8")
    with open('decryptedfile.txt', 'w') as e:
      e.write(decodedStr)
    e.close()

  elif crypt == "e":
    getfilepath = input("enter file path: ")
    with open(getfilepath) as f:
      content = f.read()
      f.close()
    urlSafeEncodedBytes = base64.urlsafe_b64encode(content.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8") 
    with open('cryptedfile.base64', 'w') as r:
      r.write(urlSafeEncodedStr)
    r.close()
