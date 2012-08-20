node default {

	include tomcat
tomcat::vhost {"master.example.com":
            
            urlvalue =>'http://192.168.203.178:8389/solr"',
 }
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
   
