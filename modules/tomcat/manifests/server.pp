class tomcat::server {
#	$catalinahome ="/usr/$tomcat::install::tomcatpackage"
	
	service {
		"$tomcat::params::tomcat":
		ensure => true,
		hasstatus => true,
#		hasrestart => true,
		enable => true,
#               restart =>"/etc/init.d/tomcat6",
             subscribe => File["$tomcat::params::dlconf/server.xml"],
#            refreshonly => true,
#		require => Class["tomcat::install"]
		
	}

	
    exec {
    	"stopped":
    	command => "service $tomcat::params::tomcat stop",
   	path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
    }
#    exec {
#    	"$catalinahome/bin/shutdown.sh":
#    	command => "/$catalinahome/bin/shutdown.sh",
#    	path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
#    }
}
