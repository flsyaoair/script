class java::install{
	
	$ujdkpa="$java::params::ujdkv"
	$cjdkpa="$java::params::cjdkv"

#	default => $jdkpackage
	case $operatingsystem {
  	Ubuntu :{
  		$java ="$ujdkpa"
  	}
  	/(CentOS|Red Had)/:{
  		$java = "$cjdkpa"
  		
  	}
  	default:{
  		$java="$ujdkpa"
  		
  	}
  }

	package {
		"$java":
#        name => $operatingsystem ? {
#        /(Red Had|CentOS|Ubuntu)/ =>"$jdkpackage",
#		Solaris =>"$jdkpackage",
#		},
		ensure =>installed,}
#		name =>"$jdkpa",

		
#		source =>puppet://$fqdn/file
	
	
#	exec {
#		"$jdkpackage":
#		 command =>"$jdkpackage",
#		 mode => 0775,
#		source => "puppet://$server/file"
		
#	}
#	file {
#		"$path/java":
#		source => "$path/java",
#	}
  
 } 	
  

  
    
