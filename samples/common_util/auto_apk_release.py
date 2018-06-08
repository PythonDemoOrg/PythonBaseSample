# -*- coding: UTF-8 -*-

# Filename : auto_apk_release.py
# author by : WeiQi

appNames = ["联营达", "易企订", "佐邻订货", "优厨帮", "蓉城易购", "创康良品", "淘广材", "烁客", "成铁生活", "新东日建材"]
appIds = ["LYD", "YQD", "ZL", "YCB", "RCYG", "CKLP", "TGC", "SK", "CTSH", "XDRJC"]
apkNames = ["lianyingda.cn", "yidianlife.com", "zoli.vip", "168ycb.com", "028rcyg.com", "cdck168.com", "zm-am.com",
            "svlok.com", "ctshgs168.com", "newdongri.com"]
targetDir = "H:\\WORK_DHB_STUDIO\\Android\\Code\\DHB\\dHB\\src\\main\\res"
sourceDir = "H:\\custom_app_img\\"

# 拷贝文件
def copyFiles(sourceDir, targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
#! python3
# 替换代码和文件，所替换的文本内容必须是当前文件的唯一字符串（可以加长需要替换扥字符串实现唯一性）
#如需增加要替换的代码内容或者资源，只需要增加数组并且调用替换方法即可
import os
#app启动名
appNames = ["app1","app2","app3"]
#gradle中的applicationId
replaceText = ["text1","text2","text3"]
#gradle中的applicationId
appIds = ["applicationId1","applicationId2","applicationId3"]
#输出apk的文件名
apkNames = ["apk1","apk2","apk3"]
#项目的资源文件夹路径
targetDir = "/Users/smartzheng/AndroidStudioProjects/MyApplication/app/src/main/res"
#配置自己存放不同apk资源图片的路径,分别命名为apk1，apk2，apk3...（apkNames的每个元素）需要替换的图片必须名字对应一致
sourceDir = "/Users/smartzheng/custom_app_imgs/"

# 拷贝替换文件，传入图片路径和项目资源目录
def copyFiles(sourceDir, targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)

#替换文本内容，传入文件路径，原字符串，目标字符串
def replaceText(f_path, text1, text2):
    with open(f_path, 'r', encoding='utf-8') as r:
        s = r.read()
        replace = s.replace(text1, text2)
    with open(f_path, 'w', encoding='utf-8') as w:
        w.write(replace)
    r.close()
    w.close()

print("begin")
# 循环执行打包操作
for i in range(len(appNames)):
    if i != 0:
        # 替换Config配置文件下的代码内容
        replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/src/main/java/com/smartzheng/Config.java',replaceText[i-1],replaceText[i])
        #替换app名字
        replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/src/main/res/values/strings.xml', appNames[i-1],appNames[i])
        #替換applicationId,即替换包名
        replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/build.gradle',appIds[i-1],appIds[i])
        #替换输出的路径
        replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/build.gradle',apkNames[i-1],apkNames[i])
        # 替换资源图片
        copyFiles(sourceDir + apkNames[i], targetDir)
        # 打包(windows为gradlew assembleRelease)
        os.system("gradle assembleRelease")

# 将代码及资源文件回归到原位
replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/src/main/java/com/smartzheng/Config.java',replaceText[len(appNames) - 1],replaceText[0])
replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/src/main/res/values/strings.xml', appNames[len(appNames) - 1],appNames[0])
replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/build.gradle',apkNames[len(appNames) - 1],apkNames[0])
replaceText(r'/Users/smartzheng/AndroidStudioProjects/MyApplication/app/build.gradle',appIds[len(appIds) - 1],appIds[0])
copyFiles(sourceDir + replaceText[0], targetDir)
print("success")