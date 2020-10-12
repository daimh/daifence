# daifence
an Intrusion Detection System that bans malicious IP addresses found from SYC packets and ssh/SMB log files

### Install
$ git clone https://github.com/daimh/daifence.git

### Initilize, assume the public network device is eno1
$ ./daifence --ipv 4 --init eno1 

### Check the SYC packets in the past 60 seconds.
$ ./daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py

### Check SSH log
$ ./daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py --ssh-invalid-users-file ssh-invalid-users.txt --ssh localhost:3

### get help
$ ./daifence -h

### Crontab example
@reboot root /root/daifence/daifence --ipv 4 --init eno1

\* * * * * root /root/daifence/daifence --ipv 4 -w 60 -m 1000 -f whitelist.txt --rule-file rules.py --ssh-invalid-users-file ssh-invalid-users.txt --ssh localhost:3

## Contribute

Contributions are always welcome!

## Copyright

Developed by [Manhong Dai](mailto:daimh@umich.edu)

Copyright © 2020 University of Michigan. License [GPLv3+](https://gnu.org/licenses/gpl.html): GNU GPL version 3 or later 

This is free software: you are free to change and redistribute it.

There is NO WARRANTY, to the extent permitted by law.

## Acknowledgment

Ruth Freedman, MPH, former administrator of MNI, UMICH

Fan Meng, Ph.D., Research Associate Professor, Psychiatry, UMICH

Huda Akil, Ph.D., Director of MNI, UMICH

Stanley J. Watson, M.D., Ph.D., Director of MNI, UMICH
