#HUB

init:
    $ y_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)
    $ z_icon_lvl = Position(xpos=0.445, ypos=10, xanchor=0.445, yanchor=5)
    $ se_icon_lvl = Position(xpos=0.3913, ypos=10, xanchor=0.3913, yanchor=5)
    $ v_icon_lvl = Position(xpos=0.338, ypos=10, xanchor=0.338, yanchor=5)
    $ ju_icon_lvl = Position(xpos=0.6085, ypos=10, xanchor=0.6085, yanchor=5)
    $ ja_icon_lvl = Position(xpos=0.555, ypos=10, xanchor=.555, yanchor=5)
    $ u_icon_lvl = Position(xpos=0.285, ypos=10, xanchor=0.285, yanchor=5)
    $ mc_icon_lvl1 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)

show yoosung_icon at y_icon_lvl
show zen_icon at z_icon_lvl
show seven_icon at se_icon_lvl
# show v_icon at v_icon_lvl
show jumin_icon at ju_icon_lvl
show jaehee_icon at ja_icon_lvl
# show unknown_icon at u_icon_lvl
# show mc_icon at mc_icon_lvl

image yoosung_icon = Transform("yoosung_icon.png", zoom=.25)
image zen_icon = Transform("zen_icon.png", zoom=.18)
image seven_icon = Transform("seven_icon.png", zoom=.23)
image v_icon = Transform("v_icon.png", zoom=.1)
image jumin_icon = Transform("jumin_icon.jpg", zoom=.165)
image jaehee_icon = Transform("jaehee_icon.png", zoom=.203)
image unknown_icon = Transform("unknown_icon.png", zoom=.097)
image mc_icon1 = Transform("mc_icon.png", zoom=.205)

init:
    $ emailb_lvl = Position(xpos=0.43, ypos=200, xanchor=10, yanchor=60)
    $ historyb_lvl = Position(xpos=0.9, ypos=300, xanchor=10, yanchor=60)
    $ albumb_lvl = Position(xpos=0.9, ypos=150, xanchor=10, yanchor=50)
    $ exitb_lvl = Position(xpos=0.9, ypos=590, xanchor=10, yanchor=60)
    $ helpb_lvl = Position(xpos=0.9, ypos=445, xanchor=10, yanchor=60)
image emailb_full = Transform("emailb_full.png", zoom=1.3)
image historyb = Transform("historyb.png", zoom=1.3)
image albumb = Transform("albumb.png", zoom=1.3)
image exitb = Transform("exitb.png", zoom=1.3)
image helpb = Transform("helpb.png", zoom=1.3)

label hearts:
    $ z_h = 0
    $ s_h = 0
    $ y_h = 0
    $ ju_h = 0
    $ ja_h = 0

label cr_progress:
    $ cr_p = 0

#chatroom
style hub1 is default:
    properties gui.button_properties("choice_button")
    size 500
    xalign 500
    xsize 165
    ysize 165
    ypadding 500
    xpadding 500
    activate_sound "chatroom_select.ogg"
#email
style hub2 is default:
    properties gui.button_properties("choice_button")
    size 500
    xalign 0.48
    yalign 0.74
    xsize 110
    ysize 110
    ypadding 500
    xpadding 500
    activate_sound "chatroom_select.ogg"

#album
# screen hub3:
#     vbox at album_choice:
#         xalign 0
#         ypos 6000
#         xpos 200
#         yanchor 0.1
#
#     # activate_sound "chatroom_select.ogg"

style hub3 is default:
    xalign 0.8
    ypos 400
    yanchor 0.5

    # spacing gui.choice_spacing

screen hub1 (reply1, label1, reply2, label2, reply3, label3):
    modal True
    vbox:
        xalign 0.5
        yalign 0.74
        spacing 200

        textbutton "[reply1]" action Jump(label1) style "hub2"
        textbutton "[reply2]" action Jump(label2) style "hub1"
        # textbutton "[reply3]" action Jump(label3) style "hub3"


style choice_button1 is default:
    properties gui.button_properties("choice_button")
    #chatroomb_full

label hub:

    show hub
    play music "mainmenusound.ogg"
    show chatroomb_full
    show emailb_full at emailb_lvl
    show historyb at historyb_lvl
    show helpb at helpb_lvl
    show albumb at albumb_lvl
    show exitb at exitb_lvl
    show yoosung_icon at y_icon_lvl
    show zen_icon at z_icon_lvl
    show seven_icon at se_icon_lvl
    show jumin_icon at ju_icon_lvl
    show jaehee_icon at ja_icon_lvl
    # show v_icon at v_icon_lvl
    # show unknown_icon at u_icon_lvl
    # show mc_icon at mc_icon_lvl

call screen hub1("","choiceemail","","choicechat","","choicealbum")

label choiceemail:

    "This doesn't work yet sorry"
    jump hub

label choicealbum:

    "This doesn't work yet sorry"
    jump hub

label choicechat:

    if cr_p == 1:
        jump day1_1

    elif cr_p == 2:
        jump day1_2

    elif cr_p == 3:
        jump day1_3

    elif cr_p == 4:
        jump day1_4

    elif cr_p == 5:
        jump day1_5
