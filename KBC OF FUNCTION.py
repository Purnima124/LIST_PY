question_list = [
    "how many continents are there?",             # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"  # teesra question
    ]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_lists = [3, 4, 1]

answer_list=[
    ["(1)Four","(3)seven"],
    ["(4)Delhi","(2)Bhupal"],
    ["(4)Agriculture","(1)software Engineering"]
]
def kbc():
    print("WELCOME TO KON BANEGA KADODPATI")
    i=question_list = [
    "how many continents are there?",             # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"  # teesra question
    ]

    options_list = [
    #pehle question ke liye options
        ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
        ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
        ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
    ]
# har ek question ke liye, uski solution key (yeh index nahi hai)
    solution_lists = [3, 4, 1]

    answer_list=[
        ["(1)Four","(3)seven"],
        ["(4)Delhi","(2)Bhupal"],
        ["(4)Agriculture","(1)software Engineering"]
    ]
    print("WELCOME TO KON BANEGA KADODPATI")
    i=0
    s=0
    count=0
    while i<len(question_list):
        print(question_list[i])
        a=0
        b=i
        while a<len(options_list[i]):
            k=options_list[b][a]
            print(a+1,k)
            a=a+1
        num1=input("Do you want 5050 life line")
        if num1=="yes":
            print("50 50 lifeline")
            if count< 1:
                print(answer_list[b])
                num2=int(input("enter your answer"))
                if num2==solution_lists[i]:
                    s+=10000
                    print("congratulation your answer correct")
                    print("you win 😀😀🤗Rs/",s)
                else:
                    print("your answer is rong")
                    print("you can paly again")
                    print("you win 😀Rs/",s)
                    break
                count+=1
        else:
            print("you already use lifeline")
            m=int(input("enter your answer"))
            if m==solution_lists[i]:
                print("congres right answer")
                s+=10000
                print("you win 😀😀😀 Rs/",s)
            else:
                print("No chance😩😩😩😩")
                print("your answer is wrong")
                print("you win😀😀😀 Rs/",s)
                break
    else:
        pass
        k=int(input("enter you won answer"))
        if k==solution_lists[i]:
            print("congres right answer")
            s+=10000
            print("you are win 😀😀😀Rs/",s)
        else:
            print("No chance")
            print("your answer is wrong😩😩😩")
            print("you are win Rs/",s)
            break
    i=i+1
     
print("____congrescutionl you are big part of!___KON BANEGA KADODPATI")
print("you are win Rs/",s)
print("Thank you are part of this")
kbc()

