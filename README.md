<h1>What is it?</h1>
  <hr>
  
This code is a bot for Whatsapp Web in Pyhton 3.8.2 using ChomeDriver.

I have create this on 2020 to automate the comunication process to the lead students on my Trainee Engeneering Program in Minas Gerais, Brazil. It is not just a concept, it's working fine up to date.

<h1>Fair play: Game Rules</h1>
<hr>

A. The <b>freedom</b> to perform for any purpose.</n>

B. The <b>freedom</b> to study how the program works.</n>

C. The <b>freedom</b> to redistribute copies and benefit people.</n>

D. The <b>freedom</b> to perfect and release your improvements.</n>


<h1>What does it do ?</h1>
<hr>

1. Open Chrome, then visit web.whatsapp.com</n>

2. Copy, write and send the mensage on Word(.docx) to textbox via Selenium. <b>Note that the message changes according to the name of the person you are sending the mensage to</b> (to do this, you have to respect the first sentence: "Olá, FULANO" and Excel Columns template)</n>

3. Do Loops on phones list stored on Excel(.xlsx)</n>

p.s: On Excelb - 1st Column: <b>Name</b> and 2nd Column: <b>Phone number</b> (format:  (+) followed by the country code, city code, and local phone number)    

<h1>FAQ</h1>
<hr>
<h5>Am I going to be banned from WhatsApp?</h5>
Hum, so you already know that Whatsapp does not allow Bots, right?

Well, you're right: Whatsapp will ban you forever if they discovery you are running a Bot on long-term. For a small test: Don't worry, go forward.

I can't understand why Mark Zuckerberg still forbid Bots, he is the kind of guy who loves to copy-cat all the good things in the Web, right? Why not simply copy WeChat features? if you go to China, you will discover that you can pay all your bills using WeChat.

I can't guarantee that you are not getting banned in a long term using this Bot. I really don't think so, but I can't guarantee.


<h5>Why you use WhatsApp Web via Selenium? Is there a better solution?</h5>
Today we have more optimize options on Python like Yowsup.
First, yowsup is a great python library! Simply awesome.
But their problem is: They connect to Whatsapp servers directly, without any middlware. So it is not so hard for whatsapp team to create ban-rules you if you are using yowsup.

I got banned many times in past, so I know, soon or later, you will get banned as well. Is just a matter of time, but with Selenium it will take longer to you be discovered if you use it gradually. I send messages in batches of 60 out of 60. 

That's why I did this code. Using whatsapp web, it is almost impossible for whatsapp team to know that you are running a Bot.


<h5>But... What are the limitations?</h5>
A lot of limitations!
As you are handling DOM direcly, you can't process hundred of messages at once. Yowsup is much better at this subject.
You have to install Whatsapp on your phone, connect it on Wifi and keep it charging all the time. So you have to have a cellphone exclusively for this Bot. You will need a computer with chrome running as well. But that's the main objective: In order to avoid being detect as a Bot, so you have to play this boring cat-and-rat game.

<h5>I think there're some bugs on your code.</h5>
Yes, there are.
Feel free to fix and commit it.

<hr>
<h3>Author:</h3> <h3>Vinícius Almeida de Souza https://www.linkedin.com/in/valmsou</h3> 
<hr>
  
