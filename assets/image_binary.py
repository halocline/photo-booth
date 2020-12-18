import requests

file = open('/Users/mdglissmann/glissmann-signature.jpg', 'rb')
# byte = file.read(1)
# count = 0

# while byte and count < 10000:
#     count += 1
#     print(byte)
#     byte = file.read(1)

blob = file.read()
# print(blob)

file.close()


domain = 'http://127.0.0.1:8080'
apiEndpoint = '/helloworld'
url = domain + apiEndpoint
auth = ('Matt', 'pass')
data = blob
# r = requests.get(url)
# print(r)
# print(r.status_code, r.reason)
# print(r.text)

apiEndpoint = '/upload'
url = domain + apiEndpoint
files = {'image': open('/Users/mdglissmann/glissmann-signature.jpg', 'rb')}
# r = requests.post(url, files=files)
r = requests.post(url, data=files)
print(blob)
print(r)
print(r.status_code, r.reason)
print(r.text)
