# Class: mysql
#
# This module manages mysql clients and provides tools for dealing with mysql
#
# Requires:
#   class puppet
#   $lsbProvider is set in site manifest
#
class mysql {
     include mysql::install
} 
