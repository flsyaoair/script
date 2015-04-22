
#devenv.com EmbedProxyServer.sln /build RELEASE /out output.txt
import os
import subprocess 
#JOB_NAME=os.environ['JOB_NAME']
JOB_NAME='0858huabeiYT_skyembedproxyserver_ver3.0.1_build'
JOB_NAMEL=JOB_NAME.rsplit('_')
#print JOB_NAMEL
def compileBuild ():
    if 'skyembedproxyserver' in JOB_NAMEL:
        print 'ok'
        
#        os.system('rar a -r test.rar bin')
        subprocess.check_call('devenv.com ..\EmbedProxyServer.sln /build RELEASE /out ..\output.txt')
        subprocess.check_call('rar a -r  ..\\skyembedproxyserver.zip ..\\bin')
#    subprocess.check_call('xcopy /Y %s %s' %(pomPath2+i,goalPath)) 

    elif 'storageServer' in JOB_NAMEL:
        print 'ok1'
        subprocess.check_call('devenv.com ..\CentralizeStorage.sln /build RELEASE /out ..\output.txt')
        subprocess.check_call('rar a -r ..\\storageServer.zip ..\\bin')
    elif 'streamingserver' in JOB_NAMEL:
        print 'ok2'
        subprocess.check_call('devenv.com ..\NewStreamingServer.sln /build RELEASE /out ..\output.txt')
        subprocess.check_call('rar a -r ..\\streamingserver.zip ..\\bin')
    elif 'PTZProxyServer' in JOB_NAMEL:
        print 'ok3'
        subprocess.check_call('devenv.com ..\PtzProxyServer.sln /build RELEASE /out ..\output.txt')
        subprocess.check_call('rar a -r ..\\PTZProxyServer.zip ..\\bin')
    elif 'workstateServer' in JOB_NAMEL:
        print 'ok4'
        subprocess.check_call('devenv.com ..\workstateServer.sln /build RELEASE /out ..\output.txt')    
        subprocess.check_call('rar a -r ..\\workstateServer.zip ..\\bin')
build=compileBuild() 
 