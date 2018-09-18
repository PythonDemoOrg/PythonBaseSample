from urllib import request
import threading
from time import sleep,ctime
from html import parser

def downjpg( filepath,FileName ="default.jpg" ):
    try:
        web = request.urlopen( filepath)
        print("access network file:"+filepath+"\n") 
        jpg = web.read()
        DstDir="H:\\image\\"
        print("�����ļ�"+DstDir+FileName+"\n")
        try:
            File = open( DstDir+FileName,"wb" )
            File.write( jpg)
            File.close()
            return
        except IOError:
            print("error\n")
            return
    except Exception:
        print("error\n")
        return 
        

def downjpgmutithread( filepathlist ):
    print("����%d���ļ���Ҫ����"%len(filepathlist)) 
    for file in filepathlist:
        print( file )
    print("��ʼ���߳�����")
    task_threads=[] #�洢�߳�
    count=1
    for file in filepathlist: 
        t= threading.Thread( target=downjpg,args=(file,"%d.jpg"%count) )
        count=count+1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join() #�ȴ������߳̽���
    print("�߳̽���")

class parserLinks( parser.HTMLParser):
    filelist=[]
    def handle_starttag(self,tag,attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    print( value)
                    self.filelist.append(value)
                    #print( self.get_starttag_text() )
    def getfilelist(self):
        return self.filelist


def main(WebUrl):
    #globals flist 
    if __name__ == "__main__":
        lparser = parserLinks()
        web = request.urlopen( WebUrl )
        #context= web.read()
        for context in web.readlines():
            _str="%s"%context
            try:
                lparser.feed( _str)
            except parser.HTMLParseError:
                #print( "parser error")
                pass
        web.close()
        imagelist= lparser.getfilelist()
        downjpgmutithread( imagelist)        
        
        #downjpgmutithread( flist) 

#WebUrl="http://www.baidu.com/" #Ҫץȥ����ҳ����,Ĭ�ϱ��浽e��
WebUrl="http://hi.baidu.com/%C7%A7%D2%B6%CF%C4%D1%A9/blog/item/0f119f5404428148d109062a.html"

main(WebUrl)
