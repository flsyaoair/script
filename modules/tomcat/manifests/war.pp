class tomcat::war 
         {
         	
#	$dlconf = "/var/lib/tomcat6/conf"
	exec {
		"war":
		command => "rm -rf $tomcat::params::dlpath/pp \
                    && cp $tomcat::params::dlwar $tomcat::params::dlpath \
                    && sleep 10",
        path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
#		require => Class["tomcat::server"],
#		subscribe => File["$tomcat::install::tomcatfile"],
#        require => Exec["stopped"],
#		notify =>Service["$tomcat::server::tomcat"],
	}
  file {
		"$tomcat::params::dlconf/server.xml":
         ensure => present,
        recurse => true,
        source => "puppet://$tomcat::params::dlconf/server.xml",
#		content =>template("tomcat/server.xml.erb"),
#		require => Exec["stopped"],
	}
	
}
