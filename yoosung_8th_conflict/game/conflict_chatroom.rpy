# init:
#     $ vlvl = Position(xpos=0.1, ypos=150, xanchor=0.5, yanchor=100)
#
# show v neutral at vlvl
#
# ## dialoogi küsimus
#
# v "Luciel reached me."
# v "I want to talk to Yoosung."
# v "Hello, MC."
# v "I apologize for causing trouble because of this."
# v "Jaehee's analysis must be in correct. I came to talk to Yoosung."
# v "Perhaps I should come back later."
#
# init:
#     $ yoosunglvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)
#
# show yoosung angri at yoosunglvl
#
# "-Yoosung entered the chatroom-"
#
# menu:
#
#     "-Yoosung entered the chatroom-"
#
#     "Yoosung, you're here!":
#         m "Yoosung, you're here!"
#         v "Jaehee's pattern analysis was right."
#         y "MC... You're here too."
#         y "Is this time to talk about patterns?"
#         y "So Seven told you?"
#         v "Yes. It's been a long time."
#
#
#     "V, Yoosung's here. Give him your explanation now!":
#         m "V, Yoosung's here. Give him your explanation now!"
#         v "I assume MC is very angry at me as well."
#         y "Do you understand this situation?"
#         y "That vou're harming someone who's important to me!?"
#         v "It's been a while."
#
# label after_menu1:
#
#     y "Of course it's been a while."
#     y "Please.. Explain properly what's happening."
#     v "I heard that you are very angry with me..."
#     y "Can't we talk about this on the phone?"
#     y "Do we have to chat like this?"
#     v "I'm not able to talk on the phone."
#     y "You talk Seven all the time..."
#     v "I have a reason."
#
# menu:
#
#     v "I have a reason."
#
#     "What the hell is really happening?":
#         m "What the hell is really happening?"
#         v "Nothing is happening, for now."
#         y "What do you mean 'for now'? MC has to know."
#         y "She has to know who's trying to harm her!"
#         v "It's best not to assume that the person is aiming for MC. Who the hacker is... I still don't know all of it."
#         y "I can't stand it any longer."
#         y "You were like this about Rika too."
#
#
#     "I’m so nervous I can’t stand it…":
#         m "What the hell is really happening?"
#         v "I am so sorry that things ended up like this..."
#         v "But I will handle everything so that nothing bad happens."
#         y "Do you think an apology will take care of everything?"
#
# label after_menu2:
#
#     y "You never told me a word about"
#     y "what happened that drove Rika to kill herself..."
#     y "You just said things were complicated.."
#     y "but this is how you always are."
#     v "We've talked enough about that already."
#     y "Rika... would never have killed herself."
#     y "I'm sure about that!"
