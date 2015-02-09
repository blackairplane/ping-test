import os, datetime, time

# Ping google.com as a test
def checkIP():
  # Take a breather
  time.sleep(10)
  
  statusUpdate(1)
  tempFile = 'test.temp'
  ip = '74.125.21.101'
  os.system("ping -t5 " + ip + " > " + tempFile)

  statusUpdate(2)
  # Check for network failures
  failed = 0
  f = open (tempFile, 'r')
  for line in f:
    if "Request timeout" in line:
      failed += 1

  statusUpdate(3)
  # Clear out our temp file 
  os.system("rm " + tempFile)

  # Append to our failure list if necessary
  if failed > 0:
    with open('failures.temp', 'a') as file:
      input = str(datetime.datetime.now()) + " - resolve error\n\r"
      file.write(input)

  statusUpdate(4)

def statusUpdate(count):
  os.system("clear")

  if count < 4:
    message = 'Testing connection'
    os.system("echo " + message + ': ' + ('#'*count))
  else:
    os.system("echo Test completed. Waiting...") 

# Init the process
os.system("clear")
os.system("echo Test will begin in 30s")
i = 0
while (i == 0):
  checkIP()
