#!/usr/bin/env python3
# encoding: utf-8

import sys
import dis
import time 
import atexit 
import gc

assert sys.version_info[0] == 3 and sys.version_info[1] >= 7, "This assignment should only be done in version 3.7+"

start_time = 0

def trace_function(frame, event, arg):
    #The trace function that receives call events
    return None

def exit_handler():
    #This function is called when program exits
    sys.settrace(None)

if __name__ == "__main__":
    #Register exit handler that is called before the application exits
    atexit.register (exit_handler)
    #Set the start time of application
    start_time = time.time ()
    #Set the trace function
    sys.settrace(trace_function)
    
    #Read the first argument
    assert len(sys.argv) >= 2, "Provide the python program to profile. Usage example: python -m snake-prof test.py"
    with open(sys.argv[1], 'rb') as fp:
        exec (fp.read ())
