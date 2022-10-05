#1st day – 8:00 – Jumin’s lonely morning

label day1_5:

call phone_start2

hide hub
hide chatroomb_full
hide emailb_full
hide historyb
hide helpb
hide albumb
hide exitb
hide yoosung_icon
hide zen_icon
hide seven_icon
hide jumin_icon
hide jaehee_icon

init:
    $ mc_icon_lvl2 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)
    $ z_icon_lvl = Position(xpos=0.445, ypos=10, xanchor=0.445, yanchor=5)
    $ ju_icon_lvl = Position(xpos=0.6085, ypos=10, xanchor=0.6085, yanchor=5)

image mc_icon2 = Transform("mc_icon.png", zoom=.205)
image zen_icon = Transform("zen_icon.png", zoom=.18)
image jumin_icon = Transform("jumin_icon.jpg", zoom=.165)

show mc_icon2 at mc_icon_lvl2
show jumin_icon at ju_icon_lvl
show zen_icon at z_icon_lvl

#chat

play music "ju_theme_1.ogg"
call screen phone_reply("You haven’t left for work yet?","choice116","Hello.","choice117")

label choice116:
    call phone_after_menu
    call message_start_m("MC", "You haven’t left for work yet?")
    call message_z("ZEN", "Good seeing you~!")
    call message_z("ZEN", "I don’t have a set work time.")
    call message_z("ZEN", "Why hasn’t the Director dude left for work yet?")
    call message_ju("Jumin Han", "I was just about to go out.")
    call message_ju("Jumin Han", "Welcome, MC.")

    jump aftermenu33

label choice117:
    call phone_after_menu
    call message_start_m("MC", "Hello.")
    call message_z("ZEN", "Welcome MC~")
    call message_ju("Jumin Han", "Hello.")
    call message_z("ZEN", "So lame that you responded to her with another hello lol")
    call message_ju("Jumin Han", "I have to be polite to a member of the RFA.")
    call message_z("ZEN", "Aha. I see you’re helpless in front of V.")
    call message_ju("Jumin Han", "Isn’t everyone in this organization?")

    call screen phone_reply3("But Jumin, don’t you have to go to work?","choice118","What were you doing, Zen?","choice119","I’m sleepy…","choice120")

    label choice118:
        call phone_after_menu
        call message_start_m("MC", "But Jumin, don’t you have to go to work?")
        call message_ju("Jumin Han", "I was about to.")
        call message_z("ZEN", "No one’s going to give the executive a hard time for being late.")
        call message_ju("Jumin Han", "Assistant Kang will say something though.")
        call message_("ZEN", "Oh, right.")

        jump aftermenu33

    label choice119:
        call phone_after_menu
        call message_start_m("MC", "What were you doing, Zen?")
        call message_z("ZEN", "I was about to get breakfast.")
        call message_z("ZEN", "I’m an actor so my schedule’s flexible.")
        call message_z("ZEN", "I’ll go to rehearsal in the afternoon lol.")
        call message_z("ZEN", "But Mr. Corporate Executive, you’re not going to work?")
        call message_ju("Jumin Han", "I was just about to leave…")

        jump aftermenu33

    label choice120:
        call phone_after_menu
        call message_start_m("MC", "I’m sleepy…")
        call message_z("ZEN", "You’re quite the sleeping beauty.")
        #Happy Zen emoji
        call message_ju("Jumin Han", "There is a way to wake up early.")
        call message_ju("Jumin Han", "You just have to plan something that excites you in the morning")
        call message_ju("Jumin Han", "For example, drinking tea while watching the morning news…")
        call message_z("ZEN", "Hmm… You mean like Micdonald’s breakfast combo?")

        jump aftermenu33

    jump aftermenu33

label aftermenu33:
    call message_ju("Jumin Han", "What are you doing at this hour, MC?")

call screen phone_reply("Now that the sun has risen, my body and mind ache in loneliness.","choice121","I was just bored lol","choice122")

label choice121:
    call phone_after_menu
    call message_start_m("MC", "Now that the sun has risen, my body and mind ache in loneliness.")
    call message_z("ZEN", "If your body and mind feel lonely whenever the sun rises… you must be lonely every day.")
    call message_z("ZEN", "Except when it rains.")
    call message_ju("Jumin Han", "The sun rises on rainy days too.")
    call message_ju("Jumin Han", "I’ve kept my loneliness in check since a long time ago.")
    call message_ju("Jumin Han", "Excess emotion is a needless luxury.")
    call message_z("ZEN", "Such a robot. Whd")
    call message_ju("Jumin Han", "I’ll take that as a compliment.")
    call message_ju("Jumin Han", "Emotions only interfere with business.")
    call message_z("ZEN", "You’re the creepy one who sucks up to everyone to make them sign contracts.")
    call message_z("ZEN", "That’s what Jaehee said before.")
    call message_ju("Jumin Han", "What’s wrong with that?")

    call screen phone_reply("I’m lonely… I’m painfully lonely.","choice123","Jumin’s kinda scary ;;","choice124")

    label choice123:
        call phone_after_menu
        call message_start_m("MC", "I’m lonely… I’m painfully lonely.")
        call message_z("ZEN", "I… always get really lonely in the fall and winter.")
        call message_z("ZEN", "You know that moment right after you wake up and feel like you’re the only one in the world?")
        call message_z("ZEN", "As it gets closer to winter, the day gets shorter…")
        call message_ju("Jumin Han", "Haha.")
        call message_ju("Jumin Han", "If you’re busy like me, you never have time to feel lonely.")
        call message_z("ZEN", "Emotionless freak;;")

        jump aftermenu34

    label choice124:
        call phone_after_menu
        call message_start_m("MC", "Jumin’s kinda scary ;;")
        call message_z("ZEN", "Right? He’s a creep.")
        call message_ju("Jumin Han", "It’s not so bad to be feared.")
        call message_z("ZEN", "MC, let’s ignore him and just talk among ourselves.")
        call message_z("ZEN", "Nothing good will come out by talking to him.")
        call message_ju("Jumin Han", "Hmm… that’s too black and white.")

        jump aftermenu34

    jump aftermenu34

label choice122:
    call phone_after_menu
    call message_start_m("MC", "I was just bored lol")
    call message_ju("Jumin Han", "I see. I guess you come here for the same reason as Zen.")
    call message_z("ZEN", "What are you talking about. It’s the same for you too.")
    call message_ju("Jumin Han", "I won’t deny that.")
    call message_ju("Jumin Han", "This chat room is quite addictive.")
    call message_ju("Jumin Han", "I can brag about Elizabeth 3rd as much as I want.")
    call message_z("ZEN", "Whatever;;")
    call message_z("ZEN", "No one cares about cat pictures.")
    #… Zen emoji
    call message_ju("Jumin Han", "Take this.")
    call message_img_ju("jumin4.png")
    #Depressed Zen emoji

    call screen phone_reply3("Wow! So pretty.","choice125","Oh. A cat.","choice126","omfg…","choice127")

    label choice125:
        call phone_after_menu
        call message_start_m("MC", "Wow! So pretty.")
        call message_ju("Jumin Han", "Thank god at least one person appreciates her beauty.")

        jump aftermenu34

    label choice126:
        call phone_after_menu
        call message_start_m("MC", "Oh. A cat.")
        call message_ju("Jumin Han", "Hmm.")

        jump aftermenu34

    label choice127:
        call phone_after_menu
        call message_start_m("MC", "omfg…")
        call message_z("ZEN", "MC’s surprised! God.")
        call message_z("ZEN", "Are you okay?")
        call message_ju("Jumin Han", "A cat is not a bomb.")
        call message_ju("Jumin Han", "A cat is a cat.")

        jump aftermenu34

label aftermenu34:
    call message_ju("Jumin Han", "I tend to believe that a person who likes animals cannot be bad…")
    call message_z("ZEN", "You only believe what you want to believe.")
    call message_ju("Jumin Han", "Certainly, is that not life?")
    call message_z("ZEN", "Don’t pretend to be so above everything!")
    call message_ju("Jumin Han", "Anyways.")
    call message_ju("Jumin Han", "Cats are the best pet, so MC, you should look into it.")
    call message_ju("Jumin Han", "Elizabeth 3rd is the only one who sees me off to work.")
    call message_ju("Jumin Han", "She’s the only one I need.")
    call message_z("ZEN", "What are you talking about;; You make all of your maids see you off.")
    call message_ju("Jumin Han", "What I mean is… Elizabeth 3rd is the only one who sees me off with a loving soul.")
    call message_z("ZEN", "Loving soul lol")
    call message_z("ZEN", "If you treated your employees with a loving soul, they’d polish your shoes and lay out a red carpet.")
    call message_ju("Jumin Han", "It’s a waste giving yourself to people you’ve employed. It’s a business relationship. Money should be all there is to it.")
    call message_z("ZEN", "Well. That depends on the person.")
    call message_z("ZEN", "What do you think, MC?")

call screen phone_reply("It’s better to treat people like actual human beings than to be so strict.","choice128","Isn’t it natural to just work as much as you get paid.","choice129")

label choice128:
    call phone_after_menu
    call message_start_m("MC", "It’s better to treat people like actual human beings than to be so strict.")
    call message_ju("Jumin Han", "I forget what you call that.")
    call message_ju("Jumin Han", "A family-like company? Ha.")
    call message_z("ZEN", "MC, ignore that pompous jerk.")
    call message_z("ZEN", "The director that I work with is really nice to the actors.")
    call message_z("ZEN", "He buys us food with his own money and stays late to encourage us.")
    call message_z("ZEN", "So I enjoy every show.")
    call message_z("ZEN", "One director I worked with before just did his job and took his paycheck…")
    call message_z("ZEN", "And the result was just that too.")
    call message_ju("Jumin Han", "That’s a good example.")
    call message_ju("Jumin Han", "It’s not my style, but I should acknowledge that society is diverse.")

    jump aftermenu35

label choice129:
    call phone_after_menu
    call message_start_m("MC", "Isn’t it natural to just work as much as you get paid.")
    call message_ju("Jumin Han", "That is correct.")
    call message_z("ZEN", "There are a lot of people who don’t work as much as they get paid.")
    call message_z("ZEN", "If their bosses give them the look, they have to work more than what was agreed…")
    call message_ju("Jumin Han", "My company doesn’t have anything like that.")
    call message_z("ZEN", "I think that whatever you do… human emotions are always involved.")
    call message_ju("Jumin Han", "A true pro never involves emotions with work.")
    call message_z("ZEN", "Can anything valuable come out without any emotion?")
    call message_ju("Jumin Han", "You can think that way since you’re an actor.")
    call message_ju("Jumin Han", "Anyways, I agree with MC.")

    jump aftermenu35

label aftermenu35:
    call message_z("ZEN", "I’ve seen people online crying out that working in your company is like being a slave, but I may be wrong.")
    call message_ju("Jumin Han", "They should be honored to be my slaves. They are probably tears of joy.")

call screen phone_reply3("I’m pretty sure it’s tears of joy +_+","choice130","Can we change the subject?","choice131","Well… Labor management relations is always a complicated issue.","choice132")

label choice130:
    call phone_after_menu
    call message_start_m("MC", "I’m pretty sure it’s tears of joy +_+")
    call message_ju("Jumin Han", "Right?")
    call message_ju("Jumin Han", "It’s probably more so for people working close to me.")
    call message_ju("Jumin Han", "Since I directly… give directions and control them.")
    #… Zen emoji
    call message_z("ZEN", "That must be hell.")
    call message_ju("Jumin Han", "Yes.")
    call message_z("ZEN", "Didn’t expect MC to agree with that jerk;;")
    call message_ju("Jumin Han", "That is appropriate.")
    call message_z("ZEN", "I’m not in a good mood right now.")

    jump aftermenu36

label choice131:
    call phone_after_menu
    call message_start_m("MC", "Can we change the subject?")
    call message_z("ZEN", "I want pizza bread.")
    call message_ju("Jumin Han", "I don’t know why pizza bread exists.")
    call message_ju("Jumin Han", "Why do we need pizza bread when we have pizza?")
    call message_ju("Jumin Han", "All the franchise bakeries seem to sell it.")
    call message_ju("Jumin Han", "Hmm. Is it because people don’t have enough money to eat pizza?")
    call message_ju("Jumin Han", "It tastes like pizza, but it’s cheaper.")
    call message_ju("Jumin Han", "I guess it familiarizes commoners with the taste of pizza.")
    call message_z("ZEN", ";; I can’t watch you insult pizza bread any longer.")
    call message_z("ZEN", "Then do people buy coffee bread because they want coffee but it’s too expensive?")
    call message_ju("Jumin Han", "Your rebuttal is very strange and unappealing.")

    jump aftermenu36

label choice132:
    call phone_after_menu
    call message_start_m("MC", "Well… Labor management relations is always a complicated issue.")
    call message_z("ZEN", "Yeah. Let’s talk about something else.")
    call message_ju("Jumin Han", "We can talk about cats.")
    call message_("ZEN", "No.")
    call message_ju("Jumin Han", "MC, do you like cats?")

    call screen phone_reply("Cats are a bit scary.","choice133","I tend to like them.","choice134")

    label choice133:
        call phone_after_menu
        call message_start_m("MC", "Cats are a bit scary.")
        call message_z("ZEN", "I’m scared of them too!")
        call message_z("ZEN", "Their eyes glint at night.")
        call message_ju("Jumin Han", "It’s a misunderstanding.")
        call message_z("ZEN", "Still, scary is scary.")
        call message_z("ZEN", "We’re pretty similar, MC…")
        call message_z("ZEN", "I kind of like you.")
        #Winking heart Zen emoji
        call message_ju("Jumin Han", "Ha, I’ll respect your taste.")
        call message_ju("Jumin Han", "But I will faithfully pursue only cats.")

        jump aftermenu36

    label choice134:
        call phone_after_menu
        call message_start_m("MC", "I tend to like them.")
        call message_ju("Jumin Han", "I knew V has a good eye for people.")
        call message_z("ZEN", "You’re an animal loving girl.")
        call message_ju("Jumin Han", "Fluffly fur, cute and pink paws…")
        call message_ju("Jumin Han", "The perfect pet that is even affectionate.")
        call message_z("ZEN", "If I have to get a pet, I’d get a dog.")
        call message_z("ZEN", "A cat’s a bit too;;; sensitive. Not for me.")

        call screen phone_reply("I prefer dogs.","choice135","I prefer cats.","choice136")

        label choice135:
            call phone_after_menu
            call message_start_m("MC", "I prefer dogs.")
            call message_z("ZEN", "Right?")
            call message_z("ZEN", "I’m allergic to fur so I can’t have pets anyways.")
            call message_z("ZEN", "But that ‘unquestionable’ loyalty that dogs have… is so innocent and heartbreaking.")
            call message_z("ZEN", "Humans will never be like that.")
            call message_ju("Jumin Han", "Ha.")
            call message_z("ZEN", "It’s a quality that you don’t have at all.")
            call message_ju("Jumin Han", "I’m human so I don’t need that quality.")
            call message_ju("Jumin Han", "Cats are enough.")
            #… Zen emoji
            call message_z("ZEN", "Yeah yeah, go marry a cat.")
            call message_z("ZEN", "I won’t have to give congratulatory money then.")
            call message_ju("Jumin Han", "So you were actually thinking of paying.")
            #Surprised Zen emoji

            jump aftermenu36

        label choice136:
            call phone_after_menu
            call message_start_m("MC", "I prefer cats.")
            call message_ju("Jumin Han", "A woman who recognizes the beauty of cats. I’ll have to reconsider you.")
            call message_ju("Jumin Han", "Do you know that even Assistant Kang doesn’t care for cats?")
            call message_ju("Jumin Han", "My heart aches that this beautiful creature is not appreciated enough.")
            call message_z("ZEN", "Hmm….")
            call message_z("ZEN", "Well, maybe MC’s sensual like cats.")
            call message_z("ZEN", "I don’t like cats, but I do love cat-like women lol")
            call message_ju("Jumin Han", "I cannot believe you’ve turned our wonderful discussion of cats vulgar.")
            call message_ju("Jumin Han", "I hope we talk more about cats when Zen’s not here, MC.")

            jump aftermenu36

    jump aftermenu36

label aftermenu36:
    call message_ju("Jumin Han", "I don’t care what other people think.")
    call message_ju("Jumin Han", "Elizabeth 3rd’s love is all I need.")
    call message_z("ZEN", "I bet you sleep while hugging the cat.")
    call message_z("ZEN", "I can’t even begin to imagine all the fur on your bed.")
    call message_ju("Jumin Han", "…Did you just imagine my bed?")
    call message_z("ZEN", "Get lost.")
    #Angry Zen emoji
    call message_ju("Jumin Han", "Ha. If you live with one, you’ll see that they are the best animals. Oh, I guess you’ll never get to because of your allergy. How tragic. You are missing out on a big joy of life.")
    call message_z("ZEN", "Don’t care. I have plenty of other joys.")
    call message_z("ZEN", "I’m going to leave now to enjoy one of those which is reading fan letters and practicing my lines.")
    call message_z("ZEN", "Bye.")

call screen phone_reply("Good bye, lovely Zen ^^","choice137","Good bye.","choice138")

label choice137:
    call phone_after_menu
    call message_start_m("MC", "Good bye, lovely Zen ^^")
    call message_z("ZEN", "…Lovely Zen?")
    call message_z("ZEN", "omg. my heart just jumped a bit.")

    jump aftermenu37

label choice138:
    call phone_after_menu
    call message_start_m("MC", "Good bye.")
    call message_("ZEN", "Have a good day MC.")

    jump aftermenu37

label aftermenu37:
    call message_ju("Jumin Han", "I’m leaving first.")
    call message_ju("Jumin Han", "Adios…")
    "Jumin Han has left the chatroom."
    hide jumin_icon
    call message_z("ZEN", "What’s with that old man…;;")
    call message_z("ZEN", "Let’s talk again soon ^^")
    #Happy Zen emoji
    "ZEN has left the chatroom."
    hide zen_icon

    hide screen phone_message
    $ cr_p += 1
    hide mc_icon2
    stop music

init:
    $ signlvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)

show sign at signlvl

""
hide sign
hide phone2

jump hub
