# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Server Checker
# Version: 1.0: Base version by author
import sys
import requests

e_msg_1 = """Error: At least One argument is required.
    Usage: 
        python server_checker.py <server_address> <server_port>
    Example:
        python server_checker.py www.google.com 80
    Note: server_port defaults to 80 if not specified.
System exiting with Error Code: 1"""
e_msg_2 = 'Error: Port Number is not between 1 and 65535. System exiting with Error Code: 2'
e_msg_3 = 'Error: Connection Timed Out. System exiting with Error Code: 3'
e_msg_4 = 'Error: Connection Failed. System exiting with Error Code: 4'


def server_checker(server, port):
    try:
        reply = requests.head(url="http://{}:{}/".format(server, port), timeout=5)
        request_codes = requests.codes.__dict__
        if reply.status_code == 200:
            print('Success. Address/IP: {} found. Response:'.format(server), reply.status_code, '(means OK)')
        else:
            response_meaning = list(request_codes.keys())[list(request_codes.values()).index(reply.status_code)]
            print('Error: Address/IP: {} responded with Response Code:'.format(server), reply.status_code, '- (means)',
                  response_meaning.upper())
    except requests.exceptions.Timeout:
        print(e_msg_3)
        sys.exit(3)
    except requests.exceptions.RequestException:
        print(e_msg_4)
        sys.exit(4)


if __name__ == '__main__':
    if len(sys.argv) in [2, 3]:
        server_address = sys.argv[1]
        if len(sys.argv) == 2:
            print('Info: Port Number has been set to 80.')
            server_port = 80
        else:
            server_port = int(sys.argv[2])
        if server_port not in range(1, 65536):
            print(e_msg_2)
            sys.exit(2)
    else:
        print(e_msg_1)
        sys.exit(1)
    server_checker(server_address, server_port)
