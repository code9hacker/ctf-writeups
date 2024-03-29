#easy #web #sql-injection #sqlmap #hashcat

# The Challenge
KORP Terminal
Your faction must infiltrate the KORP™ terminal and gain access to the Legionaries' privileged information and find out more about the organizers of the Fray. The terminal login screen is protected by state-of-the-art encryption and security protocols.
Website can be accessed with the IP:PORT provided.

# Recon
Upon visiting the website, we are presented with a login form with username and password as input. Upon messing a little bit with the values such as passing 'single-quote' character, we can see that it triggers some SQL error in the backend. This determines the possibility of sql-injection vulnerability.
!('images/first-error.png')

# The Solution
We can work up our payload to exploit the vulnerability. To faster things up, we can use sqlmap tool. It quickly finds the vulnerability and we are able to see all the data in the database with a table called 'users' present. This table was found to contain username 'admin' and password in bcrypt hash format.
To break the password, we can use hashcat tool with a wordlist such as /usr/share/wordlists/seclists/Passwords/Common-Credentials/10-million-password-list-top-10000.txt which shows the password to us.
!('images/password-cracked.png')

Upon entering the username 'admin' and found password 'password123' in the webpage, the flag was got.
!('images/success.png')