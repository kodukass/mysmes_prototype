#1st day – 02:21 – Welcome2

label day1_2:

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
    $ ja_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)
    $ mc_icon_lvl2 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)

image jaehee_icon = Transform("jaehee_icon.png", zoom=.25)
image mc_icon2 = Transform("mc_icon.png", zoom=.205)

show jaehee_icon at ja_icon_lvl
show mc_icon2 at mc_icon_lvl2

#chat

play music "ja_theme_1.ogg"
call screen phone_reply("I still have no idea how to play this game T_T","choice71","Jaehee, why are you awake?","choice72")

label choice71:
    call phone_after_menu
    call message_start_m("MC", "I still have no idea how to play this game T_T")
    call message_ja("Jaehee Kang", "Game?")
    call message_ja("Jaehee Kang", "What are you talking about?")
    call message_ja("Jaehee Kang", "Rika’s work is not a ‘game’.")
    call message_ja("Jaehee Kang", "A ‘game’ is what Yoosung obsesses over every night and gives him dark circles.")

    call screen phone_reply("Sorry if I hurt your feelings^^;","choice73","I just said it because it looked fun.","choice74")

    label choice73:
        call phone_after_menu
        call message_start_m("MC", "Sorry if I hurt your feelings^^;")
        $ ja_h += 1
        call message_ja("Jaehee Kang", "you do not have to care about my feelings.")
        call message_ja("Jaehee Kang", "I am only Mr. Han’s assistant.")
        call message_ja("Jaehee Kang", "You cannot really consider me an official member as I am not personally acquainted with V.")
        call message_ja("Jaehee Kang", "Anyways, please do not refer it as a game.")
        call message_ja("Jaehee Kang", "It is a charity organization that Rika and V worked very hard to establish.")

        jump aftermenu28

    label choice74:
        call phone_after_menu
        call message_start_m("MC", "I just said it because it looked fun.")
        call message_ja("Jaehee Kang", "Fun…?")
        call message_ja("Jaehee Kang", "Is work fun to you?")
        call message_ja("Jaehee Kang", "You are quite peculiar.")
        call message_ja("Jaehee Kang", "You may feel a sense of accomplishment, but I’m not sure about fun.")
        call message_ja("Jaehee Kang", "I cannot understand you.")

        jump aftermenu28

label choice72:
    call phone_after_menu
    call message_start_m("MC", "Jaehee, why are you awake?")
    call message_ja("Jaehee Kang", "Hello.")
    call message_ja("Jaehee Kang", "I’ve been documenting what occurred today.")
    call message_ja("Jaehee Kang", "I guess… you could call it a journal.")

    call screen phone_reply("Aren’t you tired?","choice75","You’re so diligent.","choice76")

    label choice75:
        call phone_after_menu
        call message_start_m("MC", "Aren’t you tired?")
        call message_ja("Jaehee Kang", "I usually get three to four hours of sleep every day.")
        call message_ja("Jaehee Kang", "I usually stay awake at nights.")

        call screen phone_reply("Shouldn’t you be getting more sleep…?","choice77","I’m jealous that you don’t need a lot of sleep~!","choice78")

        label choice77:
            call phone_after_menu
            call message_start_m("MC", "Shouldn’t you be getting more sleep…?")
            $ ja_h += 1
            call message_ja("Jaehee Kang", "Are you worrying for me?")
            call message_ja("Jaehee Kang", "How gracious of you.")
            call message_ja("Jaehee Kang", "But please take care of yourself first?")
            call message_ja("Jaehee Kang", "It is not easy taking over Rika’s work.")
            call message_ja("Jaehee Kang", "If anything is difficult, I will help you.")

            jump aftermenu28

        label choice78:
            call phone_after_menu
            call message_start_m("MC", "I’m jealous that you don’t need a lot of sleep~!")
            call message_ja("Jaehee Kang", ";;;")
            call message_ja("Jaehee Kang", "It’s nothing to get jealous about.")
            call message_ja("Jaehee Kang", "You are jealous of unnecessary things…")

            jump aftermenu28

    label choice76:
        call phone_after_menu
        call message_start_m("MC", "You’re so diligent.")
        call message_ja("Jaehee Kang", "Being diligent is necessary to be an assistant.")
        call message_ja("Jaehee Kang", "Are you not a diligent person, MC?")

        call screen phone_reply("I am quite the diligent one.","choice79","I’m pretty lazy;","choice80")

        label choice79:
            call phone_after_menu
            call message_start_m("MC", "I am quite the diligent one.")
            call message_ja("Jaehee Kang", "I did not know you are diligent.")
            call message_ja("Jaehee Kang", "That is good but…")
            call message_ja("Jaehee Kang", "I would like to ask if you are really aware of the current situation…")
            call message_ja("Jaehee Kang", "A normal person would have been very surprised at what happened today.")
            call message_ja("Jaehee Kang", "To be honest, I do not fully trust you.")
            call message_ja("Jaehee Kang", "I advise you to be careful of what you say and do.")

            call screen phone_reply("Thank you for your advice.","choice81","Why are you being so fussy;;","choice82")

            label choice81:
                call phone_after_menu
                call message_start_m("MC", "Thank you for your advice.")
                $ ja_h += 1
                call message_ja("Jaehee Kang", "Oh… I apologize.")
                call message_ja("Jaehee Kang", "I went over the line.")
                call message_ja("Jaehee Kang", "Thank you for being so understanding.")

                jump aftermenu28

            label choice82:
                call phone_after_menu
                call message_start_m("MC", "Why are you being so fussy;;")
                $ ja_h -= 1
                call message_ja("Jaehee Kang", "Because I am an assistant.")
                call message_ja("Jaehee Kang", "Please do not complain and I hope you hone your skills and take care of Rika’s work.")
                call message_ja("Jaehee Kang", "You can ask me for help anytime.")

                jump aftermenu28

        label choice80:
            call phone_after_menu
            call message_start_m("MC", "I’m pretty lazy;")
            call message_ja("Jaehee Kang", "I see.")
            call message_ja("Jaehee Kang", "I admire your honesty.")
            call message_ja("Jaehee Kang", "However.")
            call message_ja("Jaehee Kang", "Being lazy becomes a habit.")
            call message_ja("Jaehee Kang", "…I hope I don’t sound like I’m lecturing you.")

            call screen phone_reply("You do;;","choice83","It’s nothing. You’re just concerned for me.","choice84")

            label choice83:
                call phone_after_menu
                call message_start_m("MC", "You do;;")
                call message_ja("Jaehee Kang", "I apologize if I’ve offended you.")

                jump aftermenu28

            label choice84:
                call phone_after_menu
                call message_start_m("MC", "It’s nothing. You’re just concerned for me.")
                call message_ja("Jaehee Kang", "Thank you for thinking so.")
                call message_ja("Jaehee Kang", "All the members in the organization are good people…")
                call message_ja("Jaehee Kang", "But they tend to ignore what I say thinking I am only nitpicking.")
                call message_ja("Jaehee Kang", "It’s probably because I do not talk in a charming way.")
                call message_ja("Jaehee Kang", "Maybe you would be better than I am in that area.")

                jump aftermenu28

label aftermenu28:
    call message_ja("Jaehee Kang", "If you are confused about Rika’s work, then I will explain.")
    call message_ja("Jaehee Kang", "Emails will be sent to the computer in Rika’s apartment.")
    call message_ja("Jaehee Kang", "The arrived emails will automatically be sent to your phone.")
    call message_ja("Jaehee Kang", "They will mostly be rsvp emails for the party or questions.")
    call message_ja("Jaehee Kang", "You must be selective and convincing so that the party goes well without any problems.")
    call message_ja("Jaehee Kang", "…")
    call message_ja("Jaehee Kang", "It is quite late.")
    call message_ja("Jaehee Kang", "I must go to bed now.")
    call message_ja("Jaehee Kang", "You must be quite exhausted as well. Have a good night’s rest…")
    call message_ja("Jaehee Kang", "Good bye.")

    hide screen phone_message9
    "Jaehee Kang has left the chatroom."
    hide jaehee_icon
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

return
