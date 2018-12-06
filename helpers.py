def alphabet_position(letter):
  
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    
    for k in range(0, len(alphabet)):
        if alphabet[k] == letter:
            return k
          

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphaCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if char not in alphabet and char not in alphaCap:
        return char
    
    if char in alphabet:
        
        index = alphabet_position(char) + rot
        index = index % 26 
        
        for i in range(0,len(alphabet)):
            if i == index:
                return alphabet[i]               
    else:    
        index = alphabet_position(char) + rot
        index = index % 26 
        
        for k in range(0,len(alphaCap)):
            if k == index:
                return alphaCap[k] 
