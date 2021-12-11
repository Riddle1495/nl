import requests
import random,string
from requests_toolbelt import MultipartEncoder
import json
s = requests.session()
r = s.get("https://media1.vocaroo.com/mp3/19GLLbJKyh9n")
url = "https://onlineaudioconverter.com/php/upload-file.php"
m = MultipartEncoder(
    fields={
        'file': (
            'file.mp3',
            r.content,
            'audio/mpeg'
        )
    }
)
headers = {'Content-Type': m.content_type}
s.post(url, data=m, headers=headers)
data = {
  'targetExtension': 'wav',
  'targetChannels': 'mono',
  'targetBitDepth': 'default',
  'targetSampleRate': '24',
  'targetEncodingQuality': '2'
}
r = s.post('https://onlineaudioconverter.com/php/convert-file.php', data=data)
print("https://onlineaudioconverter.com/" + json.loads(r.text)["downloadURL"])

