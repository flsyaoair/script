class centosSystembaseTest{
#  package {
#      ["php5-cli","apache2-mpm-worker"]:
#        ensure => installed;
#          }
  file { "/usr/dest/make":
     ensure => "present",
     recurse =>true,
     owner => "root",
     group => "root",
     mode => 777,
     source => "puppet://master.example.com/package/make",
    }



   exec { "shell":
    path => "/usr/bin:/usr/sbin:/bin:/usr/share",
    subscribe => File["/usr/dest/make"],
    refreshonly => true,
   command => "sudo /usr/dest/make/make.sh",

      }
        
}
