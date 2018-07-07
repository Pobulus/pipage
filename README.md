# pipage
<b>The Pillow Pattern Generator</b> </br>
Okay so what is this program for? Does it generate patterns for pillows? </br>
No. </br>
Then what's its purpose?</br>
It's ment to give me patterns OF pillows on my couch. I got bored with coming up with them so I wanted to make program which will do it for me.
</br> Originally it was supposed to be text based, but I ended up with Tkinter GUI.

<b> USAGE </b></br>

<b>Requirements:</b>

<ul>
  <li>Python (either 2.7 or 3.6, both will work)</li>
  <li>Tkinter (if not already installed)</li>
  <li>screeninfo (optional, you can set screen width manually)
</ul></br>
 <b>Executing:</b>
 <ol>
  <li>Clone (or download an unzip) this repository</li>
  <li>In terminal navigate to project's folder</li>
  <li>In terminal: python pipage.py or: python3 pipage.py </li>
  <li>You should see a window with the width of your monitor, or smaller if you haven't installed screeninfo</li>
</ol>
If you're ok with current window size, proceed to "Control", if you want to change it, continue reading below.</br>
</br>
<b>Changing window size:</br></b>
 To make your window wider, open "pipage.py" with any plain text editor and change the value in the 3rd line: </br>
 default_width = 480 </br>
 to: </br>
 default_width = [your_screen_width]</br></br>
 
  <b>Control:</br></b>
 <ul>
  <li>Use left and right arrow keys or "BACK" and "NEXT" buttons to cycle different patterns </li>
  <li>Use space bar or  "RANDOM" button to get a random pattern</li>
<li>Enter a number from 0-143 in the entry field and pres "GO" or enter key to get a pattern with said number</li>
  </ul>
 </br></br>
 <b>EXPLANATION</b></br>
 Here's a little explanation of why have I made this project.</br>
 About a month ago I bought myself a few new pillows, and at that time I wasn't expecting they will be so problematic.</br>
 Uptil then i had two identical blue pillows, which didn't leave much liberty in arranging them on the couch. I would just </br>
 place them near eachother, sometimes tilt them by 45 degrees. Yet, I didn't anticipate the struggle that came with three </br>
 additional red pillows. In the beginning I placed them in a row, and every day I changed their positioning slightly.</br>
 Finally few days ago I ran out of ideas, so I tried solving this problem with math, that's what I came up with: </br>
 </br>
 1■ 2■ 3■ 4■ 5■
 <ul>
 <li>I have 2 blue pillows and 3 red pillows</li>
  <li>They myst be arranged symetrically, so the one in the middle must be red</li>
  <li>Since they're simetrical, pillow 1 and 5 are in the same state, just like 2 and 4, so i can treat it like 3 pillows</li>
  <li>Each pillow can be either straight or tilted by 45 degrees</li>
  <li>Blue can be a state of only pillow 1 or only pillow 2</li>
  <li>Pillow 2 can be either in front of or behind pillow 3</li>
  <li>Pillow 1 can be either in front of or behind pillow 2</li>
 </ul>
 </br>
 So with this list of assumptions i made this program. </br>
 On the program's site it look like this:</br>
Two numbers, one int binary and one in ternary, the first one consists of 4 bits. </br>
Blue on the inside</br>
| Pillow 2 tilted</br>
v v</br>
1010</br>
 ^ ^ </br>
 | Pillow 1 tilted</br>
 Pillow 3 tilted</br>
 
 so for example, value of 1101, would look like this:<br/> 
 1R◆ 2B■ 3R◆ 4B■ 5R◆ </br>
 This gives us 16 possible combinations </br>
 No to the second number, two digits in base 3</br>
 these correspond to pillows 2 and 1,</br>
 if the value is 1 they are next to the pillow on the right</br>
 if the value is 2 thay are over the pillow on the right</br>
 and if the value is 0mthay are below the pillow on the left</br>
 And this gives us 9 possible combinations</br>
 when we multiply both of those numbers we get 144 possible combinations of colors, tilts and overlaps.</br>
 </br>
 <b>IMPROVEMENTS</b>
 Can this program even be improved? Yes, certainly! We can add asimetrical patterns with two blues on one side or with a blue in the middle</br>
 also maybe more than one row, but this requires all the pillows to be tilted. but for any of these see me in 5 months, that's when I'll run out of these patterns :).
