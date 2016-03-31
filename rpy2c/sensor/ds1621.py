import smbus

class DS1621:
    'Does some stuff'
    

    # Some constants
    DS1621_READ_TEMP = 0xAA
    DS1621_READ_COUNTER = 0xA8
    DS1621_READ_SLOPE = 0xA9
    DS1621_START = 0xEE 
    DS1621_STOP = 0x22
    DS1621_THERMOSTAT_HIGH = 0xA1
    DS1621_THERMOSTAT_LOW = 0xA2
    DS1621_CONFIG = 0xAC

    def __init__(self, address, bus):
        self.address = address
        self.bus = smbus.SMBus(bus)
        
        
    def start(self):
        self.bus.write_byte(self.address, self.DS1624_START)

    def get_config(self):
        return self.bus.read_byte_data(self.address, self.DS1624_CONFIG)

    def oneshot_on(self):
        config = self.__get_config()
        config = config | 0b00000001
        self.bus.write_byte_data(self.address, self.DS1624_CONFIG, config)
        
    def oneshot_off(self):
        config = self.__get_config()
        config = config & 0b11111110
        self.bus.write_byte_data(self.address, self.DS1624_CONFIG, config)
        
    def is_done(self):
        config = self.__get_config()
        return config & 0b10000000
    
    def __read_sensor(self):
        return self.bus.read_word_data(self.address, self.DS1624_READ_TEMP)

    def __convert_temp(self, raw):
        # DS1621 is big endian, pi is little endian. DS1621 only uses first bit of second byte
        temp_integer = raw & 0x00FF
        if temp_integer > 127:
            temp_integer = temp_integer - 256    
        if raw & 0xFF00:
            temp_integer += 0.5
        return temp_integer
    
    def convert_c_f(self, temp_c):
        temp_f = temp_c * 9 / 5 + 32
        return temp_f
    
    def get_temp(self):
        raw = self.__read_sensor()
        return self.__convert_temp(raw)
    
    def get_temp_f(self):
        temp_c = self.get_temp()
        return self.convert_c_f(temp_c)