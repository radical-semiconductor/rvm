#!/usr/bin/env python3

from os.path import dirname
from random import randint
from rvm import RVMAgent, RVMDriver, RVMMonitor, RVMDatabase
from sys import exit

# Transactionless flow: Best used for direct bit-banging where
# no abstraction is required.

# Driver can be used without transaction
class ShiftRegisterDriver(RVMDriver):
    def body(self):
        self.pre_body() # DO NOT REMOVE
        self.drive("inp", randint(0,1))
        self.toggle_trans_done() # DO NOT REMOVE
        yield # DO NOT REMOVE

# Monitor can be used without input or output transactions.
class ShiftRegisterMonitor(RVMMonitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reg = [0, 0, 0]
    def body(self):
        self.pre_body() # DO NOT REMOVE
        self.reg[2] = self.reg[1]
        self.reg[1] = self.reg[0]
        self.reg[0] = self.snoop("inp")
        if self.reg[2] != self.snoop("outp"):
            print("Test failed!")
            exit(1)
        print(self.reg)
        self.toggle_trans_done() # DO NOT REMOVE
        yield # DO NOT REMOVE

def main():
    dut = RVMDatabase.build(f'{dirname(__file__)}/shift_register.v')
    agent = RVMAgent(dut, mon_class=[ShiftRegisterMonitor], drv_class=[ShiftRegisterDriver])
    if not dut.mainloop():
        print("Test passed!")
        exit(0)
    else:
        print("Test timeout!")
        exit(1)

if __name__ == "__main__":
    main()
