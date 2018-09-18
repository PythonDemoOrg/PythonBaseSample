import subprocess, time, os

CASE_LIST=[
"com.lenovo.lsf.device.test.SdacTest#testSdacReg01",
"com.lenovo.lsf.device.test.SdacTest#testSdacReg04",
"com.lenovo.lsf.device.test.SdacTest#testSdacReg06"
] #CASE_LIST END

PKG_LIST=[
"com.lenovo.lsf.device",
"com.lenovo.lsf.device.test"
]

APK_LIST=[
"LSF-Device-Lenovo-Phone.8888.apk",
"LSF-Device-Lenovo-Phone-Testcase.8888.apk"
]

#Test case
def test_case():
	for pkg in PKG_LIST:
		out = run_cmd('adb uninstall '+pkg)
		print 'Uninstall '+pkg+' '+out
		
	for apk in APK_LIST:
		out = run_cmd('adb install C:/Users/a/Desktop/'+apk)
		print 'Installing apk '+apk+'\n'+out
			
	out = run_cmd('adb root')
	if out.find('adbd is already running as root')<0: 
		print out
		time.sleep(10)
	
	out = run_cmd('adb remount')
	if out.find('remount succeeded')<0:
		raise Exception('adb remount error : %s' %out)
	
	print 'Test START.\n'
	count = 1
	for case in CASE_LIST:
		print 'Testing case'+str(count)+': '+case
		count+=1
		out = run_cmd('adb shell am instrument -e class '+case+' -w com.lenovo.lsf.device.test/android.test.InstrumentationTestRunner')
		print out
		
	print 'Test END.'
	os.system("pause")
	
#The run command method
def run_cmd(command):
	cmd_list = command.split()
	proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	#The read(), close() and wait() come from the commnunicate() optimized part
	#Since we use 2 pipes, the communicate() will start multiple threads on windows, or call poll/select on unix.
	#So we don't call communicate, and we only read stdout in main thread
	out = proc.stdout.read()
	proc.stdout.close()
	proc.wait()

	if out.find('error: device not found')>=0:
		raise Exception('%s - %s' %(command, out))
	return out.replace('\r', '')

#Run the test method
test_case()
