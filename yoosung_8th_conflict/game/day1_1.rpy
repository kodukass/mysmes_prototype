#1st day – 00:03 – Welcome1

label day1_1:

call phone_start2

init:
    $ y_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)
    $ mc_icon_lvl2 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)

image yoosung_icon = Transform("yoosung_icon.png", zoom=.25)
image mc_icon2 = Transform("mc_icon.png", zoom=.205)

hide yoosung_icon
show yoosung_icon at y_icon_lvl
show mc_icon2 at mc_icon_lvl2

#chat

play music "y_theme_same.ogg"
call message_start_y("Yoosung★", "Hey!")
call message_y("Yoosung★", "I really want to know what kind of person you are, MC.")
call screen phone_reply3("Just one lonely sheep longing for someone’s arms.","choice53","I’m a pretty unique person.","choice54","I’m just an average person.","choice55")

label choice53:
    call phone_after_menu
    call message_start_m("MC", "Just one lonely sheep longing for someone’s arms.")
    call message_y("Yoosung★", "I… I’m not quite a wolf…")
    call message_y("Yoosung★", "But if you want.. I can turn into a wo, wolf…")
    call message_y("Yoosung★", "or maybe not T_T")

    call screen phone_reply("What’s a wolf? ^^","choice56","I’m gonna eat you up RAWR","choice57")

    label choice56:
        call phone_after_menu
        call message_start_m("MC", "What’s a wolf? ^^")
        $ y_h += 1
        call message_y("Yoosung★", "Oh ^^;;")
        call message_y("Yoosung★", "Uhm… It’s… ^^;")
        call message_y("Yoosung★", "Sorry..")
        call message_y("Yoosung★", "Just forget about it.")
        call message_y("Yoosung★", "I feel like I went out of line..")
        call message_y("Yoosung★", "You seem really innocent…")
        #blushing emoji
        call message_y("Yoosung★", "I’d like to meet you in person ^^")

        jump aftermenu24

    label choice57:
        call phone_after_menu
        call message_start_m("MC", "I’m gonna eat you up RAWR")
        $ y_h += 1
        call message_y("Yoosung★", "!?!?")
        call message_y("Yoosung★", ">//< Ah.. Well!")
        call message_y("Yoosung★", "It’s late now!!!")
        #blushing emoji

        jump aftermenu24

label choice54:
    call phone_after_menu
    call message_start_m("MC", "I’m a pretty unique person.")
    $ s_h += 1
    call message_y("Yoosung★", "Wow, you must have some sort of talent.")
    call message_y("Yoosung★", "I’m so jealous of people who are good of something.")
    call message_y("Yoosung★", "Seven has an immense personality too.")
    call message_y("Yoosung★", "Well… immense is the wrong word. It’s more like unmanageable ^^;")
    call message_y("Yoosung★", "But I think you two will get along pretty well!")
    call message_y("Yoosung★", "Seven is really busy all the time though T_T")
    call message_y("Yoosung★", "He’ll talk for hours and then disappear for a day or two.")

    jump aftermenu24

label choice55:
    call phone_after_menu
    call message_start_m("MC", "I’m just an average person.")
    call message_y("Yoosung★", "Wow, thanks for answering!")
    call message_y("Yoosung★", "I’m pretty normal too ^^")
    call message_y("Yoosung★", "I’m not as rich as Jumin…")
    call message_y("Yoosung★", "Next to Zen’s good looks, no one will look at me…")
    call message_y("Yoosung★", "I don’t have a cool career like Jaehee.")
    call message_y("Yoosung★", "And it’s not as if I have some extraordinary talent like Seven.")
    call message_y("Yoosung★", "But I try my best to stay confident. ^^")

    call screen phone_reply("It’s nice to see that you’re positive.","choice58","So what.","choice59")

    label choice58:
        call phone_after_menu
        call message_start_m("MC", "It’s nice to see that you’re positive.")
        $ y_h += 1
        call message_y("Yoosung★", "Thank you. ^^")
        call message_y("Yoosung★", "I try my best to stay positive.")
        call message_y("Yoosung★", "Don’t hesitate to come to me when you feel gloomy~!")
        #happy emoji

        jump aftermenu24

    label choice59:
        call phone_after_menu
        call message_start_m("MC", "So what.")
        call message_y("Yoosung★", "What?")
        call message_y("Yoosung★", "Oh…")
        call message_y("Yoosung★", "Uhm…")
        #crying emoji
        call message_y("Yoosung★", "You’re not intentionally being mean, are you?")
        call message_y("Yoosung★", "I hope I didn’t offend you or anything…")
        call message_y("Yoosung★", "I’m not sure what I did but I’m sorry.")
        call message_y("Yoosung★", "Could you please be nicer to me?")

        jump aftermenu25

    label aftermenu25:
        call screen phone_reply("Haha I’m joking.","choice60","Nope lol","choice61")

        label choice60:
            call phone_after_menu
            call message_start_m("MC", "Haha I’m joking.")
            call message_y("Yoosung★", "Haha.")
            call message_y("Yoosung★", "I’m sure you’re having fun teasing me.")

            jump aftermenu24

        label choice61:
            call phone_after_menu
            call message_start_m("MC", "Nope lol")
            $ y_h += 1
            call message_y("Yoosung★", "T_T")

            jump aftermenu24

label aftermenu24:
    call message_y("Yoosung★", "I want to chat with you often.")
    call message_y("Yoosung★", "I didn’t get to see the photo, but Seven said you’re cute and I believe him..!")

call screen phone_reply3("Lol you’re gonna be so surprised when you see me in person.","choice62","I’m not really the cute type…","choice63","Thank you ^^","choice64")

label choice62:
    call phone_after_menu

    call message_start_m("MC", "Lol you’re gonna be so surprised when you see me in person.")
    call message_y("Yoosung★", "Why? Because you’re really pretty!? Because you’re actually a movie star!?")

    call screen phone_reply("I hope so;","choice65","Ya.","choice66")

    label choice65:
        call phone_after_menu
        call message_start_m("MC", "I hope so;")
        call message_y("Yoosung★", "To be honest, I don’t really care for gorgeous and fancy people.")
        call message_y("Yoosung★", "Zen’s a pretty famous musical theater actor.")
        call message_y("Yoosung★", "He got so many girl fans because of his looks")
        call message_y("Yoosung★", "and now he’s a huge narcissist…")
        #crying emoji
        call message_y("Yoosung★", "Whenever he looks into the mirror, he smooths out his hair like twenty times. In a strange pose;;")
        call message_y("Yoosung★", "Kind of douchey haha")

        jump aftermenu26

    label choice66:
        call phone_after_menu
        call message_start_m("MC", "Ya.")
        call message_y("Yoosung★", "Omg so rad! haha")
        call message_y("Yoosung★", "But you know.")
        call message_y("Yoosung★", "I don’t really care about looks…")
        call message_y("Yoosung★", "Pretty strange…")
        call message_y("Yoosung★", "I just like anyone who can play games with me ^^")

        jump aftermenu26

label choice63:
    call phone_after_menu
    call message_start_m("MC", "I’m not really the cute type…")
    call message_y("Yoosung★", "Still, I like you!")
    call message_y("Yoosung★", "I think anyone with a good personality looks nice.")
    call message_y("Yoosung★", "^^")
    call message_y("Yoosung★", "…I say this but honestly I’ve never even dated a girl at my school!!!")

    jump aftermenu26

label choice64:
    call phone_after_menu
    call message_start_m("MC", "Thank you ^^")
    call message_y("Yoosung★", "You talk cute too haha")
    call message_y("Yoosung★", "You must really be a cutie.")
    call message_y("Yoosung★", "I am quite the cutie myself!")
    call message_y("Yoosung★", "I made a hat with a towel at the spa to wear")
    call message_y("Yoosung★", "and all my friends tackled me telling me how cute I am.")
    call message_y("Yoosung★", "I can never wear the towel hat because of that..T_T")

    jump aftermenu26

label aftermenu26:
    call message_y("Yoosung★", "If only I could visit Rika’s apartment, I’d be able to meet you…")
    call message_y("Yoosung★", "…But V told us not to go and I can’t disrespect him. T_T")
    call message_y("Yoosung★", "So please chat with me often ^^")
    call message_y("Yoosung★", "I’ll be off now to play games!")

call screen phone_reply("What games?","choice67","Have fun~","choice68")

label choice67:
    call phone_after_menu
    call message_start_m("MC", "What games?")
    call message_y("Yoosung★", "I play a game that is popular these days which is called LOLOL.")
    call message_y("Yoosung★", "Have you heard of it?")

    call screen phone_reply("LOLOL? League of Loneliness of Life?","choice69","LOLOL? Ludicrous Otaku and Lego Otaku’s Life?","choice70")

    label choice69:
        call phone_after_menu
        call message_start_m("MC", "LOLOL? League of Loneliness of Life?")
        call message_y("Yoosung★", "Wow! I can’t believe you know League of Loneliness of Life!")
        call message_y("Yoosung★", "Not a lot of girls know that game… Ur awesome!")
        call message_y("Yoosung★", "I play in the Shooting Star server ^^")
        call message_y("Yoosung★", "If you want to play with me, I usually play from 10PM to 4AM, so keep that in mind ^^")

        jump aftermenu27

    label choice70:
        call phone_after_menu
        call message_start_m("MC", "LOLOL? Ludicrous Otaku and Lego Otaku’s Life?")
        call message_y("Yoosung★", "…What?")
        call message_y("Yoosung★", "Ludicrous Otaku? Lego Otaku?")
        call message_y("Yoosung★", "What’s that?")
        #confused emoji
        call message_y("Yoosung★", "Oh… Maybe you like Lego..? ^^;")
        call message_y("Yoosung★", "I have some I used to play with as a kid. I’ll give them to you if I get the chance.")

        jump aftermenu27

label choice68:
    call phone_after_menu
    call message_start_m("MC", "Have fun~")

    jump aftermenu27

label aftermenu27:
    call message_y("Yoosung★", "I’ll be off now. ^^")
    call message_y("Yoosung★", "Don’t stay up too late and sleep tight~!")
    hide screen phone_message5
    hide yoosung_icon
    "Yoosung★ has left the chatroom."
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
