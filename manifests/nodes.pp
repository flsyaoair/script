node 'machinemaster'{
	include systembase
	include mysql
}
        
node 'flsadministrator'{
	include win-mysql
}
   
