# turing-machine
The Turing machine was invented by Alan Turing, who had great influences on the development of computing. It was first described by Turing in 1936 in his article dealing with issues concerning computable numbers. It is also described as an automatic machine. The machine was idealized in 1935 with the view of stating that a function can be calculated effectively by purely mechanical process. After 2 years, in 1937, Turing built his electromechanical machine. In general, it has a tape, which is divided into cells, each contains a symbol. It also has a ‘head’ that can read and write these symbols, and move the tape left and right one cell at a time. <br>
Turing machines played an important role in technology and programming; because based on the machine’s logic, Turing proved that it is possible to calculate any computable function. It has changed the thought about what computers can do by giving the idea of what computation was and what it means to have a program. With the models of Turing machines, people can create a new generation of computers, and give the birth of “digital computer” and “computer science”. Nowadays, the theory of science continues to take some parts of Turing machine as models for theorists investigating questions. Therefore, we can say that this machine is the fundamental of the modern computer.
<br><br>
The Turing machine calculate the sum of 2 binary numbers: <br>
input:  '10100 011101'<br>
blank: ' ' <br>
start state:  q0 <br>
table: <br>
<ul>
  <li>q0:
    	<ul>[0,1] : {R: q1} </ul>
        </li>
  <li>q1:
    	<ul>[0,1,a,b] : {R: q1}</ul>
    	<ul>' ': {R: q2}</ul>
    </li>
  <li>q2:
    	<ul>[0,1]: {R: q2}</ul>
    	<ul>' ': {L: q3}</ul>
    </li>
  <li>q3:
    	<ul>0: {write: ' ', L: q4}</ul>
    	<ul>' ': {L: q9}</ul>
    	<ul>1: {write: ' ', L: q6}</ul>
    </li>
  <li>q4:
    	<ul>[0,1] : {L: q4}</ul>
    	<ul>' ': {L: q5}</ul>
    </li>
  <li>q5:
    	<ul>[a,b]: {L: q5}</ul>
    	<ul>0: {write: a, R: q1}</ul>
    	<ul>1: {write: b, R: q1}</ul>
    </li>
  <li>q6:
    	<ul>[0,1]: {L: q6}</ul>
    	<ul>' ': {L: q7}</ul>
    </li>
  <li>q7:
    	<ul>[a,b]: {L: q7}</ul>
    	<ul>0: {write: b, R: q1}</ul>
    	<ul>1: {write: a, L: q8}</ul>
    </li>
  <li>q8:
    	<ul>1: {write: 0, L: q8}</ul>
    	<ul>[' ', 0]: {write: 1, R: q1}</ul>
    </li>
  <li>q9:
    	<ul>b: {write: 1, L: q9}</ul>
    	<ul>a: {write: 0, L: q9}</ul>
    	<ul>[0,1,' ']: {R: done}</ul>
    </li>
  <li>done:
