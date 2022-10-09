# mysql-selfmanaged

Cloud environment: GCP

Setting up a VM:

1. Click 'Create a VM instance'
2. Enter name of VM (I chose ...)
3. Change machine type to e2-medium (2 vCPU, 4 GB)
4. Under boot disk section,change operating system to Ubuntu
5. Under boot disk section, change version type to Ubuntu 18.04 LTS x86/64
6. Under Firewall section, allow BOTH HTTP and HTTPS traffic
7. Click 'Create'

Setting up

1. Enter into VM:
2. sudo apt-get update
3. sudo apt install mysql-server mysql-client
4. sudo mysql - LOGS INTO MYSQL
5. show databases
6. create user 'dba'@'%' identified by 'ahi2020';
7. select * user from mysql.user;
8. connect= f
9. create_engine = create_engine(connection_string)
10. create database template;
