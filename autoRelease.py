import os
releaseFile=open('releases.txt','r')
content=releaseFile.readlines()
releaseFile.close()
groupId=content[0].strip('\n')
#for line in content:
#    line=line.strip('\n').
pName=groupId.rsplit('.')
if pName[0]=='nvmp':

        for line in content[1:]:
            i='-ver'
            version=line[(line.index(i)+1):-5]
            print 'version: %s' % version
            artifactId=line[:line.index(i)]
            print 'artifactId: %s' % artifactId
            lineString=line[-4:]
            print lineString

     
  
else:
        print 'it is gameOver'
      
    
#print dir(content)
#print content
#print content.index(projectName)
#for content