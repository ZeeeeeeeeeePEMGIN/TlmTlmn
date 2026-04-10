import time
import json

lovemeter = 0
code = "0828"

def main_menu():
    print("  _______ _                  _ ")
    print(" |__   __| |                | |")
    print("    | |  | |__   ___ _   _  | | _____   _____   _ __ ___   ___")
    print("    | |  | '_ \\ / _ \\ | | | | |/ _ \\ \\ / / _ \\ | '_ ` _ \\ / _ \\")
    print("    | |  | | | |  __/ |_| | | | (_) \\ V /  __/ | | | | | |  __/_ ")
    print("    |_|  |_| |_|\\___|\\__, | |_|\\___/ \\_/ \\___| |_| |_| |_|\\___( )")
    print("                      __/ |                                   |/")
    print("  _   _              |___/                                               _ ")
    print(" | | | |                | |                                             | |")
    print(" | |_| |__   ___ _   _  | | _____   _____   _ __ ___   ___   _ __   ___ | |_")
    print(" | __| '_ \\ / _ \\ | | | | |/ _ \\ \\ / / _ \\ | '_ ` _ \\ / _ \\ | '_ \\ / _ \\| __|")
    print(" | |_| | | |  __/ |_| | | | (_) \\ V /  __/ | | | | | |  __/ | | | | (_) | |_ _")
    print("  \\__|_| |_|\\___|\\__, | |_|\\___/ \\_/ \\___| |_| |_| |_|\\___| |_| |_|\\___/ \\__(_)")
    print("                  __/ |")
    print("                 |___/")
    time.sleep(1)
    print("=======================================================================================")
    print("A. Start\nB. Locker\nC. Endings\nD. Credits and honorable mentions\nE. Exit")
    print("=======================================================================================")
    time.sleep(1)
    choice = str(input("Where shall I take you? "))

    if choice == "A" or choice == "a":
        main()
    elif choice == "B" or choice == "b":
        next_move = None
        while next_move != "yes" or next_move != "Yes":
            codeguess = input("Enter the 4 number code. ")
            if codeguess == code:
                locker()
            else:
                print("Incorrect. Return to menu?")
                time.sleep(1)
                next_move = input("Yes\tor\tNo\n")
                if next_move == "Yes" or next_move == "yes":
                    main_menu()
    elif choice == "Take me to where they promised.":
        wedsecret()
    elif choice == "C" or choice == "c":
        endings()
    elif choice == "D" or choice == "d":
        creds()
    elif choice  == "E" or choice == "e":
        quit()
    else:
        print("That path does not exist.")
        main_menu()
# Day 1
def scenario1():
    global lovemeter
    print("\nAs you pass by their classroom on the way to your own, your eyes wandered to their figure, sitting down on their seat as usual.\nThey notice you, and you lock eyes...\nA. Wave enthusiastically and give them a soft smile. \nB. Stare at them for a full 5 seconds and wave awkwardly.\nC. Turn away immediately and walk off.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They wave and smile at you back. Both of you enjoyed that interaction.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("They chuckle a bit, and wave back at you.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("They seemed confused and felt a bit hurt from your ignorance.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario1()

def scenario2():
    global lovemeter
    print("\nIt's finally break, and you decide not to leave your classroom. You pull out your phone and your eyes catches the green dot on their profile.\nThey're active! Your heart skips a beat. \nA. Archive them so your heart can rest.\nB. Send them a like emoji without further explanation.\nC. Greet them with a simple 'good morning'.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Your heart seemed to calm down a bit, yet you felt a bit bad for archiving them.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("You didn't know what else to react, so you simply tap on the quick reaction. \nThey later responded with a like emoji as well, and you think it went relatively well?")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("They greet you back and end up texting more before break ends. You think your conversation went well.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario2()

def scenario3():
    global lovemeter
    print("\nLunch has finally arrived and you go down to the canteen, wanting to buy your food. You spot them—surprisingly—alone at a table and without food.\nA. You walk up to them, and ask them 'Do you want to eat lunch together?'\nB. You awkwardly walk up to them, but your brain freezes and you end up not saying ANYTHING and walk off, regretting your life decisions.\nC. You quietly leave their favorite food on their table.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They smile softly at you, and agrees. You end up spending the whole lunch period together.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("They stared at you during that whole sequence of events, and seemed a bit uncomfortable. You feel like you should kill yourself already. ")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("They stare at you once they realize you left their favorite food at their table, and you saw as their face lit up. A well 65 pesos spent. ")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario3()

def scenario4():
    global lovemeter
    global charname
    global username
    print(f"\nIt's finally dismissal and you get to go home! But before you could exit through the gate, a tap on your shoulder.\nIt was {charname}! \"Hey, {username}, wanna maybe... walk together? I've been a bit lonely lately.\"\nA. You nod awkwardly, a sheepish smile on your face.\nB. You accept without hesitation, a bright smile on your face knowing you could spend time with them.\nC. Stare at them for a full minute before accepting.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They smile back at you, and both of you prepare to walk home.")
    elif choice == "B" or choice == "b":
        input("They notice your sudden enthusiasm and chuckle a bit. \n'Let's go then.' They tell you, as your face flush from hearing their voice.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("During the whole time you were staring them, they seemed a bit uncomfortable and kept avoiding your gaze. When you finally agreed, they nodded back awkwardly and mutter, 'Let's.. go then...'.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario4()

def scenario5():
    global lovemeter
    global charname
    print(f"\nWalking beside {charname}, you can't help the fast beating of your heart against your chest. But... the silence was getting a bit awkward.\nA. You decide to begin a conversation, but while they speak, you act rather indifferent.\nB. You begin a conversation, asking about their day and telling jokes, ultimately painting a bright smile on their face.\nC. You begin a conversation, though while telling a joke, you stumble over your words and elicit a soft laugh from {charname}.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They notice your ignorance, and soon stops speaking. The whole walk home turned dead silent, as you regretted acting indifferent earlier and giving dry and quick responses.\nOnce reaching your destination, they give a half-hearted goodbye as you watch them walk away. Your heart feels rather... heavy?")
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        input("The whole walk home, both of you enjoyed each other's presence, cackling about silly jokes and talking as if your normal friends, and you felt as if your face was red the entire time.\nYou finally reached your destination, as you see them with a disappointed expression.\nYou give them a final wave, as they struck you with another sincere smile, waving back.\nYou think you both enjoyed that interaction.")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("Your face becomes flushed from sheer embarrassment, yet seeing them smile makes you forget all about it, laughing with them in the process.\nThe whole walk home felt pretty normal; the conversations sometimes felt awkward, but in a good way.\nYou finally arrive at your destination, and they flash you with their gentle smile.\nYou reciprocate them with a smile of yours and leave.\n You think you both felt it was a pleasant interaction between you both.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario5()
# Day 2
def scenario6():
    global lovemeter
    print("\nYou arrived at school earlier than usual and haven’t seen them in their classroom yet; their seat still left empty.\nA. Steal one of their pens that’s on their table and keep it.\nB. Don’t do anything and just leave.\nc. Leave a small note underneath their desk and quietly leave.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You selfishly grab one of their pens without thought, and keep it for yourself; yet you feel bad for stealing it.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("With nothing to do, you leave their desk be, and dip.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("You quietly sneak a small note underneath their desk, and get butterflies from the thought of them finding and reading it.\nYou leave in hopes they'd see it.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario6()

def scenario7():
    global lovemeter
    print("\nWhile walking with one of your friends, they suddenly nudge you, raising their eyebrows while pointing at your crush.\nAt the sight of them, your heart skips a beat. Suddenly, your friend pushes you towards them.\nA. Use your quick reaction time and dodge quickly, avoiding falling onto them.\nB. Let yourself fall on them, but afterwards apologize profusely.\nC. Pull your friend down as well and end up falling on your crush while being crushed by your friend.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Your crush and yourself were thankfully left unscathed, as you quickly get up and scold your friend, laughing maniacally.\nYou hear them trying to hold back their laugh, as your face flushes from embarrassment. You drag your friend away and finally leave.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("They tell you it's okay and to stop apologizing, for some reason with a bright smile plastered on your face.\nYou nod awkwardly, as you drag your friend away to crash out to them.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("All of you yelled from pain at the same time as your crush and yourself got crushed.\nOnce you got up, you apologized, and you ran from the embarrassment of crushing your crush.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario7()

def scenario8():
    global lovemeter
    print("\nYou’re standing in line to buy food from the canteen, and you realize they're behind you, waiting to buy food as well.\nA. Start a conversation with them.\nB. You begin to sweat profusely and quickly exit the line to spare your racing heart.\nC. You get so nervous that you forget that the line was moving so you end up standing there awkwardly before quickly moving with embarrassment.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("The conversation ends up going well, talking about the usual things friends talk about, as you both was able to soon buy your food without trouble.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("Once you're out of there, you couldn't help but overthink the fact that they may have felt you were ignoring them, since you DID sprint out of there once realizing their presence. ")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("You hear their soft chuckle behind you, as your face flushes once more. After buying your food, you bolt straight out.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario8()

def scenario9():
    global lovemeter
    print("\nYou’re finally back home when you decide to message them, telling them to stay safe while going home.\nAfter you sent it, you patiently waited for their response, but you were still left on delivered despite them being online.\nA. Send another follow-up message, but don’t overthink it.\nB. Delete your message and follow up with a “Never mind”.\nC. Leave the message alone and assume they’re busy.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Because you calmed yourself and your overthinkingness down, \nyou feel that everything is going to be okay and that one message being unread isn't the end of the world.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You regret all your life choices.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("You set your phone aside and simply think they're doing something important and decide to not overthink it that much.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario9()

def scenario10():
    global lovemeter
    print("\nAfter a few hours, they decide to reply to your message, and they ask you how you were doing and how your night was so far.\nA. You keep the conversation flowing however you fumble so bad you end up misspelling most of your messages.\nB. Reply but you think first before sending the message, carefully considering how it would affect this conversation.\nC. Leave them on read because you’re too nervous to reply and because you’re overthinking it too much.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Despite your constant misspelling of words, you think they didn't mind at all, and you even had fun talking to them. As night falls, you eventually tell each other good night.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You ended up texting all night long, as you found out more information about them. You felt warm in the inside knowing you got to spend so much time with them via messaging.")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("Although you felt bad for leaving them on read, you decided to give your heart a break, and slept it off.")
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario10()
# Day 3
def scenario11():
    global lovemeter
    print("\nIt was break time and you decided to take a quick, sneak peek at them in their classroom; however, once you were outside of their room,\nyou realized that they weren’t there at all. You come up with a conclusion that they were absent, worrying you.\nA. Text them asking if they're alright.\nB. Spam message them until break is over, crashing out because they’re absent and you think they’re dead.\nC. Send them a message saying ‘ y r u absent. ‘, thinking that nonchalantness will show you’re not desperate for them.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They text back saying, 'I'm just sick so it's fine'.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("Once they read your messages, they reply to everything, ensuring you they are indeed not dead!")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("They text back saying, 'just sick ig'. It stung you a bit, thinking you might've said the wrong thing.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario11()

def scenario12():
    global lovemeter
    print("\nClass is over and you realize you know their address ( stalker ), you contemplate whether you should go visit them to see if they’re alright,\nand you decide to go! Before going, you decide to buy a few things for them to help them.\nA. Cup noodles and tissue\nB. Chicken broth and medication\nC. E n e r g y  drink 🤪")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Although cup noodles isn't the best for sick people and they most likely have their own tissue at home,\nyou still believe it will make them feel at least a bit better.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("By buying the things a sick person will need, you feel they'll greatly appreciate you for this.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("Even you yourself didn't know why you bought it. Is energy drinks really the best thing to buy for a sick person? \nYou shrug it off, thinking it's probably fine, \nbut you feel they probably won't enjoy an energy drink in their current state very much.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario12()

def scenario13():
    global lovemeter
    print("\nBuying everything you need, you embark on your journey towards their humble abode…\nHowever, you pause in your tracks, trying to remember a crucial detail…?\nA. You dismiss it, and walk straight to their home!\nB. You walk to their home under the excuse of knowing their address from asking their friends.\nC. You remember to text them to ask for their address so you won’t seem like a creep/stalker for knowing where they live.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("Once you arrived, you took a deep breath and knocked on their door, and moments after, they open the door to see you.\nYou get ready to greet them, but was cut off with a 'How do you know where I live?' from them. \nThen dread overwhelms you, realizing what that crucial detail was earlier.\nYou make up some excuse, and they just nod in doubt.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("You arrived at their house, and you take a deep breath before knocking on the door, and moments after, they open it to see you.\nAs you were about to greet them, you were abruptly cut off with a 'How do you know where I live?' from them. \nHowever, you were prepared for this exact situation, telling them you know because of their friends.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("Once they texted you their address, you knew it was safe to approach...You arrived and there they were, waiting and expecting for you!")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario13()

def scenario14():
    global lovemeter
    print("\nThey invite you to their home, grateful that you came by and cared enough about them. They led you into the living room and asked, “How are you?”\nA. Chat with them as you place the things that you brought down on the table and sit on the couch.\nB. Fart and then stare at them awkwardly. \nC. Stiffly sit down on their couch and be super awkward.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You both started chatting and you were relieved seeing them not as sick as you thought.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You both don't say anything for a while, and you felt as if you were dying inside.\nThe silence was then abruptly cut off by them, saying they'll just go grab something in the other room. You regret living.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("They let out a chuckle and say, 'You can relax, make yourself at home.' \nYou feel a bit relieved after that and you both start chatting.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario14()

def scenario15():
    global lovemeter
    print("\nYou decide you’ve stayed for too long and tell them that you’ll be leaving soon.\nA. Get up and pat their head before leaving.\nB. Get up and just leave.\nC. Get up and say bye before leaving.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You noticed they got a bit startled from your sudden action, but they didn't try to reject it or anything. \nThey wave goodbye as they escorted you out, and you feel content as you walked back home.")
        lovemeter = lovemeter + 6
    elif choice == "B" or choice == "b":
        input("You straight up just leave and exit out their door. You hear their voice faintly saying goodbye, and you feel bad for leaving abruptly. \nYou feel as if you made the wrong choice just leaving like that.")
        lovemeter = lovemeter - 3
    elif choice == "C" or choice == "c":
        input("They say wave and say goodbye to you as well, escorting you out their home.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario15()
# Day 4
def scenario16():
    global lovemeter
    print("\nA new day arrives, and as you walk through the gates of the school, you spot them on a bench scrolling through their phone. You didn’t notice that you were already walking towards them.\nToo mesmerized by them, you suddenly realized that you were closer than before, noting how your body moved before you could think.\nA. Sit down and start a conversation, then say bye and leave when classes are about to start.\nB. Sit down then get up and leave.\nC. Sit down and awkwardly greet them 'good morning', then get up and wave bye when classes are about to start.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario16()

def scenario17():
    global lovemeter
    print("\nBreak finally arrived, and you exited the classroom. As you got in line at the canteen, you suddenly got the idea to buy them a snack, and so you did.\nWalking towards their classroom, you take a deep breath and enter the classroom ( YOU SECTION HOPPER ).\n You see them sitting on their table while looking at their phone.\nA. Come up to them and tap their shoulder, and give them the snacks before walk out.\nB. You choose not to approach him and instead throw the snack toward their table then immediately leave.\nC. Come up to them and start a conversation. When break time is almost over, you give them the snacks and wave bye as you leave.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario17()

def scenario18():
    global lovemeter
    print("\nIt’s already lunchtime, and you decided that you didn’t want to eat. You chose to relax near the fountain, and as you get closer to the fountain you notice them sitting down.\nYou decide to sit beside them. As you make yourself comfortable, you put on your earpods and play some music. You then noticed them just staring ahead at nothing.\nYou had a bold decision to give them one of your earpods.\nA. Tap their shoulder and drop the earpod in their hand.\nB. Tap their shoulder and ask, 'Do you wanna listen too?'\nC. Swat away the idea and choose not to give them an earpod.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter -1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario18()

def scenario19():
    global lovemeter
    print("\nThe day is almost over, and you were getting bored during your free time. So you decided to go to the grounds and walk around for a while. You then spot them playing in a volleyball match for their PE. You decide to sit down on a bench and watch them for a while.\nA. Cheer for their team!\nB. Just keep watching intently\nC. Stare straight at them eerily")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("They notice your intense gaze at THEM only and begin to get nervous. They made many mistakes during their game and feel guilty for their team's loss.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario19()

def scenario20():
    global lovemeter
    print("\n#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter + 6
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario20()
# Day 5
def scenario21():
    global lovemeter
    print("\n#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario21()

def scenario22():
    global lovemeter
    print("\n#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario22()

def scenario23():
    global lovemeter
    print("\n#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario23()

def scenario24():
    global lovemeter
    print("\n#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario24()

def scenario25():
    global lovemeter
    print("\nIt’s once again the end of classes, and you exit your classroom. Heading outside, you realize that it’s raining and pull out your umbrella from your bag. Before you could open it and leave, you catch them standing near the entrance, shivering from the cold air. They seemed to not have an umbrella and was waiting for the rain to clear.\nA. Give them your umbrella and accept the fact you’ll just run home drenched.\nB. Walk up to them, offer to share your umbrella, and walk them home.\nC. Look at them for a few seconds and contemplate whether or not to give them your umbrella. You decide not to and leave.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They stare at you for a moment before stopping you, offering to walk home together so you wouldn't get sick.\nYou feel your ears flush as they chuckled at your awkward nod.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario25()
# Day 6
def scenario26():
    global lovemeter
    print("\nIt’s the weekend, and you find yourself bored out of your mind. You grab your phone, and you make a bold decision to start a conversation with them online.\nA. 'good morningg, what are you doing rn?'\nB. 'Morning. What are you doing.'\nC. 'sup bro, whatcha doin’?'")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You feel it's a relatively normal conversation starter and go with it.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You overthink and end up with a way too formal message, yet it's too late to change or delete now.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("You decide on a kind of laid back message to start the conversation, thinking it'll suffice for now.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario26()

def scenario27():
    global lovemeter
    print("\nThey text you back after a couple of minutes, and they reply with a 'good morning', and a 'doing nothing rn, hbu?'\nA. 'nuthin really'\nB. “Nothing.”\nC. 'nothing muchh'")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You give them a chill response you think they'd be happy with.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("After sending it, you realize how ominous it sounds, and you came to regret sending it.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("By adding an extra 'h', you feel like you'll sound less monotonous and that they'd feel more comfortable.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario27()

def scenario28():
    global lovemeter
    print("\nThey leave you on read and you panic a bit. To continue the conversation, you say:\nA. 'Actually, I messaged u cuz I wanted to see if we can hang out together tmr?'\nB. “ya down to hang out tmr bro? Smth casual i dunno”\nC. 'Want to hang out.'")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("To save the dying conversation, you end up casually asking them to hang out tomorrow!")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You feel you're invite to going out tomorrow was too casual.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("What are you? A robot?")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario28()

def scenario29():
    global lovemeter
    print("\nThey reply moments after, saying, 'tomorrow? I’m free so sure'. What do you say after?\nA. 'Okay.'\nB. 'great!'\nC. 'k'")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("It feels a bit monotonous, but it's better than 'k'!")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("You reply with some enthusiasm in order to imply you're happy you both can hang out!")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("You realize how monotonous you are from that one message and regret everything in life.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario29()

def scenario30():
    global lovemeter
    print("\nThey continue talking, saying, 'when and where do you wanna meet up?'. You say: \nA. 'uhhh lunch probs in town'\nB. 'maybeee around lunch at town?'\nC. '12 PM sharp. Town.'")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They reply shortly afterwards with a 'sure then!'")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("They reply shortly afterwards with a 'sure then!'")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("Are you going to assassinate them or something? Because of that they left you on read.")
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario30()
# Day 7
def scenario31():
    global lovemeter
    print("\nToday is the day you and your crush will go out together.\nYou’re unsure whether it’ll be a date or not, but you feel happy knowing you get to spend time with them. What do you wear?\nA. Formal attire\nB. Alpha wolf shirt and some random ahh jeans\nC. Casual attire")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("You're unsure what to wear so you wear your best, formal outfit. \nYou look at yourself in the mirror and think it looks nice, yet feels like it might be too much for a regular outing.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("Putting on whatever your alpha wolf instincts tells you, you look at yourself in the mirror and see the most alpha-est person you've ever seen.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("You wear something casual and fitting for the outing, nothing extraordinary, but you think they'd like it.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario31()

def scenario32():
    global lovemeter
    print("\nAfter getting dressed, you leave momentarily and go towards your designated meet-up spot with them.\nYou start getting butterflies knowing they can arrive any second, and hesitate whether this was a good idea or not, but either way, you know you can’t go back.\nMoments later, they finally arrive. You take a deep breath and say,\nA. Nothing. You say nothing and stare deep into their soul awkwardly.\nB. “You look lovely.”\nC. “You look like shrek.” ")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("'Uhh...hello?' They waved at you several times, as you feel yourself getting more and more flustered. \nYou weren't sure how to act so you just stood still which emitted a soft chuckle out of them. \nYou join them, realizing this isn't that different as the other times you hung out together.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("You could've sworn you saw them get flustered a little, but you decide it was impossible and shrug it off.\nIn response, they compliment you back.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("They stare at you awkwardly for a bit, before laughing it off, yet you could see through their facade. \nYou ended up hurting them a bit from that supposed joke.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario32()

def scenario33():
    global lovemeter
    print("\nThey suggest going to grab a bite to eat since it was already 1 PM. You agree, but you’re unsure where you’re going to take them.\nWhere will you take them to?\nA. Sari sari store\nB. Cafe\nC. Jollibee")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("They give you a skeptical look once you both arrive at a Sari sari store of all places, and they tell you they’ll pick where to eat instead.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("You pick a small, cozy cafe, perfect for casual outings like this that they seem to like as well.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("You pick a rather familiar fast food restaurant, Jollibee, which they didn't mind at all.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario33()

def scenario34():
    global lovemeter
    print("\nYou arrive at the place you’ll eat at. You both order, and while waiting, you decide to break the silence with friendly chatter.\nYour food arrives momentarily, and while eating, you notice a bug on your crush’s cheek.\nA. You brush the back of your hand on their cheek to swat away the bug. \nB. Tell them that there is a bug on their face.\nC. Slap their face where the bug is.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("After realizing your rather bold gesture, you quickly sit back down on your seat and apologize,\nyet when you look back at them, they look as if they're as flustered as you.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("After you told them that, they swatted it away themselves and carry on with eating and chatting.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("After slapping them, they look at you seemingly upset and you apologize over and over, telling them your reason on why you did that.\nThey forgive you, but the entire rest of the conversations felt off. ")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario34()

def scenario35():
    global lovemeter
    print("\nAfter eating, you both decide to take a stroll around town and find a place you think you would both like. \nA. Tap their shoulder and point to the place as you start walking there.\nB. Walk towards the place without notifying them.\nC. Grab their hand and walk towards the place they might like.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("After you notify them, you both head towards a garden you're directing them to, as a final place to end the day. \nYou walked around the garden together, taking pictures of individual flowers, and over all have a chill time with them. \nDuring that stroll, you also find out they really like a peculiar flower, Zinnias.\nThe day soon ends and you both say goodbye. \nTomorrow is the day.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("You were headed towards a garden, when you realize they weren't following behind you. \nYou realized you forgot to notify them to go with you as your phone lights up from a notification. \nThey said they decided to leave since you left them all alone abruptly, and you felt you're chest tightening and suffocating you.. \nYou head to the garden you were supposed to both go to and admire flowers alone. \nTomorrow is the day.")
        lovemeter = lovemeter - 3
    elif choice == "C" or choice == "c":
        input("You make the bold decision to grab their hand, as you head to a garden you thought you'd both like as a final place to end the day. \nYou feel yourself getting more and more flustered, feeling the sensation of their hand, as you both start strolling around the garden together. \nYou admire flowers and plants, still holding their hand, enjoying the time you have left together. \nDuring that stroll, you also find out they really like a peculiar flower, Zinnias. \nThe day soon ends and you both say goodbye. \nTomorrow is the day.")
        lovemeter = lovemeter + 6
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario35()

def final():
    global lovemeter
    global charname
    global username
    print("\nToday is the day. Confession day. You don't know what's going to happen; however you trust in the choices you've made this entire week. \nBefore you go, you realize you should, of course, buy something to give during your confession. \nA. Plushie\nB. Sweets\nC. A bouquet of flowers")
    choice = input("\nWhat do you get them? ")
    if choice == "A" or choice == "a":
        print("A. A fluffy and derpy black cat plushie\nB. A cute blue penguin plushie\nC. A fluffy and cute purple cat plushie\nD. A chonky pufferfish plusie")
        second_choice = input("What kind of plushie do you get them? ")
        if charname == "Lordwyn" or "lordwyn":
            if second_choice == "A" or second_choice == "a":
                lovemeter = lovemeter + 4
            else:
                lovemeter = lovemeter + 2
        elif charname == "Zeryl" or "zeryl":
            if second_choice == "B" or second_choice == "b":
                lovemeter = lovemeter + 4
            else:
                lovemeter = lovemeter + 2
        elif charname == "Krisha" or "krisha":
            if second_choice == "C" or second_choice == "c":
                lovemeter = lovemeter + 4
            else:
                lovemeter = lovemeter + 2
        else:
            if second_choice == "D" or second_choice == "d":
                lovemeter = lovemeter + 4
            else:
                lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        print("\nA. A whole bag of Potchi placed in a black and white box\nB. Packs of dried mangoes placed in a pale green box\nC. Trick question: They don't like sweets---libre them food instead\nD. A box of white chocolates with a blue ribbon tied around it")
        second_choice = input("What kind of sweet do you get them? ")
        if charname == "Lordwyn" or "lordwyn":
            if second_choice == "A" or second_choice == "a":
                lovemeter = lovemeter + 2
            else:
                lovemeter = lovemeter + 1
        elif charname == "Zeryl" or "zeryl":
            if second_choice == "B" or second_choice == "b":
                lovemeter = lovemeter + 2
            else:
                lovemeter = lovemeter + 1
        elif charname == "Krisha" or "krisha":
            if second_choice == "C" or second_choice == "c":
                lovemeter = lovemeter + 2
            else:
                lovemeter = lovemeter + 1
        else:
            if second_choice == "D" or second_choice == "d":
                lovemeter = lovemeter + 2
            else:
                lovemeter = lovemeter + 1
    elif choice == "C" or choice == "c":
        print("\nA. Azaleas \nB. Asters \nC. Roses\nD. Zinnias")
        second_choice = input("What kind of flowers do you get them? ")
        if charname == "Lordwyn" or "lordwyn":
            if second_choice == "A" or second_choice == "a":
                lovemeter = lovemeter + 6
            else:
                lovemeter = lovemeter + 4
        elif charname == "Zeryl" or "zeryl":
            if second_choice == "B" or second_choice == "b":
                lovemeter = lovemeter + 6
            else:
                lovemeter = lovemeter + 4
        elif charname == "Krisha" or "krisha":
            if second_choice == "C" or second_choice == "c":
                lovemeter = lovemeter + 6
            else:
                lovemeter = lovemeter + 4
        else:
            if second_choice == "D" or second_choice == "d":
                lovemeter = lovemeter + 6
            else:
                lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        final()

    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        if lovemeter < 0:
            input("\nThe sunset was beyond you both, its golden rays fell on their perfect face.\nThe air was cold and humid, and you felt yourself shivering, not because of the cold, but because it was time for you to let out the feelings you’ve been meaning to say for a year.\nYou take a deep breath and look at them, staring right back at you expectantly, and there, you pour out everything.\nFrom the day you first fell in love with them, to the week you’ve both spent being together.\nEvery word.\nEvery smile.\nEvery moment.\nEverything.\nAnd finally, you say the three magic words.\n\n“I love you.”\n\n. . .")
            time.sleep(1)
            input("Yet after you said the phrase that’s been eating you up all year,\nyou saw their eyes narrow, as you see them looking at you with pure utter disgust.\nYou could feel their resentment towards you, and you come to regret everything you’ve just said.\nYour chest starts tightening up and your heart starts pounding as if it’s going to flee from your chest at any moment.\nYou panic, stumbling your words, as you decide to just apologize in an attempt to nullify the damage, yet you’re cut off by them.\n\n“How could I ever love someone as horrid as you?”\n\nYou feel yourself collapsing from hearing that sentence, as tears start blurring your image of them.\nYou collapse down on the ground, as you hear the sound of their footsteps fading.\nThey left.\nAnd the vivid image of them staring at you with pure resentment haunts you.\n\nIt feels as if your heart is breaking.\n\nYou clutch on to the gift you were supposed to give them and quietly weep.")
            end1 = "Heartbroken"
            for endings in data:
                endings["ending1"] = "Heartbroken"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print(f"\n{end1} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        elif lovemeter <= 25:
            input(f"\nThe sunset was beyond you and {charname}, as its rays landed on their perfect face, creating a scene that looked straight out of a movie.\nDiverting your eyes away from them, their piercing eyes stare at you expectantly, wondering why you called them here.\nTerrified, you hear the sound of your heart beat ringing in your ears. You couldn’t help but feel afraid.\nHowever, despite your fears and your overwhelming thoughts, you open your mouth and decide to just go for it.\n\nYour story starts on how you initially fell in love with them, and how it grew further and further as the year went by up until the recent week you spent together.\nYou let out everything you’ve kept from them and say everything you’ve been meaning to say all this time.\nAnd tying it all together, you finally say it,\n\n“I love you.”\n\n. . .")
            time.sleep(1)
            input("You unintentionally close your eyes in fear, as dread immediately creeps in.\nYou said it. You said everything you wanted to say after a year of longing.\nYet when you opened your eyes to look at them for the last time, your eyes caught the look of pity in their eyes.\nYour chest tightened and your heart felt like it was crying out seeing that.\nFlinching from them opening their mouth, you hear a sentence you were expecting.\n\n“I’m sorry, but I don’t think I feel the same way.”\n\nWith a sad pitiful look from them, you give {charname} a forced, bittersweet smile, as you hold back tears.\nThey wave you goodbye and leave momentarily, as you return with another goodbye.\n\nMaking sure they left, you collapse on the floor.\nCrying, you clutch on to the gift you were supposed to give them, as a sad, bittersweet feeling lingered in your heart.\nHowever, after every tear in your heart has been wiped away, you get up, and instead of feeling helpless,\nyou look up to the golden, setting sun beyond you.\nWith a deep breath, you compose yourself.\nDespite them not reciprocating your feelings, you’re glad that you still took the chance to confess, and who knows?\nMaybe this fateful encounter was meant to happen, and this was merely character development?\n\nBut whatever it was, at least you tried.")
            end2 = "At least I tried"
            for endings in data:
                endings["ending2"] = "At least I tried"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print(f"\n{end2} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        elif lovemeter <= 60:
            input(f"\nClutching on to the gift you’re going to give them, you wait for {charname} expectantly.\nAfter taking a deep breath, your mind starts compiling everything you were meant to say to them over the past year you’ve liked them.\nFrom the day you first laid your eyes on them, to the week you’ve both spent hanging out together.\nYou begin to think back on the decisions you’ve made this past week and trust yourself that you’ve made the right choices.\nWhatever those decisions were, you knew it was going to significantly impact this moment.\nA few minutes later, and there they were.\nTheir expecting eyes watched you while you attempted to compose yourself.\nAfter another deep breath, everything that was hidden finally poured out like a raging flood.\nThe feelings you’ve kept away.\nThe secrets you’ve held in your heart.\nThe emotions you yourself can’t explain whenever you’re with them.\nYou let it all out. And to tie all you have said together, you uttered the final words,\n\n“I love you.”\n\n. . .")
            time.sleep(1)
            input("\nYou felt a wave of relief at some point. That is, until you looked into their eyes.\nIs it... pity? No, something about the way their gaze locked onto yours felt rather bittersweet.\nSuddenly, you start panicking.\nWas this a mistake?\nShould I have done this?\nWhile you are contemplating everything, your thoughts pause from hearing their soft voice, reaching you amidst your sea of thoughts.\n\n“Look, you're really cool and all, but...”\n\n“To be completely honest, I only see you as a friend.”\n\nYou felt your chest tighten from that sentence alone. It felt as though your heart was slowly and agonizingly cracking. They continue,\n\n“But I hope this won't change anything. So... friends?”\n\nThey say as they offer their hand as a gesture of companionship.\nYou shake their hand and nod, then suddently you feel tears trickle down your cheeks.\nThey pull you into an embrace and begin to comfort you as you quietly weep; they whisper and console you, telling you that everything will be just fine.\nDespite the bittersweet feeling festering within the fathoms of your heart, you chose to accept the fact you will never be anything more than friends.\nYou might not move on or heal for a while,\nyet you know you must keep going forward.")
            end3 = "Just friends"
            for endings in data:
                endings["ending3"] = "Just friends"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print(f"\n{end3} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        elif lovemeter <= 100:
            input("")
            end4 = "Hopeful"
            for endings in data:
                endings["ending4"] = "Hopeful"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print(f"\n{end4} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        elif lovemeter <= 150:
            input(f"\nSitting in your classroom, you await your impending doom as you watch the clock’s hand intensely, anxiously waiting for dismissal.\nYou take a deep breath once again.\nMinutes upon minutes of tirelessly trying to compose yourself were in vain\nas realization that there were only 5 more minutes until the end of classes struck.\nDread begins overwhelming you, as your thoughts begin convincing you to schedule this for another day; the clock then strikes five.\nThe teacher dismisses you, and your hand goes to grab your bag while your other clutched onto the gift.\n\nPlacing your bag down outside of your classroom, you begin readying yourself physically, mentally, and emotionally (and maybe spiritually).\nWhile preparing youself for your impending doom, your eyes wander outside to find them already stationed, waiting at the amphitheater.\n\nHow were they already there??\n\nYou silently curse under your breath, knowing how underprepared you are. However, you know you can’t keep them waiting for too long.\nAfter slowly counting to ten in your head, you begin to walk towards them, your gait so slow it was almost comparable to a toddler.\nHowever, it was a given. You’re planning to confess after a year of yearning.\nA year of hiding your feelings, emotions. And it’s scary.\nBut it was now or never.\nYour mind begins recalling the decisions you’ve made over the past week, and you finally decide that you should stop being a coward,\nand trust the decisions you’ve made.\nWith newfound confidence, you quicken your pace, and your eyes meet.\nImmediately beaming in your presence, they get up to greet you, and your heart feels it's been struck by Cupid's arrow.\nFor a moment, you felt moonstruck, yet shrugged off the feeling since this wasn’t the time for that; it was time to confess.\nDeclaring the feelings you’ve hidden for so long, you begin saying everything you’ve been meaning to say.\nYou don’t care that your voice was shaking, all that mattered was that you were finally saying it.\nYou utter your kept feelings towards them, the reasons why you love them, and the secrets you’ve bottled up for the longest time.\nYou felt yourself running out of breath.\nAnd to wrap up all you've poured out, your speech ends with an awaited phrase,\n\n“I love you.”\n\n. . .")
            time.sleep(1)
            input(f"Your chest tightens; it feels as though something was piercing through your chest.\n\n'Was this a mistake? Maybe I shouldn’t have done this.'\n\nFor a while, {charname} remained quiet, and the silence slowly enveloped the both of you—a far cry from your loud, overthinking thoughts.\nYou hung your head, eyes fixated towards the concrete pavement beneath your feet, not daring to look back up at them.\nMore and more anxious thoughts continued to feed your fear.\nBefore you drown in your sea of thoughts, you hear their voice pull you out of the waters.\n\n“I love you too.”\n\n. . .")
            time.sleep(1)
            input(f"\n\n“What?”\n\n“I said I love you too, {username}.”\n\nThere you looked up at {charname}, their smile clearing every negative thought you’ve had before.\nIt was as if everything got renewed in color again.\nThe sun’s golden rays fell upon both your faces.\nThe flowers beside you felt like they bloomed twice, and for the first time, you felt hopeful rather than uneasy.\nAfter a year of loving, yearning, and longing for them, it finally happened. Something you never thought would happen, happened.\nYou remained speechless. It just felt so... surreal.\nFor a while, you couldn’t help but think this was all another delusion of yours.\nBut you knew it came down to either you accepting this reality, or letting your thoughts twist this into 'just another fantasy'.\nWith eventual confidence, you chose the former.\nDiscarding your previous inner thoughts, you feel... hopeful.\nYou both smile from ear to ear, and even they couldn’t believe it.\n\nAfter dozens of flowers plucked,\n\nhundreds of petals fallen,\nthey love you back.")
            end5 = "Happy"
            for endings in data:
                endings["ending5"] = "Happy"
                with open(filename, 'w') as file:
                    json.dump(data, file)
            time.sleep(4)
            print(f"\n{end5} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        else:
            yansecret()

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def yansecret():
    print("\nsecret scene\nchoiceA\nchoiceB")
    time.sleep(4)
    choice = str(input("\nWhat is your choice? . . . "))

    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        if choice == "A" or choice == "a":
            print("\nObsession scene")
            end6 = "Happy...?"
            for endings in data:
                endings["secretend1"] = "Happy...?"

            with open(filename, 'w') as file:
                json.dump(data, file)

            time.sleep(4)
            print(f"\n{end6} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

        else:
            print("\nbreakup scene")
            end7 = "Won't work out anymore"
            for endings in data:
                endings["secretend2"] = "Won't work out anymore"
            with open(filename, 'w') as file:
                json.dump(data, file)
            time.sleep(4)
            print(f"\n{end7} end.")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def wedsecret():
    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        print("\nwedscene KWBDFBWDFBEWJFDFBDSUBDS")
        end8 = "The future promised"
        for endings in data:
            endings["secretend3"] = "The future promised"
        with open(filename, 'w') as file:
            json.dump(data, file)
        time.sleep(4)
        print(f"\n{end8} end.")
        print("===========================")
        input("Press enter to return to main menu.")
        main_menu()

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def locker():
    choice = input("Go through their locker?\nYes\tor\tNo\n")
    print("===========================")
    if choice == "yes" or choice == "Yes":
        input("You found: Phone!")
        input("You found their phone. Weirdly enough, you knew their password.")
        second_choice = input("Go through it?\nYes\tor\tNo\n")
        print("===========================")
        if second_choice == "yes" or second_choice == "Yes":
            input("You look through a couple selfies, their recent searches, then you entered a notes app.\nWait-- Creator's note??? You open it and see:\n\n===========================\nCreator's note\n\nTell EVEREST to take you to where they promised.\n(hint: EVEREST is the one who asks you what you want to do next.\n===========================")
            input("Um...")
            input("\"Strange,\" you thought. You then heard the bell. \"I should go now...\"\nShutting the locker, you made your way to class.\n")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()
        else:
            input("\"I've already gone through their locker... their phone is a bit of a stretch,\" you told yourself. You put their phone back down and shut the locker.\n")
            print("===========================")
            input("Press enter to return to main menu.")
            main_menu()
    else:
        input("\"This is an invasion of their privacy,\" you thought to yourself. You decide to leave.\n")
        print("===========================")
        input("Press enter to return to main menu.")
        main_menu()

def endings():
    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        for endings in data:
            print(f"Ending 1: {endings["ending1"]}\nEnding 2: {endings["ending2"]}\nEnding 3: {endings["ending3"]}\nEnding 4: {endings["ending4"]}\nEnding 5: {endings["ending5"]}\nEnding 6: {endings["secretend1"]}\nEnding 7: {endings["secretend2"]}\nEnding 8: {endings["secretend3"]}")

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
    input("Press Enter to return to the main menu")
    main_menu()

def creds():
    print("===========================")
    print("They love me... They love me not.\nMade by --- The deluludevs\nDeveloper --- Zeryl Gonadan, Krisha Villa, Lordwyn Demoni\nMain coder --- Zeryl Gonadan\nSecondary coder --- Lordwyn Demoni, Krisha Villa\nStorywriter --- Lordwyn Demoni, Zeryl Gonadan, Krisha Villa\n'SHOUTOUT TO MY (Zeryl) ONE AND ONLY INSPIRATION!!!!!'")
    print("===========================")
    input("Press Enter to return to the main menu.")
    main_menu()

def flower():
    global lovemeter

    if lovemeter < 75:
        print("Pick a flower.")
        print("Press enter to pluck a petal.")
        print("===========================")
        input("They love me...")
        input("They love me not...")
        input("They love me...")
        input("They love me not...")
        input("They love me...")
        input("They love me not.")
        print("===========================")
        input("Press enter to continue.")


    elif lovemeter >= 75:
        print("Pick a flower.")
        print("Press enter to pluck a petal.")
        print("===========================")
        input("They love me...")
        input("They love me not...")
        input("They love me...")
        input("They love me not...")
        input("They love me.")
        print("===========================")
        input("Press enter to continue.")

def main():
    global charname
    global username
    time.sleep(1)
    username = input("What shall we call you? ")
    if username == "Kaye" or username == "kaye":
        print("Welcome to \"They love me, they love me not,\" our beloved teacher!")
    charname = input("What shall 'their' name be? ")
    if charname == "Zeryl" or charname == "zeryl":
        print("Unless ur a certain camia, she wants nothing to do with u /lh")
    elif charname == "Krisha" or charname == "krisha":
        print("Unless ur a fictional character, u better GET OUUUUU--")
    elif charname == "Lordwyn" or charname == "lordwyn":
        print("You must be one shady guy...")
    input(
            "MINOR WARNING!!!\nThis character has their own fixed persona---If you attempt this with your special someone, it's not guaranteed they'll like you back (ehe)")

    input(
            f"\nAugust 21, 20xx. One more week until you finally confess.\n\nIt's been a whole year ever since you first laid your eyes on them...\nYou had enough of watching from afar.. This week.. It's going to be different..!\nYou...\nWill make the first move...")

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 1 ~ *⁠.⁠✧｡⁠☆ ")
    print("===========================")
    time.sleep(1)
    scenario1()
    time.sleep(1)
    scenario2()
    time.sleep(1)
    scenario3()
    time.sleep(1)
    scenario4()
    time.sleep(1)
    scenario5()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 2 ~ *⁠.⁠✧｡⁠☆ ")
    print("===========================")
    time.sleep(1)
    scenario6()
    time.sleep(1)
    scenario7()
    time.sleep(1)
    scenario8()
    time.sleep(1)
    scenario9()
    time.sleep(1)
    scenario10()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 3 ~ *⁠.⁠✧｡⁠☆ ")
    print("===========================")
    time.sleep(1)
    scenario11()
    time.sleep(1)
    scenario12()
    time.sleep(1)
    scenario13()
    time.sleep(1)
    scenario14()
    time.sleep(1)
    scenario15()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~Day 4 ~ *⁠.⁠✧｡⁠☆ ")
    print("===========================")
    time.sleep(1)
    scenario16()
    time.sleep(1)
    scenario17()
    time.sleep(1)
    scenario18()
    time.sleep(1)
    scenario19()
    time.sleep(1)
    scenario20()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 5 ~ *⁠.⁠✧｡⁠☆")
    print("===========================")
    time.sleep(1)
    scenario21()
    time.sleep(1)
    scenario22()
    time.sleep(1)
    scenario23()
    time.sleep(1)
    scenario24()
    time.sleep(1)
    scenario25()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 6 ~ *⁠.⁠✧｡⁠☆")
    print("===========================")
    time.sleep(1)
    scenario26()
    time.sleep(1)
    scenario27()
    time.sleep(1)
    time.sleep(1)
    scenario28()
    time.sleep(1)
    scenario29()
    time.sleep(1)
    scenario30()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("   ☆｡⁠⁠✧.* ~ Day 7 ~ *⁠.⁠✧｡⁠☆")
    print("===========================")
    time.sleep(1)
    scenario31()
    time.sleep(1)
    scenario32()
    time.sleep(1)
    scenario33()
    time.sleep(1)
    scenario34()
    time.sleep(1)
    scenario35()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    flower()

    print("===========================")
    input("     Day of confession.")
    print("===========================")
    time.sleep(1)
    final()
    time.sleep(4)
    creds()
    print("===========================")
    ans = str(input("\t\tRetry?\t\t\nYes\tor\tNo\n  "))
    print("===========================")

    if ans == "Yes":
        main()
    else:
        main_menu()

main_menu()