node default{
	include centosSystembase
}
node 'machinemaster'{
	include systembase
#	include mysql
}
        
node 'flsadministrator'{
	include win-mysql
}
node 'centos2'{
	include systembase
#	include mysql
}

#test Centos6 Deploy

node '102Test'{
	include centosSystembaseTest
#	
}
node '109Test'{
	include centosSystembaseTest
#	
}
node '118Test'{
	include centosSystembaseTest
#	
}
node '119Test'{
	include centosSystembaseTest
#	
}
node '105Test'{
	include centosSystembaseTest
#	
}
   
