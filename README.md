<h1>What is it?</h1>
  <hr>
  
This code is an example of Bot for Whatsapp Web in Pyhton 3.8.2 using ChomerDriver.

I have create this piece of code on 2020 to automate the comunication process to the lead students on my Trainee Engeneering Program in Minas Gerais, Brazil. It is not just a concept, it's working fine up to date.

<h1>Fair play: Game Rules</h1>
<hr>

A. The <b>freedom</b> to perform for any purpose.</n>

B. The <b>freedom</b> to study how the program works.</n>

C. The <b>freedom</b> to redistribute copies and benefit people.</n>

D. The <b>freedom</b> to perfect and release your improvements.</n>


<h1>What does it do ?</h1>
<hr>
1. Open Chrome, then visit web.whatsapp.com</n>

2. Copy, write and send the mensage on Word(.docx) to textbox via Selenium. <b>Note that the message changes according to the name of the person you are sending the mensage to<b> (to do this, you have to respect the first sentence: "Olá, FULANO")</n>

3. Do Loops on phones list stored on Excel(.xlsx)</n>

obs: Pay attention on the Excel and Word templates. On Excel (1st Column: Name, 2nd Column: Phone number (format:  (+) followed by the country code, city code, and local phone number)    

<h1>FAQ</h1>
<hr>
<h5>Am I going to be banned from WhatsApp?</h5>
Hum, so you already know that Whatsapp does not allow Bots, right?

Well, you're right: Whatsapp will ban you forever if they discovery you are running a Bot on long-term. For a small test: Don't worry, go forward.

I can't understand why Mark Zuckerberg still forbid Bots, he is the kind of guy who loves to copy-cat all the good things in the Web, right? Why not simply copy WeChat features? if you go to China, you will discover that you can pay all your bills using WeChat, including silly things like P2P payments or restaurants. Paper money is past.

Elon Musk may be right, perhaps the little Zuckberg is just being limited in this subject, lol.

I can't guarantee that you are not getting banned in a long term using this Bot. I really don't think so, but I can't guarantee.

<h5>I think there're some bugs on your code.</h5>
Yes, there are.
Feel free to fix and commit it.


<h4>Why you use WhatsApp Web via Selenium? Is there a better solution</h4>
<hr>
Today we have more optimize options on Python like Yowsup.
First, yowsup is a great python library! Simply awesome.
But their problem is: They connect to Whatsapp servers directly, without any middlware. So it is not so hard for whatsapp team to create ban-rules you if you are using yowsup.

I got banned many times in past, so I know, soon or later, you will get banned as well. Is just a matter of time, but with Selenium it will take longer to you be discovered if you use it gradually. I send messages in batches of 60 out of 60. 

That's why I did this code. Using whatsapp web, it is almost impossible for whatsapp team to know that you are running a Bot.

<h4>But... What are the limitations?</h4>
A lot of limitations!
As you are handling DOM direcly, you can't process hundred of messages at once. Yowsup is much better at this subject.
You have to install Whatsapp on your phone, connect it on Wifi and keep it charging all the time. So you have to have a cellphone exclusively for this Bot. You will need a computer with chrome running as well. But that's the main objective: In order to avoid being detect as a Bot, so you have to play this boring cat-and-rat game.
 

<hr>
<h2>-Author: Vinícius Almeida de Souza</h2> 
  <h4>https://www.linkedin.com/in/valmsou</h4>
  
