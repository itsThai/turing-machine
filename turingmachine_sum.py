def q0(tape, index):
    print(' '.join(tape))
    if tape[index] in ['0', '1']:
        q1(tape, index+1)

def q1(tape, index):
    print(' '.join(tape))
    if tape[index]  in ['0', '1', 'a', 'b']:
        q1(tape, index+1)
    else:
        q2(tape, index+1)

def q2(tape, index):
    print(' '.join(tape))
    if tape[index]  in ['0', '1']:
        q2(tape, index+1)
    elif tape[index] in [' ']:
        q3(tape, index-1)

def q3(tape, index):
    print(' '.join(tape))
    if tape[index] in ['0']:
        tape[index] = " "
        q4(tape, index-1)
    elif tape[index] in [' ']:
        q9(tape, index-1)
    elif tape[index] in ['1']:
        tape[index] = " "
        q6(tape, index-1)

def q4(tape, index):
    print(' '.join(tape))
    if tape[index]  in ['0', '1']:
        q4(tape, index-1)
    elif tape[index] in [' ']:
        q5(tape, index-1)

def q5(tape, index):
    print(' '.join(tape))
    if tape[index] in ['a', 'b']:
        q5(tape, index-1)
    elif tape[index] in ['0']:
        tape[index] = "a"
        q1(tape, index+1)
    elif tape[index] in ['1']:
        tape[index] = "b"
        q1(tape, index +1)

def q6(tape, index):
    print(' '.join(tape))
    if tape[index]  in ['0', '1']:
        q6(tape, index -1)
    elif tape[index] in [' ']:
        q7(tape, index-1)

def q7(tape, index):
    print(' '.join(tape))
    if tape[index] in ['a', 'b']:
        q7(tape, index-1)
    elif tape[index] in ['0']:
        tape[index] = "b"
        q1(tape, index+1)
    elif tape[index] in ['1']:
        tape[index] = "a"
        q8(tape, index-1)

def q8(tape, index):
    print(' '.join(tape))
    if tape[index] in ['1']:
        tape[index] = "0"
        q8(tape, index-1)
    elif tape[index] in ['0', ' ']:
        tape[index] = "1"
        q1(tape, index+1)

def q9(tape, index):
    print(' '.join(tape))
    if tape[index] in ['1', '0', ' ']:
        print("The answer is:")
        print(' '.join(tape))

    elif tape[index] in ['a']:
        tape[index] = "0"
        q9(tape, index-1)
    elif tape[index] in ['b']:
        tape[index] = "1"
        q9(tape, index-1)


tape =list(" 10100 011101 ")
q0(tape,1)