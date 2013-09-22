#BUILD_ID_BF='3-2-1-2014-17-11_13-37-00'
BUILD_ID=''
ver=''

versionNumFlie=open('versionNumFlie','r')
versionNumFlieContent=versionNumFlie.readlines()
versionNumFlie.close()
versionNum=versionNumFlieContent[0].strip('\n')
versionCalendar=versionNumFlieContent[1].strip('\n')
BUILD_ID_BF=versionNumFlieContent[2].strip('\n')
calendarBF=BUILD_ID_BF.split('_')[0]
calendarBF=calendarBF.split('-')
calendar=BUILD_ID.split('_')[0]
calendar=calendar.split('-')
calendar=ver.replace('.', '-')+'-'+BUILD_ID

list=[0,1,2,4,5,6]
for i in list:

    if calendar[i]>calendarBF[i]:
        versionCalendar=versionCalendar+1
        if versionCalendar>99:
            versionCalendar=01
            versionNum=versionNum+1
            print versionCalendar
            
        break
print versionCalendar
print versionNum
print calendar

  
    

     


       
    
    
