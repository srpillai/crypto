
from helpers import alphabet_position, rotate_character

def encrypt(msg, rot):
    
    result = ''
    for pos in range(len(msg)):
        result = result + rotate_character(msg[pos], rot)
    return result


def main():
    msg = input("Type a message:")
    rot = (input("Rotate by:"))
    rot= int(rot)
    print(encrypt(msg, rot))
    
if __name__ == '__main__':
    main()


