import shutil
import os
#print os.environ['JAVA_HOME']
JAVA_HOME=os.environ['JAVA_HOME']
WORKSPACE=os.environ['WORKSPACE']
#WORKSPACE=r'd:\test'
path1=WORKSPACE+'\db'
path2=WORKSPACE+'\db'
path3=WORKSPACE+'\bin'
moduleName1=['sc','monitor','ptz']
moduleName2=['cn','sn','eye']
JOB_NAME='sc'
versionFile=open('version.txt','w')
versionFile.write(JOB_NAME+'\n'+JOB_NAME)
versionFile.close()
if  JOB_NAME in moduleName1:
    
    if os.path.exists('path1'):
        print "not mkdir folder"
        os.system ("cp -r %s %s" % ('version.txt', path1))
#       shutil.copyfile('version.txt',WORKSPACE+r'\version2.txt')
    else:
        print 'mkdir folder'
        os.system ("mkdir %s" %(path1))
        os.system ("cp -r %s %s" % ('version.txt', path1))
elif  JOB_NAME in moduleName2:
    
    if os.path.exists('path2'):
        print "not mkdir folder"
        os.system ("cp -r %s %s" % ('version.txt', path2))
#       shutil.copyfile('version.txt',WORKSPACE+r'\version2.txt')
    else:
        print 'mkdir folder'
        os.system ("mkdir %s" %(path2))
        os.system ("cp -r %s %s" % ('version.txt', path2))   
else:
    print  "%s is not there %s" %(JOB_NAME,'area !!')