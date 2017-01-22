import zerorpc
import json
import os

c = zerorpc.Client()

host = 'tcp://' + os.environ.get('ZEROMQ_HOST') + ':' + os.environ.get('ZEROMQ_PORT')
print("Conncting: " + host)
c.connect(host)

input = u'hotel new york'
nounChunks = c.nounChunks(input)
print('nounChunks: ')
print(nounChunks)

actual = json.loads(nounChunks)
expected = json.loads("""[{"text": "hotel"},{"text": "new york"}]""")

print('Expected: ')
print(expected)
print('Actual: ')
print(actual)

if actual == expected:
    print('Noun chunks successful')
else:
    raise Exception('Noun chunks not same')
