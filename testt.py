# # conn.send([0xD2, 0xE0, 0x00, 0x01], (0xE0, [
# #		[(0xDF, 0xAA, 0x01), b'mapp/loading_message.html'],
# #		[(0xDF, 0xAA, 0x02), b'titlemsg'], [(0xDF, 0xAA, 0x03), b'welcome text 1'],
# ]))
#
#
#
# ([0xD2, 0xE0, 0x00, 0x01], (0xE0, [(0xDF, 0xAA, 0x02), b'disablekey'], [(0xDF, 0xAA, 0x03), b'1'],
#                             [(0xDF, 0xAA, 0x01), b 69 64 6C 65 2E 68 74 6D 6C DF AA 02 0D 54 45 4D 50 4C 41 54 45 5F 56
#                              41 52 30 DF AA 03 38 3C 70 20 73 74 79 6C 65 3D 22 74 65 78 74 2D 61 6C 69 67 6E 3A 63 65 6
#                              E 74 65 72 3B 22 20 3E 50 72 6F 63 65 73 73 69 6E 67 2E 2E 2E 20 50 6C 65 61 73 65 20 57 61
#                              69 74 DF AA 02 0A 74 65 78 74 5F 73 74 79 6C 65 DF AA 03 0B 68 65 69 67 68 74 3A 20 36 30
#                              25
#
# for i in range(1, 1 + val):
#     for n in P1:
#         conn.send([0xD2, 0x01, n, 0x01])
#         timesend = time.time()
#
#         status, buf, uns = conn.receive()
#         timerecieve = time.time()
#
#         time_taken = timerecieve - timesend
#
#         log.log(str(datetime.datetime.now()), "--> Time taken for D2,01 command with p1 " + str(n) + " is :",
#                 (time_taken))
#         avg_time.append(time_taken)
#
# avgg = sum(avg_time) / (len(P1) * val)
# log.log('AVG TIME FOR DISPLAY COMMAND EXECUTION IS :', avgg)