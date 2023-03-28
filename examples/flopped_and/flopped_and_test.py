#!/usr/bin/env python3

from os.path import dirname
from random import randint
from rvm import RVMAgent, RVMTransaction, RVMMonitor, RVMDatabase
from sys import exit

class TotallyRandomTransaction(RVMTransaction):
    def randomize(self):
        randbits = lambda n : randint(0, (1 << n) - 1)
        self.trans = {k:randbits(self.widths[k]) for k in self.inputs}
        yield # DO NOT REMOVE

class FloppedAndMonitor(RVMMonitor):
    def body(self):
        self.pre_body() # DO NOT REMOVE
        print(f'A = {self.input_trans.trans["A"]}, B = {self.input_trans.trans["B"]}, C = {self.snoop("C")}')
        assert self.snoop("C") == (self.input_trans.trans["A"] and self.input_trans.trans["B"])
        self.toggle_trans_done()
        yield # DO NOT REMOVE

def main():
    dut = RVMDatabase.build(f'{dirname(__file__)}/flopped_and.v')
    agent = RVMAgent(dut, mon_class=[FloppedAndMonitor], itrans_class=TotallyRandomTransaction)
    if not dut.mainloop():
        print("Test passed!")
    else:
        print("Test timeout!")
    exit(0)

if __name__ == "__main__":
    main()
