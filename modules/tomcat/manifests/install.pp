class tomcat::install
	
{
	package {
		"$tomcat::params::tomcat":
		ensure => installed,
	}
	file {
		"$tomcat::params::tomcatfile":
#		mode =>775,
		source => "puppet://$fqdn/file/tomcat/file",
	}
#	exec {
#		"$tomcat::params::tomcatfile":
#		command => "tar -zxf $tomcatpackage.tar.gz",
#		path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
#		subscribe => File["$tomcatfile"],
#	}
}
