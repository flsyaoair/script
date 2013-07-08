import os
y='<dependency>'
x='</dependencies>'
dependency="""
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
</dependencies>
</project>
"""
releaseFile=open('releases.txt','r')
releaseContent=releaseFile.readlines()
releaseFile.close()

groupId=releaseContent[0].strip('\n')
pName=groupId.rsplit('.')
if pName[0]=='nvmp' or pName[0]=='PTSP'or pName[0]=='PTSP-64' or pName[0]=='skyFS'or pName[0]=='skyFS-64'or pName[0]=='':
    for line in releaseContent[1:]:
        line=line.strip('\n')
        i='-ver'
        version=line[(line.index(i)+1):-5]
        artifactId=line[:line.index(i)]
        extension=line[-3:]
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
    <id>%artifactId%-%version%.%extension%</id>
    <build>
      <defaultGoal>deploy:deploy-file</defaultGoal>
      <plugins>
        <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-deploy-plugin</artifactId>
        <version>2.7</version>
        <configuration>
              <url>http://192.168.203.14:8081/nexus/content/repositories/releases</url>
              <file>..\package\%artifactId%-%version%.%extension%</file> 
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
        versionFile=open('pom.xml','w')
        versionFile.write(content)       
        dependencyContent=content[content.index(y):content.index(x)]
        dependency=dependency[:(dependency.index(x))]+dependencyContent+dependency[(dependency.index(x)):]
        versionFile.close()
#        os.system ('mvn dependency:copy-dependencies')
#        os.system ('mvn -P %s' %(line))
        continue
    upPomFile=open('autoUpReleases\pom.xml','w')
    upPomFile.write(dependency)
    upPomFile.close()
    os.system('git commit -am "%s"' %(releaseContent))
    
#    os.system(command)
     
#        print dependency
        
#        os.system ('mvn dependency:copy-dependencies')
#        os.system ('mvn -P %s' %(line))
        
     
  
else:
        print 'it is gameOver'
      
    
#print dir(content)
#print content
#print content.index(projectName)
#for content