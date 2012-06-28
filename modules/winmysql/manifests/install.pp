
class win-mysql::install {
	  	package{"mysql":
	  		ensure => installed,
	  		provider => "msi",
	        source => "e:/tool/mysql5.5.msi",
#	        install_options =>{"INSTALLDIR" =>"e:/tool/mysql"},
#	        install_options => { 'INSTALLDIR' => 'C:\mysql-5.5' },
	        
	  	}  
     
}



