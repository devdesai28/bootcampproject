import hashlib

m = hashlib.md5()
text = 'dev desai'
m.update(text.encode('utf-8'))

print(m.hexdigest())