from builtins import input
import binascii

#在RH850 的 mot文件的时候，计算最后的CRC数值
def main():
    print("")
    while(1):
        calculaecrc()

def calculaecrc():
    print("//===============================//")
    source       = input("Input Souce: ")
    print("//===============================//")
    crc = 0
    length = len(source)
    for i in range(0,length-1,2):
        temp = transfer(ord(source[i])) * 16 + transfer(ord(source[i+1]))
        crc = crc + temp

    crc = 255 - (crc%256);
    crc = hex(crc) 
    print("CRC: " + crc)
    print("//================================//")

def transfer(ain):
    if ain < 58:
        aout = ain - 48 ;
    elif ain < 71:
        aout = ain - 65 + 10 ;
    else:
        aout = ain - 97 + 10;
    
    return aout

if __name__ == "__main__":
    main()
