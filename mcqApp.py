from class_app import Question

questions_list = [
    "A process is a?\n (A)single thread of execution\n (B)program in the execution\n (C)program in the memory\n (D)task\n\n",
    "What is smallest unit of the information?\n (A)a bit\n (B)a byte\n (C)a block\n (D)a nibble\n\n",
    "What is the decimal equivalent of the binary number 10111?\n (A)21\n (B)39\n (C)42\n (D)23\n\n",
    "How many color dots make up one color pixel on a screen?\n (A)265\n (B)16\n (C)8\n (D)3\n\n",
    "Which of the following values is the correct value of this hexadecimal code 1F.01B?\n (A)35.0065918\n (B)32.0065918\n (C)31.0065918\n (D)30.0065918\n\n",
    "How is the data stored on the diskette?\n (A)Ink\n (B)Laser bubbles\n (C)Magnetism\n (D)Circuit\n\n",
    " Which of the following is the smallest visual element on a video monitor?\n (A)Character\n (B)Pixel\n (C)Byte\n (D)Bit\n\n",
    "Which of the following natural element is the primary element in computer chips?\n (A)Silicon\n (B)Carbon\n (C)Iron\n (D)Uraniun\n\n",
    "Which of the following is an output device?\n (A)Keyboard\n (B)Mouse\n (C)Light pen\n (D)VDU\n\n"
]
list_questions_answers = [
    Question(questions_list[0], 'B'),
    Question(questions_list[1], 'A'),
    Question(questions_list[2], 'D'),
    Question(questions_list[3], 'D'),
    Question(questions_list[4], 'D'),
    Question(questions_list[5], 'C'),
    Question(questions_list[6], 'B'),
    Question(questions_list[7], 'A'),
    Question(questions_list[8], 'D')
]


def test(questions):
    name = input("Enter your name: ")
    score = 0
    for u in questions:
        print(u.question)
        answer = input("Enter you answer: ")
        if answer == u.response:
            score += 1
            print("Correct")
        else:
            print('Incorrect')

    if score == 9 or score==8:
        print(f"Hello {name} your score is {score}/{len(questions)} Excellent")

    elif score == 7:
        print(f"Hello {name} your score is {score}/{len(questions)} V-Good")
    elif score == 6:
        print(f"Hello {name} your score is {score}/{len(questions)} Good")
    elif score == 5:
        print(f"Hello {name} your score is {score}/{len(questions)} Average")
    elif score == 4 or score==3:
        print(f"Hello {name} your score is {score}/{len(questions)} Fail")

    else:
        print(f"Hello {name} your score is {score}/{len(questions)} Bad")
    resumeGame = input("do you want to continue (Yes/No)")
    if resumeGame == 'Yes':
        test(list_questions_answers)
    else:
        exit()


test(list_questions_answers)
