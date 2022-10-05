# # this brings up the message, first slot is the name, and second is the content
# # notice how it has _start at the end, the first one is special as there are no delays before it. use this for the first message
# call message_start("nadia", "hey, this is a phone texting thingy")  phone_message
#
# # added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
# call reply_message("oh really? what does it do lol")  phone_message3
#
# # this one is the same as the above one, but instead it has one more place for you to set an image
# # you have to make the image be small enough to fit the screen or its gonna stretch weird!
# call message_img("nadia", "it works with images too!","images/pic1.png")  phone_message_image
# call message_img("nadia", "receive cute pics from your friend","images/pic2.png")  phone_message_image
# call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird")  phone_message
# call message("nadia", "you can also do menus here")  phone_message
#
# # the next line is the menu system, first and third slot are the menu options, second and fourth one are what happens when you click it
#  phone_reply
# # i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
# call screen phone_reply("awesome!","choice1","lame","choice2")
# # i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
# ##call screen phone_reply3("awesome!","choice1","lame","choice2","im gay","choice3")
#
# label choice1:
#     # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
#     call phone_after_menu
#
#     # whenever you put the sender name to be "me" it is the player characters own message!
#     call message_start("me", "awesome")  phone_message2
#     call message("nadia", "i hope you like it")  phone_message
#
#     jump aftermenu
#
# label choice2:
#     call phone_after_menu
#     call message_start("me", "lame")  phone_message2
#     call message("nadia", "well, its a shame but your feelings are valid")  phone_message
#
#     jump aftermenu
#
# label choice3:
#     call phone_after_menu
#     call message_start("me", "im gay")
#     call message("nadia", "nice")
#
#     jump aftermenu
#
# label aftermenu:
#     call message("nadia", "check the code for comments on how the code works, thanks for your time!")  phone_message
#     call message("nadia", "the base for this code and this stretched phone background comes from cute demon crashers")  phone_message
#     call message("nadia", "the images were drawn by my gf @sloppydraws")  phone_message
#
#     # this one puts away the phone!
#     # call phone_end
#
# return
