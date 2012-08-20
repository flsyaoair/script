define tomcat::vhost ($urlvalue) {
#include tomcat

file {
		"/var/lib/tomcat6/webapps/pp/WEB-INF/classes/configs/appcontext.xml":
         ensure => present,
        recurse => true,
#        source => "puppet:///var/lib/tomcat6/webapps/pp/WEB-INF/classes/configs/appcontext.xml",
		content =>template("tomcat/appcontext.xml.erb"),
		require => Exec["stopped"],
	}
}
