#1st day – 04:35 – Zen’s complaint

label day1_3:

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

image mc_icon2 = Transform("mc_icon.png", zoom=.205)
image zen_icon = Transform("zen_icon.png", zoom=.18)

show mc_icon2 at mc_icon_lvl2
show zen_icon at z_icon_lvl

#chat

play music "z_theme_1.ogg"

call screen phone_reply("Hello, Zen.","choice85","In this dark endless night, art the water drops on the window my solitude, or thy teardrops.","choice86")

label choice85:
    call phone_after_menu

    call message_start_m("MC", "Hello, Zen.")
    call message_z("ZEN", "What’s a pretty lady staying up this late?")
    call message_z("ZEN", "Can’t fall asleep?")
    call message_z("ZEN", "Me neither.")
    call message_z("ZEN", "To be honest, my heart’s been beating so fast ever since you joined our group.")

    call screen phone_reply3("My heart’s beating fine.","choice88","^^;;","choice89","My heart’s beating fast too.","choice90")

    label choice88:
        call phone_after_menu

        call message_start_m("MC", "My heart’s beating fine.")
        call message_z("ZEN", "How could it be after seeing my looks…?")
        call message_z("ZEN", "Look at my profile photo.")
        call message_z("ZEN", "Look again.")
        call message_z("ZEN", "Look at it more.")
        call message_z("ZEN", "Your heart’s still not pounding?")

        call screen phone_reply3("A bit?","choice91","Nope;","choice92","*drool*","choice93")

        label choice91:
            call phone_after_menu

            call message_start_m("MC", "A bit?")
            $ z_h += 1
            call message_z("ZEN", "Yeah, that’s how it all starts.")
            call message_z("ZEN", "I don’t seem that attractive… just a bit over average??")
            call message_z("ZEN", "And then…")
            call message_z("ZEN", "As if… you’ve been pulled into a black hole")
            call message_z("ZEN", "you’re sucked into my infinite charm.")
            call message_z("ZEN", "You don’t have to take it all in at once.")

            jump aftermenu29

        label choice92:
            call phone_after_menu
            call message_start_m("MC", "Nope;")
            $ z_h -= 1
            call message_z("ZEN", "…Are you")
            call message_z("ZEN", "a guy?")
            #Surprised Zen emoji
            call message_z("ZEN", "Did Seven get the wrong information?;;")
            call message_z("ZEN", "Anyways… I get that my charm doesn’t work on you.")
            #Crying Zen emoji
            call message_z("ZEN", "I’m sorry I flirted a bit.")

            jump aftermenu29

        label choice93:
            call phone_after_menu
            call message_start_m("MC", "*drool*")
            $ z_h += 1
            call message_z("ZEN", "What;?")
            call message_z("ZEN", "Does that mean you like me?")
            call message_z("ZEN", "…")
            call message_z("ZEN", "I’m your type?")
            call message_z("ZEN", "I guess I’ll think of it that way for now lol")
            call message_z("ZEN", "Well… I do have a lot of fans who fell for my looks.")

            jump aftermenu29

    label choice89:
        call phone_after_menu
        call message_start_m("MC", "^^;;")
        call message_z("ZEN", "What is that polite you’re-making-me-uncomfortable emoji?")
        call message_z("ZEN", "Alright. I’ll stop haha")
        call message_z("ZEN", "You’re new, and I was just curious.")
        call message_z("ZEN", "Men can get playful no matter how old they are.")
        call message_z("ZEN", "Oh! But that doesn’t mean I’m old! Not at all!")

        jump aftermenu29

    label choice90:
        call phone_after_menu
        call message_start_m("MC", "My heart’s beating fast too.")
        call message_z("ZEN", "lol")
        call message_z("ZEN", "So cute.")
        call message_z("ZEN", "Can’t tell if your heart is really beating fast, or if you’re just typing that.")
        call message_z("ZEN", "I’ll have to see everything to know.")

        call screen phone_reply("Whuuut… Perv…","choice94","No thanks.","choice95")

        label choice94:
            call phone_after_menu
            call message_start_m("MC", "Whuuut… Perv…")
            $ z_h += 1
            call message_z("ZEN", "Perv? What’s going on inside your head?")
            call message_z("ZEN", "Hahahahaha")

            jump aftermenu29

        label choice95:
            call phone_after_menu
            call message_start_m("MC", "No thanks.")
            call message_z("ZEN", "lolol")
            call message_z("ZEN", "Aren’t I charming?")

            call screen phone_reply3("Screw you","choice96","Ya;;","choice97","I have quite an elaborate imagination.","choice98")

            label choice96:
                call phone_after_menu

                call message_start_m("MC", "Screw you")
                call message_z("ZEN", "That’s a pretty old school response.")
                call message_z("ZEN", "Lol, you’re quite funny.")

                jump aftermenu29

            label choice97:
                call phone_after_menu
                call message_start_m("MC", "Ya;;")
                call message_z("ZEN", "Are you blushing? lol")
                call message_z("ZEN", "Don’t. I’ll stop myself now.")
                call message_z("ZEN", "I was half joking lol")

                jump aftermenu29

            label choice98:
                call phone_after_menu
                call message_start_m("MC", "I have quite an elaborate imagination.")
                call message_z("ZEN", "Oh god.")
                call message_z("ZEN", "Now I’m blushing;;")

                jump aftermenu29

label choice86:
    call phone_after_menu
    call message_start_m("MC", "In this dark endless night, art the water drops on the window my solitude, or thy teardrops.")
    call message_z("ZEN", "Whut;;?")
    call message_z("ZEN", "Are you Shakespeare or something?")
    call message_z("ZEN", "Art thou from the Victorian age?")
    call message_z("ZEN", "Or do they teach sonnets at school these days?")

    call screen phone_reply("I’m Emily Bronte.","choice99","It’s not a sonnet.","choice100")

    label choice99:
        call phone_after_menu
        call message_start_m("MC", "I’m Emily Bronte.")
        $ z_h += 1
        call message_z("ZEN", "Oh, is Emily Bronte Shakespeare’s daughter?")
        call message_z("ZEN", "Maybe not?")
        #Confused Zen emoji
        call message_z("ZEN", "Again, didn’t do very well in school.")
        call message_z("ZEN", "Well anyways…")
        call message_z("ZEN", "I get that you’re being poetic.")
        call message_z("ZEN", "I don’t know what it really means though.")
        call message_z("ZEN", "But according to you, I’m crying and you’re lonely?")
        call message_z("ZEN", "Do you… want to see me… cry?")
        call message_z("ZEN", "Lol… Then you should have said so.")
        call message_z("ZEN", "I guess I do look pretty good… when I shed tears.")
        call message_z("ZEN", "I don’t really get it but a lot of girls say that. lol")
        call message_z("ZEN", "Hahaha")
        call message_z("ZEN", "Anyways… I’ll stop playing around.")

        jump aftermenu29

    label choice100:
        call phone_after_menu
        call message_start_m("MC", "It’s not a sonnet.")
        call message_z("ZEN", "Huh? Oh, I thought that anything with ‘art’ are called sonnets.")
        call message_z("ZEN", "Sorry. Didn’t do very well at school.")
        call message_z("ZEN", "Well anyways…")
        call message_z("ZEN", "I get that you’re being poetic.")
        call message_z("ZEN", "I don’t know what it really means though.")
        call message_z("ZEN", "But according to you, I’m crying and you’re lonely?")
        call message_z("ZEN", "Do you… want to see me… cry?")
        call message_z("ZEN", "Lol… Then you should have said so.")
        call message_z("ZEN", "I guess I do look pretty good… when I shed tears.")
        call message_z("ZEN", "I don’t really get it but a lot of girls say that. lol")
        call message_z("ZEN", "Hahaha")
        call message_z("ZEN", "Anyways… I’ll stop playing around.")

        jump aftermenu29

label aftermenu29:
    call message_z("ZEN", "I finally feel relieved now that you’ve joined the organization.")
    call message_z("ZEN", "To be honest, I don’t like any of the guys in the group.")
    call message_z("ZEN", "The Chairman-in-line is born with a silver spoon in his mouth and likes to brag about his money.")
    call message_z("ZEN", "Seven’s a funny guy but,")
    call message_z("ZEN", "sometimes he’s such a… weirdo;;")
    call message_z("ZEN", "Yoosung’s cute but he doesn’t really take me seriously.")
    call message_z("ZEN", "I stayed in the group because of V…^^")
    call message_z("ZEN", "I think it’ll be fun if we get to be friends.")
    call message_z("ZEN", "…It’s been five years since I’ve had a girlfriend. Damn.")

    call screen phone_reply4("Why that long?","choice101","You can go out with me.","choice102","It’s been longer for me.","choice103","You must be unattractive.","choice104")

    label choice101:
        call phone_after_menu
        call message_start_m("MC", "Why that long?")
        $ z_h += 1
        call message_z("ZEN", "Why that long?")
        call message_z("ZEN", "I wasted a couple of years trying to get in the industry..")
        call message_z("ZEN", "and now I’m too busy to meet people.")
        call message_z("ZEN", "Chatting and joking around like this is pretty much all I do these days.")

        jump aftermenu30

    label choice102:
        call phone_after_menu
        call message_start_m("MC", "You can go out with me.")
        $ z_h += 1
        call message_z("ZEN", "Wow…")
        call message_z("ZEN", "You’re a genius.")
        #Winking heart Zen emoji
        call message_z("ZEN", "Hahahaha")
        call message_z("ZEN", "Well~~")

        jump aftermenu30

    label choice103:
        call phone_after_menu
        call message_start_m("MC", "It’s been longer for me.")
        #Crying Zen emoji
        call message_z("ZEN", "T_T")
        call message_z("ZEN", "You’re more advanced than I am.")
        call message_z("ZEN", "Sorry I didn’t recognize that.")
        call message_z("ZEN", "But it’s probably not because you’re not attractive.")
        call message_z("ZEN", "I have the looks of a Greek God… but trying to earn a living and make a name for myself…")
        call message_z("ZEN", "Getting a girlfriend has become a dream.")
        call message_z("ZEN", "Let’s cheer up!")

        jump aftermenu30

    label choice104:
        call phone_after_menu
        call message_start_m("MC", "You must be unattractive.")
        $ z_h -= 1
        call message_z("ZEN", "Unattractive? lol")
        call message_z("ZEN", "I guess everyone has different tastes.")
        call message_z("ZEN", "I don’t think that I didn’t have a girlfriend because I’m unattractive.")
        call message_z("ZEN", "I was busy trying to survive in this world.")
        call message_z("ZEN", "Anyways, I get that I’m not your type.")

        jump aftermenu30

    label aftermenu30:
        call message_z("ZEN", "I think I’ll get a girlfriend when it’s time.")
        call message_z("ZEN", "It’s fun talking to you.")
        call message_z("ZEN", "I hope we can talk often lol")
        #Happy Zen emoji
        call message_z("ZEN", "Then I’ll go and rest now.")
        call message_z("ZEN", "Don’t stay up too late, pretty girl.")
        #Winking heart Zen emoji
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
