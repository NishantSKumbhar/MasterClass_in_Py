"""
@author : Nishant Sanjay Kumbhar
@goal : packet let user -> 125
            if user byte - > 1
              then packet = 125
            if user byte -> 126
              then packet -> 125*2 =   250
"""
import sys


def packet(byte: int, pack: int) -> int:
    """
    This is Packet Method
    :param byte: Number of Bytes
    :param pack: Packet of
    :return: return the final Packet.
    """
    if pack <= 0 and byte < 0:
        print("Pack and Bytes should be valid !")
        sys.exit(-1)
    elif byte <= pack:
        return pack
    elif pack < byte:
        m = byte % pack
        d = byte // pack
        if m == 0.0:
            return d*pack
        else:
            return d*pack + pack


def main():
    pack = int(input("Enter the Pack : "))
    byte = int(input("Enter the Number of Bytes : "))
    packet_number = packet(byte, pack)
    print(f"Packet for {byte} bytes is {packet_number}.")


main()
