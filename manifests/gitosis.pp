# Class: gitosis
#
# This installs and configures gitosis 
#
# Requires:
#  - Class[git]
#
class git::gitosis {
	$projectroot="/home/git/repositories/"
#  include ::git
  package {['gitosis',"gitweb"]:
    ensure => present,
    alias =>"gitinstall",
  }
  file {
  	"/etc/gitweb.conf":
  	ensure => present,
  	recurse => true,
  	content =>template("gitweb.conf.erb"),
  	require => Package ["gitinstall"]
  }
}
