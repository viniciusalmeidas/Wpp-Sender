<h2>What is it?</h2>
  <hr>
  
This code is a bot for Whatsapp Web in Pyhton 3.8.2 using ChomeDriver.

I have create this on 2020 to automate the comunication process to the lead students on my Trainee Engineering Program in Minas Gerais, Brazil. It is not just a concept, it's working fine up to date.


<h2>What does the code do ?</h2>
<hr>

0. You will select the mensagem.txt and telefones.xlsx files on your computer.</n>

<img width="304" alt="wpp-screen" src="https://user-images.githubusercontent.com/39459689/92387870-ad613b00-f0ec-11ea-8f7c-b06d17d9a3d8.png">

1. The Bot will open Chrome, then visit web.whatsapp.com</n>
Here you have to read the QRCode using the cellphone that you choose.

<img width="404" alt="wpp-qr-code" src="https://user-images.githubusercontent.com/39459689/92387947-cff35400-f0ec-11ea-8141-b0cd9d0244ec.png">

2. READY! the bot will copy, write and send the mensage from Word(.docx) to textbox via Selenium. <b>Note that the message changes according to the name of the person you are sending the mensage to</b> (to do this, you have to respect the first sentence: "Olá, FULANO" and Excel Columns template)</n>

3. This code do loops on each phone on phone list stored on Excel(.xlsx)</n>

p.s: On Excel - 1st Column: <b>Name</b> and 2nd Column: <b>Phone number</b> (format:  (+) followed by the country code, city code, and local phone number)    

Name | Phone
-------|--------
Vinicius | 55 21 987422122
John| 55 11 982736132

<h2>FAQ</h2>
<hr>
<h5>Am I going to be banned from WhatsApp?</h5>
Hum, so you already know that Whatsapp does not allow Bots, right?

Well, you're right: Whatsapp will ban you forever if they discovery you are running a Bot on long-term. For a small test: Don't worry, go forward. I can't understand why Mark Zuckerberg still forbid Bots, he is the kind of guy who loves to copy-cat all the good things in the Web.

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

<h2>Fair play: Game Rules</h2>
<hr>

A. The <b>freedom</b> to perform for any purpose.</n>

B. The <b>freedom</b> to study how the program works.</n>

C. The <b>freedom</b> to redistribute copies and benefit people.</n>

D. The <b>freedom</b> to perfect and release your improvements.</n>



<hr>

### **Author: Vinícius Almeida de Souza**

Thanks for your collaboration.

> _"Coming together is a beginning,
> staying together is progress,
> and working together is **sucess.**"_ - H. Ford

- My free projects on - [GitHub](https://github.com/viniciusalmeidas)
- My profile on - [LinkedIn](https://www.linkedin.com/in/valmsou/?originalSubdomain=br)
- My life on - [Instagram](https://www.instagram.com/v.alma_br/)
 
