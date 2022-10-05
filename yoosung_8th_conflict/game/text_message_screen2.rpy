#SCREENS

############ phone code here########
# if you dont use  1920 x 1080 youre going to have to play with these numbers to get it to work and make the phone image be smaller somehow
# just keep changing stuff and refreshing the game until it works, sorry lol


init 5:
    #zen lvl
    style phone_message_vbox:
        xalign 0.445
        yalign 300
        ypos 380
        xsize 360
        xoffset -40

    # #mc lvl
    # style phone_message_vbox2:
    #     xalign 0.445
    #     yalign 300
    #     ypos 380
    #     xsize 360
    #     xoffset -40

    #zen värv
    style phone_message_frame:
        background Solid("#e4e4e4")
        ypadding 10
        xpadding 10

    #mc värv
    style phone_message_frame2:
        background Solid("#f4f4d4")
        ypadding 10
        xpadding 10

    #yoosung värv
    style phone_message_frame3:
        background Solid("#c4f4b4")
        ypadding 10
        xpadding 10

    style phone_message_contents:
        spacing 10

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0


    style phone_message_who is phone_message:
        color "#000000"
        size 25

    style phone_message_what is phone_message:
        color "#000000"
        size 24
    style phone_reply is default:
        size 18
        xalign 0.5
        xsize 475
        background Solid("#666")
        hover_background Solid("#f4f4d4")
        ypadding 10
        xpadding 10


screen phone_message(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -584
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#f4f4d4")
            xsize 200

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message3(what):
    vbox at incoming_message:
        style_group "phone_message3"
        xoffset -584
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message3"
            background Solid("#f4f4d4")
            xsize 200

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

# here is a new menu that has more options than two
# basically i just added one more textbutton here, and the additional labels needed in the call
# if you wish to make a menu with one or four just copy the code below and modify it a bit
screen phone_reply3(reply1, label1, reply2, label2, reply3, label3,):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"


style phone_reply_text:
    xalign 0.5

screen phone_message_image(who, what, img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"
                add img
