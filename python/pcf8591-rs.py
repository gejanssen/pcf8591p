# http://www.rs-online.com/designspark/designshare/files/545a5b630700a.pdf
import smbus 
import time
i2cbus = smbus.SMBus(1)
i2cbus.write_byte(0x48,0)
print("Press Ctrl+C to exit")
while True:
  measurement = i2cbus.read_byte(0x48)
  print(measurement)
  time.sleep(1)
