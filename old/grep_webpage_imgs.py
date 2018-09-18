import sys,urllib

url='http://bbs.tianya.cn/post-funinfo-5196763-3.shtml'
wp = urllib.urlopen(url)
print 'start download...'
content = wp.read()

total=content.count('original="')
print 'total:'+str(total)
count=0
while (count<total):
	count+=1
	index=content.find('original="')
	print 'index:'+str(index)
	content=content[index+10:]
	imgUrl=content[0:content.find('jpg"')+3]
	print 'imgUrl:'+imgUrl
	imgName='5196763-3'+str(count)
	if imgUrl.endswith('jpg'):
		imgName=imgName+'.jpg'
	elif imgUrl.endswith('jpeg'):
		imgName=imgName+'.jpeg'
	elif imgUrl.endswith('gif'):
		imgName=imgName+'.gif'
	else:
		imgName=imgName+'.jpg'
	fp = open(imgName,"w+")
	imgWp=urllib.urlopen(imgUrl)
	imgContent=imgWp.read()
	fp.write(imgContent)
	fp.close()

print 'download end'