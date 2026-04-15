import time
import json
import random

lovemeter = 0
code = "0828"

def main_menu():
    print("=======================================================================================")
    print("╔╦╗┬ ┬┌─┐┬ ┬  ┬  ┌─┐┬  ┬┌─┐  ┌┬┐┌─┐   ╔╦╗┬ ┬┌─┐┬ ┬  ┬  ┌─┐┬  ┬┌─┐  ┌┬┐┌─┐  ┌┐┌┌─┐┌┬┐")
    print(" ║ ├─┤├┤ └┬┘  │  │ │└┐┌┘├┤   │││├┤     ║ ├─┤├┤ └┬┘  │  │ │└┐┌┘├┤   │││├┤   ││││ │ │ ")
    print(" ╩ ┴ ┴└─┘ ┴   ┴─┘└─┘ └┘ └─┘  ┴ ┴└─┘┘   ╩ ┴ ┴└─┘ ┴   ┴─┘└─┘ └┘ └─┘  ┴ ┴└─┘  ┘└┘└─┘ ┴o")
    print("=======================================================================================")
    time.sleep(1)
    print("A. Start\nB. Locker\nC. Endings\nD. Credits and honorable mentions\nE. Mini games\nF. Exit")
    print("=======================================================================================")
    time.sleep(1)
    choice = str(input("~ Where shall I take you? "))

    if choice == "A" or choice == "a":
        main()
    elif choice == "B" or choice == "b":
        next_move = None
        while next_move != "yes" or next_move != "Yes":
            print("=======================================================================================")
            print("╦ ╦┌┐┌┌─┐┬ ┬┌┐┌┌─┐┌┬┐  ┬  ┌─┐┌─┐┬┌─┌─┐┬─┐")
            print("║ ║││││ │││││││├┤  ││  │  │ ││  ├┴┐├┤ ├┬┘")
            print("╚═╝┘└┘└─┘└┴┘┘└┘└─┘─┴┘  ┴─┘└─┘└─┘┴ ┴└─┘┴└─")
            print("=======================================================================================")
            time.sleep(1)
            codeguess = input("~ Enter the 4 number code. ")
            if codeguess == code:
                locker()
            else:
                print("=======================================================================================")
                print("~ Incorrect. Return to menu?")
                time.sleep(1)
                next_move = input("Yes\tor\tNo\nNext move: ")
                if next_move == "Yes" or next_move == "yes":
                    main_menu()
    elif choice == "To where they promised.":
        wedsecret()
    elif choice == "C" or choice == "c":
        endings()
    elif choice == "D" or choice == "d":
        creds()
    elif choice == "E" or choice == "e":
        mini_games()
    elif choice == "F" or choice == "f":
        print("=======================================================================================")
        print("╔═╗┌─┐┌┬┐┌─┐  ╔═╗┬  ┌─┐┌─┐┬┌┐┌┌─┐   ")
        print("║ ╦├─┤│││├┤   ║  │  │ │└─┐│││││ ┬   ")
        print("╚═╝┴ ┴┴ ┴└─┘  ╚═╝┴─┘└─┘└─┘┴┘└┘└─┘ooo")
        print("=======================================================================================")
        time.sleep(3)
        quit()
    else:
        print("~ That path does not exist.")
        main_menu()
# Day 1 - The walk home with you
def scenario1():
    global lovemeter
    print("\n❀࿐ As you pass by their classroom on the way to your own, your eyes wandered to their figure, sitting down on their seat as usual.\nThey notice you, and you lock eyes...\nA. Wave enthusiastically and give them a soft smile. \nB. Stare at them for a full 5 seconds and wave awkwardly.\nC. Turn away immediately and walk off.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They wave and smile at you back. Both of you enjoyed that interaction.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ They chuckle a bit, and wave back at you.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ They seemed confused and felt a bit hurt from your ignorance.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario1()

def scenario2():
    global lovemeter
    print("\n❀࿐ It's finally break, and you decide not to leave your classroom. You pull out your phone and your eyes catches the green dot on their profile.\nThey're active! Your heart skips a beat. \nA. Archive them so your heart can rest.\nB. Send them a like emoji without further explanation.\nC. Greet them with a simple 'good morning'.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Your heart seemed to calm down a bit, yet you felt a bit bad for archiving them.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("❀࿐ You didn't know what else to react, so you simply tap on the quick reaction. \nThey later responded with a like emoji as well, and you think it went relatively well?")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ They greet you back and end up texting more before break ends. You think your conversation went well.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario2()

def scenario3():
    global lovemeter
    print("\n❀࿐ Lunch has finally arrived and you go down to the canteen, wanting to buy your food. You spot them—surprisingly—alone at a table and without food.\nA. You walk up to them, and ask them 'Do you want to eat lunch together?'\nB. You awkwardly walk up to them, but your brain freezes and you end up not saying ANYTHING and walk off, regretting your life decisions.\nC. You quietly leave their favorite food on their table.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They smile softly at you, and agrees. You end up spending the whole lunch period together.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ They stared at you during that whole sequence of events, and seemed a bit uncomfortable. You feel like you should kill yourself already. ")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ They stare at you once they realize you left their favorite food at their table, and you saw as their face lit up. A well 65 pesos spent. ")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario3()

def scenario4():
    global lovemeter
    global charname
    global username
    print(f"\n❀࿐ It's finally dismissal and you get to go home! But before you could exit through the gate, a tap on your shoulder.\nIt was {charname}! \"Hey, {username}, wanna maybe... walk together? I've been a bit lonely lately.\"\nA. You nod awkwardly, a sheepish smile on your face.\nB. You accept without hesitation, a bright smile on your face knowing you could spend time with them.\nC. Stare at them for a full minute before accepting.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They smile back at you, and both of you prepare to walk home.")
    elif choice == "B" or choice == "b":
        input("❀࿐ They notice your sudden enthusiasm and chuckle a bit. \n'Let's go then.' They tell you, as your face flush from hearing their voice.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ During the whole time you were staring them, they seemed a bit uncomfortable and kept avoiding your gaze. When you finally agreed, they nodded back awkwardly and mutter, 'Let's.. go then...'.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario4()

def scenario5():
    global lovemeter
    global charname
    print(f"\n❀࿐ Walking beside {charname}, you can't help the fast beating of your heart against your chest. But... the silence was getting a bit awkward.\nA. You decide to begin a conversation, but while they speak, you act rather indifferent.\nB. You begin a conversation, asking about their day and telling jokes, ultimately painting a bright smile on their face.\nC. You begin a conversation, though while telling a joke, you stumble over your words and elicit a soft laugh from {charname}.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They notice your ignorance, and soon stops speaking. The whole walk home turned dead silent, as you regretted acting indifferent earlier and giving dry and quick responses.\nOnce reaching your destination, they give a half-hearted goodbye as you watch them walk away. Your heart feels rather... heavy?")
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        input("❀࿐ The whole walk home, both of you enjoyed each other's presence, cackling about silly jokes and talking as if your normal friends, and you felt as if your face was red the entire time.\nYou finally reached your destination, as you see them with a disappointed expression.\nYou give them a final wave, as they struck you with another sincere smile, waving back.\nYou think you both enjoyed that interaction.")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("❀࿐ Your face becomes flushed from sheer embarrassment, yet seeing them smile makes you forget all about it, laughing with them in the process.\nThe whole walk home felt pretty normal; the conversations sometimes felt awkward, but in a good way.\nYou finally arrive at your destination, and they flash you with their gentle smile.\nYou reciprocate them with a smile of yours and leave.\n You think you both felt it was a pleasant interaction between you both.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario5()
# Day 2 - Late night chats
def scenario6():
    global lovemeter
    print("\n❀࿐ You arrived at school earlier than usual and haven’t seen them in their classroom yet; their seat still left empty.\nA. Steal one of their pens that’s on their table and keep it.\nB. Don’t do anything and just leave.\nc. Leave a small note underneath their desk and quietly leave.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You selfishly grab one of their pens without thought, and keep it for yourself; yet you feel bad for stealing it.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("❀࿐ With nothing to do, you leave their desk be, and dip.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ You quietly sneak a small note underneath their desk, and get butterflies from the thought of them finding and reading it.\nYou leave in hopes they'd see it.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario6()

def scenario7():
    global lovemeter
    print("\n❀࿐ While walking with one of your friends, they suddenly nudge you, raising their eyebrows while pointing at your crush.\nAt the sight of them, your heart skips a beat. Suddenly, your friend pushes you towards them.\nA. Use your quick reaction time and dodge quickly, avoiding falling onto them.\nB. Let yourself fall on them, but afterwards apologize profusely.\nC. Pull your friend down as well and end up falling on your crush while being crushed by your friend.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Your crush and yourself were thankfully left unscathed, as you quickly get up and scold your friend, laughing maniacally.\nYou hear them trying to hold back their laugh, as your face flushes from embarrassment. You drag your friend away and finally leave.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ They tell you it's okay and to stop apologizing, for some reason with a bright smile plastered on your face.\nYou nod awkwardly, as you drag your friend away to crash out to them.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ All of you yelled from pain at the same time as your crush and yourself got crushed.\nOnce you got up, you apologized, and you ran from the embarrassment of crushing your crush.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario7()

def scenario8():
    global lovemeter
    print("\n❀࿐ You’re standing in line to buy food from the canteen, and you realize they're behind you, waiting to buy food as well.\nA. Start a conversation with them.\nB. You begin to sweat profusely and quickly exit the line to spare your racing heart.\nC. You get so nervous that you forget that the line was moving so you end up standing there awkwardly before quickly moving with embarrassment.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ The conversation ends up going well, talking about the usual things friends talk about, as you both was able to soon buy your food without trouble.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ Once you're out of there, you couldn't help but overthink the fact that they may have felt you were ignoring them, since you DID sprint out of there once realizing their presence. ")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ You hear their soft chuckle behind you, as your face flushes once more. After buying your food, you bolt straight out.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario8()

def scenario9():
    global lovemeter
    print("\n❀࿐ You’re finally back home when you decide to message them, telling them to stay safe while going home.\nAfter you sent it, you patiently waited for their response, but you were still left on delivered despite them being online.\nA. Send another follow-up message, but don’t overthink it.\nB. Delete your message and follow up with a “Never mind”.\nC. Leave the message alone and assume they’re busy.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Because you calmed yourself and your overthinkingness down, \nyou feel that everything is going to be okay and that one message being unread isn't the end of the world.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You regret all your life choices.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ You set your phone aside and simply think they're doing something important and decide to not overthink it that much.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario9()

def scenario10():
    global lovemeter
    print("\n❀࿐ After a few hours, they decide to reply to your message, and they ask you how you were doing and how your night was so far.\nA. You keep the conversation flowing however you fumble so bad you end up misspelling most of your messages.\nB. Reply but you think first before sending the message, carefully considering how it would affect this conversation.\nC. Leave them on read because you’re too nervous to reply and because you’re overthinking it too much.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Despite your constant misspelling of words, you think they didn't mind at all, and you even had fun talking to them. As night falls, you eventually tell each other good night.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You ended up texting all night long, as you found out more information about them. You felt warm in the inside knowing you got to spend so much time with them via messaging.")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("❀࿐ Although you felt bad for leaving them on read, you decided to give your heart a break, and slept it off.")
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario10()
# Day 3 - Sick day
def scenario11():
    global lovemeter
    print("\n❀࿐ It was break time and you decided to take a quick, sneak peek at them in their classroom; however, once you were outside of their room,\nyou realized that they weren’t there at all. You come up with a conclusion that they were absent, worrying you.\nA. Text them asking if they're alright.\nB. Spam message them until break is over, crashing out because they’re absent and you think they’re dead.\nC. Send them a message saying ‘ y r u absent. ‘, thinking that nonchalantness will show you’re not desperate for them.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They text back saying, 'I'm just sick so it's fine'.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ Once they read your messages, they reply to everything, ensuring you they are indeed not dead!")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ They text back saying, 'just sick ig'. It stung you a bit, thinking you might've said the wrong thing.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario11()

def scenario12():
    global lovemeter
    print("\n❀࿐ Class is over and you realize you know their address ( stalker ), you contemplate whether you should go visit them to see if they’re alright,\nand you decide to go! Before going, you decide to buy a few things for them to help them.\nA. Cup noodles and tissue\nB. Chicken broth and medication\nC. E n e r g y  drink 🤪")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Although cup noodles isn't the best for sick people and they most likely have their own tissue at home,\nyou still believe it will make them feel at least a bit better.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ By buying the things a sick person will need, you feel they'll greatly appreciate you for this.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ Even you yourself didn't know why you bought it. Is energy drinks really the best thing to buy for a sick person? \nYou shrug it off, thinking it's probably fine, \nbut you feel they probably won't enjoy an energy drink in their current state very much.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario12()

def scenario13():
    global lovemeter
    print("\n❀࿐ Buying everything you need, you embark on your journey towards their humble abode…\nHowever, you pause in your tracks, trying to remember a crucial detail…?\nA. You dismiss it, and walk straight to their home!\nB. You walk to their home under the excuse of knowing their address from asking their friends.\nC. You remember to text them to ask for their address so you won’t seem like a creep/stalker for knowing where they live.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ Once you arrived, you took a deep breath and knocked on their door, and moments after, they open the door to see you.\nYou get ready to greet them, but was cut off with a 'How do you know where I live?' from them. \nThen dread overwhelms you, realizing what that crucial detail was earlier.\nYou make up some excuse, and they just nod in doubt.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("❀࿐ You arrived at their house, and you take a deep breath before knocking on the door, and moments after, they open it to see you.\nAs you were about to greet them, you were abruptly cut off with a 'How do you know where I live?' from them. \nHowever, you were prepared for this exact situation, telling them you know because of their friends.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ Once they texted you their address, you knew it was safe to approach...You arrived and there they were, waiting and expecting for you!")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario13()

def scenario14():
    global lovemeter
    print("\n❀࿐ They invite you to their home, grateful that you came by and cared enough about them. They led you into the living room and asked, “How are you?”\nA. Chat with them as you place the things that you brought down on the table and sit on the couch.\nB. Fart and then stare at them awkwardly. \nC. Stiffly sit down on their couch and be super awkward.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You both started chatting and you were relieved seeing them not as sick as you thought.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You both don't say anything for a while, and you felt as if you were dying inside.\nThe silence was then abruptly cut off by them, saying they'll just go grab something in the other room. You regret living.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ They let out a chuckle and say, 'You can relax, make yourself at home.' \nYou feel a bit relieved after that and you both start chatting.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario14()

def scenario15():
    global lovemeter
    print("\n❀࿐ You decide you’ve stayed for too long and tell them that you’ll be leaving soon.\nA. Get up and pat their head before leaving.\nB. Get up and just leave.\nC. Get up and say bye before leaving.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You noticed they got a bit startled from your sudden action, but they didn't try to reject it or anything. \nThey wave goodbye as they escorted you out, and you feel content as you walked back home.")
        lovemeter = lovemeter + 6
    elif choice == "B" or choice == "b":
        input("❀࿐ You straight up just leave and exit out their door. You hear their voice faintly saying goodbye, and you feel bad for leaving abruptly. \nYou feel as if you made the wrong choice just leaving like that.")
        lovemeter = lovemeter - 3
    elif choice == "C" or choice == "c":
        input("❀࿐ They say wave and say goodbye to you as well, escorting you out their home.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario15()
# Day 4 - Just a normal school day
def scenario16():
    global lovemeter
    print("\n❀࿐ A new day arrives, and as you walk through the gates of the school, you spot them on a bench scrolling through their phone. You didn’t notice that you were already walking towards them.\nToo mesmerized by them, you suddenly realized that you were closer than before, noting how your body moved before you could think.\nA. Sit down and start a conversation, then say bye and leave when classes are about to start.\nB. Sit down then get up and leave.\nC. Sit down and awkwardly greet them 'good morning', then get up and wave bye when classes are about to start.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You feel content knowing you both can talk naturally to each other!")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ Their confused gaze stare at your back, dashing away from embarrassment.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ They cooly reply with a 'Good morning to you too', and you cry internally because they seem so cool and you're just a tomato. :(")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario16()

def scenario17():
    global lovemeter
    print("\n❀࿐ Break finally arrived, and you exited the classroom. As you got in line at the canteen, you suddenly got the idea to buy them a snack, and so you did!\nWalking towards their classroom, you take a deep breath and enter the classroom ( YOU SECTION HOPPER ).\n You see them sitting on their table while looking at their phone.\nA. Come up to them and tap their shoulder, and give them the snacks before walking out.\nB. You choose not to approach them and instead throw the snack toward their table then immediately leave.\nC. Come up to them and start a conversation. When break time is almost over, you give them the snacks and wave bye as you leave.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They seemed grateful, but before they could say thank you, you nervously left.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        print("❀࿐ You quickly left and didn't turn back, but you felt oddly bad.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        print("❀࿐ They seemed to enjoy your conversation, and was grateful for the snacks.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario17()

def scenario18():
    global lovemeter
    print("\n❀࿐ It’s already lunchtime, and you decide that you don't want to eat. You chose to relax near the fountain, and as you get closer to the fountain you notice them sitting down.\nYou decide to sit beside them. As you make yourself comfortable, you put on your earpods and play some music. You then noticed them just staring ahead at nothing.\nYou had a bold decision to give them one of your earpods.\nA. Tap their shoulder and drop the earpod in their hand.\nB. Tap their shoulder and ask, 'Wanna listen to something while you zone out there?'\nC. Toss the earpod into their lap and hope that they catch it.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They blinked, looking down at the earpod in their hand. With a soft smile on their face, they accepted the earpod and put it in their ear.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        print("❀࿐ They perked up at the mention of music. They huffed at your remark, yet accepted the earpod anyway.\nThey seemed to be ever so slightly happier.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        print("❀࿐ They raised a brow as they felt a small object land on his lap. He quietly accepted the earpod after asking you about it.\nHe didn't seem to like that you just tossed it at him.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario18()

def scenario19():
    global lovemeter
    global username
    print("\n❀࿐ While listening to music, you remember that they had been sick yesterday. Recalling the events that took place the other day, you decided to ask them how they were doing.\nA. 'How are you feeling.'\nB. 'So uh... H-how're you doing?'\nC. 'Hey, uh... Are you feeling better now?'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ 'Much better,' they replied. 'Thanks for... asking?' They weren't sure if your statement was even a question,\nbut they appreciated your concern regardless.")
        lovemeter = lovemeter + 1
    elif choice == "B" or choice == "b":
        print("❀࿐ 'I'm doing alright,' they replied. They smiled wider at your awkwardness, seeming to find it amusing.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        print(f"❀࿐ They nod, a small smirk on their face as they teased, 'I feel much better now. It's all thanks to you, Dr. {username}'.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario19()

def scenario20():
    global lovemeter
    print("\n❀࿐ The day is almost over, and you were getting bored during your free time. So you decided to go to the grounds and walk around for a while. You then spot them playing in a volleyball match for their PE. You decide to sit down on a bench and watch them for a while.\nA. Cheer for their team!\nB. Just keep watching intently\nC. Stare straight at them eerily")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They seemed to perk up at you cheering for their team despite everyone else cheering for the opposing team.\nMotivated, they ended up carrying their team to victory!")
        lovemeter = lovemeter + 6
    elif choice == "B" or choice == "b":
        print("❀࿐ You had fun watching their game, and while they didn't win, they seemed like they genuinely had fun.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ They notice your intense gaze at THEM only and begin to get nervous. They made many mistakes during their game and feel guilty for their team's loss.")
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario20()
# Day 5 - library hangout
def scenario21():
    global lovemeter
    print("\n❀࿐ It is now afternoon. After finishing your club activities, you decide to hang out in the library to continue reading the new book you bought! While writing your name in the logbook, you catch them standing in line behind you. They smile and greet you when as you lock eyes.\nA. You quickly turn your head and ignore them.\nB. You greet them back, albeit shyly.\nC. Caught off guard, you greet them nervously, stumbling over your words.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They seem hurt at being ignored. You feel terrible :(")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        print("❀࿐ They smile cooly at your reply, nodding in acknowledgement.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        print("❀࿐ They chuckle softly at your nervous, stuttered reply.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario21()

def scenario22():
    global lovemeter
    print("\n❀࿐ You take a seat in the library and begin to read the book. Deeply invested in the book, you didn't notice that they took a seat beside you.\nThey suddenly lean over with intrigue and ask, 'What are you reading?'\nA. 'None of your business.'\nB. Start yapping about the book you got with the passion of a sailor.\nC. 'Oh, it's one of my favorites, [insert book name]'.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They blink, retracting as they murmur under their breath, 'just asking...' They didn't seem to enjoy that exchange.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        print("❀࿐ Despite being caught off guard by your sudden yapping sesh, they chuckle and listen intently.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        print("❀࿐ 'Is it good?' They ask, clearly interested. You begin to tell them small details about the story.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario22()

def scenario23():
    global lovemeter
    if lovemeter >= 60:
        print("\n❀࿐ After a long moment of silence, they begin eating a small snack. You them remember that you haven't eaten lunch yet and suddenly, you feel hungry.\nThey glance at you, noticing your hunger, and offer to give you a snack.\nA. Nod shyly and accept their offer.\nB. Accept their offer with a bright smile on your face.\nC. Stare at them in silence for a moment before awkwardly nodding.")
        time.sleep(1)
        choice = str(input("~ What do you do? "))

        if choice == "A" or choice == "a":
            print("❀࿐ They slide the other snack towards you, watching with a smile as you gingerly accept it.")
            lovemeter = lovemeter + 2
        elif choice == "B" or choice == "b":
            print("❀࿐  They slide the other snack towards you, a small smile on their face as you begin munching happily.")
            lovemeter = lovemeter + 4
        elif choice == "C" or choice == "c":
            print("❀࿐ They seemed somewhat amused at your awkward reply and slide the snack towards you.")
            lovemeter = lovemeter + 1
        else:
            input("Please choose an existing option. (Enter to continue.)")
            scenario23()

    elif lovemeter < 60:
        print("\n❀࿐ After a long moment of silence, they slide your favorite snack towards you. They seemed to be initiating a lot today...\nA. Ask, 'For me?' and then take the snack.\nB. Ask, 'Is this for me?' and follow up with, 'How'd you know this is my fav snack?'\nC. Don't take the snack because what if they just put it there and it's for them. :( ( you overthinker )")
        time.sleep(1)
        choice = str(input("~ What do you do? "))

        if choice == "A" or choice == "a":
            print("❀࿐ They nod at your question. A smile graces their face as they notice your grateful expression.")
            lovemeter = lovemeter + 2
        elif choice == "B" or choice == "b":
            print("❀࿐ They nod at your question. They seemed to tense up when you asked them the second question.\nThey laughed nervously and said, 'Lucky guess.'")
            lovemeter = lovemeter + 4
        elif choice == "C" or choice == "c":
            print("❀࿐ They keep glancing at you, wondering why you're not taking the snack. 'It's for you,' they eventually say with a small smile.\n'Me?' You ask before you quietly take the snack, grateful.")
            lovemeter = lovemeter + 1
        else:
            input("Please choose an existing option. (Enter to continue.)")
            scenario23()

def scenario24():
    global lovemeter
    print("\n❀࿐ As you neared the end of your book, you decide that you should wrap up your reading session for today.\nIt seems that they were gonna stay here a little longer to read...\nA. Shyly wave goodbye to them.\nB. Leave without saying anything.\nC. Before leaving, tell them 'bye bye' and wave to them as you walk out.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        print("❀࿐ They smile and wave back at you as you leave.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        print("❀࿐ They look up as you walk off, giving you a small unreciprocated wave.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        print("❀࿐ They reply with a 'goodbye' and wave back with a smile.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario24()

def scenario25():
    global lovemeter
    print("\n❀࿐ It’s once again the end of classes, and you exit your classroom. Heading outside, you realize that it’s raining and pull out your umbrella from your bag. Before you could open it and leave, you catch them standing near the entrance, shivering from the cold air. They seemed to not have an umbrella and was waiting for the rain to clear.\nA. Give them your umbrella and accept the fact you’ll just run home drenched.\nB. Walk up to them, offer to share your umbrella, and walk them home.\nC. Walk up to them and contemplate whether or not to give them your umbrella. You decide not to and leave.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They stare at you for a moment before stopping you, offering to walk home together so you wouldn't get sick.\nYou feel your ears flush as they chuckle at your awkward nod.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print("❀࿐ As you offer to share your umbrella, they smile in relief. The two of you talk on the way home, and you couldn't help but feel like they seemed content. This interaction ended up keeping you up at night.")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        print("❀࿐ They seem to perk up as you approach them, but when you suddenly turn away, a sense of false hope washes over them.\nFor a second, they thought you would share your umbrella. They guessed wrong.")
        lovemeter = lovemeter - 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario25()
# Day 6 - Operation: Get them to hang out with me!
def scenario26():
    global lovemeter
    print("\n❀࿐ It’s the weekend, and you find yourself bored out of your mind. You grab your phone, and you make a bold decision to start a conversation with them online.\nA. 'good morningg, what are you doing rn?'\nB. 'Morning. What are you doing.'\nC. 'sup bro, whatcha doin’?'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You feel it's a relatively normal conversation starter and go with it.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You overthink and end up with a way too formal message, yet it's too late to change or delete now.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ You decide on a kind of laid back message to start the conversation, thinking it'll suffice for now.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario26()

def scenario27():
    global lovemeter
    print("\n❀࿐ They text you back after a couple of minutes, and they reply with a 'good morning', and a 'doing nothing rn, hbu?'\nA. 'nuthin really'\nB. “Nothing.”\nC. 'nothing muchh'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You give them a chill response you think they'd be happy with.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ After sending it, you realize how ominous it sounds, and you came to regret sending it.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ By adding an extra 'h', you feel like you'll sound less monotonous and that they'd feel more comfortable.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario27()

def scenario28():
    global lovemeter
    print("\n❀࿐ They leave you on read and you panic a bit. To continue the conversation, you say:\nA. 'Actually, I messaged u cuz I wanted to see if we can hang out together tmr?'\nB. “ya down to hang out tmr bro? Smth casual i dunno”\nC. 'Want to hang out.'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ To save the dying conversation, you end up casually asking them to hang out tomorrow!")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You feel you're invite to going out tomorrow was too casual.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ What are you? A robot?")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario28()

def scenario29():
    global lovemeter
    print("\n❀࿐ They reply moments after, saying, 'tomorrow? I’m free so sure'. What do you say after?\nA. 'Okay.'\nB. 'great!'\nC. 'k'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ It feels a bit monotonous, but it's better than 'k'!")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ You reply with some enthusiasm in order to imply you're happy you both can hang out!")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ You realize how monotonous you are from that one message and regret everything in life.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario29()

def scenario30():
    global lovemeter
    print("\n❀࿐ They continue talking, saying, 'when and where do you wanna meet up?'. You say: \nA. 'uhhh lunch probs in town'\nB. 'maybeee around lunch at town?'\nC. '12 PM sharp. Town.'")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They reply shortly afterwards with a 'sure then!'")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ They reply shortly afterwards with a 'sure then!'")
        lovemeter = lovemeter + 6
    elif choice == "C" or choice == "c":
        input("❀࿐ Are you going to assassinate them or something? Because of that they left you on read.")
        lovemeter = lovemeter - 3
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario30()
# Day 7 - Our date-- I mean, hangout!
def scenario31():
    global lovemeter
    print("\n❀࿐ Today is the day you and your crush will go out together.\nYou’re unsure whether it’ll be a date or not, but you feel happy knowing you get to spend time with them. What do you wear?\nA. Formal attire\nB. Alpha wolf shirt and some random ahh jeans\nC. Casual attire")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ You're unsure what to wear so you wear your best, formal outfit. \nYou look at yourself in the mirror and think it looks nice, yet feels like it might be too much for a regular outing.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ Putting on whatever your alpha wolf instincts tells you, you look at yourself in the mirror and see the most alpha-est person you've ever seen.")
        lovemeter = lovemeter - 1
    elif choice == "C" or choice == "c":
        input("❀࿐ You wear something casual and fitting for the outing, nothing extraordinary, but you think they'd like it.")
        lovemeter = lovemeter + 4
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario31()

def scenario32():
    global lovemeter
    print("\n❀࿐ After getting dressed, you leave momentarily and go towards your designated meet-up spot with them.\nYou start getting butterflies knowing they can arrive any second, and hesitate whether this was a good idea or not, but either way, you know you can’t go back.\nMoments later, they finally arrive. You take a deep breath and say,\nA. Nothing. You say nothing and stare deep into their soul awkwardly.\nB. “You look lovely.”\nC. “You look like shrek.” ")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ 'Uhh...hello?' They waved at you several times, as you feel yourself getting more and more flustered. \nYou weren't sure how to act so you just stood still which emitted a soft chuckle out of them. \nYou join them, realizing this isn't that different as the other times you hung out together.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        input("❀࿐ You could've sworn you saw them get flustered a little, but you decide it was impossible and shrug it off.\nIn response, they compliment you back.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ They stare at you awkwardly for a bit, before laughing it off, yet you could see through their facade. \nYou ended up hurting them a bit from that supposed joke.")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario32()

def scenario33():
    global lovemeter
    print("\n❀࿐ They suggest going to grab a bite to eat since it was already 1 PM. You agree, but you’re unsure where you’re going to take them.\nWhere will you take them to?\nA. Sari sari store\nB. Cafe\nC. Jollibee")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ They give you a skeptical look once you both arrive at a Sari sari store of all places, and they tell you they’ll pick where to eat instead.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        input("❀࿐ You pick a small, cozy cafe, perfect for casual outings like this that they seem to like as well.")
        lovemeter = lovemeter + 4
    elif choice == "C" or choice == "c":
        input("❀࿐ You pick a rather familiar fast food restaurant, Jollibee, which they didn't mind at all.")
        lovemeter = lovemeter + 2
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario33()

def scenario34():
    global lovemeter
    print("\n❀࿐ You arrive at the place you’ll eat at. You both order, and while waiting, you decide to break the silence with friendly chatter.\nYour food arrives momentarily, and while eating, you notice a bug on your crush’s cheek.\nA. You brush the back of your hand on their cheek to swat away the bug. \nB. Tell them that there is a bug on their face.\nC. Slap their face where the bug is.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ After realizing your rather bold gesture, you quickly sit back down on your seat and apologize,\nyet when you look back at them, they look as if they're as flustered as you.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ After you told them that, they swatted it away themselves and carry on with eating and chatting.")
        lovemeter = lovemeter + 2
    elif choice == "C" or choice == "c":
        input("❀࿐ After slapping them, they look at you seemingly upset and you apologize over and over, telling them your reason on why you did that.\nThey forgive you, but the entire rest of the conversations felt off. ")
        lovemeter = lovemeter - 1
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario34()

def scenario35():
    global lovemeter
    print("\n❀࿐ After eating, you both decide to take a stroll around town and find a place you think you would both like. \nA. Tap their shoulder and point to the place as you start walking there.\nB. Walk towards the place without notifying them.\nC. Grab their hand and walk towards the place they might like.")
    time.sleep(1)
    choice = str(input("~ What do you do? "))

    if choice == "A" or choice == "a":
        input("❀࿐ After you notify them, you both head towards a garden you're directing them to, as a final place to end the day. \nYou walked around the garden together, taking pictures of individual flowers, and over all have a chill time with them. \nDuring that stroll, you also find out they really like a peculiar flower, Zinnias.\nThe day soon ends and you both say goodbye. \nTomorrow is the day.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        input("❀࿐ You were headed towards a garden, when you realize they weren't following behind you. \nYou realized you forgot to notify them to go with you as your phone lights up from a notification. \nThey said they decided to leave since you left them all alone abruptly, and you felt you're chest tightening and suffocating you.. \nYou head to the garden you were supposed to both go to and admire flowers alone. \nTomorrow is the day.")
        lovemeter = lovemeter - 3
    elif choice == "C" or choice == "c":
        input("❀࿐ You make the bold decision to grab their hand, as you head to a garden you thought you'd both like as a final place to end the day. \nYou feel yourself getting more and more flustered, feeling the sensation of their hand, as you both start strolling around the garden together. \nYou admire flowers and plants, still holding their hand, enjoying the time you have left together. \nDuring that stroll, you also find out they really like a peculiar flower, Zinnias. \nThe day soon ends and you both say goodbye. \nTomorrow is the day.")
        lovemeter = lovemeter + 6
    else:
        input("Please choose an existing option. (Enter to continue.)")
        scenario35()

def final():
    global lovemeter
    global charname
    global username
    print("\n❀࿐ Today is the day. Confession day. You don't know what's going to happen; however you trust in the choices you've made this entire week.\nBefore you go, you realize you should, of course, buy something to give during your confession. \nA. Plushie\nB. Sweets\nC. A bouquet of flowers")
    choice = input("\n~ What do you get them? ")
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
            input("\n❀࿐ The sunset was beyond you both, its golden rays fell on their perfect face.\nThe air was cold and humid, and you felt yourself shivering, not because of the cold, but because it was time for you to let out the feelings you’ve been meaning to say for a year.\nYou take a deep breath and look at them, staring right back at you expectantly, and there, you pour out everything.\nFrom the day you first fell in love with them, to the week you’ve both spent being together.\nEvery word.\nEvery smile.\nEvery moment.\nEverything.\nAnd finally, you say the three magic words.\n\n“I love you.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input("Yet after you said the phrase that’s been eating you up all year,\nyou saw their eyes narrow, as you see them looking at you with pure utter disgust.\nYou could feel their resentment towards you, and you come to regret everything you’ve just said.\nYour chest starts tightening up and your heart starts pounding as if it’s going to flee from your chest at any moment.\nYou panic, stumbling your words, as you decide to just apologize in an attempt to nullify the damage, yet you’re cut off by them.\n\n“How could I ever love someone as horrid as you?”\n\nYou feel yourself collapsing from hearing that sentence, as tears start blurring your image of them.\nYou collapse down on the ground, as you hear the sound of their footsteps fading.\nThey left.\nAnd the vivid image of them staring at you with pure resentment haunts you.\n\nIt feels as if your heart is breaking.\n\nYou clutch on to the gift you were supposed to give them and quietly weep.\n\n(Press enter to progress.)")
            end1 = "Heartbroken"
            for endings in data:
                endings["ending1"] = "Heartbroken"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end1} end.")
            print("===========================")

        elif lovemeter <= 25:
            input(f"\n❀࿐ The sunset was beyond you and {charname}, as its rays landed on their perfect face, creating a scene that looked straight out of a movie.\nDiverting your eyes away from them, their piercing eyes stare at you expectantly, wondering why you called them here.\nTerrified, you hear the sound of your heart beat ringing in your ears. You couldn’t help but feel afraid.\nHowever, despite your fears and your overwhelming thoughts, you open your mouth and decide to just go for it.\n\nYour story starts on how you initially fell in love with them, and how it grew further and further as the year went by up until the recent week you spent together.\nYou let out everything you’ve kept from them and say everything you’ve been meaning to say all this time.\nAnd tying it all together, you finally say it,\n\n“I love you.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input("You unintentionally close your eyes in fear, as dread immediately creeps in.\nYou said it. You said everything you wanted to say after a year of longing.\nYet when you opened your eyes to look at them for the last time, your eyes caught the look of pity in their eyes.\nYour chest tightened and your heart felt like it was crying out seeing that.\nFlinching from them opening their mouth, you hear a sentence you were expecting.\n\n“I’m sorry, but I don’t think I feel the same way.”\n\nWith a sad pitiful look from them, you give {charname} a forced, bittersweet smile, as you hold back tears.\nThey wave you goodbye and leave momentarily, as you return with another goodbye.\n\nMaking sure they left, you collapse on the floor.\nCrying, you clutch on to the gift you were supposed to give them, as a sad, bittersweet feeling lingered in your heart.\nHowever, after every tear in your heart has been wiped away, you get up, and instead of feeling helpless,\nyou look up to the golden, setting sun beyond you.\nWith a deep breath, you compose yourself.\nDespite them not reciprocating your feelings, you’re glad that you still took the chance to confess, and who knows?\nMaybe this fateful encounter was meant to happen, and this was merely character development?\n\nBut whatever it was, at least you tried.\n\n(Press enter to progress.)")
            end2 = "At least I tried"
            for endings in data:
                endings["ending2"] = "At least I tried"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end2} end.")
            print("===========================")

        elif lovemeter <= 60:
            input(f"\n❀࿐ Clutching on to the gift you’re going to give them, you wait for {charname} expectantly.\nAfter taking a deep breath, your mind starts compiling everything you were meant to say to them over the past year you’ve liked them.\nFrom the day you first laid your eyes on them, to the week you’ve both spent hanging out together.\nYou begin to think back on the decisions you’ve made this past week and trust yourself that you’ve made the right choices.\nWhatever those decisions were, you knew it was going to significantly impact this moment.\nA few minutes later, and there they were.\nTheir expecting eyes watched you while you attempted to compose yourself.\nAfter another deep breath, everything that was hidden finally poured out like a raging flood.\nThe feelings you’ve kept away.\nThe secrets you’ve held in your heart.\nThe emotions you yourself can’t explain whenever you’re with them.\nYou let it all out. And to tie all you have said together, you uttered the final words,\n\n“I love you.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input("\nYou felt a wave of relief at some point. That is, until you looked into their eyes.\nIs it... pity? No, something about the way their gaze locked onto yours felt rather bittersweet.\nSuddenly, you start panicking.\nWas this a mistake?\nShould I have done this?\nWhile you are contemplating everything, your thoughts pause from hearing their soft voice, reaching you amidst your sea of thoughts.\n\n“Look, you're really cool and all, but...”\n\n“To be completely honest, I only see you as a friend.”\n\nYou felt your chest tighten from that sentence alone. It felt as though your heart was slowly and agonizingly cracking. They continue,\n\n“But I hope this won't change anything. So... friends?”\n\nThey say as they offer their hand as a gesture of companionship.\nYou shake their hand and nod, then suddently you feel tears trickle down your cheeks.\nThey pull you into an embrace and begin to comfort you as you quietly weep; they whisper and console you, telling you that everything will be just fine.\nDespite the bittersweet feeling festering within the fathoms of your heart, you chose to accept the fact you will never be anything more than friends.\nYou might not move on or heal for a while,\nyet you know you must keep going forward.\n\n(Press enter to progress.)")
            end3 = "Just friends"
            for endings in data:
                endings["ending3"] = "Just friends"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end3} end.")
            print("===========================")

        elif lovemeter <= 100:
            input(f"❀࿐ Clutching the small gift in your hands, your fingers tighten around it as if it might somehow steady your racing heart.\nYou wait for {charname}, your breath uneven, your thoughts louder than the world around you.\nEverything you’ve wanted to say over the past year begins to line up in your mind messily.\nYou begin revisiting your choices. Every word, every hesitation, every choice you made to get here.\nWas it enough? Was it too much?\nBefore doubt can fully take over, you see them. They approach, eyes soft but curious.\nYou take another breath. And then—everything spills.\nIt wasn't perfect, not the way you practiced. But it was honest. Real.\nAll the feelings you tried to hide. All the moments you overthought.\nAll the little things about them that made your world feel lighter without you even realizing it.\nIt comes out like a flood you can’t stop, and maybe don’t want to anymore. And at the end of it all, you say it.\n\n“I love you.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input("Your heart pounds so loudly you’re sure they can hear it.\nFor a moment, you wanted to take it back and rewind everything just to feel safe again. But then…\n\n“I love you too.”\n\nEverything stops. Relief crashes into you so suddenly it almost hurts.\n…but it doesn’t last.\n\n“But… I’m not ready yet.”\n\nThey step closer, their expression gentle, almost apologetic.\n\n“It’s not that I don’t feel it,” they say, their voice steady but careful.\n\n“I do. I really do. You mean so much to me… more than I think I’ve ever been able to explain.”\n\nTheir gaze drops for a second before meeting yours again.\n\n“I just… I don’t want to rush something this important and risk ruining it. Or hurting you. Or us.”\nA pause.\n“We can take our time. If… you’re willing to.”\n\nThe ache in your chest doesn’t disappear, but it shifts. It softens into something quieter, something patient.\nYou look back at them, really look this time, and realize… Nothing you felt was wrong. Nothing was wasted.\n\n“I think,” you start, a faint smile forming despite everything, “I can wait a little longer.”\n\nAnd somehow, even without the perfect ending you imagined...\n\n...it still feels like the beginning of something real.\n\n(Press enter to progress.)")
            end4 = "Hopeful"
            for endings in data:
                endings["ending4"] = "Hopeful"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end4} end.")
            print("===========================")

        elif lovemeter <= 150:
            input(f"❀࿐ Sitting in your classroom, you await your impending doom as you watch the clock’s hand intensely, anxiously waiting for dismissal.\nYou take a deep breath once again.\nMinutes upon minutes of tirelessly trying to compose yourself were in vain\nas realization that there were only 5 more minutes until the end of classes struck.\nDread begins overwhelming you, as your thoughts begin convincing you to schedule this for another day; the clock then strikes five.\nThe teacher dismisses you, and your hand goes to grab your bag while your other clutched onto the gift.\n\nPlacing your bag down outside of your classroom, you begin readying yourself physically, mentally, and emotionally (and maybe spiritually).\nWhile preparing youself for your impending doom, your eyes wander outside to find them already stationed, waiting at the amphitheater.\n\nHow were they already there??\n\nYou silently curse under your breath, knowing how underprepared you are. However, you know you can’t keep them waiting for too long.\nAfter slowly counting to ten in your head, you begin to walk towards them, your gait so slow it was almost comparable to a toddler.\nHowever, it was a given. You’re planning to confess after a year of yearning.\nA year of hiding your feelings, emotions. And it’s scary.\nBut it was now or never.\nYour mind begins recalling the decisions you’ve made over the past week, and you finally decide that you should stop being a coward,\nand trust the decisions you’ve made.\nWith newfound confidence, you quicken your pace, and your eyes meet.\nImmediately beaming in your presence, they get up to greet you, and your heart feels it's been struck by Cupid's arrow.\nFor a moment, you felt moonstruck, yet shrugged off the feeling since this wasn’t the time for that; it was time to confess.\nDeclaring the feelings you’ve hidden for so long, you begin saying everything you’ve been meaning to say.\nYou don’t care that your voice was shaking, all that mattered was that you were finally saying it.\nYou utter your kept feelings towards them, the reasons why you love them, and the secrets you’ve bottled up for the longest time.\nYou felt yourself running out of breath.\nAnd to wrap up all you've poured out, your speech ends with an awaited phrase,\n\n“I love you.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input(f"Your chest tightens; it feels as though something was piercing through your chest.\n\n'Was this a mistake? Maybe I shouldn’t have done this.'\n\nFor a while, {charname} remained quiet, and the silence slowly enveloped the both of you—a far cry from your loud, overthinking thoughts.\nYou hung your head, eyes fixated towards the concrete pavement beneath your feet, not daring to look back up at them.\nMore and more anxious thoughts continued to feed your fear.\nBefore you drown in your sea of thoughts, you hear their voice pull you out of the waters.\n\n“I love you too.”\n\n. . .\n\n(Press enter to progress.)")
            time.sleep(1)
            input(f"\n\n“What?”\n\n“I said I love you too, {username}.”\n\nThere you looked up at {charname}, their smile clearing every negative thought you’ve had before.\nIt was as if everything got renewed in color again.\nThe sun’s golden rays fell upon both your faces.\nThe flowers beside you felt like they bloomed twice, and for the first time, you felt hopeful rather than uneasy.\nAfter a year of loving, yearning, and longing for them, it finally happened. Something you never thought would happen, happened.\nYou remained speechless. It just felt so... surreal.\nFor a while, you couldn’t help but think this was all another delusion of yours.\nBut you knew it came down to either you accepting this reality, or letting your thoughts twist this into 'just another fantasy'.\nWith eventual confidence, you chose the former.\nDiscarding your previous inner thoughts, you feel... hopeful.\nYou both smile from ear to ear, and even they couldn’t believe it.\n\nAfter dozens of flowers plucked,\n\nhundreds of petals fallen,\nthey love you back.\n\n(Press enter to progress.)")
            end5 = "Happy"
            for endings in data:
                endings["ending5"] = "Happy"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end5} end.")
            print("===========================")

        else:
            yansecret()

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def yansecret():
    global charname
    global username
    input(f"\n𓇢𓆸 Waiting for {charname}’s class to end, you fidget with the gift you bought for them while looking around at the surrounding greenery.\nYou look at your phone, checking the time. You notice that it's about time their class ends.\nYou take deep breaths while looking around to see if they're near.\nYou then spot them coming closer and your heart starts beating uncontrollably from your chest like it wants to jump out.\nAs they get closer to the amphitheatre, you start panicking, thinking of all the scenarios that could happen.\nYou stand up and wait for them to get closer, afraid of what’s going to happen.\nYou look up at them, staring at you intensely with an almost lovesick gaze.\nTheir smile was saccharine sweet. You feel rather... uneasy?\nYou’re unsure what to say anymore, but you gesture at them to sit beside you.\nYou end up confessing smoothly, pouring out everything you’ve felt from the very first day you both met, to this week you’ve spent together.\nAs you rant about your feelings and emotions you've held for them, you notice their gaze fixated on you.\nThey were wearing a rather wide smile on their face.\nYou pause for a moment, a bit creeped out, before finishing off your rant with a final,\n\n“I love you,”\n\nto really set in stone how you feel towards them.\nAfter you utter the final words, they abruptly grab both of your hands,\nand stare into your eyes with sheer joy — joy that seemed... crazed, in a way.\n\n“I love you too!”\n\nThey quickly reply. Too quickly. It was like they knew you were going to confess.\nDespite their odd actions, you feel ecstatic knowing they loved you back.\n\n\n. . .\n\n(Press enter to progress.)")
    time.sleep(0.5)
    print(f"\n\nIt’s been about a year since you confessed. You and {charname}’s relationship has been smooth sailing. Until…\n\nOne day, you find yourself talking with an old friend from elementary while you’re out on a walk in the park with {charname}.\nBut as you chat and laugh a little with your old friend, {charname} standing right beside you has gone oddly still.\n\nThey don’t say much. Not even the usual small comments or quiet reactions. When you glance at them, their posture is relaxed,\nbut there’s something off about it — it was too composed.\nTheir eyes are fixed on your old friend, unblinking.\n\nAfter a couple exchanged goodbyes, your friend finally takes their leave, waving as they walk off.\nThe moment their footsteps fade, {charname} suddenly turns to you with a calm smile that doesn’t quite reach their eyes.\nThey then tell you they need to use the restroom. Before you can respond, they’re already stepping away.\nTime passes. At first, you don’t think much of it. But then ten minutes go by, then a little longer.\nEventually, you decide to look for them. Your first thought was to check the public restrooms nearby.\nThe area is almost empty, just the dull echo of dripping water. You check anyway. Stalls. Around the corners. Nothing.\n\nThey aren't there.\n\nAs you step back out, you pause. A smell—subtle at first, then growing sharper as the breeze shifts.\nIt doesn’t belong in a place like this. It pulls your attention before your thoughts can even catch up. You turn your head slowly.\nThe source is the narrow alleyway beside the restrooms. Something about it feels wrong, but your feet move before your mind fully agrees.\nThe smell intensifies as you walk deeper into the alleyway. And then you see it, and a sharp wave of nausea washes over you.\n\nA pool of blood on the ground. And there, just beyond it, your old friend, lying motionless in the alley.\nYou knew exactly who the culprit was. You decide to...\n\nA. Stay in place and try to figure out what happened.\nB. Quickly and quietly leave the scene.")
    choice = str(input("\n~ What is your choice? . . . "))

    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        if choice == "A" or choice == "a":
            input("\n𓇢𓆸 You weren’t supposed to be there, but you wanted to investigate further. You didn’t fully understand why.\nBut before you could step any closer, you saw a figure turn around in the darkness.\n\nThem.\n\nFor a moment, neither of you moved. You should have run. Every instinct screamed at you to turn and pretend you never saw a thing.\nBut shock rooted you in place. And then they smiled. Not panicked. Not afraid. Relieved..?\n“Oh…” they exhaled softly, tilting their head as if seeing you was some kind of miracle. “You found me.”\nYour breath hitched. Your body finally listened, stumbling backward.\n\nBut it was too late.\n\n. . .\n\nWhen you woke up, everything hurt. The pain wasn't sharp, but it was deep. Wrong. Like something fundamental had been taken from you.\nYou tried to move... but you couldn’t.\nA strangled sound caught in your throat as panic surged, your legs refusing to respond no matter how desperately you willed them to.\n\n“What did they do?..”\n\n“Oh, dear…”\n\nTheir voice was soft. You turned your head, and there they were, watching you with adoration.\n\n“I couldn’t let you leave…” They reached out, brushing your hair back, their touch almost tender enough to make you forget. Almost.\n\n“Do you know what would have happened,” they murmured, “if I let you go?” Their smile widened, eyes bright and feverish.\n\n“You would have told someone.” A pause. “And then they would have taken you away from me.”\n\n“I couldn’t let that happen.” You tried to pull away but you couldn’t.\n\n“Why did you do it?..” You managed to murmur shakily.\n\n“I had to,” they say softly, like they’re explaining something obvious. Reasonable. “They were getting too close to you.”\n\n“They were going to ruin everything we built, and I couldn’t let that happen.” Their hand reaches out toward you.\n\n“But it’s okay now,” they whisper, their expression softening again as if nothing’s wrong. “No one’s going to take you away from me.”\n\nA soft laugh escaped them, delighted, and not mocking. But also warm, as if your fear was something precious.\n\n“You see?” they whispered. “It’s better this way.”\n\nTheir grip tightened just slightly.\n\n“As for what I did, I knew…” they added, “if you could run, you would never stay.”\n\nTheir head tilted slightly, studying your face, watching every flicker of fear like it was something to be memorized and cherished.\n\n“So I fixed it.” The words were soft as if they had done you a kindness.\nTheir hand pressed against your leg gently—testing, confirming—before withdrawing again, satisfied.\n\n“Now you’ll stay.” Their thumb brushed slowly over your knuckles, back and forth, back and forth,\nas if soothing you through a nightmare they had created. A breath.\n\n“I can’t let anyone else take my treasure from me…”\n\nThey had taken away everything that could separate you from them.\nPiece by piece. Without anger. Only care.\nThey had stripped away your tendons so you could never run away from them.\nThey didn’t see what they’d done as cruelty.\nThey saw it as love.\n\nYou were theirs.\n\nAnd they had made sure that nobody else could ever have you.\n\n(Press enter to progress.)")
            end6 = "Happy...?"
            for endings in data:
                endings["secretend1"] = "Happy...?"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end6} end.")
            print("===========================")

        else:
            input("\n𓇢𓆸 You didn’t stay. The moment everything settled, you turned and walked away, each step heavier than the last.\nYour hands trembled as you reached into your pocket, pulling out your phone. The screen blurred.\nYou blinked hard, forcing it into focus, forcing your fingers to cooperate as you dialed 911. You told yourself it was the right choice.\nYou knew it was the right choice. Still… It didn’t make it hurt any less.\n\nTime passed in a blur before they found you. Sitting alone on a cold bench, you stared blankly ahead, your thoughts looping, refusing to quiet down.\nWhen you heard footsteps, you didn’t need to look up to know it was them. Your body went still. This is it.\n\nYou straightened, forcing yourself to stand before they could say anything.\nWhen you finally looked at them, they were smiling. Their smile was soft, relieved, completely unaware.\nIt made your chest tighten painfully.\n\n“…Hey,” they greeted, their voice warm, but it faltered slightly when they noticed your expression. Their smile faded.\n\n“I… I need to tell you something.” That was all it took. They went quiet, their eyes searching yours, uncertainty creeping in.\nYou could see it — the way their shoulders tensed, the way their hands stilled at their sides.\nYou told them everything, but not everything. You talked about the good moments.\nThe way they made you laugh when you didn’t want to.\nThe way being with them felt like coming home to something you didn’t know you were missing.\nThe quiet moments. The warmth. The comfort.\nWith every word, their expression changed. Hope flickering, then wavering, then slowly unraveling into something more fragile.\n\n“I don’t think this is going to work,” you said quietly. “I’m sorry.”\n\nYou forced yourself to continue. “I did love you. I truly did.”\n\nSilence followed. They didn’t speak right away.\nWhen you finally looked at them, their expression said everything — the confusion, the hurt, the quiet realization settling in piece by piece.\n\n“…What?” they whispered, like they hadn’t quite heard you right.\n\nYour chest tightened, but you didn’t move closer. Didn’t reach out. You couldn’t.\n\nBecause you knew what they had done. You knew what they were capable of.\nAnd more than anything, you knew that staying meant watching things get worse. It meant watching them become someone you couldn’t save.\nIf you stayed, what would stop them from doing it again? Who would be next? Anyone who got too close?\nAnyone who threatened what they thought they had with you?\n\nSo you shook your head slightly, your voice softer now, almost breaking. “I can’t do this. Not anymore.”\n\nThey took a step forward. You took one back. Something in their eyes shifted. Not anger, just hurt. Deep, quiet hurt.\nAnd it nearly shattered you. But you held your ground because this wasn’t about what you wanted anymore.\nWithout another word, you turned. You didn’t look back.\n\nBecause if you did...\n\nYou weren’t sure you’d have the strength to leave.\n\n(Press enter to progress.)")
            end7 = "Won't work out anymore"
            for endings in data:
                endings["secretend2"] = "Won't work out anymore"
            with open(filename, 'w') as file:
                json.dump(data, file)
            print("=======================================================================================")
            print(f"\n{end7} end.")
            print("===========================")

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

        print("\n❀࿐ The music is gentle. Not overwhelming, just enough to fill the quiet spaces between heartbeats.\n\nYou stand at one end of the aisle, hands clasped together, trying to keep them from trembling.\nIt’s almost funny; after everything, after all the waiting, after all the moments that led here, you’re still nervous.\nBut this time, it’s different. This time, you’re not afraid.\nBecause at the other end of the aisle,\n\nthey’re there.\n\nAnd they’re smiling at you in the same way you remember from that day. Softer now. Surer. No hesitation hiding behind it anymore. Just love.\n\nYou think back, just for a second. To the gift in your hands, the way your voice shook, the moment that should have broken you—but didn’t.\n\n“I’m not ready yet.”\n\nYou remember how much it hurt. And how much it meant when they stayed anyway. When they chose you, even if the timing wasn’t perfect.\nAnd now, you’re there. Right in front of them. Closer than you’ve ever been, and somehow it still feels like the first time all over again.\nTheir eyes are shining. Yours probably are too. Everything that once felt uncertain… isn’t anymore.\n\nWhen it’s time for the vows, your heart beats faster again, but not from fear.\nYou glance down briefly, but the words you prepared don’t feel as important as the ones already sitting in your chest.\nSo you speak from there.\n\n“I think… we both know I’m not the best at saying things perfectly,” you start, a small smile on your face. “I never have been.”\n\n“But I meant it back then. Every messy, unplanned word of it.” Your gaze softens.\n\n“And I meant it when I said I could wait.”\n\nThey inhale slightly, their expression shifting, remembering. You continue.\n\n“I didn’t know what that would look like. I didn’t know how long it would take. But I knew… you were worth it.”\n\n“And somewhere along the way, waiting didn’t feel like waiting anymore. It just felt like… loving you.”\n“Growing with you. Choosing you, over and over again, until one day…” You reach for their hands.\n\n“…we didn’t have to say ‘not yet’ anymore.”\n\nA pause. Just long enough for everything to settle between you.\n\n“I love you. Still. Always. And this time,” your smile widens slightly, “we’re both ready.”\n\nWhen it’s their turn, they don’t even try to hide their tears.\n\n“I was so afraid back then,” they admit softly. “Not of you. Never of you. Just… of losing something I knew was rare.”\n\“You gave me time. You gave me patience. You gave me a kind of love that didn’t rush me, didn’t pressure me… just stayed.”\nTheir voice wavers, then steadies again.\n\n“And I spent that time realizing something.”\n“It was never about being ‘ready’ in the perfect sense.”\n“It was about being ready with you.”\n\nTheir thumb brushes against your hand, the same way it did the day you gave them that gift.\n\n“And now I am.”\n\n“I love you. And I’m so, so glad you waited… because it led us here.” \n\nLater, when everything fades into celebration; when the music grows louder, you find a quiet moment together.\nYour fingers brush theirs again, just like before. But everything feels different now.\nIt feels... complete. And as you lean into them, surrounded by a future that once felt uncertain, you realize something simple.\n\nWaiting didn’t delay your story.\n\nThis was always where it was leading.")
        end8 = "The future promised"
        for endings in data:
            endings["secretend3"] = "The future promised"
        with open(filename, 'w') as file:
            json.dump(data, file)
        time.sleep(4)
        print("=======================================================================================")
        print(f"\n{end8} end.")
        print("===========================")
        input("~ Press enter to return to main menu.")
        main_menu()

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def locker():
    print("=======================================================================================")
    choice = input("~ Go through the locker?\nYes\tor\tNo\nNext move: ")
    print("=======================================================================================")
    if choice == "yes" or choice == "Yes":
        print("❀࿐ You found: Note!")
        print("❀࿐ You found a note with a red ribbon tied around it.")
        second_choice = input("~ Untie it and read?\nYes\tor\tNo\nNext move: ")
        print("=======================================================================================")
        if second_choice == "yes" or second_choice == "Yes":
            print("❀࿐ You open it and see:")
            print("⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀")
            print("⠀⢸⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⡇⠀")
            print("⠀⢸⡇⠀⠀Go to Main Menu⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀Input : To where they⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀promised.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀Note : The input MUST ⢸⡇⠀")
            print("⠀⢸⡇⠀⠀be exactly the same.⠀ ⢸⡇⠀")
            print("⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀")
            print("⠀⢸⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸⡇⠀")
            print("⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀")
            print("❀࿐ Um...")
            print("❀࿐ \"Strange,\" you thought. You then heard the bell. \"I should go now...\"\nShutting the locker, you made your way to class.\n")
            print("=======================================================================================")
            input("~ Press enter to return to main menu.")
            main_menu()
        else:
            print("❀࿐ \"Who knows if this is personal... I shouldn't,\" you told yourself. You put the note back down and shut the locker.\n")
            print("=======================================================================================")
            input("~ Press enter to return to main menu.")
            main_menu()
    else:
        print("❀࿐ \"This is an invasion of privacy,\" you thought to yourself. You decide to leave.\n")
        print("=======================================================================================")
        input("~ Press enter to return to main menu.")
        main_menu()

def endings():
    print("=======================================================================================")
    print("╔═╗┌┐┌┌┬┐┬┌┐┌┌─┐┌─┐  ┌─┐┌┐┌┌┬┐  ┌┐ ┌─┐┌┬┐┌─┐┌─┐┌─┐")
    print("║╣ │││ │││││││ ┬└─┐  ├─┤│││ ││  ├┴┐├─┤ │││ ┬├┤ └─┐")
    print("╚═╝┘└┘─┴┘┴┘└┘└─┘└─┘  ┴ ┴┘└┘─┴┘  └─┘┴ ┴─┴┘└─┘└─┘└─┘")
    print("=======================================================================================")
    try:  # checks for errors
        # opens the json file and saves it in the variable "data"
        filename = "endings.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        for endings in data:
            print(f"˚˖᪥ Ending 1: {endings["ending1"]}\n˚˖᪥ Ending 2: {endings["ending2"]}\n˚˖᪥ Ending 3: {endings["ending3"]}\n˚˖᪥ Ending 4: {endings["ending4"]}\n˚˖᪥ Ending 5: {endings["ending5"]}\n˚˖᪥ Ending 6: {endings["secretend1"]}\n˚˖᪥ Ending 7: {endings["secretend2"]}\n˚˖᪥ Ending 8: {endings["secretend3"]}")

    # prints if errors are found
    except FileNotFoundError:
        print("Error: The file 'endings.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

    print("=======================================================================================")
    input("~ Press Enter to return to the main menu")
    main_menu()

def creds():
    print("=======================================================================================")
    print("╔═╗┬─┐┌─┐┌┬┐┬┌┬┐┌─┐")
    print("║  ├┬┘├┤  │││ │ └─┐")
    print("╚═╝┴└─└─┘─┴┘┴ ┴ └─┘")
    print("=======================================================================================")
    print("\"They love me... They love me not.\"\n\nᯓ★ Made by --- The deluludevs\nᯓ★ Developer --- Zeryl Gonadan, Krisha Villa, Lordwyn Demoni\nᯓ★ Main programmer --- Zeryl Gonadan\nᯓ★ Secondary programmer --- Lordwyn Demoni, Krisha Villa\nᯓ★ Main storywriter --- Lordwyn Demoni\nᯓ★ Secondary storywriter --- Zeryl Gonadan, Krisha Villa\nᯓ★ Romantic interest --- Your crush!/j\nᯓ★ Main character --- You! (You better get all those endings./hj)")
    print("=======================================================================================")
    print("┬ ┬┌─┐┌┐┌┌─┐┬─┐┌─┐┌┐ ┬  ┌─┐  ┌┬┐┌─┐┌┐┌┌┬┐┬┌─┐┌┐┌┌─┐")
    print("├─┤│ │││││ │├┬┘├─┤├┴┐│  ├┤   │││├┤ │││ │ ││ ││││└─┐")
    print("┴ ┴└─┘┘└┘└─┘┴└─┴ ┴└─┘┴─┘└─┘  ┴ ┴└─┘┘└┘ ┴ ┴└─┘┘└┘└─┘")
    print("=======================================================================================")
    print("ᯓ★ Ma'am Kaye --- for guiding us through this project and teaching us so we could finish this game!\nᯓ★ insert mention --- \"insert ur statement\" -Krisha\nᯓ★ insert mention --- \"insert ur statement\" -Lordwyn\nᯓ★ Spotify --- \"for giving me music to listen to so i don't go insane\" -Zeryl\nᯓ★ Coffee --- for keeping us awake to finish the game!\nᯓ★ And... you! --- for playing our game :)")
    print("=======================================================================================")
    input("Press Enter to return to the main menu.")
    main_menu()

def mini_games():
    print("=======================================================================================")
    print("╔╦╗┬┌┐┌┬  ╔═╗┌─┐┌┬┐┌─┐┌─┐")
    print("║║║│││││  ║ ╦├─┤│││├┤ └─┐")
    print("╩ ╩┴┘└┘┴  ╚═╝┴ ┴┴ ┴└─┘└─┘")
    print("=======================================================================================")
    print("˚˖᪥ Play to try increasing the lovemeter's fixed value!\n(WARNING : The lovemeter's fixed value will reset to 0 after exiting the game)\n\nA. Pick a flower (+2 love)\nB. Operation: Guess what they're thinking of! (+4 love)\nC. How well do you know them? (+6 love)")
    print("=======================================================================================")
    choice = input("Game choice: ")
    if choice == "A" or choice == "a":
        minigame1()
    elif choice == "B" or choice == "b":
        minigame2()
    elif choice == "C" or choice == "c":
        minigame3()
    else:
        print("Please enter an existing mini game.")
        mini_games()

def minigame1():
    global lovemeter
    print("=======================================================================================")
    print("┌─┐┬┌─┐┬┌─  ┌─┐  ┌─┐┬  ┌─┐┬ ┬┌─┐┬─┐ ")
    print("├─┘││  ├┴┐  ├─┤  ├┤ │  │ ││││├┤ ├┬┘ ")
    print("┴  ┴└─┘┴ ┴  ┴ ┴  └  ┴─┘└─┘└┴┘└─┘┴└─o")
    print("=======================================================================================")
    input("˚˖᪥ Press enter to pick a flower.")
    print("=======================================================================================")
    flower_choice = random.randint(1,2)
    if flower_choice == 1:
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⣀⣀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠋⠀⠸⣄⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("˚˖᪥ Press enter to pluck a petal.")
        print("===========================")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not.")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("=======================================================================================")
        print("˚˖᪥ +0 love gained. . .")
        input("Press enter to return to the main menu.")
        main_menu()
    else:
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡞⠉⠊⢱⣀⣀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠉    ⡸⠋⠀⠸⣄⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⣀⣀⡤⠊⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀")
        print("˚˖᪥ Press enter to pluck a petal.")
        print("===========================")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎ ")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊ ")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠉⢇⣀⣸⠀⠀")
        print("~ They love me.")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("=======================================================================================")
        print("˚˖᪥ +2 love gained!")
        lovemeter = 2
        input("Press enter to return to the main menu.")
        main_menu()

def minigame2():
    global lovemeter
    print("=======================================================================================")
    print("╔═╗┌─┐┌─┐┬─┐┌─┐┌┬┐┬┌─┐┌┐┌     ╔═╗┬ ┬┌─┐┌─┐┌─┐  ┬ ┬┬ ┬┌─┐┌┬┐  ┌┬┐┬ ┬┌─┐┬ ┬┬─┐┌─┐  ┌┬┐┬ ┬┬┌┐┌┬┌─┬┌┐┌┌─┐  ┌─┐┌─┐┬")
    print("║ ║├─┘├┤ ├┬┘├─┤ │ ││ ││││o    ║ ╦│ │├┤ └─┐└─┐  │││├─┤├─┤ │    │ ├─┤├┤ └┬┘├┬┘├┤    │ ├─┤││││├┴┐│││││ ┬  │ │├┤ │")
    print("╚═╝┴  └─┘┴└─┴ ┴ ┴ ┴└─┘┘└┘o    ╚═╝└─┘└─┘└─┘└─┘  └┴┘┴ ┴┴ ┴ ┴    ┴ ┴ ┴└─┘ ┴ ┴└─└─┘   ┴ ┴ ┴┴┘└┘┴ ┴┴┘└┘└─┘  └─┘└  o")
    print("=======================================================================================")
    print("ᯓ★ They want you to try and guess the word they're thinking of! Guess the 7 letter word correctly to gain +4 love! (Total of 7 tries)\n\"✅️\": The letter is in the right spot\n\"➕\": The letter is in the word, but in the wrong spot\n\"❌\": The letter is in the wrong spot\nHint: The word is related to this game!")
    print("=======================================================================================")
    words = ["flowers", "confess", "longing", "passion", "choices", "present", "promise", "honesty", "diverge"]
    hidden_word = random.choice(words)
    attempt = 7
    while attempt > 0:
        guess = str(input("ᯓ★ Guess the word: "))
        if guess == hidden_word:
            print("ᯓ★ You guessed what they were thinking of!\n˚˖᪥ +4 love gained!")
            lovemeter = 4
            print("=======================================================================================")
            input("Press enter to return to the main menu.")
            break
        else:
            attempt = attempt - 1
            print(f"ᯓ★ You have {attempt} attempt(s) left.")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✅️ ")
                elif word in hidden_word:
                    print(word + " ➕ ")
                else:
                    print(word + " ❌ ")
            if attempt == 0:
                print("ᯓ★ You could not guess what they were thinking of...\n˚˖᪥ +0 love gained...")
                print("=======================================================================================")
                print("Press enter to return to the main menu.")
                main_menu()
    main_menu()

def minigame3():
    global lovemeter
    print("=======================================================================================")
    print("╦ ╦┌─┐┬ ┬  ╦ ╦┌─┐┬  ┬    ╔╦╗┌─┐  ╦ ╦┌─┐┬ ┬  ╦╔═┌┐┌┌─┐┬ ┬  ╔╦╗┬ ┬┌─┐┌┬┐┌─┐")
    print("╠═╣│ ││││  ║║║├┤ │  │     ║║│ │  ╚╦╝│ ││ │  ╠╩╗││││ ││││   ║ ├─┤├┤ │││ ┌┘")
    print("╩ ╩└─┘└┴┘  ╚╩╝└─┘┴─┘┴─┘  ═╩╝└─┘   ╩ └─┘└─┘  ╩ ╩┘└┘└─┘└┴┘   ╩ ┴ ┴└─┘┴ ┴ o")
    print("=======================================================================================")
    print("ᯓ★ We recommend you play this after at least 1 playthrough :)")
    choice = input("Continue?\nYes\tor\tNo")
    if choice == "Yes" or choice == "yes":
        score = 0
        print("=======================================================================================")
        print("ᯓ★ Answer questions about them! Get a passing score to gain +6 love! (Total of 5 questions)")
        print("=======================================================================================")
        print("ᯓ★ First question:")
        time.sleep(1)
        choice = input("˚˖᪥ How much does their favorite food cost?\nA. 50\nB. 45\nC. 65\n\nYour answer: ")
        if choice == "C" or choice == "c":
            print("˚˖᪥ Correct!")
            score = score + 1
        else:
            print("˚˖᪥ Incorrect! The answer was C.")
        print("===========================")
        print("ᯓ★ Second question:")
        time.sleep(1)
        choice = input("˚˖᪥ What is their favorite flower?\nA. Zinnias\nB. Sunflowers\nC. Peonies\n\nYour answer: ")
        if choice == "A" or choice == "a":
            print("˚˖᪥ Correct!")
            score = score + 1
        else:
            print("˚˖᪥ Incorrect! The answer was A.")
        print("===========================")
        print("ᯓ★ Third question:")
        time.sleep(1)
        choice = input("˚˖᪥ What is their favorite animal?\nA. Dogs\nB. Cats\nC. Rabbits\n\nYour answer: ")
        if choice == "B" or choice == "b":
            print("˚˖᪥ Correct!")
            score = score + 1
        else:
            print("˚˖᪥ Incorrect! The answer was B.")
        print("===========================")
        print("ᯓ★ Fourth question:")
        time.sleep(1)
        choice = input("˚˖᪥ Do they like listening to music?\nA. Yes\nB. No\n\nYour answer: ")
        if choice == "A" or choice == "a":
            print("˚˖᪥ Correct!")
            score = score + 1
        else:
            print("˚˖᪥ Incorrect! The answer was A.")
        print("===========================")
        print("ᯓ★ Final question:")
        time.sleep(1)
        choice = input("˚˖᪥ Do they have a plushie in their room?\nA. Yes\nB. No\n\nYour answer: ")
        if choice == "A" or choice == "a":
            print("˚˖᪥ Correct!")
            score = score + 1
        else:
            print("˚˖᪥ Incorrect! The answer was A.")
        print("=======================================================================================")
        if score >= 3:
            print(f"ᯓ★ Your score is: {score}/5\nᯓ★ You passed!\n˚˖᪥ +6 love gained!")
            print("=======================================================================================")
            lovemeter = 6
            input("Press enter to return to the main menu.")
            main_menu()
        else:
            print(f"ᯓ★ Your score is: {score}/5\nᯓ★ You failed...\n˚˖᪥ +0 love gained...")
            print("=======================================================================================")
            input("Press enter to return to the main menu.")
            main_menu()

    else:
        print("=======================================================================================")
        print("Press enter to return to the main menu.")
        main_menu()

def flower():
    global lovemeter

    if lovemeter <= 60:
        print("┌─┐┬┌─┐┬┌─  ┌─┐  ┌─┐┬  ┌─┐┬ ┬┌─┐┬─┐ ")
        print("├─┘││  ├┴┐  ├─┤  ├┤ │  │ ││││├┤ ├┬┘ ")
        print("┴  ┴└─┘┴ ┴  ┴ ┴  └  ┴─┘└─┘└┴┘└─┘┴└─o")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⣀⣀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠋⠀⠸⣄⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("Press enter to pluck a petal.")
        print("===========================")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠑⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠛⠉⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡞⠉⠊⢱⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⢷⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("~ They love me not.")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("===========================")
        input("Press enter to continue.")

    elif lovemeter > 60:
        print("┌─┐┬┌─┐┬┌─  ┌─┐  ┌─┐┬  ┌─┐┬ ┬┌─┐┬─┐ ")
        print("├─┘││  ├┴┐  ├─┤  ├┤ │  │ ││││├┤ ├┬┘ ")
        print("┴  ┴└─┘┴ ┴  ┴ ┴  └  ┴─┘└─┘└┴┘└─┘┴└─o")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡞⠉⠊⢱⣀⣀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠉    ⡸⠋⠀⠸⣄⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⣀⣀⡤⠊⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀")
        print("Press enter to pluck a petal.")
        print("===========================")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠁⠀⠉⠳⡄⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⣄⣠⠎⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀⠀⠀")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎⠀⠈⢧⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⣇⣀⡀⡸⠀")
        print("~ They love me...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⠉⢇⣀⣸⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⡄⠀⣠⡎ ")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊ ")
        print("~ They love me not...")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⡞⠉⠊⢱⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏    ⡸⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢅⡀⠀⠀⡷⠒⢧⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠉⢇⣀⣸⠀⠀")
        print("~ They love me.")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⡷⠒⢧⠀⠀⠀⠀⠀⠀⠀")
        input("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⢇⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀")
        print("===========================")
        input("Press enter to continue.")

def main():
    global charname
    global username
    print("=======================================================================================")
    print("╔═╗┌─┐┌┬┐┌─┐  ┌─┐┌┬┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐  ")
    print("║ ╦├─┤│││├┤   └─┐ │ ├─┤├┬┘ │ │││││ ┬  ")
    print("╚═╝┴ ┴┴ ┴└─┘  └─┘ ┴ ┴ ┴┴└─ ┴ ┴┘└┘└─┘o  o  o")
    print("=======================================================================================")
    time.sleep(3)
    username = input("What shall we call you? ")
    if username == "Kaye" or username == "kaye":
        print("Welcome to \"They love me, they love me not,\" our beloved teacher!")
    charname = input("What shall 'their' name be? ")
    if charname == "Zeryl" or charname == "zeryl":
        print("Art thou Everblight? /j")
    elif charname == "Krisha" or charname == "krisha":
        print("This one only has eyes for a certain rose :p")
    elif charname == "Lordwyn" or charname == "lordwyn":
        print("You must be... one shady guy...")

    input("MINOR WARNING!!!\nThis character has their own fixed persona---If you attempt this with your special someone, it's not guaranteed they'll like you back (ehe)")

    input(f"\nAugust 21, 20xx. One more week until you finally confess.\n\nIt's been a whole year ever since you first laid your eyes on them...\nYou had enough of watching from afar.. This week.. It's going to be different..!\nYou...\nWill make the first move...")

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 1 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 2 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 3 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 4 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 5 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 6 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ☆｡⁠⁠✧.* ❀࿐ Day 7 ࿐❀ *⁠.⁠✧｡⁠☆")
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
    print("===========================")
    print("╔╦╗┌─┐┬ ┬  ┌─┐┌┐┌┌┬┐ ")
    print(" ║║├─┤└┬┘  ├┤ │││ ││ ")
    print("═╩╝┴ ┴ ┴   └─┘┘└┘─┴┘o")
    print("===========================")

    flower()

    print("===========================")
    input(" ❀࿐ Day of confession. ࿐❀")
    print("===========================")
    time.sleep(1)
    final()
    time.sleep(3)
    creds()
    print("===========================")
    ans = str(input("\t\t~ Retry?\t\t\nYes\tor\tNo\n  "))
    print("===========================")

    if ans == "Yes":
        main()
    else:
        main_menu()

main_menu()