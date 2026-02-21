import time

lovemeter = 0
code = "0828"
badges_collected = {"end1": "?", "end2": "?", "end3": "?", "end4": "?", "end5": "?", "end6": "?", "end7": "?"}


def main_menu():
    print("They love me... They love me not.")
    time.sleep(1)
    print("===========================")
    print("A. Start\nB. Locker\nC. Badegs\nD. Credits and honorable mentions")
    print("===========================")
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
        badges()
    elif choice == "D" or choice == "d":
        creds()
        time.sleep(2)
        main_menu()
    else:
        print("That path does not exist.")
        main_menu()


def scenario1():
    global lovemeter
    print(
        "As you pass by their classroom on the way to your own, your eyes wandered to their figure, sitting down on their seat as usual. They notice you, and you lock eyes...\nA. Wave enthusiastically and give them a soft smile. \nB. Stare at them for a full 5 seconds and wave awkwardly.\nC. Turn away immediately and walk off.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print("They wave and smile at you back. Both of you enjoyed that interaction.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print("They chuckle a bit, and wave back at you.")
        lovemeter = lovemeter + 2
    else:
        print("They seemed confused and felt a bit hurt from your ignorance.")
        lovemeter = lovemeter - 1


def scenario2():
    global lovemeter
    print(
        "\nIt's finally break, and you decide not to leave your classroom. You pull out your phone and your eyes catches the green dot on their profile. They're active! Your heart skips a beat. \nA. Archive them so your heart can rest.\nB. Send them a like emoji without further explanation.\nC. Greet them with a simple 'good morning'.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print("Your heart seemed to calm down a bit, yet you felt a bit bad for archiving them.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        print(
            "You didn't know what else to react, so you simply tap on the quick reaction. \nThey later responded with a like emoji as well, and you think it went relatively well?")
        lovemeter = lovemeter + 2
    else:
        print("They greet you back and end up texting more before break ends. You think your conversation went well.")
        lovemeter = lovemeter + 4


def scenario3():
    global lovemeter
    print(
        "Lunch has finally arrived and you go down to the canteen, wanting to buy your food. You spot them---surprisingly---alone at a table and without food.\nA. You walk up to them, and ask them 'Do you want to eat lunch together?'\nB. You awkwardly walk up to them, but your brain freezes and you end up not saying ANYTHING and walk off, regretting your life decisions.\nC. You quietly leave their favorite food on their table.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print("They smile softly at you, and agrees. You end up spending the whole lunch period together.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print(
            "They stared at you during that whole sequence of events, and seemed a bit uncomfortable. You feel like you should kill yourself already. ")
        lovemeter = lovemeter - 1
    else:
        print(
            "They stare at you once they realize you felt their favorite food at their table, and you saw as their face lit up. A well 65 pesos spent. ")
        lovemeter = lovemeter + 2


def scenario4():
    global lovemeter
    global charname
    global username
    print(
        f"It's finally dismissal and you get to go home! But before you could exit through the gate, a tap on your shoulder. It was {charname}! \"Hey, {username}, wanna maybe... walk together? I've been a bit lonely lately.\"\nA. You nod awkwardly, a sheepish smile on your face.\nB. You accept without hesitation, a bright smile on your face knowing you could spend time with them.\nC. Stare at them for a full minute before accepting.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print("They smile back at you, and both of you prepare to walk home.")
    elif choice == "B" or choice == "b":
        print(
            "They notice your sudden enthusiasm and chuckle a bit. \n'Let's go then.' They tell you, as your face flush from hearing their voice.")
        lovemeter = lovemeter + 4
    else:
        print(
            "During the whole time you were staring them, they seemed a bit uncomfortable and kept avoiding your gaze. When you finally agreed, they nodded back awkwardly and mutter, 'Let's.. go then...'.")
        lovemeter = lovemeter - 1


def scenario5():
    global lovemeter
    global charname
    print(
        f"Walking beside {charname}, you can't help the fast beating of your heart against your chest. But... the silence was getting a bit awkward.\nA. You decide to begin a conversation, but while they speak, you act rather indifferent.\nB. You begin a conversation, asking about their day and telling jokes, ultimately painting a bright smile on their face.\nC. You begin a conversation, though while telling a joke, you stumble over your words and elicit a soft laugh from {charname}.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print(
            "They notice your ignorance, and soon stops speaking. The whole walk home turned dead silent, as you regretted acting indifferent earlier and giving dry and quick responses.\nOnce reaching your destination, they give a half-hearted goodbye as you watch them walk away. Your heart feels rather... heavy?")
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        print(
            "The whole walk home, both of you enjoyed each other's presence, cackling about silly jokes and talking as if your normal friends, and you felt as if your face was red the entire time.\nYou finally reached your destination, as you see them with a disappointed expression.\nYou give them a final wave, as they struck you with another sincere smile, waving back.\nYou think you both enjoyed that interaction.")
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter + 4


def scenario6():
    global lovemeter
    print(
        "You arrived at school earlier than usual and haven’t seen them in their classroom yet; their seat still left empty.\nA. Steal one of their pens that’s on their table and keep it.\nB. Don’t do anything and just leave.\nc. Leave a small note underneath their desk and quietly leave.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print(
            "You selfishly grab one of their pens without thought, and keep it for yourself; yet you feel bad for stealing it.")
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        print("With nothing to do, you leave their desk be, and dip.")
        lovemeter = lovemeter + 2
    else:
        print(
            "You quietly sneak a small note underneath their desk, and get butterflies from the thought of them finding and reading it. You leave in hopes they'd see it.")
        lovemeter = lovemeter + 4


def scenario7():
    global lovemeter
    print(
        "While walking with one of your friends, they suddenly nudge you, raising their eyebrows while pointing at your crush. At the sight of them, your heart skips a beat. Suddenly, your friend pushes you towards them.\nA. Use your quick reaction time and dodge quickly, avoiding falling onto them.\nB. Let yourself fall on them, but afterwards apologize profusely.\nC. Pull your friend down as well and end up falling on your crush while being crushed by your friend.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print(
            "Your crush and yourself were thankfully left unscathed, as you quickly get up and scold your friend, laughing maniacally. You hear them trying to hold back their laugh, as your face flushes from embarrassment. You drag your friend away and finally leave.")
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        print(
            "They tell you it's okay and to stop apologizing, for some reason with a bright smile plastered on your face.\nYou nod awkwardly, as you drag your friend away to crash out to them.")
        lovemeter = lovemeter + 4
    else:
        print(
            "All of you yelled from pain at the same time as your crush and yourself got crushed. Once you got up, you apologized, and you ran from the embarrassment of crushing your crush.")
        lovemeter = lovemeter - 1


def scenario8():
    global lovemeter
    print(
        "You’re standing in line to buy food from the canteen, and you realize they're behind you, waiting to buy food as well.\nA. Start a conversation with them.\nB. You begin to sweat profusely and quickly exit the line to spare your racing heart.\nC. You get so nervous that you forget that the line was moving so you end up standing there awkwardly before quickly moving with embarrassment.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print(
            "The conversation ends up going well, talking about the usual things friends talk about, as you both was able to soon buy your food without trouble.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print(
            "Once you're out of there, you couldn't help but overthink the fact that they may have felt you were ignoring them, since you DID sprint out of there once realizing their presence. ")
        lovemeter = lovemeter - 1
    else:
        print(
            "You hear their soft chuckle behind you, as your face flushes once more. After buying your food, you bolt straight out.")
        lovemeter = lovemeter + 2


def scenario9():
    global lovemeter
    print(
        "You’re finally back home when you decide to message them, telling them to stay safe while going home. After you sent it, you patiently waited for their response, but you were still left on delivered despite them being online\nA. Send another follow-up message, but don’t overthink it.\nB. Delete your message and follow up with a “Never mind”.\nC. Leave the message alone and assume they’re busy.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print(
            "They asked what you unsent, and you only responded by saying it was nothing. You regret all your life choices.")  # can we make this so that if they pick this, they wont be able to do situation 10???????
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario10():
    global lovemeter
    print(
        "After a few hours, they decide to reply to your message, and they ask you how you were doing and how your night was so far.\nA. You keep the conversation flowing however you fumble so bad you end up misspelling most of your messages.\nB.Reply but you think first before sending the message, carefully considering how it would affect this conversation.\nC. Leave them on read because you’re too nervous to reply and because you’re overthinking it too much.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        print(
            "Despite your constant misspelling of words, you think they didn't mind at all, and you even had fun talking to them, as night falls, and you eventually tell each other good night.")
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        print(
            "You ended up texting all night long, as you found out more information about them. You felt warm in the inside knowing you got to spend so much time with them via messaging.")  # user gains hint about crush's fav flowers and things to help in confessing and giving gift?
        lovemeter = lovemeter + 6
    else:
        print(
            "Although you felt bad for leaving them on read, you decided to give your heart a break, and slept it off.")
        lovemeter = lovemeter - 3


# day three

def scenario11():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario12():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario13():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 4


def scenario14():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario15():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 6
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 3
    else:
        lovemeter = lovemeter + 4


def scenario16():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario17():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario18():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario19():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario20():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 6


def scenario21():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario22():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario23():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario24():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario25():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter - 3


def scenario26():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario27():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario28():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario29():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario30():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter - 3


def scenario31():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario32():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario33():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario34():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario35():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 3
    else:
        lovemeter = lovemeter + 6


def final():
    global lovemeter
    print("End scene")

    choice = input("What do you get them? ")
    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 6

    if lovemeter < 5:
        print("harsh rejection")
        end1 = "Heartbroken"
        badges_collected["end1"] = "Heartbroken"
        time.sleep(4)
        print(f"{end1} end.")
        print("===========================")

    elif lovemeter <= 25:
        print("blunt rejection")
        end2 = "At least I tried"
        badges_collected["end2"] = "At least I tried"
        time.sleep(4)
        print(f"{end2} end.")
        print("===========================")

    elif lovemeter <= 50:
        print("polite rejection")
        end3 = "Just friends"
        badges_collected["end3"] = "Just friends"
        time.sleep(4)
        print(f"{end3} end.")
        print("===========================")

    elif lovemeter <= 75:
        print("promise of a future")
        end4 = "Hopeful"
        badges_collected["end4"] = "Hopeful"
        time.sleep(4)
        print(f"{end4} end.")
        print("===========================")

    elif lovemeter <= 100:
        print("reciprocation")
        end5 = "Happy"
        badges_collected["end5"] = "Happy"
        time.sleep(4)
        print(f"{end5} end.")
        print("===========================")
    else:
        yansecret()


def yansecret():
    print("secret scene\nchoiceA\nchoiceB")
    time.sleep(4)
    choice = str(input("What is your choice? . . . "))

    if choice == "A" or choice == "a":
        print("Obsession scene")
        end6 = "Happy...?"
        badges_collected["end6"] = "Happy...?"
        time.sleep(4)
        print(f"{end6} end.")
        print("===========================")

    else:
        print("breakup scene")
        end7 = "Won't work out anymore"
        badges_collected["end7"] = "Won't work out anymore"
        time.sleep(4)
        print(f"{end7} end.")
        print("===========================")


def wedsecret():
    print("wedscene KWBDFBWDFBEWJFDFBDSUBDS")
    time.sleep(5)
    main_menu()


def locker():
    choice = input("Go through their locker?\nYes\tor\tNo\n")
    if choice == "yes" or choice == "Yes":
        input("You found: Phone!")
        input("You found their phone. Weirdly enough, you knew their password.")
        second_choice = input("Go through it?\nYes\tor\tNo\n")
        if second_choice == "yes" or second_choice == "Yes":
            input(
                "You look through a couple selfies, their recent searches, then you entered a notes app.\nWait-- Creator's note??? You open it and see:\n\n===========================\nCreator's note\n\nTell EVEREST to take you to where they promised.\n(hint: EVEREST is the one who asks you what you want to do next.\n===========================")
            input("Um...")
            input(
                "\"Strange,\" you thought. You then heard the bell. \"I should go now...\"\nShutting the locker, you made your way to class.\n")
        else:
            input(
                "\"I've already gone through their locker... their phone is a bit of a stretch,\" you told yourself. You put their phone back down and shut the locker.\n")
    else:
        input("\"This is an invasion of their privacy,\" you thought to yourself. You decide to leave.\n")
        main_menu()


def badges(badges_collected):
    print("Ending 1: ", badges_collected["end1"], "\nEnding 2: ", badges_collected["end2"], "\nEnding 3: ",
          badges_collected["end3"], "\nEnding 4: ", badges_collected["end4"], "\nEnding 5: ", badges_collected["end5"],
          "\nEnding 6: ", badges_collected["end6"], "\nEnding 7: ", badges_collected["end7"])
    input("Press Enter to return to the main menu")
    main_menu()


def creds():
    print("===========================")
    print(
        "They love me... They love me not.\nMade by --- The deluludevs\nDeveloper --- Zeryl Gonadan, Krisha Villa, Lordwyn Demoni\nMain coder --- Zeryl Gonadan\nSecondary coder --- Lordwyn Demoni, Krisha Villa\nStorywriter --- Lordwyn Demoni, Zeryl Gonadan, Krisha Villa\n'SHOUTOUT TO MY (Zeryl) ONE AND ONLY INSPIRATION!!!!!'")
    print("===========================")
    time.sleep(2)


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
        input("☆｡⁠⁠✧.* ~ Day 1 ~ *⁠.⁠✧｡⁠☆ ")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~ Day 2 ~ *⁠.⁠✧｡⁠☆ ")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~ Day 3 ~ *⁠.⁠✧｡⁠☆ ")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~Day 4 ~ *⁠.⁠✧｡⁠☆ ")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~ Day 5 ~ *⁠.⁠✧｡⁠☆")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~ Day 6 ~ *⁠.⁠✧｡⁠☆")
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

        print("===========================")
        input("☆｡⁠⁠✧.* ~ Day 7 ~ *⁠.⁠✧｡⁠☆")
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

        print("===========================")
        input("Day of confession.")
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
    # deluludevs so real