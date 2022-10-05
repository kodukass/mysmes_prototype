#1st day – 07:00 – Yoosung’s complaint

label day1_4:

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
    $ y_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)

image mc_icon2 = Transform("mc_icon.png", zoom=.205)
image yoosung_icon = Transform("yoosung_icon.png", zoom=.25)

show mc_icon2 at mc_icon_lvl2
show yoosung_icon at y_icon_lvl

#chat

play music "y_theme_same.ogg"
call message_start_y("Yoosung★", "Do you know that Zen always complains about being single these days?")
call message_y("Yoosung★", "But I’ve never even been in a relationship T_T")

call screen phone_reply3("Are you not interested in girls?","choice105","You’ve never had a girlfriend;;;?","choice106","Me too…","choice107")

label choice105:
    call phone_after_menu
    call message_start_m("MC", "Are you not interested in girls?")
    call message_y("Yoosung★", "I think I am interested.")
    call message_y("Yoosung★", "…I guess…")
    call message_y("Yoosung★", "I feel better when I team up with a girl character when playing games.")
    call message_y("Yoosung★", "And it makes it more interesting if there’s a girl in the guild…")
    call message_y("Yoosung★", "But of course, the competition always gets intense and I never get a chance… T_T")
    call message_y("Yoosung★", "I don’t think I’m not interested though.")
    call message_y("Yoosung★", "When Seven said that you’re a girl, my heart did… jump?! a little.")
    call message_y("Yoosung★", "Heehee…")

    jump aftermenu31

label choice106:
    call phone_after_menu
    call message_start_m("MC", "You’ve never had a girlfriend;;;?")
    call message_y("Yoosung★", "No…")
    call message_y("Yoosung★", "All I did in school was study…")
    call message_y("Yoosung★", "…and play in a band and become school president…")
    call message_y("Yoosung★", "I’ve been asked out on dates before!!!")
    call message_y("Yoosung★", "But I didn’t say ‘yes’ because I wanted to focus on study… And…")
    call message_y("Yoosung★", "…")
    call message_y("Yoosung★", "I can’t say any more T_T")

    call screen phone_reply3("Cheer up^^;","choice108","I’ll tell you how to get it on.","choice109","Hahahaha Tsk tsk","choice110")

    label choice108:
        call phone_after_menu
        call message_start_m("MC", "Cheer up^^;")
        call message_y("Yoosung★", "I don’t know how to cheer up…")
        call message_y("Yoosung★", "But I guess all you have to do is rely on your instincts(?)!?")
        call message_y("Yoosung★", "I’m twenty one now and that means I’m an adult!")

        jump aftermenu31

    label choice109:
        call phone_after_menu
        call message_start_m("MC", "I’ll tell you how to get it on.")
        call message_y("Yoosung★", "!?")
        call message_y("Yoosung★", "What?")
        call message_y("Yoosung★", "Uh… Does that mean;;")
        call message_y("Yoosung★", "Oh…")
        call message_y("Yoosung★", "I’m blushing… T_T")
        call message_y("Yoosung★", "Don’t tease me too much.")
        #Blushing Yoosung emoji

        jump aftermenu31

    label choice110:
        call phone_after_menu
        call message_start_m("MC", "Hahahaha Tsk tsk")
        call message_y("Yoosung★", "Omg…")
        call message_y("Yoosung★", "Are you laughing at me?")
        call message_y("Yoosung★", "…")
        call message_y("Yoosung★", "I guess I deserve that T_T")
        call message_y("Yoosung★", "But I feel weirdly comfortable getting laughed at…")
        call message_y("Yoosung★", "Haha…")

        jump aftermenu31

label choice107:
    call phone_after_menu
    call message_start_m("MC", "Me too…")
    call message_y("Yoosung★", "Oh…")
    call message_y("Yoosung★", "I knew you were innocent…!")
    call message_y("Yoosung★", "To be honest, no one’s as innocent as I am in the group.")
    call message_y("Yoosung★", "I’m probably the only one who’s never been in a relationship before.")
    #Crying Yoosung emoji
    call message_y("Yoosung★", "Well… I don’t know about Seven though…")
    call message_y("Yoosung★", "Anyways!!")
    call message_y("Yoosung★", "I’m not lonely because I have you!")
    call message_y("Yoosung★", ";; It’s a bit sad saying this buy")
    call message_y("Yoosung★", "let us single people cheer up!")
    call message_y("Yoosung★", "…Let’s get fried chicken together some time.")
    call message_y("Yoosung★", "T_T")

    call screen phone_reply("Fried chicken makes you fat… ^^;","choice111","Sounds kewl.","choice112")

    label choice111:
        call phone_after_menu
        call message_start_m("MC", "Fried chicken makes you fat… ^^;")
        call message_y("Yoosung★", "Oh…")
        call message_y("Yoosung★", "I… I see. I guess it’s wrong to ask a girl to eat fried chicken with me T_T")
        call message_y("Yoosung★", "Sorry…")

        jump aftermenu31

    label choice112:
        call phone_after_menu
        call message_start_m("MC", "Sounds kewl.")
        call message_y("Yoosung★", "Kewl!!!")
        call message_y("Yoosung★", "I really like you T_T")

        jump aftermenu31

label aftermenu31:
    call message_y("Yoosung★", "I have class at 9 so I have to go take the bus now.")
    call message_y("Yoosung★", "The poor fate of a college student…!")
    call message_y("Yoosung★", "Oh right! Do you want to see what I made for breakfast?")
    call message_img_y("yoosung2.png")

call screen phone_reply3("Enjoy your breakfast ^^","choice113","I wanna marry ya.","choice114","Gimme food too.","choice115")

label choice113:
    call phone_after_menu
    call message_start_m("MC", "Enjoy your breakfast ^^")
    call message_y("Yoosung★", "You have to eat breakfast too!")
    call message_y("Yoosung★", "Breakfast is your energy source for the day.")
    call message_y("Yoosung★", "I’d love to cook for you once we’re not banned from the apartment.")

    jump aftermenu32

label choice114:
    call phone_after_menu
    call message_start_m("MC", "I wanna marry ya.")
    call message_y("Yoosung★", "Whut")
    #Blushing Yoosung emoji

    jump aftermenu32

label choice115:
    call phone_after_menu
    call message_start_m("MC", "Gimme food too.")
    call message_y("Yoosung★", "I’ll cook for you next time ^^")

    jump aftermenu32

label aftermenu32:
    call message_y("Yoosung★", "I have to go now. I’m almost running late!")
    call message_y("Yoosung★", "MC, let’s talk soon! >_<")
    "Yoosung★ has left the chatroom."
    hide yoosung_icon
    hide screen phone_message5
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
