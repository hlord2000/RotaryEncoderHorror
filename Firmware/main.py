# The MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT

# example for MicroPython rotary encoder

import sys
if sys.platform == 'esp8266' or sys.platform == 'esp32':
    from rotary_irq_esp import RotaryIRQ
elif sys.platform == 'pyboard':
    from rotary_irq_pyb import RotaryIRQ
elif sys.platform == 'rp2':
    from rotary_irq_rp2 import RotaryIRQ
else:
    print('Warning:  The Rotary module has not been tested on this platform')

import time

encoder_pin_dict = [(28,29),(27,26),(6,7),(22,20),(4,5),(9,8)]

rotary_list = []
for x in range(len(encoder_pin_dict)):
    rotary_list.append(    
        RotaryIRQ(pin_num_clk=encoder_pin_dict[x][0],
                  pin_num_dt=encoder_pin_dict[x][1],
                  min_val=0,
                  max_val=24,
                  reverse=False,
                  range_mode=RotaryIRQ.RANGE_UNBOUNDED,
                  pull_up=True,
                  half_step=True)
    )
last_value = [0 for x in range(6)]

while True:
    for x in range(6):
        current_val = rotary_list[x].value()
        if current_val > last_value[x]:
            print(x,0)
        elif current_val < last_value[x]:
            print(x,1)
        last_value[x] = current_val
