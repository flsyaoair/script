class java::install($jdkpackage){
#	default => $jdkpackage
	$jdkpackage="$java::params::jdksersion"
#	$server="$HOSTNAME"
#	$path="puppet://$server/file"
	package {
		"$jdkpackage":
#        name => $operatingsystem ? {
#        /(Red Had|CentOS|Ubuntu)/ =>"$jdkpackage",
#		Solaris =>"$jdkpackage",
#		},
		ensure =>installed,
		
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
  
  }
    
