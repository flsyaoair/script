class tomcat::params {
	$version ="5.5.35"
        $tomcat ="tomcat6"   
#       tomcat6 webapps address
#        http://192.168.203.178:8983/solr  
        $tomcatfile ="/etc/puppet/modules/tomcat/file"
        $dlpath ="/var/lib/tomcat6/webapps"
	$dlwar ="/usr/repositories/pp.war"
        $dlconf = "/var/lib/tomcat6/conf"
}
