#no clue if this works:

import sys
import os
import hashlib

#setting up the hashing function


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



  
