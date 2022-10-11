import socket

# this is encoding our data
ENCODING = 'utf-8'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Here I ask the user what IP address we are connecting to and setting it to a variable
    print(f"What IP are we connecting to: ")
    TEST_IP_ADDRESS = input()
    # Here I ask the user for what port the data will be sent through and set it to a variable
    print(f"What port are we connecting to: ")
    PORT = int(input())
    # Here we are connecting to that IP and Port we asked for earlier
    s.connect((TEST_IP_ADDRESS, PORT))
    # Here I ask the user for the keyword that will trigger the data to be sent
    print(f"Enter the keyword for the server: ")
    KEYWORD = (input())
    # Just printing what the user input for keyword
    print(f"keyword is", KEYWORD)
    # I convert that input to a byte by encoding to be sent to server
    watch = KEYWORD.encode("utf-8")
    # Here is where I send the keyword to trigger the server
    s.send(watch)
    # Here I receive the quote from the server if the keyword was right
    data = s.recv(1024)
    # these two lines of code are testing the encoding and decoding of the client server base
    temp = data.decode('utf-8')
    print(f"temp is: ", temp)
# word document explaining my server
# Cap in wireshark
    # Here I simply print what I received
    print(f"Received {data!r}")
