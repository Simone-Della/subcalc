#!/usr/bin/python3

#
# Subnet Calculator
# version 0.01
#
# Author: Simone Dellabora
#
# file: subcalc.py
# Software subnet calculator.
#
# Python version 3
#

# import module
import os
import sys
import ipaddress
import pprint



def main():

# Description start program
  print ("\n")
  print ("***********************************************")
  print ("*       Subnet Calculator (CIDR) - v0.01      *")
  print ("***********************************************")
  print ("*       Author: Simone Dellabora              *")
  print ("***********************************************")
  print ("\n")

# Variable ip address
  try:
    ipaddr = input("Insert ip/mask or ip/prefix: ")
    ip = ipaddress.IPv4Interface(ipaddr)
  except ValueError:
    sys.exit("not a valid ip!")

# Var
  network = ipaddress.ip_network(ip.network)
  all_hosts = list(network.hosts())
  count = 0

  print ("\n")
  print ("network: ", network)
  print ("broadcast: ", network.broadcast_address)
  print ("wildmask: ", ip.with_hostmask)
  print ("netmask: ", ip.with_netmask)
  print ("ip version: ", ip.version)


  for object in all_hosts:
    count = count + 1
  print ("hosts per subnet: ", count)

  try:
    print ("host address range: ", all_hosts[0], "-", all_hosts[-1])
  except IndexError:
    print ("host address range: none")

# Print all hosts for subnet on an external file
  print ("\n")

  question_file = input("Do you want to print all the hosts on an external file ? - yes/no \n")

  if question_file == "yes":
    head = "\n"
    file = open('hosts__%s.txt' % network.network_address, 'w' )
    for ip in all_hosts:
      host = str(ip) + head
      file.write(str(host))
    file.close()
    print ("ok")
  elif question_file == "no":
    print ("file not printed!")
  else:
    print ("Not a valid answer, ")


  print ("\n")


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
