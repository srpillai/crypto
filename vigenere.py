
from helpers import alphabet_position, rotate_character
          
def encrypt(text, rot):
    
    result = ""                                                               
    numeric = 0
    rotate = []
    
    for k in rot:                                                               
        letter = alphabet_position(k)
        rotate.append(letter)        

    for index in range(len(text)):                                              
        if text[index].isalpha():                                               
            extra = (index - numeric) % len(rotate)
            value = rotate_character(text[index], rotate[extra])
            result = result + value
        else:                                 #check for space character                                    
            numeric = numeric + 1                                                
            result = result + text[index] 
            
    return result

def main():
    msg = input("Type a message:")
    rot = (input("Rotate by:"))
    print(encrypt(msg, rot))
    

if __name__ == '__main__':
    main()

