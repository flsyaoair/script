'''
Created on 2013-9-30

@author: Administrator
'''
import os
import subprocess 
pomPath=r'F:\package'
dirname=os.listdir(pomPath)
dirname1='/'.join(dirname)
print dirname1
pomPath=r'F:\package'
goalPath='e:\\package'+'\\'
pomPath2=pomPath+'\\'
#localPath=os.getcwd()
#print localPath
#print dirname1
def diff():
    if os.path.isfile('pomfile.txt'):
        
        readmems=open('pomfile.txt','r')
        readmemline=readmems.readlines()
        readmemline=readmemline[0]
        for i in dirname:
    #    print readmems
            if i in readmemline:
                print i
            else:
                
#                subprocess.check_call('cd %s ' %(pomPath))
                subprocess.check_call('xcopy /Y %s %s' %(pomPath2+i,goalPath))
#                print i
            
        readmems.close()
    else: 
        os.system('echo > pomfile.txt')
        subprocess.check_call('xcopy /Y/S %s %s' %(pomPath,goalPath))

diff=diff()
readme=open('pomfile.txt','w')
readme.write(dirname1)
readme.close() 