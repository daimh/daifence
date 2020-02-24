# daifence
an Intrusion Detection System that bans malicious IP addresses found from SYC packets and ssh/SMB log files

###### Install
$ git clone https://github.com/daimh/daifence.git

###### initilize, assume the public network device is eno1
$ ./daifence --init eno1 

###### check the SYC packets in the past 60 seconds.
$ ./daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py

###### also check SSH log
$ ./daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py --ssh-invalid-users-file ssh-invalid-users.txt --ssh localhost:3

###### get help
$ ./daifence -h

###### crontab example
@reboot root /root/daifence/daifence  --init eno1
* * * * * root /root/daifence/daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py --ssh-invalid-users-file ssh-invalid-users.txt --ssh localhost:3
