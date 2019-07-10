import string
import can
import struct
# file = open('/home/sholy/can_0.bin', 'rb')
# content = file.readline()
#
# print(content)
# file.close()
# te = can.Printer('/home/sholy/can_0.bin')
# tes = can.RedirectReader('/home/sholy/can_0.bin')
# print(tes.on_message_received())
# print(te.file)
# print(te.file.buffer.read())
# te.file.close()
# can.util.load_config()
# can.logger
# print(can.Printer('/home/sholy/can_0.bin'))

# file = open('/home/sholy/can_0.bin','rb')
# tes = file.read(100)
# print(tes)
# # for d in tes:
# #     print(d)
# dic = {'can':bytes([0xf2,0xea,0xee])}
# print(tes.startswith(dic['can']))
# st = can.bus.time()
# var_arr = struct.unpack(st,tes)
# print(var_arr)

import queue

my = queue.Queue()
i = 0
for i in range(5):
    my.put(i)

while not my.empty():
    print(my.get())

