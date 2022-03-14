The Turing machine was invented by Alan Turing, who had great influences on the development of computing. It was first described by Turing in 1936 in his article dealing with issues concerning computable numbers. It is also described as an automatic machine. The machine was idealized in 1935 with the view of stating that a function can be calculated effectively by purely mechanical process. After 2 years, in 1937, Turing built his electromechanical machine. In general, it has a tape, which is divided into cells, each contains a symbol. It also has a ‘head’ that can read and write these symbols, and move the tape left and right one cell at a time. 
Turing machines played an important role in technology and programming; because based on the machine’s logic, Turing proved that it is possible to calculate any computable function. It has changed the thought about what computers can do by giving the idea of what computation was and what it means to have a program. With the models of Turing machines, people can create a new generation of computers, and give the birth of “digital computer” and “computer science”. Nowadays, the theory of science continues to take some parts of Turing machine as models for theorists investigating questions. Therefore, we can say that this machine is the fundamental of the modern computer.
The Turing machine calculate the sum of 2 binary numbers: 
input:  '10100 011101'
blank: ' '
start state:  q0
table:

  q0:
    	[0,1] : {R: q1}
  q1:
    	[0,1,a,b] : {R: q1}
    	' ': {R: q2}
  q2:
    	[0,1]: {R: q2}
    	' ': {L: q3}
  q3:
    	0: {write: ' ', L: q4}
    	' ': {L: q9}
    	1: {write: ' ', L: q6}
  q4:
    	[0,1] : {L: q4}
    	' ': {L: q5}
  q5:
    	[a,b]: {L: q5}
    	0: {write: a, R: q1}
    	1: {write: b, R: q1}
  q6:
    	[0,1]: {L: q6}
    	' ': {L: q7}
  q7:
    	[a,b]: {L: q7}
    	0: {write: b, R: q1}
    	1: {write: a, L: q8}
  q8:
    	1: {write: 0, L: q8}
    	[' ', 0]: {write: 1, R: q1}
  q9:
    	b: {write: 1, L: q9}
    	a: {write: 0, L: q9}
    	[0,1,' ']: {R: done}
  done:
