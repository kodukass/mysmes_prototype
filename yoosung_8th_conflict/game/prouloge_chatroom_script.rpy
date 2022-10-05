
 #PROULOGE
 label start:
         $ z_h = 0
         $ s_h = 0
         $ y_h = 0
         $ ju_h = 0
         $ ja_h = 0

         $ cr_p = 0

 menu:

     "What gamemode?"

     "Casual/Deep Story":
         jump intro_start

     "Another Story":
         jump another_story
         # jump error

 # label error:
 #     # "Sorry it's not finished :("
 #     # "I'll choose Casual/Deep Story for you :)"
 #     # "One moment..."
 #     # jump intro_start
 #     jump another_story

 label intro_start:

 menu:

     "Watch intro-video?"

     "Yes":
         jump intro


     "No":
         jump start_start

 label intro:
     $ renpy.movie_cutscene("intro.mpg")
     jump start_start

 define m = Character("MC")
 define u = Character("Unknown")

 init:
     $ u_icon_lvl = Position(xpos=0.285, ypos=10, xanchor=0.285, yanchor=5)
     $ mc_icon_lvl = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)

 # show unknown_icon at u_icon_lvl
 # show mc_icon at mc_icon_lvl

 image unknown_icon = Transform("unknown_icon.png", zoom=.097)
 image mc_icon = Transform("mc_icon.png", zoom=.205)

 label start_start:

 stop music
 $ renpy.movie_cutscene("hakkvait.mpg")
 call phone_start
 show unknown_icon at u_icon_lvl
 show mc_icon at mc_icon_lvl

 call message_start_u("Unknown", "...Hello...?")

 call reply_message("MC", "?")

 call message_u("Unknown", "Can you see this?")

 call screen phone_reply("Yes, I can.","choice1","Who are you?","choice2")

 label choice1:
     call phone_after_menu

     call message_start_m("MC", "Yes, I can.")
     call message_u("Unknown", "... Finally connected. Thank god.")

     jump aftermenu

 label choice2:
     call phone_after_menu
     call message_start_m("MC", "Who are you?")

     jump aftermenu

 label aftermenu:
     call message_u("Unknown", "I'm sure you're surprised.")
     call message_u("Unknown", "It’s not everyday you get a text from a stranger.")
     call message_u("Unknown", "I’m a bit flustered myself. I found a smartphone at the subway station, but all it had was this messenger app.")
     call message_u("Unknown", "I want to find the owner, but I don’t see any contact info or call records…")
     call message_u("Unknown", "I’ve been sending messages with this app but no reply…")
     call message_u("Unknown", "All I see is an address and some important-looking numbers saved in notes.")
     call message_u("Unknown", "I’d like to go there myself but I’m currently abroad…")

 call screen phone_reply3("First… who are you?","choice3","I thought this app was for chatting with pretty boys?","choice4","An address?","choice5")

 label choice3:
     call phone_after_menu

     call message_start_m("MC", "First… who are you?")
     call message_u("Unknown", "Me? Oh sorry. I didn’t even introduce myself.")
     call message_u("Unknown", "I’m just… a student studying abroad. I’m Korean.")
     call message_u("Unknown", "I could tell you my name, but it doesn’t really matter.")
     call message_u("Unknown", "You won’t find me on search engines. ^^;")
     call message_u("Unknown", "But, anyways…")
     call message_u("Unknown", "Can you help me find the owner of this phone?")

     jump aftermenu2

 label choice4:
     call phone_after_menu
     call message_start_m("MC", "I thought this app was for chatting with pretty boys?")
     call message_u("Unknown", "What? Oh.")
     call message_u("Unknown", "I guess you’re seeing this message because of something you downloaded.")
     call message_u("Unknown", "I’m not sure, but I think it’s an app that’s connected to the one I’m using?")
     call message_u("Unknown", "Can you help me find the owner of this phone?")

     jump aftermenu2

 label choice5:
     call phone_after_menu
     call message_start_m("MC", "An address?")
     call message_u("Unknown", "Yes. There’s a Korean address and a long number. I think it’s a password.")
     call message_u("Unknown", "Do you mind going to the address?")
     call message_u("Unknown", "That’s all that’s saved in this phone.")

     jump aftermenu2

 label aftermenu2:
     call message_u("Unknown", "I know you’re surprised to have someone suddenly pop up and ask you a favor like this.")
     call message_u("Unknown", "But still…")
     call message_u("Unknown", "I’d appreciate it if you could help.")

 call screen phone_reply4("Why should I help you?","choice6","Uh… Why are you talking to me as if I’m your friend?","choice7","Why are you obsessed with finding the owner? You can just give it to the police or the post office.","choice8", "How can I help you?", "choice9")

 label choice6:
     call phone_after_menu

     call message_start_m("MC", "Why should I help you?")
     call message_u("Unknown", "Since you’re the only clue I have.")
     call message_u("Unknown", "I’ve been trying to find the owner with this phone, but I didn’t find any clues until now.")
     call message_u("Unknown", "I would really like to find the owner.")
     call message_u("Unknown", "Then God will be happy.")
     call message_u("Unknown", "Oh! Sorry I didn’t mention it before. I’m religious.")
     call message_u("Unknown", "Never mind what I just said. I’m sorry if I weirded you out.")
     call message_u("Unknown", "Can you please help me? I’ll make it up to you if I get to go back to Korea.")

     jump aftermenu3

 label choice7:
     call phone_after_menu
     call message_start_m("MC", "Uh… Why are you talking to me as if I’m your friend?")
     call message_u("Unknown", "Oh. Sorry. ^^;")
     call message_u("Unknown", "Living aboard makes you lonely.")
     call message_u("Unknown", "You don’t have to be such a stranger too…")
     call message_u("Unknown", "Anyways, can you please help me?")
     call message_u("Unknown", "I’d really like to find the owner.")
     call message_u("Unknown", "It’d be great if you could go to the address and find some hints.")

     jump aftermenu3

 label choice8:
     call phone_after_menu
     call message_start_m("MC", "Why are you obsessed with finding the owner? You can just give it to the police or the post office.")
     call message_u("Unknown", "Well… Normal people won’t be able to understand…")
     call message_u("Unknown", "To be honest, I have a religion.")
     call message_u("Unknown", "My religion says that you must not miss any opportunity to do good, no matter how small.")
     call message_u("Unknown", "Well, some say that it’s just being nosy.")
     call message_u("Unknown", "But I’m not like normal people.")
     call message_u("Unknown", "I can’t help but think about how stressed the owner might be…")

     jump aftermenu3

 label choice9:
     call phone_after_menu
     call message_start_m("MC", "How can I help you?")
     call message_u("Unknown", "Uhm… I’d like for you to go to the address saved here.")
     call message_u("Unknown", "I saw the street view through the internet, and I’ve been there before.")
     call message_u("Unknown", "It’s an apartment in downtown. Very crowded.")

     jump aftermenu3

 label aftermenu3:
     call message_u("Unknown", "It’s really a safe place. If you feel unsafe, you can turn around.")
     call message_u("Unknown", "I know the area. It’s developed.")
     call message_u("Unknown", "Please?")

 call screen phone_reply("No. You’re creepy.","choice10","Fine… I’m leaving right away if it feels sketchy.","choice11")

 label choice10:
     call phone_after_menu
     call message_start_m("MC", "No. You’re creepy.")
     call message_u("Unknown", "Creepy?…^^;;")
     call message_u("Unknown", "I’m not a creep.")
     call message_u("Unknown", "Haven’t you ever heard of the saying ‘you get a treat if you listen to older men’…?")

     call screen phone_reply("I’ll listen to you.","choice12","No;;","choice13")

     label choice12:
         call phone_after_menu
         call message_start_m("MC", "I’ll listen to you.")
         call message_u("Unknown", "Haha, I was joking.")
         call message_u("Unknown", "But you seem like you’ll listen to me^^")

         jump aftermenu5

     label choice13:
         call phone_after_menu
         call message_start_m("MC", "No;;")
         call message_u("Unknown", "Sorry. I was just kidding ^^;;;")

         jump aftermenu5

     label aftermenu5:
         call message_u("Unknown", "Anyways…")
         call message_u("Unknown", "I know I’m asking too much.")
         call message_u("Unknown", "You might think I’m odd.")
         call message_u("Unknown", "…I am a bit odd to be honest.")
         call message_u("Unknown", "But would you consider it? I’m talking to you right now.")
         call message_u("Unknown", "Two complete strangers at two completely different places… It’s a miracle we’ve connected.")
         call message_u("Unknown", "No one responded to my messages. You’re the first one.")
         call message_u("Unknown", "I don’t know how we got connected…")
         call message_u("Unknown", "But maybe this was meant to be?")
         call message_img_u("common_52.png")
         call message_u("Unknown", "That is me in the photo.")
         call message_u("Unknown", "Maybe this will make you less suspicious…?")
         call message_u("Unknown", "I’m returning to Korea soon, so I’ll definitely make it up to you.")
         call message_u("Unknown", "If you feel unsafe near the place, you can just delete the app.")
         call message_u("Unknown", "Please, I’m begging you.")
         call reply_message("MC", "Alright… I’m returning asap if something seems strange.")

         jump aftermenu4

 label choice11:
     call phone_after_menu
     call message_start_m("MC", "Fine… I’m leaving right away if it feels sketchy.")

     jump aftermenu4

 label aftermenu4:
     call message_u("Unknown", "You trust me…")
     call message_u("Unknown", "Thank you!")
     call message_u("Unknown", "Just a sec. I’ll send you the address.")
     call message_u("Unknown", "Found it.")
     call message_u("Unknown", "< /Address/ Clink Link >")
     call message_u("Unknown", "< /Address/ Clink Link >")

     hide screen phone_message4

     show uks kinni

     ""

     m "There is a password door lock."

     hide uks kinni

     call message_u("Unknown", "Are you there? ^^ See. Nothing strange.")
     call message_u("Unknown", "Is there a password lock on the door?")

 call screen phone_reply("Hmm. Don’t see one.","choice14","Yes.","choice15")

 label choice14:
     call phone_after_menu

     call message_start_m("MC", "Hmm. Don’t see one.")
     call message_u("Unknown", "That’s strange.")
     call message_u("Unknown", "There’s really nothing?")
     call message_u("Unknown", "There’s nothing to put in the password?")

     call screen phone_reply("JK. It’s here.","choice22","There’s nothing.","choice23")

     label choice22:
         call phone_after_menu
         call message_start_m("MC", "JK. It’s here.")
         call message_u("Unknown", "Haha, nice.")
         call message_u("Unknown", "You’re pretty funny.")

         jump aftermenu7

     label choice23:
         call phone_after_menu
         call message_start_m("MC", "There’s nothing.")
         hide screen phone_message2

         show uks kinni

         ""

         m "There is a password door lock."

         hide uks kinni
         call message_u("Unknown", "…")
         call message_u("Unknown", "You sure?")

         jump aftermenu11

     label aftermenu11:
         call screen phone_reply("JK. It’s here.","choice24","It’s not here.","choice25")

         label choice24:
             call phone_after_menu
             call message_start_m("MC", "JK. It’s here.")
             call message_u("Unknown", "Thank god.")
             call message_u("Unknown", "I get that you want to joke around")
             call message_u("Unknown", "but if it’s too much, I might take it the wrong way.")

             jump aftermenu7

         label choice25:
             call phone_after_menu
             call message_start_m("MC", "It’s not here.")

             jump bad_prouloge_ending

 label choice15:
     call phone_after_menu
     call message_start_m("MC", "Yes.")
     jump aftermenu7

 label aftermenu7:
     call message_u("Unknown", "I’ll send you the digits. Try it.")
     call message_u("Unknown", "< /Password/ Clink Link >")

 call screen phone_reply("(Pause for a moment.)","choice16","(Input the password.)","choice17")

 label choice16:
     call phone_after_menu

     call message_start_m("MC", "…Shouldn’t I ring the doorbell first?")
     call message_u("Unknown", "Hmm. You’re right!")
     call message_u("Unknown", "Sorry, I wasn’t thinking straight.")
     call message_u("Unknown", "Then ring the doorbell.")
     call message_u("Unknown", "Then ring the doorbell.")

     hide screen phone_message4

     show uks kinni

     ""

     m "(Ring the doorbell.)"
     m "(There is no answer.)"

     hide uks kinni

     jump aftermenu8

 label choice17:
     call phone_after_menu

     show uks kinni

     ""

     m "(Input the password.)"

     hide uks kinni

     show uks lahti

     ""

     hide uks lahti

     jump aftermenu9

 label aftermenu8:
     call screen phone_reply("I want to go back.;;","choice18","I don’t think anyone’s inside…","choice19")

     label choice18:
         call phone_after_menu
         call message_start_m("MC", "I want to go back.;;")
         call message_u("Unknown", "What? No.")
         call message_u("Unknown", "Soon, you’ll see the hottie")
         call message_u("Unknown", "Whoops… Typo.")
         call message_u("Unknown", "Put in the password.")
         call message_u("Unknown", "You can just leave a note. Yeah?")
         call reply_message("MC", "Okay… Alright.")
         call message_u("Unknown", "Good girl ^^")
         call message_u("Unknown", "Good girl ^^")

         hide screen phone_message4

         show uks kinni

         ""

         m "(Input the password.)"

         hide uks kinni

         show uks lahti

         ""

         hide uks lahti

         jump aftermenu9

     label choice19:
         call phone_after_menu
         call message_start_m("MC", "I don’t think anyone’s inside…")
         call message_u("Unknown", "Hmm. No choice then.")
         call message_u("Unknown", "I guess the place is empty.")
         call message_u("Unknown", "Why don’t you press the code?")
         call reply_message("MC", "Uhm… Okay. I will.")

         hide screen phone_message4

         show uks kinni

         ""

         m "(Input the password.)"

         show uks lahti

         ""

         hide uks lahti

         hide uks kinni

         jump aftermenu9

 label aftermenu9:
     call reply_message("MC", "The door’s open.")
     call message_u("Unknown", "Good. Why don’t you go inside?")

 call screen phone_reply("Can I just enter a stranger’s house?","choice20","I guess I will.","choice21")

 label choice20:
     call phone_after_menu

     call message_start_m("MC", "Can I just enter a stranger’s house?")
     call message_u("Unknown", "You can just leave a note. I’ll give you my info.")
     call message_u("Unknown", "If something happens, you can just show my messages. That’ll do.")
     call reply_message("MC", "Then… Alright.")
     call message_u("Unknown", "tühi")

     hide screen phone_message4

     jump aftermenu10

 label choice21:
     call phone_after_menu
     call message_start_m("MC", "I guess I will.")
     call message_u("Unknown", "Th")
     call message_u("Unknown", "ank")
     call message_u("Unknown", "you…")
     call message_u("Unknown", "you…")

     hide screen phone_message4

     jump aftermenu10

 label aftermenu10:

     "Unknown has left the chatroom."

     $ cr_p += 1

     show tuba

     ""
     $ renpy.movie_cutscene("hakkhääl1.mpg")

     jump part2



 label bad_prouloge_ending:

     call message_u("Unknown", "Really?")
     play music "unknown_theme.ogg"
     call message_u("Unknown", "That’s strange.")
     call message_u("Unknown", "I see with my own eyes that…")
     call message_u("Unknown", "You are standing in front of a password door lock.")
     call message_u("Unknown", "Are you gonna continue lying?")
     call reply_message("MC", "What?? Can you see me?")
     call message_u("Unknown", "Haha yes")
     call message_u("Unknown", "I guess that’s it then")
     call message_u("Unknown", "Plan failed")
     ""
     hide screen phone_message4

     scene hallway bg

     init:
         $ yoosunglvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)

     u "The plan failed."

     show saeran tavaline at yoosunglvl

     u "I’ll have to find someone else."

     menu:

         "I’ll have to find someone else."

         "This is creepy! I’m getting out of here.":
             m "This is creepy! I’m getting out of here."
             u "Hmm."
             u "That’s feisty."

         "Who the hell are you?!":
             m "Who the hell are you?!"
             u "You don’t need to know."
             u "What should I do with you..?"

     label after_menu1:

         show saeran happy at yoosunglvl
         u "I’d like to let you go, but you already know me."
         u "Sorry, but you’ll have to come with me."
         u "I could just get rid of you…"
         show saeran tavaline at yoosunglvl
         u "but that’d be a shame."
         u "You’re so cute."
         u "You can be my assistant."
         u "Right…"
         u "He said he has an assistant. I’d like one too."
         u "Should I use… you?"
         show saeran happy at yoosunglvl
         u "Come here."
         u "I’ll be good to you."
         show saeran tavaline at yoosunglvl
         u "Come with me."

     menu:

         "Come with me."

         "Okay.":
             m "Okay."
             show saeran happy at yoosunglvl
             u "Haha!"
             u "I can feel… that you’re quite similar to me."
             u "This is exciting."
             show saeran creepy at yoosunglvl
             u "Well, you never had a choice anyways."

         "No…":
             m "No…"
             show saeran happy at yoosunglvl
             u "Nonsense~"
             u "If you don’t come with me…"
             u "I’ll have to find a way to destroy the information you know"
             u "But you’re not a computer"
             show saeran creepy at yoosunglvl
             u "so I can’t just delete you."
             u "Well, you never had a choice anyways."

     label after_menu2:

         u "Now, let’s go."
         image saeran_creepy1 = Transform("saeran creepy.png", zoom=1.2)
         hide saeran creepy
         show saeran_creepy1 at yoosunglvl
         u "I’ll be nice."
         image saeran_creepy2 = Transform("saeran tavaline.png", zoom=1.2)
         hide saeran_creepy1
         show saeran_creepy2 at yoosunglvl
         u "I’m a much better person than him."
         hide saeran_creepy2
         show black bg
         "BAD ENDING"
         ""

 return
