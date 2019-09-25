import urllib.request
import os

print('Download data...')
url = 'https://cn.bing.com/'
urlFile = urllib.request.urlopen(url)
data = urlFile.read()
urlFile.close()
data = data.decode('utf-8', errors='ignore')
pre = u'href=\"'  # 注意空格
aft = u'=hp\"'
urlStart = data.find(pre) + len(pre)
urlEnd = data.find(aft, urlStart)
imgUrl = data[urlStart: urlEnd + len(aft) - 1]
print('--------------' + 'imgUrl' + '--------------')
print(imgUrl)
preImg = u'<a id=\"sh_cp\" class=\"sc_light\" title=\"'
imgNameStart = data.find(preImg) + len(preImg)
print(data.find(preImg))
imgNameEnd = data.find('\" aria-label=\"', imgNameStart)
imgName = data[imgNameStart: imgNameEnd] + u'.jpg'
imgName = imgName.replace("©", "")
imgName = imgName.replace("/", " ")
if not os.path.exists(imgName):
    print('Download image......')
    urllib.request.urlretrieve(url + imgUrl, imgName)
print('Download complete')
