import os
#from xml.dom import minidom 
#from xml.dom.minidom import parse
#xmlDoc = parse('pom.xml')
#
##print xmlDoc.toxml()
##print xmlDoc.childNodes
#BIT_element = xmlDoc.firstChild
##print BIT_element.toxml()
##print BIT_element.childNodes
#list=BIT_element.childNodes
#print list[5]
#versionFile.write(JOB_NAME+'\n'+JOB_NAME)
#template = versionFile.replace('<id>', 'start')
#template = versionFile.replace('<id>', 'end')
#versionFile.write("JOB_NAME"+'\n'+"JOB_NAME")
#os.system ('mvn dependency:copy-dependencies')

versionFile=open('version.txt','r')
content=versionFile.readlines() 
versionFile.close() 
path=r'Z:\nexus-2.0.4-1-bundle\sonatype-work\nexus\storage\releases'
print content[0].strip('\n')
path=path + content[0].strip('\n')
print path
os.system ("cp -r %s %s" %('version.txt', path))
for line in content[1:]:
     lineContent=line.strip('\n')
     os.system ('mvn -P %s' %(lineContent))     
     print  "%s is there %s" %(line,'area !')



