import os
import stat
from os.path import join, getsize

def delFile(top, del_name):
	print 'Now starting to delete rubbish files:'
	for root, dirs, files in os.walk(top, topdown = False):
		for name in files:
			print name
			#if name == del_name:
				#full_path = os.path.join(root, name)
				#os.chmod(full_path, stat.S_IWRITE|stat.S_IREAD)
				#os.remove(full_path)
				#print full_path + ' removed.'

def browse(top):
	print 'Now browsing files:'
	for root, dirs, files in os.walk(top, topdown = True):
		#for name in files:
		#	print name
		#for dir in dirs:
		#	print dir
			print root
			
def start():
	#top = 'c:\\'
	#del_name = 'alipay'
	#delFile(top, del_name)
	dir = 'D:\My YY'
	browse(dir)

def verify():
	passwd = raw_input('Plz input passwd:')
	if passwd == 'jack' or passwd == 'JACK':
		print 'Hi, jack.'
		return 'ok'
	else:
		print 'Wrong passwd!'
		return 'bad'

def main():
	while True:
		#ok = verify()
		#if ok == 'ok' or ok == 'OK':
			start()
			break

main()
