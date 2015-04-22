import os
import subprocess 
dirname=os.listdir('dd')
dirname1='/'.join(dirname)
path='e:\\test'
path1='e:\\test1'
def diff():
    readmems=open('pomfile.txt','r')
    readmemline=readmems.readlines()
    readmemline=readmemline[0]
    for i in dirname:
#    print readmems
        if i in readmemline:
            print 'ok'
            subprocess.check_call('cmd',shell=True)
#            subprocess.check_call('xcopy /Y %s %s' %(i,path))
           
        else:
#            print path
#            print i
            
            subprocess.check_call('xcopy /Y %s %s' %(i,path))
            subprocess.check_call('xcopy /Y %s %s' %(i,path1))
#            subprocess.check_call('xcopy /Y %s %s' %(i,path))
#            print i
        
    readmems.close()
#    return i
diff=diff()
readme=open('pomfile.txt','w')
readme.write(dirname1)
readme.close()   

#name='s_dv64_dv'
#name[:-2]
#if '64' in name[:-2]:
#    print 1
#    
#
#else:
#     print 2   





#try:
#    
#    f = open("file-not-exists", "r")
#except IOError as e:
#    dir(e)
#    print("open exception: %s: %s\n" %(e.errno, e.strerror))

#
#versionFile=open('version.txt','w')
#versionFile.write('BUILD_NUMBER')
#versionFile.close()
#name='tbb-tb-ver1.0.5_dac.rar-sc_dd_uu'
##name=name.rsplit('_')
##print name.extend
#print name[:-name.index('-')]
#print  dir(name)

#list=['sc','tb']
#list2=['tbb','tb']
#name='s_dv_dv'
#name=name.rsplit('-')
#print name
##name=['df','sd']
#for value in name:
##    print value
#    value=value.rsplit('-')
##    value=value.strip(',')
##    print value
#    for i in value:
##        print i
#        if i in list:
#            print 'ok'
#            break
#        elif i in list2:
#            print 'ok2'
#            break
#        else:
#            continue
#        break
#    else:
#        continue
#    break
#else:
#    print 'gg'
      
  
#    print value
#if valueName='sc':
#    print ok
 
    
#subprocess
#import os
#var='test'
#os.environ['var']=var
#
#os.system('set var=%var%')
#from optparse import OptionParser    
#    
#parser = OptionParser()    
##parser.add_option("-f", "--file", dest="filename",    
##                  help="write report to FILE", metavar="FILE")    
##parser.add_option("-q", "--quiet",    
##                  action="store_false", dest="verbose", default=True,    
##                  help="don't print status messages to stdout")    
##    
##(options, args) = parser.parse_args()
#
#
#parser.add_option("-f", "--file",    
#                  action="store", type="string", dest="filename")    
#args = ["-f", "foo.txt"]    
#(options, args) = parser.parse_args(args)    
#print options.filename  


#class Character():
#    def intersect(self,seq1,seq2):
#        res = ['b','v','d'] # Start empty
##        i=['b','v']
#        for x in seq1: # Scan seq1
#            variable="nvmp"
#            if x in seq2: # Common item?
#                res.append(x) # Add to end
#        else:
#             variable="nvmp1"
#        return variable
##Character=Character()
##character=Character().intersect('avc','sch')
#va=Character().intersect('avc','sch')
##print character
#print va

#seq1="dfg"
#seq2='ugd'
#def intersect():
#        res = ['b','v'] # Start empty
##        i=['b','v']
#        for x in seq1: # Scan seq1
#            if x in seq2: # Common item?
#                res.append(x) # Add to end
#        return res
#print intersect('df','dfg')





#class FirstClass(): # Define a class object
#     def setdata(self, value): # Define class methods
#         self.data = value # self is the instance
#     def display(self):
#         print self.data # self.data: per instance
#
#x=FirstClass()
#x.setdata('tt')
#x.display()
