class tomcat::server {
#	$catalinahome ="/usr/$tomcat::install::tomcatpackage"
	
	service {
		"tomcat6":
		ensure => true,
		hasstatus => true,
#		hasrestart => true,
		enable => true,
#               restart =>"/etc/init.d/tomcat6",
             subscribe => File["/var/lib/tomcat6/conf/server.xml"],
#            refreshonly => true,
#		require => Class["tomcat::install"]
		
	}

	
    exec {
    	"stopped":
    	command => "service tomcat6 stop",
   	path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
    }
#    exec {
#    	"$catalinahome/bin/shutdown.sh":
#    	command => "/$catalinahome/bin/shutdown.sh",
#    	path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
#    }
}
