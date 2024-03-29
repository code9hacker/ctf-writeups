#easy #web #docker #bash-commands

# The Challenge
Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.
Website can be accessed with the IP:PORT provided.
Also, code is provided as can be seen in /web_timekorp

# Recon
Looking at the code architecture, we can notice that it is a docker image. The file containing the flag is also present at the root of the folder named 'flag'. The Dockerfile interestingly shows that this file is copied to the root folder of the container, so we knows where this file be in the challenge website.
The code is written in PHP and uses a Model-View-Controller pattern.

# The Solution
In MVC pattern, the controller is where our code would be so we look at that and find that it's taking a date-time format as input and creating a TimeModel object. Looking at the TimeModel file, we can see that there is a getTime() method that calls the exec() method of PHP to run the 'date' bash command to print the date/time in the format provided. Since there is no restriction to user provided 'format' string, this becomes a command injection vulnerability where we can inject any command and see the result on the webpage.

The command is generated as
$this->command = "date '+" . $format . "' 2>&1";

So, we just need to figure out how to build a syntactically correct bash command. We can use the pipe operator to combine multiple commands to achieve our goal.

Payload = %H:%M:%S'+2>%261+|+cat+'/flag

!('images/success.png')
