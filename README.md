# rpy2c
Raspberry Pi pYthon i2c Library

I'm writing libraries to interface with a variety of i2c peripherals.

My goal is to make it easy (like Arduino level easy) to interface with these parts as well as exposing enough commands to allow for complex and wonderful interactions that I had never thought of before.

So far I've mostly done DS1624 and partly done DS1621.

```
import time
from rpy2c.sensor import ds1624

sensor = ds1624.DS1624(0x48, 1)
sensor.start()

time.sleep(.1)
print "1624: %02.02fC" % sensor.get_temp()
print "1624: %02.02fF" % sensor.get_temp_f()
```