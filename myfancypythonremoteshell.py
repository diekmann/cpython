#!./python
import pty
import os, sys, signal

def stdin_read(env, fd):
    child_pid, master_fd = env
    r = os.read(fd, 1024)
    if not r:
        print("stdin EOF {}".format(child_pid), file=sys.stderr, flush=True)
        #os.write(master_fd, b'\x04')
        os.kill(child_pid, signal.SIGHUP) #yolo, maybe it is already dead
    return r

pty.spawn('/bin/sh', stdin_read=stdin_read)
