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

# Function remove file with size equal to 0
def removeTXT(name_fileTXT):
  dimension = 0
  for dirpath, dirs, name_fileTXT in os.walk('.'):
    for file in name_fileTXT:
      path = os.path.join(dirpath, file)
      if os.stat(path).st_size == dimension:
        os.remove(path)
def removeXLS(name_fileXLS):
  dimension = 0
  for dirpath, dirs, name_fileXLS in os.walk('.'):
    for file in name_fileXLS:
      path = os.path.join(dirpath, file)
      if os.stat(path).st_size == dimension:
        os.remove(path)


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


  name_fileTXT = 'hosts__%s.txt' % network.network_address
  name_fileXLS = 'hosts__%s.xls' % network.network_address

# Open file and write ip of subnet
  if question_file == "yes":
    print ("\n")
    print ("-1   format .txt")
    print ("-2   format .xls")
    print ("\n")
    typefile = input("Press 1 or 2\n")
    if typefile == "1":
      head = "\n"
      file = open(name_fileTXT, 'w' )
      for ip in all_hosts:
        host = str(ip) + head
        file.write(str(host))
      file.close()
      print ("ok")
    elif typefile == "2":
      head = "\n"
      file = open(name_fileXLS, 'w' )
      for ip in all_hosts:
        host = str(ip) + head
        file.write(str(host))
      file.close()
      print ("ok")
    else:
      typefile
  elif question_file == "no":
    print ("file not printed!")
  else:
    print ("Not a valid answer, restart!")

# remove file if size is equal to 0
  removeXLS(name_fileXLS)
  removeTXT(name_fileTXT)

  print ("\n")
  print ("end")
  print ("\n")



# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
