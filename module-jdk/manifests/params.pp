class java::params {
	$ujdkversion = "openjdk-6-jdk"
	$cjdkversion ="java"
	case $operatingsystem {
  	Ubuntu :{
  		$jdkversion="$ujdkversion"
  	}
  	/(CentOS|Red Had)/:{
  		$jdkversion = "$cjdkversion"
  		
  	}
  	default:{
  		$jdkversion="$ujdkversion"
  		
  	}
	
		
	}
	
	}
	
