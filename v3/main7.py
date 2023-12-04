import http.client
from hashlib import sha1 as sha1Utils, md5 as md5Utils

conn = http.client.HTTPSConnection("solution.wps.cn")

APPID = "SX20231106HJJKCX"
APPKEY = b"mExaJlJZwKaLcIbpQAuCyhYhVmioEOxm"

Content_Md5 = b"d41d8cd98f00b204e9800998ecf8427e"

Content_Type = b"application/json"
Date = b"Wed, 23 Jan 2013 06:43:08 GMT"

signature = sha1Utils(APPKEY + Content_Md5 + Content_Type + Date).hexdigest()

print(signature)
# output > 083500176fa3aab58ca2dc962978013b3ca2b6df

Authorization = 'WPS-2:%s:%s' % (APPID, signature)
print(Authorization)
# output > WPS-2:******:083500176fa3aab58ca2dc962978013b3ca2b6df


payload = "{\"url\":\"https://www.chengdu.gov.cn/chengdu/ygdw/2019-12/26/32871b00143c4a349f74491956a2a1b1/files/4421922b264e4f3fa8192dc5c2fc399c.pdf\",\"filename\":\"demo.doc\"}"

headers = {
    'Date': Date,
    'Content-Md5': Content_Md5,
    'Content-Type': "application/json",
    'Authorization': Authorization
}

conn.request("POST", "/api/developer/v1/office/save/as/docx", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
