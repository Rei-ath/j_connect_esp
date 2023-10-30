from machine import Pin, PWM
import time

class Motor:
    def __init__(self, pin_a, pin_b, enable_pin):
        self.pin_a = Pin(pin_a, Pin.OUT)
        self.pin_b = Pin(pin_b, Pin.OUT)
        self.enable_pin = Pin(enable_pin)
        self.pwm = self.__set_pwm__()
        self.pwm_percentage = 0
        self.direction = 0
        self.OFF = 0
        self.FORWARD_DIRECTION = 1
        self.BACKWARD_DIRECTION = 2
        # self.rotation = 90
    
    # PWM METHODS START
    def __set_pwm__(self):
        pwm = PWM(Pin(self.enable_pin))
        return pwm
    
    def set_pwm_init(self, freq, duty_u16=None, duty_cycle=None, duty_ns=None):
        if (duty_u16 is not None) and (duty_cycle is not None):
            raise ValueError("Enter either duty_u16 or duty_cycle, not both.")

        if duty_u16 is not None:
            self.pwm.init(freq=freq, duty_u16=duty_u16)
        elif duty_cycle is not None:
            # Scale the float duty_cycle to fit within the range of 0 to 1023
            # scaled_duty = int(duty_cycle * 1023)
            self.pwm.init(freq=freq, duty=duty_cycle)
        elif duty_ns is not None:
            self.pwm.init(freq=freq, duty_ns=duty_ns)
        else:
            raise ValueError("Specify either duty_u16 or duty_cycle.")
            
    def set_pwm_duty_u16(self,duty_u16):
        self.pwm.duty_u16(duty_u16)
        return self.pwm.duty_u16()

    def set_pwm_frequency(self, freq):
        self.pwm.freq(freq)

    def set_pwm_duty_cycle(self, duty_cycle):
        self.pwm.duty(duty_cycle)
        return self.pwm.duty()

    
    def set_pwm_duty_ns(self,duty_ns):
        self.pwm.duty_ns(duty_ns)
        return self.pwm.duty_ns()

    def set_speed_in_percentage(self,percentage):
        if percentage > 100 or percentage <= 0:
            raise ValueError("""
percentage must more than 0 and less than 100 or equal to 100

***if percentage u want to set is 0 use self.stop() instead*** 
""")
        _percentage = 100 // percentage
        # print('_percentage',_percentage)
        # print('2**16//_percentage',2**16//_percentage-1)
        self.pwm.duty_u16(2**16//_percentage - 1)
        self.pwm_percentage = percentage
        return self.pwm_percentage
        
    def get_pwm_values(self,name):
        if name is None or name == 'all' or name == 'none':
            values = {
                'percentage': self.pwm_percentage,
                'duty_cycle': self.pwm.duty(),
                'duty_u16': self.pwm.duty_u16(),
                'freq': self.pwm.freq(),
                'duty_ns' : self.pwm.duty_ns()
            }
            return values
        if name == 'percentage':
            return self.pwm_percentage
        elif name == 'duty_cycle':
            return self.pwm.duty()
        elif name == 'duty_u16':
            return self.pwm.duty_u16()
        elif name == 'freq':
            return self.pwm.freq()
        elif name == 'duty_ns':
            return self.pwm.duty_ns()
        else:
            raise ValueError("give percentage or duty_cycle or duty_u16 or freq or all or none")
    
    # PWM METHODS END   


    # MOTOR NETHODS START
    def move_forward(self):
        print("Moving Forward")
        self.pin_a.off()
        self.pin_b.on()
        self.direction = 1
        return self.direction
    
    def move_backward(self):
        print("Moving Backwards")
        self.pin_a.on()
        self.pin_b.off()
        self.direction = 2
        return self.direction

    def stop(self):
        print("Motor stopped")
        self.pin_a.off()
        self.pin_b.off()
        self.direction = 0
        return self.direction

    def bothon(self):
        self.pin_a.on()
        self.pin_b.on()
        self.direction = -1
        return self.direction
    
    #  MOTOR METHODS END