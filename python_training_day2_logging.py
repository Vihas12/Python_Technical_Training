# import logging
# logging.basicConfig(filename='logging_txt/newfile.txt',level=logging.DEBUG)
# logging.debug("this indicates the debugging information")
# logging.info("this indicates the important information")
# logging.error("this indicates the error information")
# logging.warning("this indictaes the warning information")
# logging.critical("this indicates the critical information")

# import logging
# logging.basicConfig(filename="logging_txt/newexcept.txt",level=logging.DEBUG)
# try:
#     val1 = int(input("Enter first value: "))
#     val2 = int(input("Enter second value: "))
#     print(val1/val2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
#     logging.exception(msg)