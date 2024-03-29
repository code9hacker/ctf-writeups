#easy #web #javascript

# The Challenge
Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!
Website can be accessed with the IP:PORT provided.

# Recon
Looking at the website, it seemed like kind of a game that takes some inputs and prints some texts. Then it presents more input. Looking at the traffic throught burp, we see a few interesting JS files main.js, game.js and commands.js.

# The Solution
The main.js files includes API calls to /api endpoint. The /api/monitor is used to continue the game and check the provided input if its correct or not. This is done by the following code
async function CheckMessage() {
    fetchingResponse = true;
    currentCommand = commandHistory[commandHistory.length - 1];

    if (availableOptions[currentStep].includes(currentCommand) || availableOptions['secret'].includes(currentCommand)) {
        await fetch('/api/monitor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'command': currentCommand })
        })

We can see if the provided input is in the 'availableOptions[currentStep]' or 'availableOptions[secret]', then it is accepted. 
Now, we check how the this variable's value is set and we find another API call that is made to /api/options that fetches the allowed commands.

For secret, we find
   "secret": [
      "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"
    ]

Providing this input in the webpage provides the flag.
!('images/success.png')