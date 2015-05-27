import socket
# the public network interface
HOST = socket.gethostbyname(socket.gethostname())
# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))
while True:

    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # receive all packages
#S    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # receive a package
    newfile = open("results.txt", "at")
    packets = (s.recvfrom(65565)[0],"hey", s.recvfrom(65565)[1])
    print packets
    newfile.write(str(packets[0]))
    newfile.write(str(packets[1]))
    newfile.write("\n")
    newfile.close()
    print (s.recvfrom(65565))

    # disabled promiscuous mode
    #s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    input("get another?")