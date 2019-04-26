Crypto

Background

A Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

The Vigenère cipher uses a Caesar cipher with a different shift at each position in the text; the value of the shift is defined using a repeating keyword. If the keyword is as long as the message, is chosen at random, never becomes known to anyone else, and is never reused, this is the one-time pad cipher, proven unbreakable.

This crypto  assignment consists of 2 parts:
1. Caesar: An encryption algorithm.
2. Vigenere: An even cooler encryption algorithm.

The Caesar

This is a general version of rot13 function that uses the Caesar cipher to encrypt a message. The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to “its right” in the alphabet. So for example the letter “a” becomes the letter “n”. If a letter is past the middle of the alphabet then the counting wraps around to the letter “a” again, so “n” becomes “a”, “o” becomes “b” and so on.

The caesar is a more general version of the rot13 algorithm that allows a message to be encrypted using any rotation amount, not just 13. Ultimately, users will be able to type a message in the terminal, and specify a rotation amount (13, 4, 600, etc), and your program will print the resulting encrypted message.

The Vigenere

Vigenere uses a word as the encryption key, rather than an integer. Your finished program will behave like this:

For example, 

$ python vigenere.py
Type a message:
The crow flies at midnight!
Encryption key:
boom
Answer: Uvs osck rmwse bh auebwsih!

You probably noticed that Vigenere is very similar to Caesar. The only difference is that the rotation amount varies throughout the course of the message.

Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

Download a copy from the Github: https://github.com/srpillai/crypto

Prerequisites

You will need a chrome or similar browser and a python compiler

Installing

Clone or Download a copy from the Github: https://github.com/srpillai/crypto

Built With

* Python - The language

Contributing

Created as part of LaunchCode unit-2  LC-101 course

Author

* Radhakrishnan Pillai - Initial work - LaunchCoder 2019

License

This project is licensed under the MIT License 

Acknowledgments
* LaunchCode Unit-1 Team
* Inspiration: LaunchCode, Kansas City, MO

