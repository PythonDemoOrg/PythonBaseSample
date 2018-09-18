#import urllib  
#url = "http://img3.laibafile.cn/p/m/175002960.jpg"  
#path = "C:/Users/hwq/Desktop/175002960.jpg"  
#data = urllib.urlopen(url).read()  
#f = file(path,"wb")  
#f.write(data)  
#f.close()

import os, urllib
 
class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0"
 
urllib._urlopener = AppURLopener()
url = "http://img3.laibafile.cn/p/m/175002960.jpg"
filename = os.path.basename(url)
urllib.urlretrieve(url , filename)