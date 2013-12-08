#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time, sys


class easydriver(object):
    def __init__(self,pin_step=0,delay=0.1,pin_direction=0,pin_ms1=0,pin_ms2=0,pin_ms3=0,pin_sleep=0,pin_enable=0,pin_reset=0,name="Stepper"):
        self.pin_step = pin_step
        self.delay = delay / 2
        self.pin_direction = pin_direction
        self.pin_microstep_1 = pin_ms1
        self.pin_microstep_2 = pin_ms2
        self.pin_microstep_3 = pin_ms3
        self.pin_sleep = pin_sleep
        self.pin_enable = pin_enable
        self.pin_reset = pin_reset
        self.name = name

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        if self.pin_step > 0:
            gpio.setup(self.pin_step, gpio.OUT)
        if self.pin_direction > 0:
            gpio.setup(self.pin_direction, gpio.OUT)
            gpio.output(self.pin_direction, True)
        if self.pin_microstep_1 > 0:
            gpio.setup(self.pin_microstep_1, gpio.OUT)
            gpio.output(self.pin_microstep_1, False)
        if self.pin_microstep_2 > 0:
            gpio.setup(self.pin_microstep_2, gpio.OUT)
            gpio.output(self.pin_microstep_2, False)
        if self.pin_microstep_3 > 0:
            gpio.setup(self.pin_microstep_3, gpio.OUT)
            gpio.output(self.pin_microstep_3, False)
        if self.pin_sleep > 0:
            gpio.setup(self.pin_sleep, gpio.OUT)
            gpio.output(self.pin_sleep,True)
        if self.pin_enable > 0:
            gpio.setup(self.pin_enable, gpio.OUT)
            gpio.output(self.pin_enable,False)
        if self.pin_reset > 0:
            gpio.setup(self.pin_reset, gpio.OUT)
            gpio.output(self.pin_reset,True)


    def step(self):
        gpio.output(self.pin_step,True)
        time.sleep(self.delay)
        gpio.output(self.pin_step,False)
        time.sleep(self.delay)

    def set_direction(self,direction):
        gpio.output(self.pin_direction,direction)

    def set_full_step(self):
        gpio.output(self.pin_microstep_1,False)
        gpio.output(self.pin_microstep_2,False)
        gpio.output(self.pin_microstep_3,False)
        
    def set_half_step(self):
        gpio.output(self.pin_microstep_1,True)
        gpio.output(self.pin_microstep_2,False)
        gpio.output(self.pin_microstep_3,False)
        
    def set_quarter_step(self):
        gpio.output(self.pin_microstep_1,False)
        gpio.output(self.pin_microstep_2,True)
        gpio.output(self.pin_microstep_3,False)
        
    def set_eighth_step(self):
        gpio.output(self.pin_microstep_1,True)
        gpio.output(self.pin_microstep_2,True)
        gpio.output(self.pin_microstep_3,False)

    def set_sixteenth_step(self):
        gpio.output(self.pin_microstep_1,True)
        gpio.output(self.pin_microstep_2,True)
        gpio.output(self.pin_microstep_3,True)

    def sleep(self):
        gpio.output(self.pin_sleep,False)

    def wake(self):
        gpio.output(self.pin_sleep,True)
    
    def disable(self):
        gpio.output(self.pin_enable,True)

    def enable(self):
        gpio.output(self.pin_enable,False)

    def reset(self):
        gpio.output(self.pin_reset,False)
        time.sleep(1)
        gpio.output(self.pin_reset,True)

    def set_delay(self, delay):
        self.delay = delay / 2

    def finish(self):
        gpio.cleanup()
