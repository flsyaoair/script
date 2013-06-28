import os
from xml.dom import minidom 
from xml.dom.minidom import parse
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
print content
for line in content:
     lineContent=line.strip('\n')
#     os.system ('mvn -P %s' %(lineContent))
     print  "%s is there %s" %(line,'area !')



