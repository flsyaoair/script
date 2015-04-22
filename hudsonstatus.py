# -*- coding: UTF-8 -*- 
import urllib
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):   
        HTMLParser.__init__(self)   
        self.links = [] 
#        self.keyValue ='' 
    a_text = False
    i_text = False 

   
    def handle_starttag(self,tag,attr):  
        if tag == 'a': 
            print attr
            for (i,j) in attr:
                  if j=='tip':
                      for (i,j) in attr:
                          if i=='href':
                              self.links.append(j)
                               


                              self.a_text = True  
               
    def handle_endtag(self,tag):  
        if tag == 'a':  
            self.a_text = False
                  
              
    def handle_data(self,data):
        if self.a_text: 
            print data 

                  
def getPage():
    admin ='admin'
    password ='csst10'
    url = 'http://admin:password@192.168.203.10:8081/hudson/view/NVMP_java_build/job/storageServer4_ver3.6_build/'
    url=url.replace('admin', admin)
    url=url.replace('password', password)
    page = urllib.urlopen(url)
    html = page.read()
    hp = MyHTMLParser()   
    hp.feed(html)   
    hp.close()
    i=hp.links[0]
#    print i
    i=i.split('/')
    
    print i[len(i)-2:len(i)-1]
#    help (type(i))
#    url=
    print(hp.links[0]) 

bulid= getPage()