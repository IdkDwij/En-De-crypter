import os, de, en, sys

content = ""
print(sys.argv)

try:
  if sys.argv[1] == "d":
    if sys.argv[2] == "b":
      if os.path.isfile(sys.argv[3]) == True:
        de.debinary(sys.argv[3])
    elif sys.argv[2] == "base":
      if os.path.isfile(sys.argv[3]) == True:
        de.debase(sys.argv[3])
  elif sys.argv[1] == "e":
    if sys.argv[2] == "b":
      if os.path.isfile(sys.argv[3]) == True:
        en.enbinary(sys.argv[3])
    elif sys.argv[2] == "base":
      if os.path.isfile(sys.argv[3]) == True:
        en.enbase(sys.argv[3])
except:
  crypt = input("Decrypt(d) or Encrypt(e): ")
  level = input(
    "Binary encrypter/decrypter[b] or base64 encrypter/decrypter[base]")
  getpath = input("enter file path: ")
  if os.path.isfile(getpath) == True:
    if level == "b":
      if crypt == "d":
        de.basede(getpath)
      elif crypt == "e":
        en.enbinary(getpath)
    elif level == "base":
      if crypt == "d":
        de.debase(getpath)
      elif crypt == "e":
        en.enbase(getpath)
  else:
    print("invalid file path")
