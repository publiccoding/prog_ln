import sys
import signal
import time
import os

#  1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
#  6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
# 11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
# 16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
# 21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
# 26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
# 31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
# 38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
# 43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
# 48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
# 53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
# 58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
# 63) SIGRTMAX-1	64) SIGRTMAX

def signalHandler(a,b):
    print("Signal received ",a,"==",b)

original_signalint = signal.getsignal(signal.SIGINT)
original_sigquit_handler = signal.getsignal(signal.SIGQUIT)
print(original_signalint)
signal.signal(signal.SIGINT,signalHandler)
#signal.signal(signal.SIGUSR1,signalHandler)
print('My PID is:', os.getpid())
while(1):
    print("Wait...")
    time.sleep(10)
signal.signal(signal.SIGINT, original_signalint)
    



# import sys
# import signal
# import socket

# def handler(s, f):
#     print 'Signal handler called with signal', s
#     raise IOError("Couldn't connect!")

# signal.signal(signal.SIGALRM, handler)

# ## set an alarm to go off after 5 sec, this is our timeout
# signal.alarm(5)

# ## the operation that may take a long time/or wait indefinitely, than we expect it to
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("www.some-non-existant-website.com", 80))

# # Disable the alarm, in case the previous operation goes through
# signal.alarm(0)


# import signal
# import threading
# import os
# import time

# def signal_handler(num, stack):
#     print('Received signal %d in %s' % (num, threading.currentThread()))

# signal.signal(signal.SIGINT, signal_handler)

# def wait_for_signal():
#     print('Waiting for signal in', threading.currentThread())
#     signal.pause()
#     print('Done waiting')

# # Start a thread that will not receive the signal
# receiver = threading.Thread(target=wait_for_signal, name='receiver')
# receiver.start()
# time.sleep(0.1)

# def send_signal():
#     print('Sending signal in', threading.currentThread())
#     os.kill(os.getpid(), signal.SIGINT)

# sender = threading.Thread(target=send_signal, name='sender')
# sender.start()
# sender.join()

# # Wait for the thread to see the signal (not going to happen!)
# print('Waiting for', receiver)
# signal.alarm(2)
# receiver.join()