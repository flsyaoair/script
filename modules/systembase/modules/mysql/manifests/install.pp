class mysql::install{
	package{["MySQL-server.rpm","MySQL-client.rpm"]:
		ensure=> installed,
                provider =>yum,
		require=> User["mysql"],
                source => "puppet://master.example.com/package/mysql",
                subscribe => File["/usr/dest/mysql"],
	}
	
	user {"mysql":
		ensure => present,
		comment =>"Mysql user",
		gid =>"mysql",
		shell =>"/bin/false",
		require => Group["mysql"],
	}
	
	group {"mysql":
		ensure => present,
	}

       file { "/usr/dest/mysql":
                ensure => "present",
                recurse =>true,
                owner => "root",
                group => "root",
                mode => 777,
                source => "puppet://master.example.com/package/mysql",
    }
	
}
