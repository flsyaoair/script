class tomcat::install(
	$tomcatpackage="apache-tomcat-$tomcat::params::version",
	$tomcatfile ="/etc/puppet/modules/tomcat/file",
) {
#	package {
#		"tomcat-server":
#		ensure => install,
#	}
	file {
		"$tomcatfile":
#		mode =>775,
		source => "puppet://$fqdn/file/tomcat/file",
	}
	exec {
		"$tomcatfile":
		command => "tar -zxf $tomcatfile/$tomcatpackage.tar.gz",
		path =>"/usr/bin:/usr/sbin:/bin:/usr/share",
		subscribe => File["$tomcatfile"],
	}
}
