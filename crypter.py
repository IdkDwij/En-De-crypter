crypt = input("Decrypt(d) or Encrypt(e): ")



if crypt == "d":
  getpath = input("enter file path: ")
  with open(getpath) as f:
    global contents
    contents = f.read()
  f.close()
  decrypted = "".join([chr(int(binary, 2)) for binary in contents.split(" ")])
  with open('decryptedfile.binary', 'w') as e:
    e.write(decrypted)
  e.close()

elif crypt == "e":
  getfilepath = input("enter file path: ")
  with open(getfilepath) as f:
    global content
    content = f.read()
  f.close()
  binaryencrypt = ' '.join(format(ord(x), 'b') for x in content) 
  with open('cryptedfile.binary', 'w') as r:
    r.write(binaryencrypt)
  r.close()
