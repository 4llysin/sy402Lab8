import sys
import os
import hashlib

#things to ignore: 
ignoreList = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]


#if
#open csv for reading
#split csv by commas
#close csv

#if file exists, open for read, close
#if it doesnt, open and write

#OS.WALK??? if any files in ignored dict, continue, 
#else: file gets date and time and gets hashed


#set up hash function
# BUF_SIZE is totally arbitrary, change for your app!
BUFFER_SIZE = 65536  # lets read stuff in 64kb chunks!

for filename in os.listdir(directory):
  sha256 = hashlib.sha256()
  with open(filename, 'rb') as file:
      while True:
          data = file.read(BUFFER_SIZE)
          if not data:
              break
          sha256.update(data)

  print("SHA256: {0}".format(sha256.hexdigest()))


#compare hashes
#print statement if difference is found


  
