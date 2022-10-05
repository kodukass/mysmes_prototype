#SAMPLE TEXT CODE

# call message_start_y("Yoosung★", "")
# call message_start_s("707", "")
# call message_start_v("V", "")
# call message_start_ju("Jumin Han", "")
# call message_start_ja("Jaehee Kang", "")
# call message_start_z("ZEN", "")
# call message_start_u("Unknown", "")
# call message_start_m("me", "")
#
# call message_s("707", "")
# call message_y("Yoosung★", "")
# call message_z("ZEN", "")
# call message_ju("Jumin Han", "")
# call message_ja("Jaehee Kang", "")
# call message_v("V", "")
# call message_u("Unknown", "")
# call reply_message("MC", "")
#
# call message_("", "")
#
# call message_start_("", "")


#PILT

# call message_img_(".png")

#KAKS VALIKUT

# call screen phone_reply("","choice?","","choice?")
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
    # call message_("", "")
#
#     jump aftermenu?
#
# label aftermenu?:
#     call message_("", "")
#
#KOLM VALIKUT
#
# call screen phone_reply3("","choice?","","choice?","","choice?")
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label aftermenu?:
#     call message_("", "")

#NELI VALIKUT

# call screen phone_reply4("","choice?","","choice?","","choice?","","choice?")
#
# label choice?:
#     call phone_after_menu
#
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label choice?:
#     call phone_after_menu
#     call message_start_m("MC", "")
#     call message_("", "")
#
#     jump aftermenu?
#
# label aftermenu?:
#     call message_("", "")

#STORY MODE

#DIALOG
#
# m ""
#
#HÄÄL
#
# voice "asr.ogg"
# r ""

#CHATROOM ALGUS

# label day_:
#
# call phone_start2
#
# hide hub
# hide chatroomb_full
# hide emailb_full
# hide historyb
# hide helpb
# hide albumb
# hide exitb
# hide yoosung_icon
# hide zen_icon
# hide seven_icon
# hide jumin_icon
# hide jaehee_icon
#
# init:
#     $ mc_icon_lvl2 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)
#
# image mc_icon2 = Transform("mc_icon.png", zoom=.205)
#
# show mc_icon2 at mc_icon_lvl2
#
# play music ".ogg"

# #CHATROOM LÕPP

#     hide screen phone_message
#     $ cr_p += 1
#     hide mc_icon2
#     stop music
#
# init:
#     $ signlvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
#
# show sign at signlvl
#
# ""
# hide sign
# hide phone2
#
# jump hub
