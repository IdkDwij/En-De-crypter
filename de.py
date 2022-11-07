import base64, os


def binaryde(ciphertext):
  with open(ciphertext) as f:
    content = f.read()
  f.close()
  decrypted = "".join([chr(int(binary, 2)) for binary in content.split(" ")])
  with open(f'debinary-{os.path.splitext(ciphertext)[0]}.txt', 'w') as e:
    e.write(decrypted)
  e.close()


def debase(ciphertext):
  with open(ciphertext) as f:
    content = f.read()
  f.close()
  decodedBytes = base64.b64decode(content)
  decodedStr = str(decodedBytes, "utf-8")
  with open(f'debase-{os.path.splitext(ciphertext)[0]}.txt', 'w') as e:
    e.write(decodedStr)
  e.close()
