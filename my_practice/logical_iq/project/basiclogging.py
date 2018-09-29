import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected 
# WARNING: (default) An indication that something unexpected happened, or indicative of some problem in the near future(e.g 'disk space low'). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Level	    Numeric value
# CRITICAL	50
# ERROR	    40
# WARNING	30
# INFO	    20
# DEBUG	    10
# NOTSET	0

# Format	Description
# %(name)s	Name of the logger (logging channel).
# %(levelno)s	Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(levelname)s	Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# %(pathname)s	Full pathname of the source file where the logging call was issued (if available).
# %(filename)s	Filename portion of pathname.
# %(module)s	Module (name portion of filename).
# %(lineno)d	Source line number where the logging call was issued (if available).
# %(created)f	Time when the LogRecord was created (as returned by time.time()).
# %(asctime)s	Human-readable time when the LogRecord was created. By default this is of the form ``2003-07-08 16:49:45,896'' (the numbers after the comma are millisecond portion of the time).
# %(msecs)d	Millisecond portion of the time when the LogRecord was created.
# %(thread)d	Thread ID (if available).
# %(threadName)s	Thread name (if available).
# %(process)d	Process ID (if available).
# %(message)s	The logged message, computed as msg % args.


# Attribute name	Format	                                    Description
# args	        You shouldn’t need to format this yourself.	The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).
# asctime	        %(asctime)s	                                Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).
# created	        %(created)f	                                Time when the LogRecord was created (as returned by time.time()).
# exc_info	You shouldn’t need to format this yourself.	Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.
# filename	%(filename)s	Filename portion of pathname.
# funcName	%(funcName)s	Name of function containing the logging call.
# levelname	%(levelname)s	Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# levelno	%(levelno)s	Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# lineno	%(lineno)d	Source line number where the logging call was issued (if available).
# message	%(message)s	The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
# module	%(module)s	Module (name portion of filename).
# msecs	%(msecs)d	Millisecond portion of the time when the LogRecord was created.
# msg	You shouldn’t need to format this yourself.	The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).
# name	%(name)s	Name of the logger used to log the call.
# pathname	%(pathname)s	Full pathname of the source file where the logging call was issued (if available).
# process	%(process)d	Process ID (if available).
# processName	%(processName)s	Process name (if available).
# relativeCreated	%(relativeCreated)d	Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
# stack_info	You shouldn’t need to format this yourself.	Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.
# thread	%(thread)d	Thread ID (if available).
# threadName	%(threadName)s	Thread name (if available).



# logger = logging.getLogger()
# handler = logging.StreamHandler()
# formatter = logging.Formatter(
#         '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)


logfile = 'test.log'
# logging.basicConfig(filename=logfile,filemode='a',format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s %(lineno)d', datefmt='%H:%M:%S')

logging.info("Testing")
logging.debug("this is test")

def add(n1,n2):
    logging.warning("this is not warning just display {:d}, {:d}".format(n1,n2))
    return n1 + n2 

a = add(2,3)
logging.error("string")
logging.critical('EXit')