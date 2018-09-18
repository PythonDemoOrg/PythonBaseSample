import os

#key=win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'Software',0,win32con.KEY_READ)
#print key

EXE_LIST=[
"C:\Program Files\Tencent\QQ\QQProtect\Bin\QQProtect.exe",           #QQ
"D:\Program Files\yy\YY.exe",										 #YY
"C:\\Users\hwq\AppData\Roaming\\360se6\Application\\360se.exe",      #360Browser
"D:\\adt-bundle-windows-x86\eclipse\eclipse.exe",                    #Eclipse
"C:\Program Files\Evernote\Evernote\Evernote.exe",					 #Evernote
"D:\Program Files\VMwareWorkstation\\vmware.exe",					 #Vmware
]

def execute():
	for path in EXE_LIST:
		os.startfile(path)
	
execute()