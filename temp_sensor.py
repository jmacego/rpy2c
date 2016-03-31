import time
from rpy2c.sensor import ds1624
from rpy2c.sensor import ds1621

sensor = ds1624.DS1624(0x48, 1)
sensor2 = ds1621.DS1621(0x4C, 1)
sensor.start()
sensor2.start()

time.sleep(.1)
# print bin(sensor.__read_sensor())
print "1621: %02.02fC" % sensor2.get_temp()
print "1624: %02.02fC" % sensor.get_temp()
print "1621: %02.02fF" % sensor2.get_temp_f()
print "1624: %02.02fF" % sensor.get_temp_f()