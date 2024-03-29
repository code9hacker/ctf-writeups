#easy #python-basics

# The Challenge
Think you can escape my grasp? Challenge accepted! I dare you to try and break free, but beware, it won't be easy. I'm ready for whatever tricks you have up your sleeve!
To access the challenge, use nc serverIP:port
Challenge files are provided, see misc_unbreakable folder

# Recon
After looking at the code, we know we have to print the contents of 'flag.txt' file. The program uses eval() function which takes user input and runs the given python statement. Also, there is a blacklist of characters.

# Solution
To get the contents of a file, the easiest python statement is open('flag.txt','r').read(). And no character is in blacklist.
Also, the program adds a '()' to the statement, so running payload print(open('flag.txt','r').read()) is not possible. The simple trick to get away with that is add a comment character to the payload, so anything that program adds after the input becomes a comment.

# Payload
print(open('flag.txt','r').read())#