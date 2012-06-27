file { "/etc/puppet/puppet.conf":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 0777,
     source => "puppet://master.example.com/config/puppet/puppet.conf",
    }
