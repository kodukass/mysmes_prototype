#SCRIPT

# # The game starts here.
# #
# label start:
# # always start with this, it hides the regular text box, brings up the phone and has a short delay
# most of these calls include delays to make this look nicer
# you can find the code behind these calls in options.rpy
# call phone_start
#
# init:
#     $ y_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)
#     $ z_icon_lvl = Position(xpos=0.445, ypos=10, xanchor=0.445, yanchor=5)
#     $ se_icon_lvl = Position(xpos=0.3913, ypos=10, xanchor=0.3913, yanchor=5)
#     $ v_icon_lvl = Position(xpos=0.338, ypos=10, xanchor=0.338, yanchor=5)
#     $ ju_icon_lvl = Position(xpos=0.6085, ypos=10, xanchor=0.6085, yanchor=5)
#     $ ja_icon_lvl = Position(xpos=0.555, ypos=10, xanchor=.555, yanchor=5)
#     $ u_icon_lvl = Position(xpos=0.285, ypos=10, xanchor=0.285, yanchor=5)
#     $ mc_icon_lvl = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)
#
# show yoosung_icon at y_icon_lvl
# show zen_icon at z_icon_lvl
# show seven_icon at se_icon_lvl
# show v_icon at v_icon_lvl
# show jumin_icon at ju_icon_lvl
# show jaehee_icon at ja_icon_lvl
# show unknown_icon at u_icon_lvl
# show mc_icon at mc_icon_lvl
#
# image yoosung_icon = Transform("yoosung_icon.png", zoom=.25)
# image zen_icon = Transform("zen_icon.png", zoom=.18)
# image seven_icon = Transform("seven_icon.png", zoom=.23)
# image v_icon = Transform("v_icon.png", zoom=.1)
# image jumin_icon = Transform("jumin_icon.jpg", zoom=.165)
# image jaehee_icon = Transform("jaehee_icon.png", zoom=.203)
# image unknown_icon = Transform("unknown_icon.png", zoom=.097)
# image mc_icon = Transform("mc_icon.png", zoom=.205)

#OPTIONS

image phone1 = "images/chatroom_hacked1.png"
image phone2 = "images/chatroom_hommik1.png"

# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300

#zen
transform phone_message_bubble_tip:
    xoffset 196
    yoffset -10
#saeran
transform phone_message_bubble_tip3:
    xoffset -2
    yoffset -10
#mc
transform phone_message_bubble_tip2:
    xoffset 170
    yoffset -10
#yoosung
transform phone_message_bubble_tip4:
    xoffset 262
    yoffset -10
#seven
transform phone_message_bubble_tip5:
    xoffset 130
    yoffset -10
#v
transform phone_message_bubble_tip6:
    xoffset 65
    yoffset -10
#jumin
transform phone_message_bubble_tip7:
    xoffset 398
    yoffset -10
#jaehee
transform phone_message_bubble_tip8:
    xoffset 331
    yoffset -10

transform scrolling_out_message:
    easeout 0 yoffset -30 alpha 0

transform incoming_message:
    yoffset 200
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message


#### labels to shortcut stuff so you dont need to copypaste stuff repeatedly! #####
#hacked bg
label phone_start:
    window hide
    show phone1 at phone_pickup
    $ renpy.pause(0.2)
    return
#hommik bg
label phone_start2:
    window hide
    show phone2 at phone_pickup
    $ renpy.pause(0.2)
    return
#zen pilt
label phone_msgi_z:
    $ renpy.pause()
    hide screen phone_message_image_z
    $ renpy.pause(0.1)
    return
#zen
label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return
#mc
label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return
#saeran
label phone_msg3:
    $ renpy.pause()
    hide screen phone_message4
    $ renpy.pause(0.1)
    return
#yoosung
label phone_msg4:
    $ renpy.pause()
    hide screen phone_message5
    $ renpy.pause(0.1)
    return
#seven
label phone_msg5:
    $ renpy.pause()
    hide screen phone_message6
    $ renpy.pause(0.1)
    return
#v
label phone_msg6:
    $ renpy.pause()
    hide screen phone_message7
    $ renpy.pause(0.1)
    return
#jumin
label phone_msg7:
    $ renpy.pause()
    hide screen phone_message8
    $ renpy.pause(0.1)
    return
#jaehee
label phone_msg8:
    $ renpy.pause()
    hide screen phone_message9
    $ renpy.pause(0.1)
    return
#saeran pilt
label phone_msgi_u:
    $ renpy.pause()
    hide screen phone_message_image_u
    $ renpy.pause(0.1)
    return
#yoosung pilt
label phone_msgi_y:
    $ renpy.pause()
    hide screen phone_message_image_y
    $ renpy.pause(0.1)
    return
#v pilt
label phone_msgi_v:
    $ renpy.pause()
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    return
#jumin pilt
label phone_msgi_ju:
    $ renpy.pause()
    hide screen phone_message_image_ju
    $ renpy.pause(0.1)
    return
#jaehee pilt
label phone_msgi_ja:
    $ renpy.pause()
    hide screen phone_message_image_ja
    $ renpy.pause(0.1)
    return
#seven pilt
label phone_msgi_s:
    $ renpy.pause()
    hide screen phone_message_image_s
    $ renpy.pause(0.1)
    return

label phone_after_menu:
    # $ renpy.pause(0)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    return

label phone_end:
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    show phone at phone_hide
    $ renpy.pause(0.2)
    return

label message_u(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message4(who, what)
    return

label message_y(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message5(who, what)
    return
#seven
label message_s(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message6(who, what)
    return

label message_z(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

label message_v(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message7(who, what)
    return

label message_ju(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message8(who, what)
    return

label message_ja(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message9(who, what)
    return
#me
label reply_message(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    # $ renpy.pause(0.1)
    return

label message_img_u(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_u(img)
    # $ renpy.pause(0.1)
    return

label message_img_z(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_z(img)
    # $ renpy.pause(0.1)
    return

label message_img_y(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_y(img)
    # $ renpy.pause(0.1)
    return

label message_img_ju(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_ju(img)
    # $ renpy.pause(0.1)
    return

label message_img_ja(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_ja(img)
    # $ renpy.pause(0.1)
    return

label message_img_s(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_s(img)
    # $ renpy.pause(0.1)
    return

label message_img_v(img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    hide screen phone_message5
    hide screen phone_message6
    hide screen phone_message7
    hide screen phone_message8
    hide screen phone_message9
    hide screen phone_message_image_u
    hide screen phone_message_image_z
    hide screen phone_message_image_y
    hide screen phone_message_image_ju
    hide screen phone_message_image_ja
    hide screen phone_message_image_s
    hide screen phone_message_image_v
    $ renpy.pause(0.1)
    show screen phone_message_image_v(img)
    # $ renpy.pause(0.1)
    return

#saeran
label message_start_u(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message4(who, what)
    return

#seven
label message_start_s(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message6(who, what)
    return

#yoosung
label message_start_y(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message5(who, what)
    return

#zen
label message_start_z(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

#v
label message_start_v(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message7(who, what)
    return

#jumin
label message_start_ju(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message8(who, what)
    return

#jaehee
label message_start_ja(who, what):
    if who.lower() == "MC":
        show screen phone_message2(who, what)
    else:
        show screen phone_message9(who, what)
    return

#me
label message_start_m(who, what):
    show screen phone_message2(who, what)
return

#SCREENS

############ phone code here########
# if you dont use  1920 x 1080 youre going to have to play with these numbers to get it to work and make the phone image be smaller somehow
# just keep changing stuff and refreshing the game until it works, sorry lol


init 5:

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

    #saeran värv
    style phone_message_frame4:
        background Solid("#ebb0ff")
        ypadding 10
        xpadding 10

    #seven värv
    style phone_message_frame5:
        background Solid("#fedbd0")
        ypadding 10
        xpadding 10

    #v värv
    style phone_message_frame6:
        background Solid("#a0e4f3")
        ypadding 10
        xpadding 10

    #jumin värv
    style phone_message_frame7:
        background Solid("#cedef2")
        ypadding 10
        xpadding 10

    #jaehee värv
    style phone_message_frame8:
        background Solid("#edd3ae")
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
        properties gui.button_properties("choice_button")
        size 100
        xalign 20
        xsize 600
        ypadding 18
        xpadding 100
        activate_sound "chatroom_select.ogg"

#saatja zen
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

#saatja saeran
screen phone_message4(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip3.png" at phone_message_bubble_tip3

        frame:
            style_group "phone_message"
            background Solid("#ebb0ff")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#saatja yoosung
screen phone_message5(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip4.png" at phone_message_bubble_tip4

        frame:
            style_group "phone_message"
            background Solid("#c4f4b4")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#saatja seven
screen phone_message6(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip5.png" at phone_message_bubble_tip5

        frame:
            style_group "phone_message"
            background Solid("#fedbd0")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#saatja v
screen phone_message7(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip6.png" at phone_message_bubble_tip6

        frame:
            style_group "phone_message"
            background Solid("#a0e4f3")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#saatja jumin
screen phone_message8(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip7.png" at phone_message_bubble_tip7

        frame:
            style_group "phone_message8"
            background Solid("#cedef2")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#saatja jaehee
screen phone_message9(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip8.png" at phone_message_bubble_tip8

        frame:
            style_group "phone_message"
            background Solid("#edd3ae")

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

#vastaja menu
screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset 200
        xalign 0.5
        yoffset 80
        yalign 1
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#f4f4d4")
            xsize 200

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                text what style "phone_message_what"
#vastaja tavaline
screen phone_message3(what):
    vbox at incoming_message:
        style_group "phone_message3"
        xoffset 120
        xalign 0.5
        yoffset 80
        yalign 1
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#f4f4d4")
            xsize 200

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

style choice_button is default:
    properties gui.button_properties("choice_button")

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

screen phone_reply4(reply1, label1, reply2, label2, reply3, label3, reply4, label4):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"
        textbutton "[reply4]" action Jump(label4) style "phone_reply"

style phone_reply_text:
    xalign 0.5

# screen phone_message_image_z(who, what, img):
screen phone_message_image_z(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_u(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip3.png" at phone_message_bubble_tip3

        frame:
            style_group "phone_message"
            background Solid("#ebb0ff")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_y(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip4.png" at phone_message_bubble_tip4

        frame:
            style_group "phone_message"
            background Solid("#c4f4b4")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_ju(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip7.png" at phone_message_bubble_tip7

        frame:
            style_group "phone_message"
            background Solid("#cedef2")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_ja(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip8.png" at phone_message_bubble_tip8

        frame:
            style_group "phone_message"
            background Solid("#edd3ae")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_s(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip5.png" at phone_message_bubble_tip5

        frame:
            style_group "phone_message"
            background Solid("#fedbd0")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img

screen phone_message_image_v(img):
    vbox at incoming_message:
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip6.png" at phone_message_bubble_tip6

        frame:
            style_group "phone_message"
            background Solid("#a0e4f3")

            vbox:
                style "phone_message_contents"
                # text who style "phone_message_who"
                # text what style "phone_message_what"
                add img
