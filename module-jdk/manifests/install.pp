class java::install{
	$jdkpackage="$java::params::jdksersion"
#	$server="$HOSTNAME"
#	$path="puppet://$server/file"
	package {
		"$jdkpackage":
		ensure =>install,
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