import json
import requests

url = 'https://api.muxiaoguo.cn/api/dujitang'

res = requests.get(url)

result = json.loads(res.text)

str = result['data']['comment']

f = open('./README.md', 'a')

f.write('* ' +str + '\n')

f.close()