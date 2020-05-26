import sys
import socket
import time
import signal
from timeit import default_timer as timer
from tcping import variables


def get_results(count, passed, failed):
    lRate = 0
    if failed != 0:
        lRate = failed / (count) * 100
        lRate = "%.2f" % lRate

    print("\nPing Results: Connections (Total/Pass/Fail): [{:}/{:}/{:}] (Failed: {:}%)".format((count), passed,
                                                                                                   failed, str(lRate)))


def signal_handler(signal, frame):
    get_results(variables.count, variables.passed, variables.failed)
    sys.exit(0)


def ping_hosts(host, port, maxcount):

    signal.signal(signal.SIGINT, signal_handler)

    while variables.count < maxcount:

        variables.count += 1

        success = False

        s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        s_start = timer()

        try:
            s.connect((host, int(port)))
            s.shutdown(socket.SHUT_RD)
            success = True

        except socket.timeout:
            print("Connection timed out!")
            variables.failed += 1
        except OSError as e:
            print("Error:", e)
            variables.failed += 1

        # Stop Timer
        s_stop = timer()
        s_runtime = "%.2f" % (1000 * (s_stop - s_start))

        if success:
            print("Connected to %s[%s]: tcp_seq=%s time=%s ms" % (host, port, (variables.count - 1), s_runtime))
            variables.passed += 1

        # Sleep for 1sec
        if variables.count < maxcount:
            time.sleep(1)
    return
