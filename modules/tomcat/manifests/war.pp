class tomcat::war 
         {
	$dlpath ="/usr/apache-tomcat-5.5.35/webapps"
	$dlwar ="/usr/repositorise/pp.war"
	exec {
		"war":
		command => "cp $dlwar /var/lib/tomcat6/webapps",
                path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
#		require => Class["tomcat::server"],
#		subscribe => File["$tomcat::install::tomcatfile"],
                require => Exec["stopped"],
#		notify =>Service["$tomcat::server::tomcat"],
	}
  file {
		"/var/lib/tomcat6/conf/server.xml":
                ensure => present,
                recurse => true,
               source => "puppet:///var/lib/tomcat6/conf/server.xml",
#		content =>template("tomcat/server.xml.erb"),
		require => Exec["stopped"],
	}
}
