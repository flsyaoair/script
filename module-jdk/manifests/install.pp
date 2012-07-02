class java::install($jdkpackage){
	
	$ujdkpa="$java::params::ujdkv"
	$cjdkpa="$java::params::cjdkv"

#	default => $jdkpackage
	
#	$server="$HOSTNAME"
#	$path="puppet://$server/file"
	package {
		"java":
#        name => $operatingsystem ? {
#        /(Red Had|CentOS|Ubuntu)/ =>"$jdkpackage",
#		Solaris =>"$jdkpackage",
#		},
		ensure =>installed,
		name =>$jdkpa,

		
#		source =>puppet://$fqdn/file
	}
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
  
  	case $operatingsystem {
  	Ubuntu :{
  		$jdkpa="$ujdkpa"
  	}
  	/(CentOS|Red Had)/:{
  		$jdkpa = "$cjdkpa"
  		
  	}
  	default:{
  		$jdkpa="$ujdkpa"
  		
  	}
  }
  
  }
  
    
