#easy #pwntools

# The Challenge
Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!
To access the challenge, use nc serverIP:port

# Recon
We can see that the challenge takes an integer and gives the flag's character at that index.
!('images/first_recon.png')

# Solution
It's pretty straightforward. To make it fast, we will make a script in python to solve it. The script is going to enter an integer one at a time, read the response line and create the flag.
!('images/solution.png')
