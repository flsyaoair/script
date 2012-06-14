tar -zxf ruby-1.8.7-p352.tar.gz
cd ruby-1.8.7-p352
./configure --prefix=/usr/local
make
make install
cd ..
tar -zxf facter-1.6.8.tar.gz 
cd facter-1.6.8
ruby install.rb
cd ..
tar -zxf puppet-2.7.14.tar.gz
cd puppet-2.7.14
ruby install.rb
