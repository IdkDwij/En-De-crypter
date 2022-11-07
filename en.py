import base64, os


def enbinary(ciphertext):
  with open(ciphertext) as f:
    content = f.read()
  f.close()
  binaryencrypt = ' '.join(format(ord(x), 'b') for x in content)
  with open(f'enbinary-{os.path.splitext(ciphertext)[0]}.encrypt', 'w') as r:
    r.write(binaryencrypt)
  r.close()


def enbase(ciphertext):
  with open(ciphertext) as f:
    content = f.read()
    f.close()
  urlSafeEncodedBytes = base64.urlsafe_b64encode(content.encode("utf-8"))
  urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
  with open(f'enbase-{os.path.splitext(ciphertext)[0]}.encrypt', 'w') as r:
    r.write(urlSafeEncodedStr)
  r.close()
