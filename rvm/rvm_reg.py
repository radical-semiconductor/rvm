#!/usr/bin/env python3.10

# Rebranding of pyuvm's s18_register_model.py
# "Good artists copy; great artists steal." - Pablo Picasso

class RVMRegBlock:
    def __init__(self):
        self._regs = []
    def get_registers(self):
        return self._regs
    def _add_register(self, reg):
        self._regs.append(reg)

class RVMRegMap:
    def __init__(self, base_addr):
        self._parent = None
        self._base_addr = base_addr
        self._regs = {}
    def configure(self, parent, base_addr):
        self._parent = parent
        self._base_addr = base_addr
    def get_parent(self):
        return self._parent
    def get_base_addr(self):
        return self._base_addr
    def add_reg(self, reg, offset):
        self._regs[offset] = reg
    def get_registers(self):
        return list(self._regs.values())
    def get_reg_by_offset(self, offset):
        return self._regs[offset]

class RVMReg:
    def __init__(self, addr):
        self._parent = None
        self._fields = []
        self._addr = addr
    def configure(self, parent):
        self._parent = parent
        parent._add_register(self)
    def get_parent(self):
        return self._parent
    def get_addr(self):
        return self._addr
    def get_fields(self):
        return self._fields
    def _add_field(self, field):
        self._fields.append(field)

class RVMRegField:
    def __init__(self):
        self._parent = None
        self._size = None
        self._lsb_pos = None
        self._access = None
        self._is_volatile = None
        self._reset = None
    def configure(self, parent, size, lsb_pos, access, is_volatile, reset):
        self._parent = parent
        parent._add_field(self)
        self._size = size
        self._lsb_pos = lsb_pos
        self._access = access
        self._is_volatile = is_volatile
        self._reset = reset
    def get_parent(self):
        return self._parent
    def get_lsb_pos(self):
        return self._lsb_pos
    def get_n_bits(self):
        return self._size
    def get_access(self):
        return self._access
    def is_volatile(self):
        return self._is_volatile
    def get_reset(self):
        return self._reset
    def get_name(self):
        return self.name
