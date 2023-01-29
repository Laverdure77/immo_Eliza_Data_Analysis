class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'        # Yellow
    FAIL = '\033[91m'           # Red
    ENDC = '\033[0m'        # Reset default
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# def colour_print(text,colour):
#     if colour == 'OKBLUE':
#         string = bcolors.OKBLUE + text + bcolors.ENDC
#         print(string)
#     elif colour == 'HEADER':
#         string = bcolors.HEADER + text + bcolors.ENDC
#         print(string)
#     elif colour == 'OKCYAN':
#         string = bcolors.OKCYAN + text + bcolors.ENDC
#         print(string)
#     elif colour == 'OKGREEN':
#         string = bcolors.OKGREEN + text + bcolors.ENDC
#         print(string)
#     elif colour == 'WARNING':
#         string = bcolors.WARNING + text + bcolors.ENDC
#         print(string)
#     elif colour == 'FAIL':
#         string = bcolors.HEADER + text + bcolors.ENDC
#         print(string)
#     elif colour == 'BOLD':
#         string = bcolors.BOLD + text + bcolors.ENDC
#         print(string)
#     elif colour == 'UNDERLINE':
#         string = bcolors.UNDERLINE + text + bcolors.ENDC
#         print(string)

# value = 1
# text = f"this is the value: {value}"
# colour_print('Hello world','OKBLUE')
# colour_print('easy one','OKCYAN')
# print(bcolors.BOLD + bcolors.WARNING + bcolors.UNDERLINE+"this is the value: "+  bcolors.FAIL +f"{value}"+bcolors.ENDC)
# colour_print('copy and paste','OKGREEN')
# colour_print('done','OKBLUE')
# colour_print(text,'OKBLUE')
# print(f"{bcolors.BOLD} Hello")