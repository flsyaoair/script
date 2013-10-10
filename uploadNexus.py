'''
Created on 2013-9-22

@author: Administrator
'''
import os
import subprocess 
y='<dependency>'
x='</dependencies>' 
#JOB_NAME='hbjh_sc_ver3.0.1_build'
#JOB_NAME='skyFS-controller_master_centos32'
JOB_NAME=os.environ['JOB_NAME']
#JAVA_HOME=os.environ['JAVA_HOME']
WORKSPACE=os.environ['WORKSPACE']
BUILD_NUMBER=os.environ['BUILD_NUMBER']
#GIT_COMMIT=os.environ['GIT_COMMIT']
moduleName1=['sc']
moduleName2=['skyFS']
moduleName3=['skyembedproxyserver','storageServer','streamingserver','PTZProxyServer','workstateServer']
GroupIdNexus=['sc','scp']
#WORKSPACE="fls"
#hudsonVersion='ver1.7.1'
class hudsonBuild():
    def upload(self,moduleName1,moduleName2,moduleName3):
        global JOB_NAME
        JOB_NAMEL=JOB_NAME.rsplit('_')
        for value in JOB_NAMEL:
            value=value.rsplit('-')
            for i in value:
        #        print i
                if i in moduleName1:
                    groupId='NVMP'
                    print 'ok'
                    break
                elif i in moduleName2:
                    groupId='skyFS'
                    print 'ok2'
                    break
                elif i in moduleName3:
                    groupId='NVMP-c'
                    print 'ok3'
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            groupId="1"
        return groupId
    
def configNexus():
    
    groupId=hudsonBuild().upload(moduleName1,moduleName2,moduleName3) 
    global JOB_NAME
    global WORKSPACE
    global BUILD_NUMBER
    JOB_NAME_L=JOB_NAME.rsplit('_')
#    print JOB_NAME_L
    i='_ver'
    x='_b-'
#    y='_'
    if groupId=='1':
        groupId=JOB_NAME_L[0]
        branch=JOB_NAME_L[2]
        version=JOB_NAME_L[3]+'.'+BUILD_NUMBER
        artifactId=JOB_NAME_L[1]+'_'+JOB_NAME_L[2]+'_'+JOB_NAME_L[4]
        extension='zip'
        fileName=JOB_NAME_L[1]+'.'+extension
    elif groupId=='NVMP':
        JOB_NAME_L_1=JOB_NAME_L[0]
        version=JOB_NAME[(JOB_NAME.index(i)+1):(JOB_NAME.index(i)+9)]
        version=version+'.'+BUILD_NUMBER
        if JOB_NAME_L_1=='sc':
            groupId=groupId+'.'+version.replace('.','_')
            artifactId=JOB_NAME_L[0]
        else:   
            groupId=groupId+'.'+JOB_NAME_L_1
            artifactId=JOB_NAME_L[0]+'_'+JOB_NAME_L[1]
        extension='war'
        fileName=artifactId+'-'+version+'.'+extension
        WORKSPACE=WORKSPACE+'\dest' 
    elif groupId=='skyFS':
        hudsonVersion=os.environ['version']
        branch=JOB_NAME_L[1]
        version=hudsonVersion
        version=version+'.'+BUILD_NUMBER
        if '64' in  JOB_NAME_L[len(JOB_NAME_L)-1]:
            
            groupId='skyFS-64'+'.'+version.replace('.','_')
        
        else:
            groupId=groupId+'.'+version.replace('.','_')    
        artifactId=JOB_NAME_L[0]+'_'+JOB_NAME_L[1]+'_'+JOB_NAME_L[len(JOB_NAME_L)-1]
        extension='zip'
        fileName=JOB_NAME_L[0]+'.'+extension
        WORKSPACE=WORKSPACE
    elif groupId=='NVMP-c':
        JOB_NAME_L_1=JOB_NAME_L[0]
        extension='zip'
        if JOB_NAME_L_1 in moduleName3:
            groupId='nvmp'
            version=JOB_NAME_L[1]
            groupId=groupId+'.'+version.replace('.','_')
            artifactId=JOB_NAME_L[0]
            fileName=JOB_NAME_L[0]+'.'+extension
        else:
            groupId='nvmp.'+JOB_NAME_L[0]
        #        branch=JOB_NAME_L[2]
            version=JOB_NAME_L[2]+'.'+BUILD_NUMBER
            artifactId=JOB_NAME_L[0]+'_'+JOB_NAME_L[1]
           
            fileName=JOB_NAME_L[1]+'.'+extension         
    else:
        print 'not ok !!!!!!!!'
        extension='zip'
        WORKSPACE=WORKSPACE+'\dest'

    content="""
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<repositories>  
  <repository>  
    <id>local-nexus</id>  
    <url>http://192.168.203.14:8081/nexus/content/repositories/snapshots</url>  
    <releases>  
      <enabled>true</enabled>  
    </releases>  
    <snapshots>  
      <enabled>true</enabled>  
    </snapshots>  
  </repository>  
</repositories>  
<groupId>com.csst</groupId>
<artifactId>release</artifactId>
<version>lasted</version>
<packaging>rar</packaging>
<name>release</name>
<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>


<profiles>
<profile>
<id>%fileName%</id>
<build>
  <defaultGoal>deploy:deploy-file</defaultGoal>
  <plugins>
    <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-deploy-plugin</artifactId>
    <version>2.7</version>
    <configuration>
          <url>http://192.168.203.14:8081/nexus/content/repositories/releases</url>
          <file>%WORKSPACE%\%fileName%</file> 
          <repositoryId>nexus-snapshots</repositoryId>
          <groupId>%groupId%</groupId>
          <artifactId>%artifactId%</artifactId>
          <version>%version%</version>
          <type>%extension%</type>
      </configuration>          
    </plugin>  
  </plugins>
</build>
</profile>
</profiles> 


<build> 
<plugins> 
<plugin> 
     <artifactId>maven-dependency-plugin</artifactId> 
       <configuration> 
            <outputDirectory>../package</outputDirectory> 
            <excludeTransitive>false</excludeTransitive> 
            <stripVersion>false</stripVersion> 
        </configuration> 
    </plugin>
</plugins>
</build>
<dependencies>
<dependency>
<groupId>%groupId%</groupId>
<artifactId>%artifactId%</artifactId>
<version>%version%</version>
<type>%extension%</type>
</dependency>
</dependencies>
</project>
"""
        
    content=content.replace('%groupId%',groupId)
    content=content.replace('%artifactId%',artifactId)
    content=content.replace('%version%',version)
    content=content.replace('%extension%',extension)
    content=content.replace('%WORKSPACE%',WORKSPACE)
    content=content.replace('%fileName%',fileName)
    versionFile=open('pom.xml','w')
    versionFile.write(content)       
    versionFile.close()
#    filepack=artifactId+version+extension
    subprocess.check_call('mvn -P %s' %(fileName))
#    os.system ('mvn dependency:copy-dependencies')
#    os.system ('mvn -P %s' %(line))
#upload=uploadNexus().upload(moduleName1,moduleName2,moduleName3)
uploadNexus=configNexus()
#print upload
        
    
 



  
        