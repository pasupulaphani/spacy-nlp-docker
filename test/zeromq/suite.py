import zerorpc
import json

c = zerorpc.Client()
c.connect('tcp://127.0.0.1:4242')

input = u'hotel new york'
actual = json.loads(c.nounChunks(input))
expected = json.loads("""[{"text": "hotel"},{"text": "new york"}]""")

print('expected: ')
print(expected)
print('actual: ')
print(actual)

if actual == expected:
    print('Noun chunks successful')
else:
    raise Exception('Noun chunks not same')
