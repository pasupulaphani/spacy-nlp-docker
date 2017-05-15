import zerorpc
import json
import os

c = zerorpc.Client()

host = os.environ.get('ZEROMQ_HOST')
host = host if host else "0.0.0.0"
port = os.environ.get('ZEROMQ_PORT')
port = port if port else "4242"

conn_str = 'tcp://' + host + ':' + port
print("Conncting: " + conn_str)
c.connect(conn_str)

input = u'hotel in new york'
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
