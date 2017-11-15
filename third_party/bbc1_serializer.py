import struct, binascii, copy
from ctypes import *

class List_c_uint8(Structure):
    pass

def __init__(self, _libc):
    self.libc = _libc

def get_c_uint8_value(self):
    return self.value

def get_c_uint8_next(self):
    return self.next

def get_c_uint8_next_parameter(self):
    return self.next[0]

def set_c_uint8_value(self, _value):
    self.value = _value

def set_c_uint8_next(self, _next):
    self.next = _next

def get_packet_c_uint8_value(self):
    packet = bytearray()
    packet.extend(self.value.to_bytes(sizeof(c_uint8), 'big'))
    return bytes(packet)

def get_packet_list_c_uint8(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_c_uint8_value())
    return packet

def get_c_uint8_length(self):
    length = 0
    length = length + sizeof(c_uint8)
    return length

def get_length_c_uint8_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_c_uint8_length()
    return length

List_c_uint8._fields_ = [('value', c_uint8),('next', POINTER(List_c_uint8))]
List_c_uint8.__init__ = __init__
List_c_uint8.get_c_uint8_value = get_c_uint8_value
List_c_uint8.get_c_uint8_next = get_c_uint8_next
List_c_uint8.get_c_uint8_next_parameter = get_c_uint8_next_parameter
List_c_uint8.set_c_uint8_value = set_c_uint8_value
List_c_uint8.set_c_uint8_next = set_c_uint8_next
List_c_uint8.get_packet_c_uint8_value = get_packet_c_uint8_value
List_c_uint8.get_packet_list_c_uint8 = get_packet_list_c_uint8
List_c_uint8.get_c_uint8_length = get_c_uint8_length
List_c_uint8.get_length_list_c_uint8 = get_length_c_uint8_list

class List_c_uint16(Structure):
    pass

def __init__(self, _libc):
    self.libc = _libc

def get_c_uint16_value(self):
    return self.value

def get_c_uint16_next(self):
    return self.next

def get_c_uint16_next_parameter(self):
    return self.next[0]

def set_c_uint16_value(self, _value):
    self.value = _value

def set_c_uint16_next(self, _next):
    self.next = _next

def get_packet_c_uint16_value(self):
    packet = bytearray()
    packet.extend(self.value.to_bytes(sizeof(c_uint16), 'big'))
    return bytes(packet)

def get_packet_list_c_uint16(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_c_uint16_value())
    return packet

def get_c_uint16_length(self):
    length = 0
    length = length + sizeof(c_uint16)
    return length

def get_length_c_uint16_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_c_uint16_length()
    return length

List_c_uint16._fields_ = [('value', c_uint16),('next', POINTER(List_c_uint16))]
List_c_uint16.__init__ = __init__
List_c_uint16.get_c_uint16_value = get_c_uint16_value
List_c_uint16.get_c_uint16_next = get_c_uint16_next
List_c_uint16.get_c_uint16_next_parameter = get_c_uint16_next_parameter
List_c_uint16.set_c_uint16_value = set_c_uint16_value
List_c_uint16.set_c_uint16_next = set_c_uint16_next
List_c_uint16.get_packet_c_uint16_value = get_packet_c_uint16_value
List_c_uint16.get_packet_list_c_uint16 = get_packet_list_c_uint16
List_c_uint16.get_c_uint16_length = get_c_uint16_length
List_c_uint16.get_length_list_c_uint16 = get_length_c_uint16_list

class List_c_uint32(Structure):
    pass

def __init__(self, _libc):
    self.libc = _libc

def get_c_uint32_value(self):
    return self.value

def get_c_uint32_next(self):
    return self.next

def get_c_uint32_next_parameter(self):
    return self.next[0]

def set_c_uint32_value(self, _value):
    self.value = _value

def set_c_uint32_next(self, _next):
    self.next = _next

def get_packet_c_uint32_value(self):
    packet = bytearray()
    packet.extend(self.value.to_bytes(sizeof(c_uint32), 'big'))
    return bytes(packet)

def get_packet_list_c_uint32(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_c_uint32_value())
    return packet

def get_c_uint32_length(self):
    length = 0
    length = length + sizeof(c_uint32)
    return length

def get_length_c_uint32_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_c_uint32_length()
    return length

List_c_uint32._fields_ = [('value', c_uint32),('next', POINTER(List_c_uint32))]
List_c_uint32.__init__ = __init__
List_c_uint32.get_c_uint32_value = get_c_uint32_value
List_c_uint32.get_c_uint32_next = get_c_uint32_next
List_c_uint32.get_c_uint32_next_parameter = get_c_uint32_next_parameter
List_c_uint32.set_c_uint32_value = set_c_uint32_value
List_c_uint32.set_c_uint32_next = set_c_uint32_next
List_c_uint32.get_packet_c_uint32_value = get_packet_c_uint32_value
List_c_uint32.get_packet_list_c_uint32 = get_packet_list_c_uint32
List_c_uint32.get_c_uint32_length = get_c_uint32_length
List_c_uint32.get_length_list_c_uint32 = get_length_c_uint32_list

class List_c_uint64(Structure):
    pass

def __init__(self, _libc):
    self.libc = _libc

def get_c_uint64_value(self):
    return self.value

def get_c_uint64_next(self):
    return self.next

def get_c_uint64_next_parameter(self):
    return self.next[0]

def set_c_uint64_value(self, _value):
    self.value = _value

def set_c_uint64_next(self, _next):
    self.next = _next

def get_packet_c_uint64_value(self):
    packet = bytearray()
    packet.extend(self.value.to_bytes(sizeof(c_uint64), 'big'))
    return bytes(packet)

def get_packet_list_c_uint64(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_c_uint64_value())
    return packet

def get_c_uint64_length(self):
    length = 0
    length = length + sizeof(c_uint64)
    return length

def get_length_c_uint64_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_c_uint64_length()
    return length

List_c_uint64._fields_ = [('value', c_uint64),('next', POINTER(List_c_uint64))]
List_c_uint64.__init__ = __init__
List_c_uint64.get_c_uint64_value = get_c_uint64_value
List_c_uint64.get_c_uint64_next = get_c_uint64_next
List_c_uint64.get_c_uint64_next_parameter = get_c_uint64_next_parameter
List_c_uint64.set_c_uint64_value = set_c_uint64_value
List_c_uint64.set_c_uint64_next = set_c_uint64_next
List_c_uint64.get_packet_c_uint64_value = get_packet_c_uint64_value
List_c_uint64.get_packet_list_c_uint64 = get_packet_list_c_uint64
List_c_uint64.get_c_uint64_length = get_c_uint64_length
List_c_uint64.get_length_list_c_uint64 = get_length_c_uint64_list

class Length_Value(Structure):
    _fields_ = [
        ('len', c_uint32),
        ('value', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.len = 0x00
        self.len = 0x00
        self.value = c_void_p()

    def inited(self):
        self.len = 0x00
        self.len = 0x00
        self.value = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.len.to_bytes(4,'big'))
        if self.len != 0:
            packet.extend(cast(self.value, POINTER(c_char))[:self.len])
        return bytes(packet)

    def get_length(self):
        return sizeof(c_uint32) + self.len

    def print_Length_Value(self):
        print('len ',self.len)
        if self.len > 0:
            print('value ',cast(self.value, POINTER(c_char))[:self.len])

    def set_len(self, _len):
        self.len = _len

    def set_value(self, _value):
        self.value = cast(_value, c_void_p)

    def set_value_using_index(self, index, _value):
        self.value[index] = _value

    def get_len(self):
        return self.len

    def get_value(self):
        return cast(self.value,POINTER(c_char))[:self.len]

    def free_value_of_Length_Value(self):
        self.libc.free_value_of_Length_Value(self.value)


class List_Length_Value(Structure):
    pass

List_Length_Value._fields_ = [('len', c_uint32),('value', c_void_p),('next', POINTER(List_Length_Value))]

def __init__(self, _libc):
    self.libc = _libc

List_Length_Value.__init__ = __init__

def get_Length_Value_len(self):
    return self.len

List_Length_Value.get_Length_Value_len = get_Length_Value_len

def get_Length_Value_value(self):
    return cast(self.value, POINTER(c_char))[:self.len]

List_Length_Value.get_Length_Value_value = get_Length_Value_value

def get_Length_Value_next(self):
    return self.next

List_Length_Value.get_Length_Value_next = get_Length_Value_next

def get_Length_Value_next_parameter(self):
    return self.next[0]

List_Length_Value.get_Length_Value_next_parameter = get_Length_Value_next_parameter

def set_Length_Value_len(self, _len):
    self.len = _len

List_Length_Value.set_Length_Value_len = set_Length_Value_len

def set_Length_Value_value(self, _value):
    self.value = cast(_value, c_void_p)

List_Length_Value.set_Length_Value_value = set_Length_Value_value

def set_Length_Value_next(self, _next):
    self.next = _next

List_Length_Value.set_Length_Value_next = set_Length_Value_next

def get_packet_Length_Value_value(self):
    packet = bytearray()
    packet.extend(self.len.to_bytes(4,'big'))
    packet.extend(cast(self.value, POINTER(c_char))[:self.len])
    return packet

List_Length_Value.get_packet_Length_Value_value = get_packet_Length_Value_value

def get_packet_list_Length_Value(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Length_Value_value())
    return packet

List_Length_Value.get_packet_list_Length_Value = get_packet_list_Length_Value

def get_Length_Value_length(self):
    length = 0
    length = length + sizeof(c_uint32)
    if self.len > 0:
        length = length + self.len
    return length


List_Length_Value.get_Length_Value_length = get_Length_Value_length

def get_length_Length_Value_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Length_Value_length()
    return length

List_Length_Value.get_length_Length_Value_list = get_length_Length_Value_list

def print_Length_Value(self):
    print('len ',self.len)
    if self.len > 0:
        print('value ',cast(self.value, POINTER(c_char))[:self.len])

List_Length_Value.print_Length_Value = print_Length_Value

def print_list_Length_Value(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Length_Value()
    return

List_Length_Value.print_list_Length_Value = print_list_Length_Value


class u_int256_t(Structure):
    _fields_ = [
        ('len', c_uint16),
        ('value', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.len = 0x00
        self.len = 0x00
        self.value = c_void_p()

    def inited(self):
        self.len = 0x00
        self.len = 0x00
        self.value = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.len.to_bytes(2,'big'))
        if self.len != 0:
            packet.extend(cast(self.value, POINTER(c_char))[:self.len])
        return bytes(packet)

    def get_length(self):
        return sizeof(c_uint16) + self.len

    def print_u_int256_t(self):
        print('len ',self.len)
        if self.len > 0:
            print('value ',cast(self.value, POINTER(c_char))[:self.len])

    def set_len(self, _len):
        self.len = _len

    def set_value(self, _value):
        self.value = cast(_value, c_void_p)

    def set_value_using_index(self, index, _value):
        self.value[index] = _value

    def get_len(self):
        return self.len

    def get_value(self):
        return cast(self.value,POINTER(c_char))[:self.len]

    def free_value_of_u_int256_t(self):
        self.libc.free_value_of_u_int256_t(self.value)


class List_u_int256_t(Structure):
    pass

List_u_int256_t._fields_ = [('len', c_uint16),('value', c_void_p),('next', POINTER(List_u_int256_t))]

def __init__(self, _libc):
    self.libc = _libc

List_u_int256_t.__init__ = __init__

def get_u_int256_t_len(self):
    return self.len

List_u_int256_t.get_u_int256_t_len = get_u_int256_t_len

def get_u_int256_t_value(self):
    return cast(self.value, POINTER(c_char))[:self.len]

List_u_int256_t.get_u_int256_t_value = get_u_int256_t_value

def get_u_int256_t_next(self):
    return self.next

List_u_int256_t.get_u_int256_t_next = get_u_int256_t_next

def get_u_int256_t_next_parameter(self):
    return self.next[0]

List_u_int256_t.get_u_int256_t_next_parameter = get_u_int256_t_next_parameter

def set_u_int256_t_len(self, _len):
    self.len = _len

List_u_int256_t.set_u_int256_t_len = set_u_int256_t_len

def set_u_int256_t_value(self, _value):
    self.value = cast(_value, c_void_p)

List_u_int256_t.set_u_int256_t_value = set_u_int256_t_value

def set_u_int256_t_next(self, _next):
    self.next = _next

List_u_int256_t.set_u_int256_t_next = set_u_int256_t_next

def get_packet_u_int256_t_value(self):
    packet = bytearray()
    packet.extend(self.len.to_bytes(2,'big'))
    packet.extend(cast(self.value, POINTER(c_char))[:self.len])
    return packet

List_u_int256_t.get_packet_u_int256_t_value = get_packet_u_int256_t_value

def get_packet_list_u_int256_t(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_u_int256_t_value())
    return packet

List_u_int256_t.get_packet_list_u_int256_t = get_packet_list_u_int256_t

def get_u_int256_t_length(self):
    length = 0
    length = length + sizeof(c_uint16)
    if self.len > 0:
        length = length + self.len
    return length


List_u_int256_t.get_u_int256_t_length = get_u_int256_t_length

def get_length_u_int256_t_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_u_int256_t_length()
    return length

List_u_int256_t.get_length_u_int256_t_list = get_length_u_int256_t_list

def print_u_int256_t(self):
    print('len ',self.len)
    if self.len > 0:
        print('value ',cast(self.value, POINTER(c_char))[:self.len])

List_u_int256_t.print_u_int256_t = print_u_int256_t

def print_list_u_int256_t(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_u_int256_t()
    return

List_u_int256_t.print_list_u_int256_t = print_list_u_int256_t


class Cross_Ref(Structure):
    _fields_ = [
        ('asset_group_id', u_int256_t),
        ('transaction_id', u_int256_t)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.asset_group_id = u_int256_t(self.libc)
        self.transaction_id = u_int256_t(self.libc)

    def inited(self):
        self.asset_group_id.inited()
        self.transaction_id.inited()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.asset_group_id.get_packet())
        packet.extend(self.transaction_id.get_packet())
        return bytes(packet)

    def get_length(self):
        return self.asset_group_id.get_length() + self.transaction_id.get_length()

    def print_Cross_Ref(self):
        self.asset_group_id.print_u_int256_t()
        self.transaction_id.print_u_int256_t()

    def set_asset_group_id(self, _asset_group_id):
        self.asset_group_id = _asset_group_id

    def set_transaction_id(self, _transaction_id):
        self.transaction_id = _transaction_id

    def get_asset_group_id(self):
        return self.asset_group_id

    def get_transaction_id(self):
        return self.transaction_id


class List_Cross_Ref(Structure):
    pass

List_Cross_Ref._fields_ = [('asset_group_id', u_int256_t),('transaction_id', u_int256_t),('next', POINTER(List_Cross_Ref))]

def __init__(self, _libc):
    self.libc = _libc

List_Cross_Ref.__init__ = __init__

def get_Cross_Ref_asset_group_id(self):
    return self.asset_group_id

List_Cross_Ref.get_Cross_Ref_asset_group_id = get_Cross_Ref_asset_group_id

def get_Cross_Ref_transaction_id(self):
    return self.transaction_id

List_Cross_Ref.get_Cross_Ref_transaction_id = get_Cross_Ref_transaction_id

def get_Cross_Ref_next(self):
    return self.next

List_Cross_Ref.get_Cross_Ref_next = get_Cross_Ref_next

def get_Cross_Ref_next_parameter(self):
    return self.next[0]

List_Cross_Ref.get_Cross_Ref_next_parameter = get_Cross_Ref_next_parameter

def set_Cross_Ref_asset_group_id(self, _asset_group_id):
    self.asset_group_id = _asset_group_id

List_Cross_Ref.set_Cross_Ref_asset_group_id = set_Cross_Ref_asset_group_id

def set_Cross_Ref_transaction_id(self, _transaction_id):
    self.transaction_id = _transaction_id

List_Cross_Ref.set_Cross_Ref_transaction_id = set_Cross_Ref_transaction_id

def set_Cross_Ref_next(self, _next):
    self.next = _next

List_Cross_Ref.set_Cross_Ref_next = set_Cross_Ref_next

def get_packet_Cross_Ref_value(self):
    packet = bytearray()
    packet.extend(self.asset_group_id.get_packet())
    packet.extend(self.transaction_id.get_packet())
    return packet

List_Cross_Ref.get_packet_Cross_Ref_value = get_packet_Cross_Ref_value

def get_packet_list_Cross_Ref(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Cross_Ref_value())
    return packet

List_Cross_Ref.get_packet_list_Cross_Ref = get_packet_list_Cross_Ref

def get_Cross_Ref_length(self):
    length = 0
    length = length + self.asset_group_id.get_length()
    length = length + self.transaction_id.get_length()
    return length


List_Cross_Ref.get_Cross_Ref_length = get_Cross_Ref_length

def get_length_Cross_Ref_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Cross_Ref_length()
    return length

List_Cross_Ref.get_length_Cross_Ref_list = get_length_Cross_Ref_list

def print_Cross_Ref(self):
    self.asset_group_id.print_u_int256_t()
    self.transaction_id.print_u_int256_t()

List_Cross_Ref.print_Cross_Ref = print_Cross_Ref

def print_list_Cross_Ref(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Cross_Ref()
    return

List_Cross_Ref.print_list_Cross_Ref = print_list_Cross_Ref


class Asset_Base(Structure):
    _fields_ = [
        ('asset_id', u_int256_t),
        ('user_id', u_int256_t),
        ('nonce_length', c_uint16),
        ('nonce', c_void_p),
        ('asset_file_size', c_uint32),
        ('asset_file_digest', u_int256_t),
        ('body_size', c_uint16),
        ('body', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.asset_id = u_int256_t(self.libc)
        self.user_id = u_int256_t(self.libc)
        self.nonce_length = 0x00
        self.nonce_length = 0x00
        self.nonce = c_void_p()
        self.asset_file_size = 0x00
        self.asset_file_digest = u_int256_t(self.libc)
        self.body_size = 0x00
        self.body_size = 0x00
        self.body = c_void_p()

    def inited(self):
        self.asset_id.inited()
        self.user_id.inited()
        self.nonce_length = 0x00
        self.nonce_length = 0x00
        self.nonce = c_void_p()
        self.asset_file_size = 0x00
        self.asset_file_digest.inited()
        self.body_size = 0x00
        self.body_size = 0x00
        self.body = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.asset_id.get_packet())
        packet.extend(self.user_id.get_packet())
        packet.extend(self.nonce_length.to_bytes(2,'big'))
        if self.nonce_length != 0:
            packet.extend(cast(self.nonce, POINTER(c_char))[:self.nonce_length])
        packet.extend(self.asset_file_size.to_bytes(4,'big'))
        packet.extend(self.asset_file_digest.get_packet())
        packet.extend(self.body_size.to_bytes(2,'big'))
        if self.body_size != 0:
            packet.extend(cast(self.body, POINTER(c_char))[:self.body_size])
        return bytes(packet)

    def get_length(self):
        return self.asset_id.get_length() + self.user_id.get_length() + sizeof(c_uint16) + self.nonce_length + sizeof(c_uint32) + self.asset_file_digest.get_length() + sizeof(c_uint16) + self.body_size

    def print_Asset_Base(self):
        self.asset_id.print_u_int256_t()
        self.user_id.print_u_int256_t()
        print('nonce_length ',self.nonce_length)
        if self.nonce_length > 0:
            print('nonce ',cast(self.nonce, POINTER(c_char))[:self.nonce_length])
        print('asset_file_size ',self.asset_file_size)
        self.asset_file_digest.print_u_int256_t()
        print('body_size ',self.body_size)
        if self.body_size > 0:
            print('body ',cast(self.body, POINTER(c_char))[:self.body_size])

    def set_asset_id(self, _asset_id):
        self.asset_id = _asset_id

    def set_user_id(self, _user_id):
        self.user_id = _user_id

    def set_nonce_length(self, _nonce_length):
        self.nonce_length = _nonce_length

    def set_nonce(self, _nonce):
        self.nonce = cast(_nonce, c_void_p)

    def set_nonce_using_index(self, index, _nonce):
        self.nonce[index] = _nonce

    def set_asset_file_size(self, _asset_file_size):
        self.asset_file_size = _asset_file_size

    def set_asset_file_digest(self, _asset_file_digest):
        self.asset_file_digest = _asset_file_digest

    def set_body_size(self, _body_size):
        self.body_size = _body_size

    def set_body(self, _body):
        self.body = cast(_body, c_void_p)

    def set_body_using_index(self, index, _body):
        self.body[index] = _body

    def get_asset_id(self):
        return self.asset_id

    def get_user_id(self):
        return self.user_id

    def get_nonce_length(self):
        return self.nonce_length

    def get_nonce(self):
        return cast(self.nonce,POINTER(c_char))[:self.nonce_length]

    def get_asset_file_size(self):
        return self.asset_file_size

    def get_asset_file_digest(self):
        return self.asset_file_digest

    def get_body_size(self):
        return self.body_size

    def get_body(self):
        return cast(self.body,POINTER(c_char))[:self.body_size]

    def free_nonce_of_Asset_Base(self):
        self.libc.free_nonce_of_Asset_Base(self.nonce)

    def free_body_of_Asset_Base(self):
        self.libc.free_body_of_Asset_Base(self.body)


class List_Asset_Base(Structure):
    pass

List_Asset_Base._fields_ = [('asset_id', u_int256_t),('user_id', u_int256_t),('nonce_length', c_uint16),('nonce', c_void_p),('asset_file_size', c_uint32),('asset_file_digest', u_int256_t),('body_size', c_uint16),('body', c_void_p),('next', POINTER(List_Asset_Base))]

def __init__(self, _libc):
    self.libc = _libc

List_Asset_Base.__init__ = __init__

def get_Asset_Base_asset_id(self):
    return self.asset_id

List_Asset_Base.get_Asset_Base_asset_id = get_Asset_Base_asset_id

def get_Asset_Base_user_id(self):
    return self.user_id

List_Asset_Base.get_Asset_Base_user_id = get_Asset_Base_user_id

def get_Asset_Base_nonce_length(self):
    return self.nonce_length

List_Asset_Base.get_Asset_Base_nonce_length = get_Asset_Base_nonce_length

def get_Asset_Base_nonce(self):
    return cast(self.nonce, POINTER(c_char))[:self.nonce_length]

List_Asset_Base.get_Asset_Base_nonce = get_Asset_Base_nonce

def get_Asset_Base_asset_file_size(self):
    return self.asset_file_size

List_Asset_Base.get_Asset_Base_asset_file_size = get_Asset_Base_asset_file_size

def get_Asset_Base_asset_file_digest(self):
    return self.asset_file_digest

List_Asset_Base.get_Asset_Base_asset_file_digest = get_Asset_Base_asset_file_digest

def get_Asset_Base_body_size(self):
    return self.body_size

List_Asset_Base.get_Asset_Base_body_size = get_Asset_Base_body_size

def get_Asset_Base_body(self):
    return cast(self.body, POINTER(c_char))[:self.body_size]

List_Asset_Base.get_Asset_Base_body = get_Asset_Base_body

def get_Asset_Base_next(self):
    return self.next

List_Asset_Base.get_Asset_Base_next = get_Asset_Base_next

def get_Asset_Base_next_parameter(self):
    return self.next[0]

List_Asset_Base.get_Asset_Base_next_parameter = get_Asset_Base_next_parameter

def set_Asset_Base_asset_id(self, _asset_id):
    self.asset_id = _asset_id

List_Asset_Base.set_Asset_Base_asset_id = set_Asset_Base_asset_id

def set_Asset_Base_user_id(self, _user_id):
    self.user_id = _user_id

List_Asset_Base.set_Asset_Base_user_id = set_Asset_Base_user_id

def set_Asset_Base_nonce_length(self, _nonce_length):
    self.nonce_length = _nonce_length

List_Asset_Base.set_Asset_Base_nonce_length = set_Asset_Base_nonce_length

def set_Asset_Base_nonce(self, _nonce):
    self.nonce = cast(_nonce, c_void_p)

List_Asset_Base.set_Asset_Base_nonce = set_Asset_Base_nonce

def set_Asset_Base_asset_file_size(self, _asset_file_size):
    self.asset_file_size = _asset_file_size

List_Asset_Base.set_Asset_Base_asset_file_size = set_Asset_Base_asset_file_size

def set_Asset_Base_asset_file_digest(self, _asset_file_digest):
    self.asset_file_digest = _asset_file_digest

List_Asset_Base.set_Asset_Base_asset_file_digest = set_Asset_Base_asset_file_digest

def set_Asset_Base_body_size(self, _body_size):
    self.body_size = _body_size

List_Asset_Base.set_Asset_Base_body_size = set_Asset_Base_body_size

def set_Asset_Base_body(self, _body):
    self.body = cast(_body, c_void_p)

List_Asset_Base.set_Asset_Base_body = set_Asset_Base_body

def set_Asset_Base_next(self, _next):
    self.next = _next

List_Asset_Base.set_Asset_Base_next = set_Asset_Base_next

def get_packet_Asset_Base_value(self):
    packet = bytearray()
    packet.extend(self.asset_id.get_packet())
    packet.extend(self.user_id.get_packet())
    packet.extend(self.nonce_length.to_bytes(2,'big'))
    packet.extend(cast(self.nonce, POINTER(c_char))[:self.nonce_length])
    packet.extend(self.asset_file_size.to_bytes(4,'big'))
    packet.extend(self.asset_file_digest.get_packet())
    packet.extend(self.body_size.to_bytes(2,'big'))
    packet.extend(cast(self.body, POINTER(c_char))[:self.body_size])
    return packet

List_Asset_Base.get_packet_Asset_Base_value = get_packet_Asset_Base_value

def get_packet_list_Asset_Base(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Asset_Base_value())
    return packet

List_Asset_Base.get_packet_list_Asset_Base = get_packet_list_Asset_Base

def get_Asset_Base_length(self):
    length = 0
    length = length + self.asset_id.get_length()
    length = length + self.user_id.get_length()
    length = length + sizeof(c_uint16)
    if self.nonce_length > 0:
        length = length + self.nonce_length
    length = length + sizeof(c_uint32)
    length = length + self.asset_file_digest.get_length()
    length = length + sizeof(c_uint16)
    if self.body_size > 0:
        length = length + self.body_size
    return length


List_Asset_Base.get_Asset_Base_length = get_Asset_Base_length

def get_length_Asset_Base_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Asset_Base_length()
    return length

List_Asset_Base.get_length_Asset_Base_list = get_length_Asset_Base_list

def print_Asset_Base(self):
    self.asset_id.print_u_int256_t()
    self.user_id.print_u_int256_t()
    print('nonce_length ',self.nonce_length)
    if self.nonce_length > 0:
        print('nonce ',cast(self.nonce, POINTER(c_char))[:self.nonce_length])
    print('asset_file_size ',self.asset_file_size)
    self.asset_file_digest.print_u_int256_t()
    print('body_size ',self.body_size)
    if self.body_size > 0:
        print('body ',cast(self.body, POINTER(c_char))[:self.body_size])

List_Asset_Base.print_Asset_Base = print_Asset_Base

def print_list_Asset_Base(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Asset_Base()
    return

List_Asset_Base.print_list_Asset_Base = print_list_Asset_Base


class Asset(Structure):
    _fields_ = [
        ('asset_id', u_int256_t),
        ('user_id', u_int256_t),
        ('nonce_length', c_uint16),
        ('nonce', c_void_p),
        ('asset_file_size', c_uint32),
        ('asset_file_digest', u_int256_t),
        ('body_size', c_uint16),
        ('body', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.asset_id = u_int256_t(self.libc)
        self.user_id = u_int256_t(self.libc)
        self.nonce_length = 0x00
        self.nonce_length = 0x00
        self.nonce = c_void_p()
        self.asset_file_size = 0x00
        self.asset_file_digest = u_int256_t(self.libc)
        self.body_size = 0x00
        self.body_size = 0x00
        self.body = c_void_p()

    def inited(self):
        self.asset_id.inited()
        self.user_id.inited()
        self.nonce_length = 0x00
        self.nonce_length = 0x00
        self.nonce = c_void_p()
        self.asset_file_size = 0x00
        self.asset_file_digest.inited()
        self.body_size = 0x00
        self.body_size = 0x00
        self.body = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.asset_id.get_packet())
        packet.extend(self.user_id.get_packet())
        packet.extend(self.nonce_length.to_bytes(2,'big'))
        if self.nonce_length != 0:
            packet.extend(cast(self.nonce, POINTER(c_char))[:self.nonce_length])
        packet.extend(self.asset_file_size.to_bytes(4,'big'))
        packet.extend(self.asset_file_digest.get_packet())
        packet.extend(self.body_size.to_bytes(2,'big'))
        if self.body_size != 0:
            packet.extend(cast(self.body, POINTER(c_char))[:self.body_size])
        return bytes(packet)

    def get_length(self):
        return self.asset_id.get_length() + self.user_id.get_length() + sizeof(c_uint16) + self.nonce_length + sizeof(c_uint32) + self.asset_file_digest.get_length() + sizeof(c_uint16) + self.body_size

    def print_Asset(self):
        self.asset_id.print_u_int256_t()
        self.user_id.print_u_int256_t()
        print('nonce_length ',self.nonce_length)
        if self.nonce_length > 0:
            print('nonce ',cast(self.nonce, POINTER(c_char))[:self.nonce_length])
        print('asset_file_size ',self.asset_file_size)
        self.asset_file_digest.print_u_int256_t()
        print('body_size ',self.body_size)
        if self.body_size > 0:
            print('body ',cast(self.body, POINTER(c_char))[:self.body_size])

    def set_asset_id(self, _asset_id):
        self.asset_id = _asset_id

    def set_user_id(self, _user_id):
        self.user_id = _user_id

    def set_nonce_length(self, _nonce_length):
        self.nonce_length = _nonce_length

    def set_nonce(self, _nonce):
        self.nonce = cast(_nonce, c_void_p)

    def set_nonce_using_index(self, index, _nonce):
        self.nonce[index] = _nonce

    def set_asset_file_size(self, _asset_file_size):
        self.asset_file_size = _asset_file_size

    def set_asset_file_digest(self, _asset_file_digest):
        self.asset_file_digest = _asset_file_digest

    def set_body_size(self, _body_size):
        self.body_size = _body_size

    def set_body(self, _body):
        self.body = cast(_body, c_void_p)

    def set_body_using_index(self, index, _body):
        self.body[index] = _body

    def get_asset_id(self):
        return self.asset_id

    def get_user_id(self):
        return self.user_id

    def get_nonce_length(self):
        return self.nonce_length

    def get_nonce(self):
        return cast(self.nonce,POINTER(c_char))[:self.nonce_length]

    def get_asset_file_size(self):
        return self.asset_file_size

    def get_asset_file_digest(self):
        return self.asset_file_digest

    def get_body_size(self):
        return self.body_size

    def get_body(self):
        return cast(self.body,POINTER(c_char))[:self.body_size]

    def free_nonce_of_Asset(self):
        self.libc.free_nonce_of_Asset(self.nonce)

    def free_body_of_Asset(self):
        self.libc.free_body_of_Asset(self.body)


class List_Asset(Structure):
    pass

List_Asset._fields_ = [('asset_id', u_int256_t),('user_id', u_int256_t),('nonce_length', c_uint16),('nonce', c_void_p),('asset_file_size', c_uint32),('asset_file_digest', u_int256_t),('body_size', c_uint16),('body', c_void_p),('next', POINTER(List_Asset))]

def __init__(self, _libc):
    self.libc = _libc

List_Asset.__init__ = __init__

def get_Asset_asset_id(self):
    return self.asset_id

List_Asset.get_Asset_asset_id = get_Asset_asset_id

def get_Asset_user_id(self):
    return self.user_id

List_Asset.get_Asset_user_id = get_Asset_user_id

def get_Asset_nonce_length(self):
    return self.nonce_length

List_Asset.get_Asset_nonce_length = get_Asset_nonce_length

def get_Asset_nonce(self):
    return cast(self.nonce, POINTER(c_char))[:self.nonce_length]

List_Asset.get_Asset_nonce = get_Asset_nonce

def get_Asset_asset_file_size(self):
    return self.asset_file_size

List_Asset.get_Asset_asset_file_size = get_Asset_asset_file_size

def get_Asset_asset_file_digest(self):
    return self.asset_file_digest

List_Asset.get_Asset_asset_file_digest = get_Asset_asset_file_digest

def get_Asset_body_size(self):
    return self.body_size

List_Asset.get_Asset_body_size = get_Asset_body_size

def get_Asset_body(self):
    return cast(self.body, POINTER(c_char))[:self.body_size]

List_Asset.get_Asset_body = get_Asset_body

def get_Asset_next(self):
    return self.next

List_Asset.get_Asset_next = get_Asset_next

def get_Asset_next_parameter(self):
    return self.next[0]

List_Asset.get_Asset_next_parameter = get_Asset_next_parameter

def set_Asset_asset_id(self, _asset_id):
    self.asset_id = _asset_id

List_Asset.set_Asset_asset_id = set_Asset_asset_id

def set_Asset_user_id(self, _user_id):
    self.user_id = _user_id

List_Asset.set_Asset_user_id = set_Asset_user_id

def set_Asset_nonce_length(self, _nonce_length):
    self.nonce_length = _nonce_length

List_Asset.set_Asset_nonce_length = set_Asset_nonce_length

def set_Asset_nonce(self, _nonce):
    self.nonce = cast(_nonce, c_void_p)

List_Asset.set_Asset_nonce = set_Asset_nonce

def set_Asset_asset_file_size(self, _asset_file_size):
    self.asset_file_size = _asset_file_size

List_Asset.set_Asset_asset_file_size = set_Asset_asset_file_size

def set_Asset_asset_file_digest(self, _asset_file_digest):
    self.asset_file_digest = _asset_file_digest

List_Asset.set_Asset_asset_file_digest = set_Asset_asset_file_digest

def set_Asset_body_size(self, _body_size):
    self.body_size = _body_size

List_Asset.set_Asset_body_size = set_Asset_body_size

def set_Asset_body(self, _body):
    self.body = cast(_body, c_void_p)

List_Asset.set_Asset_body = set_Asset_body

def set_Asset_next(self, _next):
    self.next = _next

List_Asset.set_Asset_next = set_Asset_next

def get_packet_Asset_value(self):
    packet = bytearray()
    packet.extend(self.asset_id.get_packet())
    packet.extend(self.user_id.get_packet())
    packet.extend(self.nonce_length.to_bytes(2,'big'))
    packet.extend(cast(self.nonce, POINTER(c_char))[:self.nonce_length])
    packet.extend(self.asset_file_size.to_bytes(4,'big'))
    packet.extend(self.asset_file_digest.get_packet())
    packet.extend(self.body_size.to_bytes(2,'big'))
    packet.extend(cast(self.body, POINTER(c_char))[:self.body_size])
    return packet

List_Asset.get_packet_Asset_value = get_packet_Asset_value

def get_packet_list_Asset(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Asset_value())
    return packet

List_Asset.get_packet_list_Asset = get_packet_list_Asset

def get_Asset_length(self):
    length = 0
    length = length + self.asset_id.get_length()
    length = length + self.user_id.get_length()
    length = length + sizeof(c_uint16)
    if self.nonce_length > 0:
        length = length + self.nonce_length
    length = length + sizeof(c_uint32)
    length = length + self.asset_file_digest.get_length()
    length = length + sizeof(c_uint16)
    if self.body_size > 0:
        length = length + self.body_size
    return length


List_Asset.get_Asset_length = get_Asset_length

def get_length_Asset_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Asset_length()
    return length

List_Asset.get_length_Asset_list = get_length_Asset_list

def print_Asset(self):
    self.asset_id.print_u_int256_t()
    self.user_id.print_u_int256_t()
    print('nonce_length ',self.nonce_length)
    if self.nonce_length > 0:
        print('nonce ',cast(self.nonce, POINTER(c_char))[:self.nonce_length])
    print('asset_file_size ',self.asset_file_size)
    self.asset_file_digest.print_u_int256_t()
    print('body_size ',self.body_size)
    if self.body_size > 0:
        print('body ',cast(self.body, POINTER(c_char))[:self.body_size])

List_Asset.print_Asset = print_Asset

def print_list_Asset(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Asset()
    return

List_Asset.print_list_Asset = print_list_Asset


class Reference(Structure):
    _fields_ = [
        ('asset_group_id', u_int256_t),
        ('transaction_id', u_int256_t),
        ('event_index', c_uint16),
        ('signature_indice_num', c_uint16),
        ('signature_indices', POINTER(List_c_uint16))
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.asset_group_id = u_int256_t(self.libc)
        self.transaction_id = u_int256_t(self.libc)
        self.event_index = 0x00
        self.signature_indice_num = 0x00
        self.signature_indices = pointer(List_c_uint16(self.libc))

    def inited(self):
        self.asset_group_id.inited()
        self.transaction_id.inited()
        self.event_index = 0x00
        self.signature_indice_num = 0x00
        self.signature_indices = pointer(List_c_uint16(self.libc))

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.asset_group_id.get_packet())
        packet.extend(self.transaction_id.get_packet())
        packet.extend(self.event_index.to_bytes(2,'big'))
        packet.extend(self.signature_indice_num.to_bytes(2,'big'))
        packet.extend(self.signature_indices[0].get_packet_list_c_uint16(self.signature_indice_num))
        return bytes(packet)

    def get_length(self):
        return self.asset_group_id.get_length() + self.transaction_id.get_length() + sizeof(c_uint16) + sizeof(c_uint16) + self.signature_indices[0].get_length_list_c_uint16(self.signature_indice_num)

    def print_Reference(self):
        self.asset_group_id.print_u_int256_t()
        self.transaction_id.print_u_int256_t()
        print('event_index ',self.event_index)
        print('signature_indice_num ',self.signature_indice_num)
        if self.signature_indice_num > 0:
            current = self.signature_indices[0]
            for i in range(self.signature_indice_num):
                current = current.next[0]
                print('signature_indices ', current.value)

    def set_asset_group_id(self, _asset_group_id):
        self.asset_group_id = _asset_group_id

    def set_transaction_id(self, _transaction_id):
        self.transaction_id = _transaction_id

    def set_event_index(self, _event_index):
        self.event_index = _event_index

    def set_signature_indice_num(self, _signature_indice_num):
        self.signature_indice_num = _signature_indice_num

    def set_signature_indices(self, _signature_indices):
        self.signature_indices = _signature_indices

    def add_to_signature_indices_list (self, _signature_indices):
        current = self.signature_indices[0]

        if self.signature_indice_num < 1:
            self.signature_indice_num = self.signature_indice_num + 1
            current.next = pointer(_signature_indices)
            return

        for i in range(self.signature_indice_num):
            current = current.next[0]
            if self.signature_indice_num - 1 == i:
                self.signature_indice_num = self.signature_indice_num + 1
                current.next = pointer(_signature_indices)
                return

    def get_asset_group_id(self):
        return self.asset_group_id

    def get_transaction_id(self):
        return self.transaction_id

    def get_event_index(self):
        return self.event_index

    def get_signature_indice_num(self):
        return self.signature_indice_num

    def get_signature_indices_list_using_index (self, _index):
        current = self.signature_indices[0].next[0]

        if self.signature_indice_num < 1 or self.signature_indice_num < _index or _index <= 0:
            return current

        for i in range(self.signature_indice_num):
            current = current.next[0]
            if _index - 1 == i:
                return current


class List_Reference(Structure):
    pass

List_Reference._fields_ = [('asset_group_id', u_int256_t),('transaction_id', u_int256_t),('event_index', c_uint16),('signature_indice_num', c_uint16),('signature_indices', POINTER(List_c_uint16)),('next', POINTER(List_Reference))]

def __init__(self, _libc):
    self.libc = _libc

List_Reference.__init__ = __init__

def get_Reference_asset_group_id(self):
    return self.asset_group_id

List_Reference.get_Reference_asset_group_id = get_Reference_asset_group_id

def get_Reference_transaction_id(self):
    return self.transaction_id

List_Reference.get_Reference_transaction_id = get_Reference_transaction_id

def get_Reference_event_index(self):
    return self.event_index

List_Reference.get_Reference_event_index = get_Reference_event_index

def get_Reference_signature_indice_num(self):
    return self.signature_indice_num

List_Reference.get_Reference_signature_indice_num = get_Reference_signature_indice_num

def get_Reference_signature_indices(self):
    return self.signature_indices

List_Reference.get_Reference_signature_indices = get_Reference_signature_indices

def get_Reference_next(self):
    return self.next

List_Reference.get_Reference_next = get_Reference_next

def get_Reference_next_parameter(self):
    return self.next[0]

List_Reference.get_Reference_next_parameter = get_Reference_next_parameter

def set_Reference_asset_group_id(self, _asset_group_id):
    self.asset_group_id = _asset_group_id

List_Reference.set_Reference_asset_group_id = set_Reference_asset_group_id

def set_Reference_transaction_id(self, _transaction_id):
    self.transaction_id = _transaction_id

List_Reference.set_Reference_transaction_id = set_Reference_transaction_id

def set_Reference_event_index(self, _event_index):
    self.event_index = _event_index

List_Reference.set_Reference_event_index = set_Reference_event_index

def set_Reference_signature_indice_num(self, _signature_indice_num):
    self.signature_indice_num = _signature_indice_num

List_Reference.set_Reference_signature_indice_num = set_Reference_signature_indice_num

def set_Reference_signature_indices(self, _signature_indices):
    self.signature_indices = _signature_indices

List_Reference.set_Reference_signature_indices = set_Reference_signature_indices

def set_Reference_next(self, _next):
    self.next = _next

List_Reference.set_Reference_next = set_Reference_next

def get_packet_Reference_value(self):
    packet = bytearray()
    packet.extend(self.asset_group_id.get_packet())
    packet.extend(self.transaction_id.get_packet())
    packet.extend(self.event_index.to_bytes(2,'big'))
    packet.extend(self.signature_indice_num.to_bytes(2,'big'))
    packet.extend(self.signature_indices[0].get_packet_list_c_uint16(self.signature_indice_num))
    return packet

List_Reference.get_packet_Reference_value = get_packet_Reference_value

def get_packet_list_Reference(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Reference_value())
    return packet

List_Reference.get_packet_list_Reference = get_packet_list_Reference

def get_Reference_length(self):
    length = 0
    length = length + self.asset_group_id.get_length()
    length = length + self.transaction_id.get_length()
    length = length + sizeof(c_uint16)
    length = length + sizeof(c_uint16)
    if self.signature_indice_num > 0:
        length = length + self.signature_indices[0].get_packet_list_c_uint16(self.signature_indice_num)
    return length


List_Reference.get_Reference_length = get_Reference_length

def get_length_Reference_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Reference_length()
    return length

List_Reference.get_length_Reference_list = get_length_Reference_list

def print_Reference(self):
    self.asset_group_id.print_u_int256_t()
    self.transaction_id.print_u_int256_t()
    print('event_index ',self.event_index)
    print('signature_indice_num ',self.signature_indice_num)
    if self.signature_indice_num > 0:
        current = self.signature_indices[0]
        for i in range(self.signature_indice_num):
            current = current.next[0]
        print('signature_indices ',current.value)

List_Reference.print_Reference = print_Reference

def print_list_Reference(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Reference()
    return

List_Reference.print_list_Reference = print_list_Reference


class Event(Structure):
    _fields_ = [
        ('asset_group_id', Length_Value),
        ('reference_num', c_uint16),
        ('reference_indices', POINTER(List_c_uint16)),
        ('mandatory_approver_num', c_uint16),
        ('mandatory_approvers', POINTER(List_Length_Value)),
        ('option_approval_numerator', c_uint16),
        ('option_approval_denominator', c_uint16),
        ('option_approvers', POINTER(List_Length_Value)),
        ('asset_length', c_uint32),
        ('asset', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.asset_group_id = Length_Value(self.libc)
        self.reference_num = 0x00
        self.reference_indices = pointer(List_c_uint16(self.libc))
        self.mandatory_approver_num = 0x00
        self.mandatory_approvers = pointer(List_Length_Value(self.libc))
        self.option_approval_numerator = 0x00
        self.option_approval_denominator = 0x00
        self.option_approvers = pointer(List_Length_Value(self.libc))
        self.asset_length = 0x00
        self.asset_length = 0x00
        self.asset = c_void_p()

    def inited(self):
        self.asset_group_id.inited()
        self.reference_num = 0x00
        self.reference_indices = pointer(List_c_uint16(self.libc))
        self.mandatory_approver_num = 0x00
        self.mandatory_approvers = pointer(List_Length_Value(self.libc))
        self.option_approval_numerator = 0x00
        self.option_approval_denominator = 0x00
        self.option_approvers = pointer(List_Length_Value(self.libc))
        self.asset_length = 0x00
        self.asset_length = 0x00
        self.asset = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.asset_group_id.get_packet())
        packet.extend(self.reference_num.to_bytes(2,'big'))
        packet.extend(self.reference_indices[0].get_packet_list_c_uint16(self.reference_num))
        packet.extend(self.mandatory_approver_num.to_bytes(2,'big'))
        packet.extend(self.mandatory_approvers[0].get_packet_list_Length_Value(self.mandatory_approver_num))
        packet.extend(self.option_approval_numerator.to_bytes(2,'big'))
        packet.extend(self.option_approval_denominator.to_bytes(2,'big'))
        packet.extend(self.option_approvers[0].get_packet_list_Length_Value(self.option_approval_denominator))
        packet.extend(self.asset_length.to_bytes(4,'big'))
        if self.asset_length != 0:
            packet.extend(cast(self.asset, POINTER(c_char))[:self.asset_length])
        return bytes(packet)

    def get_length(self):
        return self.asset_group_id.get_length() + sizeof(c_uint16) + self.reference_indices[0].get_length_list_c_uint16(self.reference_num) + sizeof(c_uint16) + self.mandatory_approvers[0].get_length_Length_Value_list(self.mandatory_approver_num) + sizeof(c_uint16) + sizeof(c_uint16) + self.option_approvers[0].get_length_Length_Value_list(self.option_approval_denominator) + sizeof(c_uint32) + self.asset_length

    def print_Event(self):
        self.asset_group_id.print_Length_Value()
        print('reference_num ',self.reference_num)
        if self.reference_num > 0:
            current = self.reference_indices[0]
            for i in range(self.reference_num):
                current = current.next[0]
                print('reference_indices ', current.value)
        print('mandatory_approver_num ',self.mandatory_approver_num)
        if self.mandatory_approver_num > 0:
            self.mandatory_approvers[0].print_list_Length_Value(self.mandatory_approver_num)
        print('option_approval_numerator ',self.option_approval_numerator)
        print('option_approval_denominator ',self.option_approval_denominator)
        if self.option_approval_denominator > 0:
            self.option_approvers[0].print_list_Length_Value(self.option_approval_denominator)
        print('asset_length ',self.asset_length)
        if self.asset_length > 0:
            print('asset ',cast(self.asset, POINTER(c_char))[:self.asset_length])

    def set_asset_group_id(self, _asset_group_id):
        self.asset_group_id = _asset_group_id

    def set_reference_num(self, _reference_num):
        self.reference_num = _reference_num

    def set_reference_indices(self, _reference_indices):
        self.reference_indices = _reference_indices

    def set_mandatory_approver_num(self, _mandatory_approver_num):
        self.mandatory_approver_num = _mandatory_approver_num

    def set_mandatory_approvers(self, _mandatory_approvers):
        self.mandatory_approvers = _mandatory_approvers

    def set_option_approval_numerator(self, _option_approval_numerator):
        self.option_approval_numerator = _option_approval_numerator

    def set_option_approval_denominator(self, _option_approval_denominator):
        self.option_approval_denominator = _option_approval_denominator

    def set_option_approvers(self, _option_approvers):
        self.option_approvers = _option_approvers

    def set_asset_length(self, _asset_length):
        self.asset_length = _asset_length

    def set_asset(self, _asset):
        self.asset = cast(_asset, c_void_p)

    def set_asset_using_index(self, index, _asset):
        self.asset[index] = _asset

    def add_to_reference_indices_list (self, _reference_indices):
        current = self.reference_indices[0]

        if self.reference_num < 1:
            self.reference_num = self.reference_num + 1
            current.next = pointer(_reference_indices)
            return

        for i in range(self.reference_num):
            current = current.next[0]
            if self.reference_num - 1 == i:
                self.reference_num = self.reference_num + 1
                current.next = pointer(_reference_indices)
                return

    def add_to_mandatory_approvers_list (self, _mandatory_approvers):
        current = self.mandatory_approvers[0]

        if self.mandatory_approver_num < 1:
            self.mandatory_approver_num = self.mandatory_approver_num + 1
            current.next = pointer(_mandatory_approvers)
            return

        for i in range(self.mandatory_approver_num):
            current = current.next[0]
            if self.mandatory_approver_num - 1 == i:
                self.mandatory_approver_num = self.mandatory_approver_num + 1
                current.next = pointer(_mandatory_approvers)
                return

    def add_to_option_approvers_list (self, _option_approvers):
        current = self.option_approvers[0]

        if self.option_approval_denominator < 1:
            self.option_approval_denominator = self.option_approval_denominator + 1
            current.next = pointer(_option_approvers)
            return

        for i in range(self.option_approval_denominator):
            current = current.next[0]
            if self.option_approval_denominator - 1 == i:
                self.option_approval_denominator = self.option_approval_denominator + 1
                current.next = pointer(_option_approvers)
                return

    def get_asset_group_id(self):
        return self.asset_group_id

    def get_reference_num(self):
        return self.reference_num

    def get_reference_indices_list_using_index (self, _index):
        current = self.reference_indices[0].next[0]

        if self.reference_num < 1 or self.reference_num < _index or _index <= 0:
            return current

        for i in range(self.reference_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_mandatory_approver_num(self):
        return self.mandatory_approver_num

    def get_mandatory_approvers_list_using_index (self, _index):
        current = self.mandatory_approvers[0].next[0]

        if self.mandatory_approver_num < 1 or self.mandatory_approver_num < _index or _index <= 0:
            return current

        for i in range(self.mandatory_approver_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_option_approval_numerator(self):
        return self.option_approval_numerator

    def get_option_approval_denominator(self):
        return self.option_approval_denominator

    def get_option_approvers_list_using_index (self, _index):
        current = self.option_approvers[0].next[0]

        if self.option_approval_denominator < 1 or self.option_approval_denominator < _index or _index <= 0:
            return current

        for i in range(self.option_approval_denominator):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_asset_length(self):
        return self.asset_length

    def get_asset(self):
        return cast(self.asset,POINTER(c_char))[:self.asset_length]

    def free_asset_of_Event(self):
        self.libc.free_asset_of_Event(self.asset)


class List_Event(Structure):
    pass

List_Event._fields_ = [('asset_group_id', Length_Value),('reference_num', c_uint16),('reference_indices', POINTER(List_c_uint16)),('mandatory_approver_num', c_uint16),('mandatory_approvers', POINTER(List_Length_Value)),('option_approval_numerator', c_uint16),('option_approval_denominator', c_uint16),('option_approvers', POINTER(List_Length_Value)),('asset_length', c_uint32),('asset', c_void_p),('next', POINTER(List_Event))]

def __init__(self, _libc):
    self.libc = _libc

List_Event.__init__ = __init__

def get_Event_asset_group_id(self):
    return self.asset_group_id

List_Event.get_Event_asset_group_id = get_Event_asset_group_id

def get_Event_reference_num(self):
    return self.reference_num

List_Event.get_Event_reference_num = get_Event_reference_num

def get_Event_reference_indices(self):
    return self.reference_indices

List_Event.get_Event_reference_indices = get_Event_reference_indices

def get_Event_mandatory_approver_num(self):
    return self.mandatory_approver_num

List_Event.get_Event_mandatory_approver_num = get_Event_mandatory_approver_num

def get_Event_mandatory_approvers(self):
    return self.mandatory_approvers

List_Event.get_Event_mandatory_approvers = get_Event_mandatory_approvers

def get_Event_option_approval_numerator(self):
    return self.option_approval_numerator

List_Event.get_Event_option_approval_numerator = get_Event_option_approval_numerator

def get_Event_option_approval_denominator(self):
    return self.option_approval_denominator

List_Event.get_Event_option_approval_denominator = get_Event_option_approval_denominator

def get_Event_option_approvers(self):
    return self.option_approvers

List_Event.get_Event_option_approvers = get_Event_option_approvers

def get_Event_asset_length(self):
    return self.asset_length

List_Event.get_Event_asset_length = get_Event_asset_length

def get_Event_asset(self):
    return cast(self.asset, POINTER(c_char))[:self.asset_length]

List_Event.get_Event_asset = get_Event_asset

def get_Event_next(self):
    return self.next

List_Event.get_Event_next = get_Event_next

def get_Event_next_parameter(self):
    return self.next[0]

List_Event.get_Event_next_parameter = get_Event_next_parameter

def set_Event_asset_group_id(self, _asset_group_id):
    self.asset_group_id = _asset_group_id

List_Event.set_Event_asset_group_id = set_Event_asset_group_id

def set_Event_reference_num(self, _reference_num):
    self.reference_num = _reference_num

List_Event.set_Event_reference_num = set_Event_reference_num

def set_Event_reference_indices(self, _reference_indices):
    self.reference_indices = _reference_indices

List_Event.set_Event_reference_indices = set_Event_reference_indices

def set_Event_mandatory_approver_num(self, _mandatory_approver_num):
    self.mandatory_approver_num = _mandatory_approver_num

List_Event.set_Event_mandatory_approver_num = set_Event_mandatory_approver_num

def set_Event_mandatory_approvers(self, _mandatory_approvers):
    self.mandatory_approvers = _mandatory_approvers

List_Event.set_Event_mandatory_approvers = set_Event_mandatory_approvers

def set_Event_option_approval_numerator(self, _option_approval_numerator):
    self.option_approval_numerator = _option_approval_numerator

List_Event.set_Event_option_approval_numerator = set_Event_option_approval_numerator

def set_Event_option_approval_denominator(self, _option_approval_denominator):
    self.option_approval_denominator = _option_approval_denominator

List_Event.set_Event_option_approval_denominator = set_Event_option_approval_denominator

def set_Event_option_approvers(self, _option_approvers):
    self.option_approvers = _option_approvers

List_Event.set_Event_option_approvers = set_Event_option_approvers

def set_Event_asset_length(self, _asset_length):
    self.asset_length = _asset_length

List_Event.set_Event_asset_length = set_Event_asset_length

def set_Event_asset(self, _asset):
    self.asset = cast(_asset, c_void_p)

List_Event.set_Event_asset = set_Event_asset

def set_Event_next(self, _next):
    self.next = _next

List_Event.set_Event_next = set_Event_next

def get_packet_Event_value(self):
    packet = bytearray()
    packet.extend(self.asset_group_id.get_packet())
    packet.extend(self.reference_num.to_bytes(2,'big'))
    packet.extend(self.reference_indices[0].get_packet_list_c_uint16(self.reference_num))
    packet.extend(self.mandatory_approver_num.to_bytes(2,'big'))
    packet.extend(self.mandatory_approvers.get_packet())
    packet.extend(self.option_approval_numerator.to_bytes(2,'big'))
    packet.extend(self.option_approval_denominator.to_bytes(2,'big'))
    packet.extend(self.option_approvers.get_packet())
    packet.extend(self.asset_length.to_bytes(4,'big'))
    packet.extend(cast(self.asset, POINTER(c_char))[:self.asset_length])
    return packet

List_Event.get_packet_Event_value = get_packet_Event_value

def get_packet_list_Event(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Event_value())
    return packet

List_Event.get_packet_list_Event = get_packet_list_Event

def get_Event_length(self):
    length = 0
    length = length + self.asset_group_id.get_length()
    length = length + sizeof(c_uint16)
    if self.reference_num > 0:
        length = length + self.reference_indices[0].get_packet_list_c_uint16(self.reference_num)
    length = length + sizeof(c_uint16)
    if self.mandatory_approver_num > 0:
        length = length + self.mandatory_approvers[0].get_packet_list_Length_Value(self.mandatory_approver_num)
    length = length + sizeof(c_uint16)
    length = length + sizeof(c_uint16)
    if self.option_approval_denominator > 0:
        length = length + self.option_approvers[0].get_packet_list_Length_Value(self.option_approval_denominator)
    length = length + sizeof(c_uint32)
    if self.asset_length > 0:
        length = length + self.asset_length
    return length


List_Event.get_Event_length = get_Event_length

def get_length_Event_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Event_length()
    return length

List_Event.get_length_Event_list = get_length_Event_list

def print_Event(self):
    self.asset_group_id.print_Length_Value()
    print('reference_num ',self.reference_num)
    if self.reference_num > 0:
        current = self.reference_indices[0]
        for i in range(self.reference_num):
            current = current.next[0]
        print('reference_indices ',current.value)
    print('mandatory_approver_num ',self.mandatory_approver_num)
    self.mandatory_approvers[0].print_list_Length_Value(self.mandatory_approver_num)
    print('option_approval_numerator ',self.option_approval_numerator)
    print('option_approval_denominator ',self.option_approval_denominator)
    self.option_approvers[0].print_list_Length_Value(self.option_approval_denominator)
    print('asset_length ',self.asset_length)
    if self.asset_length > 0:
        print('asset ',cast(self.asset, POINTER(c_char))[:self.asset_length])

List_Event.print_Event = print_Event

def print_list_Event(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Event()
    return

List_Event.print_list_Event = print_list_Event


class Signature(Structure):
    _fields_ = [
        ('type', c_uint32),
        ('public_key_length', c_uint32),
        ('public_key', c_void_p),
        ('signature_length', c_uint32),
        ('signature', c_void_p)
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.type = 0x00
        self.public_key_length = 0x00
        self.public_key_length = 0x00
        self.public_key = c_void_p()
        self.signature_length = 0x00
        self.signature_length = 0x00
        self.signature = c_void_p()

    def inited(self):
        self.type = 0x00
        self.public_key_length = 0x00
        self.public_key_length = 0x00
        self.public_key = c_void_p()
        self.signature_length = 0x00
        self.signature_length = 0x00
        self.signature = c_void_p()

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.type.to_bytes(4,'big'))
        packet.extend(self.public_key_length.to_bytes(4,'big'))
        if self.public_key_length != 0:
            packet.extend(cast(self.public_key, POINTER(c_char))[:self.public_key_length])
        packet.extend(self.signature_length.to_bytes(4,'big'))
        if self.signature_length != 0:
            packet.extend(cast(self.signature, POINTER(c_char))[:self.signature_length])
        return bytes(packet)

    def get_length(self):
        return sizeof(c_uint32) + sizeof(c_uint32) + self.public_key_length + sizeof(c_uint32) + self.signature_length

    def print_Signature(self):
        print('type ',self.type)
        print('public_key_length ',self.public_key_length)
        if self.public_key_length > 0:
            print('public_key ',cast(self.public_key, POINTER(c_char))[:self.public_key_length])
        print('signature_length ',self.signature_length)
        if self.signature_length > 0:
            print('signature ',cast(self.signature, POINTER(c_char))[:self.signature_length])

    def set_type(self, _type):
        self.type = _type

    def set_public_key_length(self, _public_key_length):
        self.public_key_length = _public_key_length

    def set_public_key(self, _public_key):
        self.public_key = cast(_public_key, c_void_p)

    def set_public_key_using_index(self, index, _public_key):
        self.public_key[index] = _public_key

    def set_signature_length(self, _signature_length):
        self.signature_length = _signature_length

    def set_signature(self, _signature):
        self.signature = cast(_signature, c_void_p)

    def set_signature_using_index(self, index, _signature):
        self.signature[index] = _signature

    def get_type(self):
        return self.type

    def get_public_key_length(self):
        return self.public_key_length

    def get_public_key(self):
        return cast(self.public_key,POINTER(c_char))[:self.public_key_length]

    def get_signature_length(self):
        return self.signature_length

    def get_signature(self):
        return cast(self.signature,POINTER(c_char))[:self.signature_length]

    def free_public_key_of_Signature(self):
        self.libc.free_public_key_of_Signature(self.public_key)

    def free_signature_of_Signature(self):
        self.libc.free_signature_of_Signature(self.signature)


class List_Signature(Structure):
    pass

List_Signature._fields_ = [('type', c_uint32),('public_key_length', c_uint32),('public_key', c_void_p),('signature_length', c_uint32),('signature', c_void_p),('next', POINTER(List_Signature))]

def __init__(self, _libc):
    self.libc = _libc

List_Signature.__init__ = __init__

def get_Signature_type(self):
    return self.type

List_Signature.get_Signature_type = get_Signature_type

def get_Signature_public_key_length(self):
    return self.public_key_length

List_Signature.get_Signature_public_key_length = get_Signature_public_key_length

def get_Signature_public_key(self):
    return cast(self.public_key, POINTER(c_char))[:self.public_key_length]

List_Signature.get_Signature_public_key = get_Signature_public_key

def get_Signature_signature_length(self):
    return self.signature_length

List_Signature.get_Signature_signature_length = get_Signature_signature_length

def get_Signature_signature(self):
    return cast(self.signature, POINTER(c_char))[:self.signature_length]

List_Signature.get_Signature_signature = get_Signature_signature

def get_Signature_next(self):
    return self.next

List_Signature.get_Signature_next = get_Signature_next

def get_Signature_next_parameter(self):
    return self.next[0]

List_Signature.get_Signature_next_parameter = get_Signature_next_parameter

def set_Signature_type(self, _type):
    self.type = _type

List_Signature.set_Signature_type = set_Signature_type

def set_Signature_public_key_length(self, _public_key_length):
    self.public_key_length = _public_key_length

List_Signature.set_Signature_public_key_length = set_Signature_public_key_length

def set_Signature_public_key(self, _public_key):
    self.public_key = cast(_public_key, c_void_p)

List_Signature.set_Signature_public_key = set_Signature_public_key

def set_Signature_signature_length(self, _signature_length):
    self.signature_length = _signature_length

List_Signature.set_Signature_signature_length = set_Signature_signature_length

def set_Signature_signature(self, _signature):
    self.signature = cast(_signature, c_void_p)

List_Signature.set_Signature_signature = set_Signature_signature

def set_Signature_next(self, _next):
    self.next = _next

List_Signature.set_Signature_next = set_Signature_next

def get_packet_Signature_value(self):
    packet = bytearray()
    packet.extend(self.type.to_bytes(4,'big'))
    packet.extend(self.public_key_length.to_bytes(4,'big'))
    packet.extend(cast(self.public_key, POINTER(c_char))[:self.public_key_length])
    packet.extend(self.signature_length.to_bytes(4,'big'))
    packet.extend(cast(self.signature, POINTER(c_char))[:self.signature_length])
    return packet

List_Signature.get_packet_Signature_value = get_packet_Signature_value

def get_packet_list_Signature(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Signature_value())
    return packet

List_Signature.get_packet_list_Signature = get_packet_list_Signature

def get_Signature_length(self):
    length = 0
    length = length + sizeof(c_uint32)
    length = length + sizeof(c_uint32)
    if self.public_key_length > 0:
        length = length + self.public_key_length
    length = length + sizeof(c_uint32)
    if self.signature_length > 0:
        length = length + self.signature_length
    return length


List_Signature.get_Signature_length = get_Signature_length

def get_length_Signature_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Signature_length()
    return length

List_Signature.get_length_Signature_list = get_length_Signature_list

def print_Signature(self):
    print('type ',self.type)
    print('public_key_length ',self.public_key_length)
    if self.public_key_length > 0:
        print('public_key ',cast(self.public_key, POINTER(c_char))[:self.public_key_length])
    print('signature_length ',self.signature_length)
    if self.signature_length > 0:
        print('signature ',cast(self.signature, POINTER(c_char))[:self.signature_length])

List_Signature.print_Signature = print_Signature

def print_list_Signature(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Signature()
    return

List_Signature.print_list_Signature = print_list_Signature


class Intermediate(Structure):
    _fields_ = [
        ('transaction_base_digest', u_int256_t),
        ('cross_ref_num', c_uint16),
        ('cross_refs', POINTER(List_Length_Value))
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.transaction_base_digest = u_int256_t(self.libc)
        self.cross_ref_num = 0x00
        self.cross_refs = pointer(List_Length_Value(self.libc))

    def inited(self):
        self.transaction_base_digest.inited()
        self.cross_ref_num = 0x00
        self.cross_refs = pointer(List_Length_Value(self.libc))

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.transaction_base_digest.get_packet())
        packet.extend(self.cross_ref_num.to_bytes(2,'big'))
        packet.extend(self.cross_refs[0].get_packet_list_Length_Value(self.cross_ref_num))
        return bytes(packet)

    def get_length(self):
        return self.transaction_base_digest.get_length() + sizeof(c_uint16) + self.cross_refs[0].get_length_Length_Value_list(self.cross_ref_num)

    def print_Intermediate(self):
        self.transaction_base_digest.print_u_int256_t()
        print('cross_ref_num ',self.cross_ref_num)
        if self.cross_ref_num > 0:
            self.cross_refs[0].print_list_Length_Value(self.cross_ref_num)

    def set_transaction_base_digest(self, _transaction_base_digest):
        self.transaction_base_digest = _transaction_base_digest

    def set_cross_ref_num(self, _cross_ref_num):
        self.cross_ref_num = _cross_ref_num

    def set_cross_refs(self, _cross_refs):
        self.cross_refs = _cross_refs

    def add_to_cross_refs_list (self, _cross_refs):
        current = self.cross_refs[0]

        if self.cross_ref_num < 1:
            self.cross_ref_num = self.cross_ref_num + 1
            current.next = pointer(_cross_refs)
            return

        for i in range(self.cross_ref_num):
            current = current.next[0]
            if self.cross_ref_num - 1 == i:
                self.cross_ref_num = self.cross_ref_num + 1
                current.next = pointer(_cross_refs)
                return

    def get_transaction_base_digest(self):
        return self.transaction_base_digest

    def get_cross_ref_num(self):
        return self.cross_ref_num

    def get_cross_refs_list_using_index (self, _index):
        current = self.cross_refs[0].next[0]

        if self.cross_ref_num < 1 or self.cross_ref_num < _index or _index <= 0:
            return current

        for i in range(self.cross_ref_num):
            current = current.next[0]
            if _index - 1 == i:
                return current


class List_Intermediate(Structure):
    pass

List_Intermediate._fields_ = [('transaction_base_digest', u_int256_t),('cross_ref_num', c_uint16),('cross_refs', POINTER(List_Length_Value)),('next', POINTER(List_Intermediate))]

def __init__(self, _libc):
    self.libc = _libc

List_Intermediate.__init__ = __init__

def get_Intermediate_transaction_base_digest(self):
    return self.transaction_base_digest

List_Intermediate.get_Intermediate_transaction_base_digest = get_Intermediate_transaction_base_digest

def get_Intermediate_cross_ref_num(self):
    return self.cross_ref_num

List_Intermediate.get_Intermediate_cross_ref_num = get_Intermediate_cross_ref_num

def get_Intermediate_cross_refs(self):
    return self.cross_refs

List_Intermediate.get_Intermediate_cross_refs = get_Intermediate_cross_refs

def get_Intermediate_next(self):
    return self.next

List_Intermediate.get_Intermediate_next = get_Intermediate_next

def get_Intermediate_next_parameter(self):
    return self.next[0]

List_Intermediate.get_Intermediate_next_parameter = get_Intermediate_next_parameter

def set_Intermediate_transaction_base_digest(self, _transaction_base_digest):
    self.transaction_base_digest = _transaction_base_digest

List_Intermediate.set_Intermediate_transaction_base_digest = set_Intermediate_transaction_base_digest

def set_Intermediate_cross_ref_num(self, _cross_ref_num):
    self.cross_ref_num = _cross_ref_num

List_Intermediate.set_Intermediate_cross_ref_num = set_Intermediate_cross_ref_num

def set_Intermediate_cross_refs(self, _cross_refs):
    self.cross_refs = _cross_refs

List_Intermediate.set_Intermediate_cross_refs = set_Intermediate_cross_refs

def set_Intermediate_next(self, _next):
    self.next = _next

List_Intermediate.set_Intermediate_next = set_Intermediate_next

def get_packet_Intermediate_value(self):
    packet = bytearray()
    packet.extend(self.transaction_base_digest.get_packet())
    packet.extend(self.cross_ref_num.to_bytes(2,'big'))
    packet.extend(self.cross_refs.get_packet())
    return packet

List_Intermediate.get_packet_Intermediate_value = get_packet_Intermediate_value

def get_packet_list_Intermediate(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Intermediate_value())
    return packet

List_Intermediate.get_packet_list_Intermediate = get_packet_list_Intermediate

def get_Intermediate_length(self):
    length = 0
    length = length + self.transaction_base_digest.get_length()
    length = length + sizeof(c_uint16)
    if self.cross_ref_num > 0:
        length = length + self.cross_refs[0].get_packet_list_Length_Value(self.cross_ref_num)
    return length


List_Intermediate.get_Intermediate_length = get_Intermediate_length

def get_length_Intermediate_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Intermediate_length()
    return length

List_Intermediate.get_length_Intermediate_list = get_length_Intermediate_list

def print_Intermediate(self):
    self.transaction_base_digest.print_u_int256_t()
    print('cross_ref_num ',self.cross_ref_num)
    self.cross_refs[0].print_list_Length_Value(self.cross_ref_num)

List_Intermediate.print_Intermediate = print_Intermediate

def print_list_Intermediate(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Intermediate()
    return

List_Intermediate.print_list_Intermediate = print_list_Intermediate


class Transaction_Base(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('timestamp', c_uint64),
        ('event_num', c_uint16),
        ('events', POINTER(List_Length_Value)),
        ('reference_num', c_uint16),
        ('references', POINTER(List_Length_Value))
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.version = 0x00
        self.timestamp = 0x00
        self.event_num = 0x00
        self.events = pointer(List_Length_Value(self.libc))
        self.reference_num = 0x00
        self.references = pointer(List_Length_Value(self.libc))

    def inited(self):
        self.version = 0x00
        self.timestamp = 0x00
        self.event_num = 0x00
        self.events = pointer(List_Length_Value(self.libc))
        self.reference_num = 0x00
        self.references = pointer(List_Length_Value(self.libc))

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.version.to_bytes(4,'big'))
        packet.extend(self.timestamp.to_bytes(8,'big'))
        packet.extend(self.event_num.to_bytes(2,'big'))
        packet.extend(self.events[0].get_packet_list_Length_Value(self.event_num))
        packet.extend(self.reference_num.to_bytes(2,'big'))
        packet.extend(self.references[0].get_packet_list_Length_Value(self.reference_num))
        return bytes(packet)

    def get_length(self):
        return sizeof(c_uint32) + sizeof(c_uint64) + sizeof(c_uint16) + self.events[0].get_length_Length_Value_list(self.event_num) + sizeof(c_uint16) + self.references[0].get_length_Length_Value_list(self.reference_num)

    def print_Transaction_Base(self):
        print('version ',self.version)
        print('timestamp ',self.timestamp)
        print('event_num ',self.event_num)
        if self.event_num > 0:
            self.events[0].print_list_Length_Value(self.event_num)
        print('reference_num ',self.reference_num)
        if self.reference_num > 0:
            self.references[0].print_list_Length_Value(self.reference_num)

    def set_version(self, _version):
        self.version = _version

    def set_timestamp(self, _timestamp):
        self.timestamp = _timestamp

    def set_event_num(self, _event_num):
        self.event_num = _event_num

    def set_events(self, _events):
        self.events = _events

    def set_reference_num(self, _reference_num):
        self.reference_num = _reference_num

    def set_references(self, _references):
        self.references = _references

    def add_to_events_list (self, _events):
        current = self.events[0]

        if self.event_num < 1:
            self.event_num = self.event_num + 1
            current.next = pointer(_events)
            return

        for i in range(self.event_num):
            current = current.next[0]
            if self.event_num - 1 == i:
                self.event_num = self.event_num + 1
                current.next = pointer(_events)
                return

    def add_to_references_list (self, _references):
        current = self.references[0]

        if self.reference_num < 1:
            self.reference_num = self.reference_num + 1
            current.next = pointer(_references)
            return

        for i in range(self.reference_num):
            current = current.next[0]
            if self.reference_num - 1 == i:
                self.reference_num = self.reference_num + 1
                current.next = pointer(_references)
                return

    def get_version(self):
        return self.version

    def get_timestamp(self):
        return self.timestamp

    def get_event_num(self):
        return self.event_num

    def get_events_list_using_index (self, _index):
        current = self.events[0].next[0]

        if self.event_num < 1 or self.event_num < _index or _index <= 0:
            return current

        for i in range(self.event_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_reference_num(self):
        return self.reference_num

    def get_references_list_using_index (self, _index):
        current = self.references[0].next[0]

        if self.reference_num < 1 or self.reference_num < _index or _index <= 0:
            return current

        for i in range(self.reference_num):
            current = current.next[0]
            if _index - 1 == i:
                return current


class List_Transaction_Base(Structure):
    pass

List_Transaction_Base._fields_ = [('version', c_uint32),('timestamp', c_uint64),('event_num', c_uint16),('events', POINTER(List_Length_Value)),('reference_num', c_uint16),('references', POINTER(List_Length_Value)),('next', POINTER(List_Transaction_Base))]

def __init__(self, _libc):
    self.libc = _libc

List_Transaction_Base.__init__ = __init__

def get_Transaction_Base_version(self):
    return self.version

List_Transaction_Base.get_Transaction_Base_version = get_Transaction_Base_version

def get_Transaction_Base_timestamp(self):
    return self.timestamp

List_Transaction_Base.get_Transaction_Base_timestamp = get_Transaction_Base_timestamp

def get_Transaction_Base_event_num(self):
    return self.event_num

List_Transaction_Base.get_Transaction_Base_event_num = get_Transaction_Base_event_num

def get_Transaction_Base_events(self):
    return self.events

List_Transaction_Base.get_Transaction_Base_events = get_Transaction_Base_events

def get_Transaction_Base_reference_num(self):
    return self.reference_num

List_Transaction_Base.get_Transaction_Base_reference_num = get_Transaction_Base_reference_num

def get_Transaction_Base_references(self):
    return self.references

List_Transaction_Base.get_Transaction_Base_references = get_Transaction_Base_references

def get_Transaction_Base_next(self):
    return self.next

List_Transaction_Base.get_Transaction_Base_next = get_Transaction_Base_next

def get_Transaction_Base_next_parameter(self):
    return self.next[0]

List_Transaction_Base.get_Transaction_Base_next_parameter = get_Transaction_Base_next_parameter

def set_Transaction_Base_version(self, _version):
    self.version = _version

List_Transaction_Base.set_Transaction_Base_version = set_Transaction_Base_version

def set_Transaction_Base_timestamp(self, _timestamp):
    self.timestamp = _timestamp

List_Transaction_Base.set_Transaction_Base_timestamp = set_Transaction_Base_timestamp

def set_Transaction_Base_event_num(self, _event_num):
    self.event_num = _event_num

List_Transaction_Base.set_Transaction_Base_event_num = set_Transaction_Base_event_num

def set_Transaction_Base_events(self, _events):
    self.events = _events

List_Transaction_Base.set_Transaction_Base_events = set_Transaction_Base_events

def set_Transaction_Base_reference_num(self, _reference_num):
    self.reference_num = _reference_num

List_Transaction_Base.set_Transaction_Base_reference_num = set_Transaction_Base_reference_num

def set_Transaction_Base_references(self, _references):
    self.references = _references

List_Transaction_Base.set_Transaction_Base_references = set_Transaction_Base_references

def set_Transaction_Base_next(self, _next):
    self.next = _next

List_Transaction_Base.set_Transaction_Base_next = set_Transaction_Base_next

def get_packet_Transaction_Base_value(self):
    packet = bytearray()
    packet.extend(self.version.to_bytes(4,'big'))
    packet.extend(self.timestamp.to_bytes(8,'big'))
    packet.extend(self.event_num.to_bytes(2,'big'))
    packet.extend(self.events.get_packet())
    packet.extend(self.reference_num.to_bytes(2,'big'))
    packet.extend(self.references.get_packet())
    return packet

List_Transaction_Base.get_packet_Transaction_Base_value = get_packet_Transaction_Base_value

def get_packet_list_Transaction_Base(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Transaction_Base_value())
    return packet

List_Transaction_Base.get_packet_list_Transaction_Base = get_packet_list_Transaction_Base

def get_Transaction_Base_length(self):
    length = 0
    length = length + sizeof(c_uint32)
    length = length + sizeof(c_uint64)
    length = length + sizeof(c_uint16)
    if self.event_num > 0:
        length = length + self.events[0].get_packet_list_Length_Value(self.event_num)
    length = length + sizeof(c_uint16)
    if self.reference_num > 0:
        length = length + self.references[0].get_packet_list_Length_Value(self.reference_num)
    return length


List_Transaction_Base.get_Transaction_Base_length = get_Transaction_Base_length

def get_length_Transaction_Base_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Transaction_Base_length()
    return length

List_Transaction_Base.get_length_Transaction_Base_list = get_length_Transaction_Base_list

def print_Transaction_Base(self):
    print('version ',self.version)
    print('timestamp ',self.timestamp)
    print('event_num ',self.event_num)
    self.events[0].print_list_Length_Value(self.event_num)
    print('reference_num ',self.reference_num)
    self.references[0].print_list_Length_Value(self.reference_num)

List_Transaction_Base.print_Transaction_Base = print_Transaction_Base

def print_list_Transaction_Base(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Transaction_Base()
    return

List_Transaction_Base.print_list_Transaction_Base = print_list_Transaction_Base


class Transaction(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('timestamp', c_uint64),
        ('event_num', c_uint16),
        ('events', POINTER(List_Length_Value)),
        ('reference_num', c_uint16),
        ('references', POINTER(List_Length_Value)),
        ('cross_ref_num', c_uint16),
        ('cross_refs', POINTER(List_Length_Value)),
        ('signature_num', c_uint16),
        ('signatures', POINTER(List_Length_Value))
    ]

    def __init__(self, _libc):
        self.libc = _libc
        self.version = 0x00
        self.timestamp = 0x00
        self.event_num = 0x00
        self.events = pointer(List_Length_Value(self.libc))
        self.reference_num = 0x00
        self.references = pointer(List_Length_Value(self.libc))
        self.cross_ref_num = 0x00
        self.cross_refs = pointer(List_Length_Value(self.libc))
        self.signature_num = 0x00
        self.signatures = pointer(List_Length_Value(self.libc))

    def inited(self):
        self.version = 0x00
        self.timestamp = 0x00
        self.event_num = 0x00
        self.events = pointer(List_Length_Value(self.libc))
        self.reference_num = 0x00
        self.references = pointer(List_Length_Value(self.libc))
        self.cross_ref_num = 0x00
        self.cross_refs = pointer(List_Length_Value(self.libc))
        self.signature_num = 0x00
        self.signatures = pointer(List_Length_Value(self.libc))

    def get_packet(self):
        packet = bytearray()
        packet.extend(self.version.to_bytes(4,'big'))
        packet.extend(self.timestamp.to_bytes(8,'big'))
        packet.extend(self.event_num.to_bytes(2,'big'))
        packet.extend(self.events[0].get_packet_list_Length_Value(self.event_num))
        packet.extend(self.reference_num.to_bytes(2,'big'))
        packet.extend(self.references[0].get_packet_list_Length_Value(self.reference_num))
        packet.extend(self.cross_ref_num.to_bytes(2,'big'))
        packet.extend(self.cross_refs[0].get_packet_list_Length_Value(self.cross_ref_num))
        packet.extend(self.signature_num.to_bytes(2,'big'))
        packet.extend(self.signatures[0].get_packet_list_Length_Value(self.signature_num))
        return bytes(packet)

    def get_length(self):
        return sizeof(c_uint32) + sizeof(c_uint64) + sizeof(c_uint16) + self.events[0].get_length_Length_Value_list(self.event_num) + sizeof(c_uint16) + self.references[0].get_length_Length_Value_list(self.reference_num) + sizeof(c_uint16) + self.cross_refs[0].get_length_Length_Value_list(self.cross_ref_num) + sizeof(c_uint16) + self.signatures[0].get_length_Length_Value_list(self.signature_num)

    def print_Transaction(self):
        print('version ',self.version)
        print('timestamp ',self.timestamp)
        print('event_num ',self.event_num)
        if self.event_num > 0:
            self.events[0].print_list_Length_Value(self.event_num)
        print('reference_num ',self.reference_num)
        if self.reference_num > 0:
            self.references[0].print_list_Length_Value(self.reference_num)
        print('cross_ref_num ',self.cross_ref_num)
        if self.cross_ref_num > 0:
            self.cross_refs[0].print_list_Length_Value(self.cross_ref_num)
        print('signature_num ',self.signature_num)
        if self.signature_num > 0:
            self.signatures[0].print_list_Length_Value(self.signature_num)

    def set_version(self, _version):
        self.version = _version

    def set_timestamp(self, _timestamp):
        self.timestamp = _timestamp

    def set_event_num(self, _event_num):
        self.event_num = _event_num

    def set_events(self, _events):
        self.events = _events

    def set_reference_num(self, _reference_num):
        self.reference_num = _reference_num

    def set_references(self, _references):
        self.references = _references

    def set_cross_ref_num(self, _cross_ref_num):
        self.cross_ref_num = _cross_ref_num

    def set_cross_refs(self, _cross_refs):
        self.cross_refs = _cross_refs

    def set_signature_num(self, _signature_num):
        self.signature_num = _signature_num

    def set_signatures(self, _signatures):
        self.signatures = _signatures

    def add_to_events_list (self, _events):
        current = self.events[0]

        if self.event_num < 1:
            self.event_num = self.event_num + 1
            current.next = pointer(_events)
            return

        for i in range(self.event_num):
            current = current.next[0]
            if self.event_num - 1 == i:
                self.event_num = self.event_num + 1
                current.next = pointer(_events)
                return

    def add_to_references_list (self, _references):
        current = self.references[0]

        if self.reference_num < 1:
            self.reference_num = self.reference_num + 1
            current.next = pointer(_references)
            return

        for i in range(self.reference_num):
            current = current.next[0]
            if self.reference_num - 1 == i:
                self.reference_num = self.reference_num + 1
                current.next = pointer(_references)
                return

    def add_to_cross_refs_list (self, _cross_refs):
        current = self.cross_refs[0]

        if self.cross_ref_num < 1:
            self.cross_ref_num = self.cross_ref_num + 1
            current.next = pointer(_cross_refs)
            return

        for i in range(self.cross_ref_num):
            current = current.next[0]
            if self.cross_ref_num - 1 == i:
                self.cross_ref_num = self.cross_ref_num + 1
                current.next = pointer(_cross_refs)
                return

    def add_to_signatures_list (self, _signatures):
        current = self.signatures[0]

        if self.signature_num < 1:
            self.signature_num = self.signature_num + 1
            current.next = pointer(_signatures)
            return

        for i in range(self.signature_num):
            current = current.next[0]
            if self.signature_num - 1 == i:
                self.signature_num = self.signature_num + 1
                current.next = pointer(_signatures)
                return

    def get_version(self):
        return self.version

    def get_timestamp(self):
        return self.timestamp

    def get_event_num(self):
        return self.event_num

    def get_events_list_using_index (self, _index):
        current = self.events[0].next[0]

        if self.event_num < 1 or self.event_num < _index or _index <= 0:
            return current

        for i in range(self.event_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_reference_num(self):
        return self.reference_num

    def get_references_list_using_index (self, _index):
        current = self.references[0].next[0]

        if self.reference_num < 1 or self.reference_num < _index or _index <= 0:
            return current

        for i in range(self.reference_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_cross_ref_num(self):
        return self.cross_ref_num

    def get_cross_refs_list_using_index (self, _index):
        current = self.cross_refs[0].next[0]

        if self.cross_ref_num < 1 or self.cross_ref_num < _index or _index <= 0:
            return current

        for i in range(self.cross_ref_num):
            current = current.next[0]
            if _index - 1 == i:
                return current

    def get_signature_num(self):
        return self.signature_num

    def get_signatures_list_using_index (self, _index):
        current = self.signatures[0].next[0]

        if self.signature_num < 1 or self.signature_num < _index or _index <= 0:
            return current

        for i in range(self.signature_num):
            current = current.next[0]
            if _index - 1 == i:
                return current


class List_Transaction(Structure):
    pass

List_Transaction._fields_ = [('version', c_uint32),('timestamp', c_uint64),('event_num', c_uint16),('events', POINTER(List_Length_Value)),('reference_num', c_uint16),('references', POINTER(List_Length_Value)),('cross_ref_num', c_uint16),('cross_refs', POINTER(List_Length_Value)),('signature_num', c_uint16),('signatures', POINTER(List_Length_Value)),('next', POINTER(List_Transaction))]

def __init__(self, _libc):
    self.libc = _libc

List_Transaction.__init__ = __init__

def get_Transaction_version(self):
    return self.version

List_Transaction.get_Transaction_version = get_Transaction_version

def get_Transaction_timestamp(self):
    return self.timestamp

List_Transaction.get_Transaction_timestamp = get_Transaction_timestamp

def get_Transaction_event_num(self):
    return self.event_num

List_Transaction.get_Transaction_event_num = get_Transaction_event_num

def get_Transaction_events(self):
    return self.events

List_Transaction.get_Transaction_events = get_Transaction_events

def get_Transaction_reference_num(self):
    return self.reference_num

List_Transaction.get_Transaction_reference_num = get_Transaction_reference_num

def get_Transaction_references(self):
    return self.references

List_Transaction.get_Transaction_references = get_Transaction_references

def get_Transaction_cross_ref_num(self):
    return self.cross_ref_num

List_Transaction.get_Transaction_cross_ref_num = get_Transaction_cross_ref_num

def get_Transaction_cross_refs(self):
    return self.cross_refs

List_Transaction.get_Transaction_cross_refs = get_Transaction_cross_refs

def get_Transaction_signature_num(self):
    return self.signature_num

List_Transaction.get_Transaction_signature_num = get_Transaction_signature_num

def get_Transaction_signatures(self):
    return self.signatures

List_Transaction.get_Transaction_signatures = get_Transaction_signatures

def get_Transaction_next(self):
    return self.next

List_Transaction.get_Transaction_next = get_Transaction_next

def get_Transaction_next_parameter(self):
    return self.next[0]

List_Transaction.get_Transaction_next_parameter = get_Transaction_next_parameter

def set_Transaction_version(self, _version):
    self.version = _version

List_Transaction.set_Transaction_version = set_Transaction_version

def set_Transaction_timestamp(self, _timestamp):
    self.timestamp = _timestamp

List_Transaction.set_Transaction_timestamp = set_Transaction_timestamp

def set_Transaction_event_num(self, _event_num):
    self.event_num = _event_num

List_Transaction.set_Transaction_event_num = set_Transaction_event_num

def set_Transaction_events(self, _events):
    self.events = _events

List_Transaction.set_Transaction_events = set_Transaction_events

def set_Transaction_reference_num(self, _reference_num):
    self.reference_num = _reference_num

List_Transaction.set_Transaction_reference_num = set_Transaction_reference_num

def set_Transaction_references(self, _references):
    self.references = _references

List_Transaction.set_Transaction_references = set_Transaction_references

def set_Transaction_cross_ref_num(self, _cross_ref_num):
    self.cross_ref_num = _cross_ref_num

List_Transaction.set_Transaction_cross_ref_num = set_Transaction_cross_ref_num

def set_Transaction_cross_refs(self, _cross_refs):
    self.cross_refs = _cross_refs

List_Transaction.set_Transaction_cross_refs = set_Transaction_cross_refs

def set_Transaction_signature_num(self, _signature_num):
    self.signature_num = _signature_num

List_Transaction.set_Transaction_signature_num = set_Transaction_signature_num

def set_Transaction_signatures(self, _signatures):
    self.signatures = _signatures

List_Transaction.set_Transaction_signatures = set_Transaction_signatures

def set_Transaction_next(self, _next):
    self.next = _next

List_Transaction.set_Transaction_next = set_Transaction_next

def get_packet_Transaction_value(self):
    packet = bytearray()
    packet.extend(self.version.to_bytes(4,'big'))
    packet.extend(self.timestamp.to_bytes(8,'big'))
    packet.extend(self.event_num.to_bytes(2,'big'))
    packet.extend(self.events.get_packet())
    packet.extend(self.reference_num.to_bytes(2,'big'))
    packet.extend(self.references.get_packet())
    packet.extend(self.cross_ref_num.to_bytes(2,'big'))
    packet.extend(self.cross_refs.get_packet())
    packet.extend(self.signature_num.to_bytes(2,'big'))
    packet.extend(self.signatures.get_packet())
    return packet

List_Transaction.get_packet_Transaction_value = get_packet_Transaction_value

def get_packet_list_Transaction(self, num):
    packet = bytearray()
    if num < 1:
        return packet
    current = self
    for i in range(num):
        current = current.next[0]
        packet.extend(current.get_packet_Transaction_value())
    return packet

List_Transaction.get_packet_list_Transaction = get_packet_list_Transaction

def get_Transaction_length(self):
    length = 0
    length = length + sizeof(c_uint32)
    length = length + sizeof(c_uint64)
    length = length + sizeof(c_uint16)
    if self.event_num > 0:
        length = length + self.events[0].get_packet_list_Length_Value(self.event_num)
    length = length + sizeof(c_uint16)
    if self.reference_num > 0:
        length = length + self.references[0].get_packet_list_Length_Value(self.reference_num)
    length = length + sizeof(c_uint16)
    if self.cross_ref_num > 0:
        length = length + self.cross_refs[0].get_packet_list_Length_Value(self.cross_ref_num)
    length = length + sizeof(c_uint16)
    if self.signature_num > 0:
        length = length + self.signatures[0].get_packet_list_Length_Value(self.signature_num)
    return length


List_Transaction.get_Transaction_length = get_Transaction_length

def get_length_Transaction_list(self, num):
    length = 0
    if num < 1:
        return length
    current = self
    for i in range(num):
        current = current.next[0]
        length = length + current.get_Transaction_length()
    return length

List_Transaction.get_length_Transaction_list = get_length_Transaction_list

def print_Transaction(self):
    print('version ',self.version)
    print('timestamp ',self.timestamp)
    print('event_num ',self.event_num)
    self.events[0].print_list_Length_Value(self.event_num)
    print('reference_num ',self.reference_num)
    self.references[0].print_list_Length_Value(self.reference_num)
    print('cross_ref_num ',self.cross_ref_num)
    self.cross_refs[0].print_list_Length_Value(self.cross_ref_num)
    print('signature_num ',self.signature_num)
    self.signatures[0].print_list_Length_Value(self.signature_num)

List_Transaction.print_Transaction = print_Transaction

def print_list_Transaction(self, num):
    if num < 1:
        return
    current = self
    for i in range(num):
        current = current.next[0]
        current.print_Transaction()
    return

List_Transaction.print_list_Transaction = print_list_Transaction


