# Class: pj-tomcat
#
# This module manages pj-tomcat
#
# Parameters:
#
# Actions:
#
# Requires:
#
# Sample Usage:
#
# [Remember: No empty lines between comments and class definition]

class tomcat {
	include tomcat::params,tomcat::server,tomcat::war

	

#node default {
#file { "/tmp/test.txt":
#	content =>"fffff",
#}
#}
}
