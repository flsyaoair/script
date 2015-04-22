import os
import subprocess
#JOB_NAME=os.environ['CLONE']
CLONE="gameover_master"
REPOSURL="gameover_git@192.168.203.211:gameover.git;gameover1_git@192.168.203.211:gameover1.git;"
REPOSURL=REPOSURL.rsplit(';')
class cloneRepository ():
    def dis (self):
        repos=CLONE.rsplit(';')
        for i in repos:
            reposD=i.rsplit('_')
            repositoy=reposD[0]
            reposBranch=reposD[1]
            if os.path.exists(repositoy):
                subprocess.check_call('cd %s && git checkout %s && git pull ' %(repositoy,reposBranch))
            
            else:
                for i in REPOSURL:
                    if repositoy+"_" in i:
                        repositoyurl=i.rsplit('_')[1]
                        subprocess.check_call('git clone %s' %(repositoyurl))
        return repositoy
def test ():
    cloneRepository().dis()
up=test()
  
        
        
        