import math

# questions from the following website: https://depression.org.nz/is-it-depression-anxiety/self-test/depression-test/


#function to add spaces after text for better legibility
def add_space():
    print("")

#main function to run whole program, calls to it later
def Beam_Program_Running():
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    # starting questions and directions of print statements
    print(color.YELLOW + "Beam" + color.END)
    add_space()
    add_space()
    print(color.GREEN + "Hi there! Welcome to Beam. We're here to help." +
          color.END)
    add_space()
    print(
        color.GREEN +
        "To get started, you'll need to answer a few questions about how you're feeling, so we can gauge what advice we can give you."
        + color.END)
    add_space()
    print(
        color.GREEN +
        "Please answer all questions truthfully so we can help you the best we can."
        + color.END)
    add_space()
    add_space()
    print(
        color.GREEN +
        "These questions are on a scale from 1-5, 1 being not at all, and 5 being constantly."
        + color.END)
    add_space()
    add_space()
    #asks the user to verify they want to start the questions
    useragreement = input(color.CYAN + "Enter 1 to get started.")

    #sets variables for user number input
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    #sets empty list to store user inputs
    userinputs = []

    #sets empty list to stre user feedback
    user_feedback = []
    #if statement to see if user inputted the correct 'ok' and begins first question
    #q1
    if useragreement == '1':
        add_space()
        u_a_q1 = int(
            input(
                "#1. (On a scale of 1-5) How often have you been bothered by feeling down, depressed, irritable, or hopeless over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q1)
    else:
        Beam_Program_Running()
        print(
            "You did not enter a valid command or you do not wish to answer the questions. Please scroll to restart."
        )
        #Beam_Program_Running()
        add_space()

    #q2
    if u_a_q1 == one or two or three or four or five:
        u_a_q2 = int(
            input(
                "#2. (On a scale of 1-5) How often have you been bothered that you have little interest or pleasure in doing things over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q2)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q3
    if u_a_q2 == one or two or three or four or five:
        u_a_q3 = int(
            input(
                "#3. (On a scale of 1-5) How often have you been bothered by trouble falling asleep, staying asleep, or sleeping too much over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q3)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q4
    if u_a_q3 == one or two or three or four or five:
        u_a_q4 = int(
            input(
                "#4. (On a scale of 1-5) How often have you been bothered that you have poor appetite, weight loss, or overeating over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q4)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q5
    if u_a_q4 == one or two or three or four or five:
        u_a_q5 = int(
            input(
                "#5. (On a scale of 1-5) How often have you been bothered by being irritated by the people you love for no reason or wanting to be constantly left alone over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q5)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q6
    if u_a_q5 == one or two or three or four or five:
        u_a_q6 = int(
            input(
                "#6. (On a scale of 1-5) How often have you been bothered by feeling bad about yourself – or feeling that you are a failure, or that you have let yourself or your family down over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q6)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q7
    if u_a_q6 == one or two or three or four or five:
        u_a_q7 = int(
            input(
                "#7. (On a scale of 1-5) How often have you been bothered by moving or speaking so slowly that other people could have noticed?"
            ))
        add_space()
        userinputs.append(u_a_q7)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q8
    if u_a_q7 == one or two or three or four or five:
        u_a_q8 = int(
            input(
                "#8. (On a scale of 1-5) Do you find yourself extremely emotional or sensitive to worrying subjects or events?"
            ))
        add_space()
        userinputs.append(u_a_q8)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q9
    if u_a_q8 == one or two or three or four or five:
        u_a_q9 = int(
            input(
                "#9. (On a scale of 1-5) How often have you been bothered by thoughts that you would be better off dead, or of hurting yourself in some way over the last two weeks?"
            ))
        add_space()
        userinputs.append(u_a_q9)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
        )
        Beam_Program_Running()
        add_space()

    #q10
    if u_a_q9 == one or two or three or four or five:
        u_a_q10 = int(
            input(
                "#10. Do you often have thoughts of harming or killing yourself because of reasons above or any reason?"
            ))
        add_space()
        userinputs.append(u_a_q10)
    else:
        print(
            "You did not enter a valid OK command or you do not wish to answer the questions. Please reload or restart."
            + color.END)
        Beam_Program_Running()
    add_space()

    #adds the sums of all the user inputs and totals them as integers
    sum1 = int(u_a_q1) + int(u_a_q2)
    sum2 = int(u_a_q3) + int(u_a_q4)
    sum3 = int(u_a_q5) + int(u_a_q6)
    sum4 = int(u_a_q7) + int(u_a_q8)
    sum5 = int(u_a_q9) + int(u_a_q10)

    #adds the sum variables together
    total_score = sum1 + sum2 + sum3 + sum4 + sum5

    #creates loading effect
    for x in range(3):
        print("Loading...")
    add_space()

    #prints user's score out of 50
    print(color.GREEN + "You scored", total_score, "out of 50")
    add_space()

    #prints end total for user and corresponds to a rating of their mental heath occurences
    if (total_score >= 40):
        print(
            "You have a very high occurence of mental illness symptoms. Please consider consulitng a mental health professional now to get help or look to a loved one to talk about how you are feeling."
        )
    elif (total_score >= 30):
        print(
            "You have a high occurence of mental illness symptoms. If your symptoms persist or get worse, please consider consulting a mental health professional to get help or look to a loved one to talk about how you are feeling."
        )
    elif (total_score >= 20):
        print(
            "You have a moderate occurrence of mental illness symptoms. If your symptoms worsen signifigantly, please consider consulting a mental health professional to get help or look to a loved one to talk about how you are feeling."
        )
    elif (total_score >= 10):
        print(
            "You have a low occurence of mental illness symptoms. In the future, if your answers start to become 3s or 4s to many questions, please consider consulting a mental health professional to get help or look to a loved one to talk about how you are feeling."
        )
    else:
        print(
            "You have a very low occurence of mental illness symptoms. If you do feel that any one of the situations you answered to increase or persist in the future look to a loved one to talk abou thow you are feeling, or consult a mental health professional."
        )
    add_space()

    #prompts user to look further to see specific advice for their problems
    print(
        "If you entered 3 or higher to any of the previous questions keep reading for specific advice."
    )
    add_space()

    #if statements to show that if the user responding 3 or higher to any of the questions, they are shown some specific advice

    #q1 advice
    if (u_a_q1) >= 3:
        print(
            "#1. It seems that you suffer from little to severe depression and/or anxiety. Try to make time for self care-- doing things that you love. Also, talk to somebody you trust about how you are feeling to get some of your conflicts resolved or talked through."
        )
        add_space()

    #q2 advice
    if (u_a_q2) >= 3:
        print(
            "#2. It seems that you have lost motivation and/or inspiration for things you love. Try to chunk out overwhelming tasks into small steps that are easier to tackle. Also, set goals and reward yourself when you accomplish them."
        )
        add_space()

    #q3 advice
    if (u_a_q3) >= 3:
        print(
            "#3. It seems that you have trouble sleeping. This insomnia could be caused by a mental health problem. Try to go to bed earlier than usual and turn off all electronic screens an hour before going to bed."
        )
        add_space()

    #q4 advice
    if (u_a_q4) >= 3:
        print(
            "#4. It seems that you are either under or over eating or using food to cope with your stress. If you are struggling with either, try to eat 3 healthy, balanced meals a day with fufilling snacks in between meals when you are hungry. If you still feel you are unhappy with your body consult with a trusted loved one or seek professional advice."
        )
        add_space()

    #q5 advice
    if (u_a_q5) >= 3:
        print(
            "#5. It seems that your feelings are causing you to withdraw from the people that you love. Try making an effort to become socially engaged or put yourself out there enough to find those you have common interest with. Remember that you can always talk to family, loved ones and friends and they are here to help."
        )
        add_space()

    #q6 advice
    if (u_a_q6) >= 3:
        print(
            "#6. It seems that you have self-esteem issues or trouble doubting yourself often. When your thoughts begin to spiral and get out of control, fight back from these inner thoguhts. By doing this you stop and prevent this pattern from happening again. Keep clarity of your current situation and remember that most setbacks are temporary."
        )
        add_space()

    #q7 advice
    if (u_a_q7) >= 3:
        print(
            "#7. It seems that you are or are beginning to move slowly or talk slowly enough that people begin to notice. This can correspond with your sleep or feelings of fatigue. Try your best to get through each day or if needed,find ways to fix your sleeping schedule that best suits you. If you need more energy try to watch funny videos, eat a healthy diet, and surround yourself with loved ones."
        )
        add_space()

    #q8 advice
    if (u_a_q8) >= 3:
        print(
            "#8. It seems that you are being overwhelmed with your emotions. While this may be a tough period or time in your life remember that you are human. Your emotions are completely valid. This can be a result of stress, tramua, grief, or big changes in your life. Talk to someone you trust. Bottling your emotions will only make things worse. Remember that there will always be someone willing to help and listen. "
        )
        add_space()

    #q9 advice
    if (u_a_q9) >= 3:
        print(
            "#9. It seems that you have persistent unwelcome or upsetting thoughts. While it can be hard to make these thoughts go away, distracting yourself can help, but the best thing to do when these thoughts persist is to talk to someone. This can be hard to do at times, but know that there are people who can listen. Find any close friends, family members, or even hotlines that can help."
        )
        add_space()

    #q10 advice
    if (u_a_q10) >= 3:
        print(
            "#10. It seems that you have thoughts surrounding the idea of harming yourself. If you have ANY thoughts of suicide or self harm please talk to a trusted adult or loved one. You should never go through situations like this alone. Talk through your thoughts and problems with someone you trust or seek professional help if things worsen. Just remember: you are never alone and there are always people who can help and listen."
            + color.END)
        add_space()

    add_space()
    #more print statements to clarify use and reliability
    print(
        color.YELLOW +
        """Beam is a subjective app that gives advice based on the information you give us. Some of our advice may or may not help you. Please take what we say with as much reliabilty as you want, but for real and personal guidance through this time, it is best to talk it out with someone you trust and/or surround yourself with those/things that you love. We hoped this self-assessment helped in any way possible. """)
    add_space()

    print(
        color.CYAN +
        "Thank you for participating in this quiz. If did/did not find any of this advice helpful or reassuring please rate us below.")
    add_space()
      #user rates their feedback
    u_app_rating = int(
        input("""Please rate your feedback:
    1: The advice did not help at all and worsened my feelings. 
    2: The advice was not useful and/or did not help. 
    3: The advice was OK and reassured me only a little. 
    4: The advice was good and I feel slightly better/reassured. 
    5: The advice was great and I feel a lot more reassured about what I can do for myself."""))

    user_feedback.append(u_app_rating) 
    add_space()
    add_space()

    #prompts the user if they are done with the assessment they can enter 'done' and it will end
    u_done = input(
        "Enter '1' if you are finished with your assesments. Again, thank you very much for partaking in this quiz and remember: you are never alone. Reach this hotline if needed: 1-800-273-8255."
    )
    add_space()
    if u_done == 1:
        u_done = True
        print(
            "Goodbye! If you would like to take it again, please enter ok once again."
            + color.END)
    else:
        u_done = False
        add_space()
        add_space()
        add_space()
        #restarts program if user wants to take it again
        Beam_Program_Running()

#runs full program
Beam_Program_Running()


