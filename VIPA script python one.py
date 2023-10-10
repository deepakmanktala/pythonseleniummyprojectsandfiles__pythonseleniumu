from testharness import *
from testharness.tlvparser import TLVParser, tagStorage
from sys import exit
from testharness.syslog import getSyslog
import time


def transtest_function():
    log = getSyslog()
    conn = connection.Connection()

    print("At conn.connect()")
    isSearial = False
    if not isSearial:
        req_unsolicited = conn.connect()
        status, buf, uns = conn.receive()
        if req_unsolicited:

            # Receive unsolicited
            status, buf, uns = conn.receive()
            if status != 0x9000:
                log.logerr('Unsolicited fail')
                exit(-1)
            log.log('Unsolicited', TLVParser(buf))
    else:
        req_unsolicited = conn.connect()

    # Get VF Certificate
    # status, buf, uns = conn.receive()

    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 00 60')
    status, buf, uns = conn.receive()

    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 01 61')
    status, buf, uns = conn.receive()

    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 02 62')
    status, buf, uns = conn.receive()
    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 03 63')
    status, buf, uns = conn.receive()
    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 04 64')
    status, buf, uns = conn.receive()

    conn.send_rawhex('01 00 0C C5 06 01 00 07 E0 05 DF 83 10 01 05 65')
    status, buf, uns = conn.receive()
    # Stream Upload to set in streaming mode
    conn.send_rawhex('01 00 17 00 A5 05 00 12 6F 10 84 08 67 76 72 31 2E 63 72 74 80 04 00 00 05 26 E9')
    status, buf, uns = conn.receive()
    time.sleep(4)
    # send GVR crt in streammode
    conn.send_rawhex(
        '2D 2D 2D 2D 2D 42 45 47 49 4E 20 43 45 52 54 49 46 49 43 41 54 45 2D 2D 2D 2D 2D 0A 4D 49 49 44 6E 7A 43 43 41 6F 65 67 41 77 49 42 41 67 49 48 54 51 6B 67 41 41 41 42 41 6A 41 4E 42 67 6B 71 68 6B 69 47 39 77 30 42 41 51 73 46 41 44 42 68 4D 51 73 77 43 51 59 44 56 51 51 47 0A 45 77 4A 56 55 7A 45 5A 4D 42 63 47 41 31 55 45 43 77 77 51 51 30 46 66 55 6B 39 50 56 46 39 56 57 44 4E 66 4F 6C 56 59 4D 7A 45 57 4D 42 51 47 41 31 55 45 41 77 77 4E 54 54 45 78 4E 6A 63 78 0A 51 6B 51 77 4E 6A 41 77 4D 54 45 66 4D 42 30 47 43 53 71 47 53 49 62 33 44 51 45 4A 41 52 59 51 64 33 64 33 4C 6D 64 70 62 47 4A 68 63 6D 4E 76 4C 6D 4E 76 62 54 41 65 46 77 30 78 4E 7A 41 30 0A 4D 44 4D 77 4D 44 41 77 4D 44 42 61 46 77 30 30 4D 44 45 79 4D 7A 45 77 4D 44 41 77 4D 44 42 61 4D 46 6F 78 43 7A 41 4A 42 67 4E 56 42 41 59 54 41 6C 56 54 4D 52 63 77 46 51 59 44 56 51 51 4C 0A 44 41 35 44 51 56 39 56 57 44 4E 66 54 45 52 66 4F 6C 56 59 4D 7A 45 52 4D 41 38 47 41 31 55 45 41 77 77 49 4D 44 45 35 4F 44 49 35 4E 7A 41 78 48 7A 41 64 42 67 6B 71 68 6B 69 47 39 77 30 42 0A 43 51 45 57 45 48 64 33 64 79 35 6E 61 57 78 69 59 58 4A 6A 62 79 35 6A 62 32 30 77 67 67 45 69 4D 41 30 47 43 53 71 47 53 49 62 33 44 51 45 42 41 51 55 41 41 34 49 42 44 77 41 77 67 67 45 4B 0A 41 6F 49 42 41 51 44 44 33 79 59 6E 4C 44 57 66 6D 59 63 5A 37 78 34 64 6B 41 7A 36 54 69 35 65 32 41 39 39 73 6F 4F 6A 63 4A 6E 44 37 2B 4B 46 46 6F 5A 43 72 6B 4B 65 62 54 71 32 50 69 42 35 0A 4B 53 37 69 6B 72 64 79 4D 58 57 4C 42 63 56 4F 66 65 43 73 45 56 41 41 77 72 33 48 45 62 6E 56 2B 6C 65 42 6E 46 58 4B 61 67 2F 51 61 74 72 66 4D 72 4A 6A 48 67 68 39 2B 6A 34 39 42 79 39 56 0A 30 69 4E 38 38 41 45 77 66 54 49 6B 41 65 32 79 69 74 48 36 45 37 4F 61 45 63 43 51 79 56 73 4D 51 76 2F 41 43 43 73 61 50 4E 58 4F 4A 63 39 79 47 6D 68 43 31 39 63 54 4E 4F 75 63 54 4E 38 41 0A 68 36 6C 4D 72 30 46 6C 57 6E 39 35 43 35 4F 38 63 7A 6C 33 41 57 6A 65 75 6F 37 4F 4A 32 68 2B 46 59 2F 4F 48 58 4C 67 5A 37 72 49 42 69 66 62 71 68 79 72 55 63 42 51 2B 78 54 75 66 75 73 38 0A 58 37 4B 57 71 47 57 59 56 2F 32 78 35 61 55 2B 79 44 34 57 2F 50 30 51 6C 48 4D 53 7A 51 57 6F 78 33 34 4B 48 6A 77 62 50 2F 55 39 70 31 78 30 44 54 4B 4E 35 6E 2F 2F 74 72 37 4C 37 69 72 76 0A 50 34 2B 61 5A 2B 2B 48 6D 44 2B 63 32 66 31 2F 76 2B 70 41 49 34 7A 48 33 6B 50 56 41 67 4D 42 41 41 47 6A 59 7A 42 68 4D 42 38 47 41 31 55 64 49 77 51 59 4D 42 61 41 46 4E 4F 69 43 33 43 42 0A 74 47 4A 30 6D 54 73 4E 46 79 76 4C 6E 69 54 6F 77 7A 56 6C 4D 42 30 47 41 31 55 64 44 67 51 57 42 42 54 41 48 57 39 78 61 36 4A 42 35 6F 37 58 2F 48 6A 45 4A 63 46 50 76 69 34 69 33 6A 41 50 0A 42 67 4E 56 48 52 4D 42 41 66 38 45 42 54 41 44 41 51 48 2F 4D 41 34 47 41 31 55 64 44 77 45 42 2F 77 51 45 41 77 49 42 78 6A 41 4E 42 67 6B 71 68 6B 69 47 39 77 30 42 41 51 73 46 41 41 4F 43 0A 41 51 45 41 54 2B 30 42 45 30 34 2B 36 64 54 6C 78 38 50 43 45 62 4A 73 36 53 6A 47 69 55 69 69 43 39 50 76 42 30 79 70 78 33 78 52 49 38 44 4D 2B 2F 57 58 37 65 70 71 31 70 36 42 39 72 54 4A 0A 51 77 68 7A 58 6B 59 53 62 75 53 46 62 42 43 52 74 58 43 69 70 54 55 6D 37 45 39 62 2F 72 76 45 32 68 6C 79 41 69 6B 51 6F 67 34 36 6E 52 62 68 5A 6A 6E 41 67 69 32 2F 59 55 66 79 47 49 48 5A 0A 74 64 32 38 62 4D 64 63 54 46 39 67 4A 5A 33 5A 4E 50 7A 35 75 32 65 2B 58 72 6B 67 59 73 42 58 61 74 38 31 31 46 6B 64 4A 33 2F 6A 48 4B 45 39 6A 6D 4E 64 49 72 6C 34 49 4A 70 2F 31 44 4A 62 0A 5A 70 41 4D 30 53 6D 54 37 6C 61 4D 68 70 73 6C 78 78 75 69 49 78 67 2B 68 69 6D 76 4B 50 56 4E 34 30 54 37 4C 5A 69 38 45 69 42 58 42 4E 71 50 67 36 4C 54 71 7A 47 35 51 2B 44 41 5A 44 44 67 0A 54 2F 61 6D 39 44 73 47 4E 70 38 42 68 62 55 36 68 78 72 55 67 4A 35 45 32 55 54 53 59 67 50 5A 70 36 48 77 44 4A 61 78 30 6E 2F 68 57 74 62 6B 37 61 78 6F 32 58 44 72 50 52 48 5A 36 43 44 64 0A 34 49 66 34 58 41 74 4B 35 41 6A 37 30 61 30 59 71 70 35 34 71 63 64 62 78 67 3D 3D 0A 2D 2D 2D 2D 2D 45 4E 44 20 43 45 52 54 49 46 49 43 41 54 45 2D 2D 2D 2D 2D 0A')
    status, buf, uns = conn.receive()
    # stream upload data
    print('receive for stream data')

    conn.send_rawhex('01 00 18 C5 07 00 00 13 E0 11 DF 83 10 01 01 DF 83 12 08 67 76 72 31 2E 63 72 74 2A')
    status, buf, uns = conn.receive()
    print('stream second part')

    print(
        "Garbage  Garbage Garbage Garbage Garbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage GarbageGarbage  Garbage Garbage Garbage GarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbageGarbage")

    # Read record SFI 3,record 02
    conn.send([0x00, 0xB2, 0x02, 0x1C])
    status, buf, uns = conn.receive()
    log.log("rev: ", str(buf))

    # Read record SFI 3,record 02
    conn.send([0x00, 0xB2, 0x02, 0x1C, 0x7F])
    status, buf, uns = conn.receive_raw()

    # 1st GENAC
    conn.send(
        [0x80, 0xAE, 0x80, 0x00, 0x1D, 0x00, 0x00, 0x00, 0x00, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03,
         0x80, 0x02, 0x80, 0x04, 0x80, 0x00, 0x09, 0x78, 0x16, 0x10, 0x21, 0x00, 0x2F, 0x10, 0xAF, 0xBF])
    status, buf, uns = conn.receive()
    log.log("rev: ", str(buf))

    # Get response
    # conn.send([0x00, 0xC0, 0x00, 0x00, 0x14])
    # status, buf, uns = conn.receive()
    # log.log("rev: ", str(buf))

    # 2nd GENAC
    conn.send(
        [0x80, 0xAE, 0x40, 0x00, 0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x03, 0x80, 0x02, 0x80, 0x04, 0x80, 0x20, 0x09, 0x78, 0x16, 0x10, 0x21, 0x00, 0x2F, 0x10, 0xAF, 0xBF,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    status, buf, uns = conn.receive()
    log.log("rev: ", str(buf))

    # Get response
    # conn.send([0x00, 0xC0, 0x00, 0x00, 0x14])
    # status, buf, uns = conn.receive()
    # log.log("rev: ", str(buf))


if __name__ == '__main__':
    utility.register_testharness_script(transtest_function)
    utility.do_testharness()
