'''
Created on 2013-9-16

@author: Administrator
'''

import os
import subprocess  
JOB_NAME=os.environ['JOB_NAME']
JAVA_HOME=os.environ['JAVA_HOME']
WORKSPACE=os.environ['WORKSPACE']
BUILD_NUMBER=os.environ['BUILD_NUMBER']
GIT_COMMIT=os.environ['GIT_COMMIT']
#folder1='\\tt'
#folder2='\\tt'
#folder3='\\tt'
moduleName1=['sc']
moduleName2=[]
moduleName3=[]
path1=WORKSPACE+'\\tt'
path2=WORKSPACE+'\\tt'
path3=WORKSPACE+'\\tt'
versionFile=open('version.txt','w')
versionFile.write(JOB_NAME++':'+'BUILD_NUMBER'+BUILD_NUMBER+'GIT_COMMIT'+GIT_COMMIT)
versionFile.close()
JOB_NAME=JOB_NAME.rsplit('_')
for value in JOB_NAME:
#    print value
    value=value.rsplit('-')
#    value=value.strip(',')
    print value
    for i in value:
#        print i
        if i in moduleName1:
            print 'ok'
            break
        elif i in moduleName2:
            subprocess.check_call("cp -r %s %s" % ('version.txt', path2))
            print 'ok2'
            break
        elif i in moduleName3:
            subprocess.check_call("cp -r %s %s" % ('version.txt', path3))
            print 'ok3'
            break
        else:
            continue
        break
    else:
        continue
    break


#if  JOB_NAME in moduleName1:
#    
#    if os.path.exists(path):
#        print "not mkdir folder"
#        subprocess.check_call("cp -r %s %s" % ('version.txt', path))
#    else:
#        print 'mkdir folder'
#        subprocess.check_call("mkdir tt ")
#        subprocess.check_call("cp -r %s %s" % ('version.txt', path))
else:
#    print  "%s is not there %s" %(JOB_NAME,'area !!')
    return 'JOB_NAME is not here'

#if __name__ == '__main__':
#    pass