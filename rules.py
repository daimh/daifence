#Honeypot ports
len(set([20,21,23,25]).intersection([l[DPT] for l in L])) > 0
#Honeypot IP address. The example below assumes the computer has a honeypot IP address 1.2.3.4
len(set(['1.2.3.4']).intersection([l[DST] for l in L])) > 0
#Excessive packets
len(L) > 100 or len(set(L)) > 10
#SSH/HTTP/HTTPS attack on multiple IP addresses
len(set([l[DST] for l in L if l[DPT] in [22, 80, 443] ])) > 3
