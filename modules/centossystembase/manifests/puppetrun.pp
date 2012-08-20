class centosSystembase::puppetrun {

 file { "/usr/dest/make/make.sh":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://109test/pack/make/make.sh",
    }
     file { "/usr/dest/make/test.sh":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://109test/pack/make/test.sh",
    }



   exec { "/usr/dest/make/make.sh":
    path => "/usr/bin:/usr/sbin:/bin:/usr/share",
    subscribe => File["/usr/dest/make/make.sh"],
    refreshonly => true,
   command => "sudo /usr/dest/make/make.sh",
 # example/make.sh:dstat -cdlmnpsyt --output $HOSTNAME.csv,
 #                 scp -r  $HOSTNAME.csv  root@$HOSTNAME:/root/rtsprecord   

      }
      exec { "/usr/dest/make/test.sh":
    path => "/usr/bin:/usr/sbin:/bin:/usr/share",
    subscribe => File["/usr/dest/make/test.sh"],
    refreshonly => true,
   command => "sudo /usr/dest/make/test.sh",
 # example/make.sh:dstat -cdlmnpsyt --output $HOSTNAME.csv,
 #                 scp -r  $HOSTNAME.csv  root@$HOSTNAME:/root/rtsprecord   

      }
      }
      
