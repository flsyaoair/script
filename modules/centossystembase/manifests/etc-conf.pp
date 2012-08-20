class centosSystembase::etc-conf {
	file { "/etc/sudoers":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://109test/config/sudoers",
    }
    file { "/etc/puppet/auth.conf":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://109test/config/puppet/auth.conf",
    }
     file { "/etc/puppet/puppet.conf":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://109test/config/puppet/puppet.conf",
    }
  
	
}
