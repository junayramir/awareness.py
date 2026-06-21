nameof_the_user=input('Enter your name: ')
print("hello " + nameof_the_user)
ques=input("DISCLAIMER:THIS GAME IS CODED FOR AWARENESS PURPOSES ONLY.IT MAY NOT APPLY TO A LOT OF CONDITIONS(press ENTER).")
ques1=input("lets look at the rules(KEEP PRESSING ENTER)")
rule1=input("In this game,u will be choosing ur own adventure")
rule2=input("u will be given various sort of questions which u will get to answer")
rule3=input("some questions will consist of either a yes or no")
rule4=input("some will also be needed to answer by urself.")
rule5=input("its a basic game so dont worry, u will have a good time")
statement=input("so now that u know the rules, lets start playing?(yes/no);").lower()
if statement=='no':
    print("okay,u may leave")
else:
    ques2=input("suppose u are about to walk across a lake and the bridge randomly broke, do u take another route or swim?: ")
    if ques2=='swim' or ques2=='take another route':
     print('great!u are now across the river')
    ques3=input("after u cross the river u feel really tired,u come across a water fountain. do u drink water from it?(yes/no); " ).lower()
    if ques3=='yes':
     print('yay!u are no longer thirsty')
     ques4 = input(
         "u keep walking,u come across a weird guy walking upto a kid sitting alone.do u go up to them?(yes/no);").lower()
     if ques4 == 'yes':
         print("goodjob!we should always help out people in danger")
     else:
         print("bad choice!what if smth happens to that child? ")
         print("children are vulnerable and sometimes are unaware of the dangers in the world.")
         print("children are the future of our society.regardless of that, we should develop enough empathy and compassion towards other human being")
         print("okay,lets continue anyways")

    else:
     extra_ques=input("u are really dehydrated! why didnt u drink the water?water is essential for our health,"
                     "our body is 70% water!: ")
    print("alright!i understand.lets move on")
    ques4=input("u keep walking,u come across a weird guy walking upto a kid sitting alone.do u go up to them?(yes/no);").lower()
    if ques4=='yes':
       print("goodjob!we should always help out people in danger")
    else:
      print("bad choice!what if smth happens to that child? ")
      print("children are vulnerable and sometimes are unaware of the dangers in the world.")
      print("children are the future of our society.regardless of that, we should develop enough empathy and compassion towards other human being")
      print("okay,lets continue anyways")

    ques=input("later on, while u were walking a person comes up to u, they call u many sorts of name and racism was faced in a waay.do u stand up for urself?(yes/no):").lower()
    if ques=='yes':
        print("goodjob! racism is an unfair treatment,discrimination or prejudice against people")
        print("every person deserves to be treated equally regardless of race and looks.")
        print("thus,standing up for ourselves can help spread awareness and thus a better society")
    else:
     print("bad choice!racism is an unfair treatment,discrimination or prejudice against people.")
     print("every person deserves to be treated the same regardless of their looks and race.")
     print("standing up for ourselves help spread awareness and thus a better society")





