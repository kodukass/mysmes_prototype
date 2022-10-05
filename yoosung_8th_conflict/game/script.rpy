# The script of the game goes in this file.
# jump telo

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define y = Character("Yoosung")
# define m = Character("MC")
# define v = Character("V")
#
#
# # The game starts here.
#
# label start:
#
#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#
#     scene chatroom_hommik
#
#     # confirm screen
#
#     # "08:01 -Did you sleep well?-"
#
#     init:
#         $ textmclvl = Position(xpos=0.5, ypos=570, xanchor=0.5, yanchor=140)
#
#     show text_mc at textmclvl
#
#     ""
#
#     init:
#         $ textkesklvl = Position(xpos=0.4, ypos=575, xanchor=0.3, yanchor=140)
#
#     show text_mc at textmclvl + textkesklvl
#
#     show text_keskmine at textkesklvl
#
#     ""




    # init:
    #     $ yoosunglvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
    #
    # show yoosung happy at yoosunglvl
    #
    # "-Yoosung entered the chatroom-"
    #
    # menu:
    #
    #     "-Yoosung entered the chatroom-"
    #
    #     "Yoosung, did you sleep well?":
    #         m "Yoosung, did you sleep well?"
    #         #heart
    #         y "Did you have good dreams?"
    #         y "I missed you so much last night."
    #         y "You can't dream of anyone else other than me."
    #         y "I might get jealous.."
    #         # y blushing face
    #
    #
    #     "Yoosung! I missed you. Love love.":
    #         m "Yoosung! I missed you. Love love."
    #         y "MC!"
    #         y "Did I make you wait long? For you to be sp straight forward..."
    #         y "I missed you too."
    #
    # label after_menu1:
    #
    #     y "Can't believe I got a girlfriend"
    #     y "Before anyone else lol"
    #     y "I feel like I've won!"
    #
    #     menu:
    #
    #         "I feel like I've won!"
    #
    #         "You are a winner.":
    #             m "You are a winner."
    #             # heart
    #
    #         "Zen should get a girlfriend soon too~":
    #             m "Zen should get a girlfriend soon too~"
    #
    #     label after_menu2:
    #
    #         y "How do you always make me feel good?"
    #         y "I'm always a winner if you're by my side."
    #         # y happy emoji
    #         y "But do you think Zen really has a stalker?"

    # init:
    #     $ signlvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
    #
    # show sign at signlvl
    #
    # ""
    # menu:
    #
    #     ""
    #
    #     "Sign":
    #         label after_sign:

    # scene yoosung_tuba_2
    #
    # ##õige positsioon !ÄRA KUSTUTA ÄRA!
    # init:
    #     $ yoosunglvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
    #
    # show yoosung cry at yoosunglvl
    #
    # # These display lines of dialogue.
    #
    # y "This doesn't make sense"
    #
    # y "V's a liar"
    #
    # show yoosung eyes closed
    #
    # y "..."
    #
    # y "Rika"
    #
    # show yoosung cry
    #
    # y "Why did you disappear like that...?"
    #
    # init:
    #     $ signlvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
    #
    # show sign at signlvl
    #
    # ""


   # script

    # screen choice(items):
    #     style_prefix "choice"
    #
    #     vbox:
    #         for i in items:
    #             textbutton i.caption action i.action

    # screen choice(items):
    #
    # window:
    #     style "menu_window"
    #
    #     vbox:
    #         style "menu"
    #
    #         for i in items:
    #
    #             if i.action:
    #
    #                 button:
    #                     action i.action
    #                     style "menu_choice_button"
    #
    #                     text i.caption style "menu_choice"
    #
    #             else:
    #                 text i.caption style "menu_caption"

    ## This ends the game.

    # return
