#easy #pwntools

# The Challenge
The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...
To access the challenge, use nc serverIP:port

# Recon
Upon running nc command, we can see that the program demands responses with below rules
1. For every 'GORGE' word, return 'STOP'
2. For every 'PHREAK' word, return 'DROP'
3. For every 'FIRE' word, return 'ROLL'
4. For multiple commands like 'PHREAK, FIRE', return 'DROP-ROLL'
!('images/recon.png')

# Solution
To solve this challenge, we read each line and print the desired output. It takes a while and in the end returns the flag.
!('images/getting_flag.png')