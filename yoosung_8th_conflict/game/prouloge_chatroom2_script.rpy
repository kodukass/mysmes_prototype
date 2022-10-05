#PROULOUGE PART 2

label part2:
call phone_start2

init:
    $ y_icon_lvl = Position(xpos=0.5, ypos=10, xanchor=0.5, yanchor=5)
    $ z_icon_lvl = Position(xpos=0.445, ypos=10, xanchor=0.445, yanchor=5)
    $ se_icon_lvl = Position(xpos=0.3913, ypos=10, xanchor=0.3913, yanchor=5)
    $ v_icon_lvl = Position(xpos=0.338, ypos=10, xanchor=0.338, yanchor=5)
    $ ju_icon_lvl = Position(xpos=0.6085, ypos=10, xanchor=0.6085, yanchor=5)
    $ ja_icon_lvl = Position(xpos=0.555, ypos=10, xanchor=.555, yanchor=5)
    $ u_icon_lvl = Position(xpos=0.285, ypos=10, xanchor=0.285, yanchor=5)
    $ mc_icon_lvl1 = Position(xpos=0.6596, ypos=10, xanchor=0.6596, yanchor=5)

# show yoosung_icon at y_icon_lvl
# show zen_icon at z_icon_lvl
# show seven_icon at se_icon_lvl
# show v_icon at v_icon_lvl
# show jumin_icon at ju_icon_lvl
# show jaehee_icon at ja_icon_lvl
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

# label hearts:
#     $ z_h = 0
#     $ s_h = 0
#     $ y_h = 0
#     $ ju_h = 0
#     $ ja_h = 0

#chat

play music "mainmenusound.ogg"
show mc_icon1 at mc_icon_lvl1
show yoosung_icon at y_icon_lvl
call message_start_y("Yoosung★", "Failed my midterms fml T_T")
#crying emoji
call message_s("707", "Cuz u played LOLOL all night lol.")
show seven_icon at se_icon_lvl
call message_ju("Jumin Han", "If you want to work for our company, you should take care of your GPA.")
show jumin_icon at ju_icon_lvl
call message_y("Yoosung★", "I’m still on the list?! +_+")
#starry eye emoji
call message_ju("Jumin Han", "Yes.")
call message_s("707", "Nice~ Can’t believe u get to work straight after college lol")
call message_s("707", "In this day and age!")
call message_z("ZEN", "Lame. It’s nepotism.")
show zen_icon at z_icon_lvl
call message_ju("Jumin Han", "It’s called recruitment actually.")
call message_z("ZEN", "It’s giving a free pass instead of actually training the worker.")
call message_ju("Jumin Han", "Whatever. I couldn’t care less what you say.")
call message_z("ZEN", "What’s the difference between recruitment and nepotism?")
call message_s("707", "Thought they r the same? O_O?")
#confused emoji
call message_ju("Jumin Han", "It’s nepotism if you recruit a person you know and they aren’t of any help.")
call message_y("Yoosung★", "Oh… So you become a candidate for nepotism the same time you’re recruited!")
#zen annoyed emoji
call message_s("707", "Huh? Wait!!")
call message_y("Yoosung★", "Hmm? Why?")
call message_z("ZEN", "What ??")
call message_s("707", "Think someone entered the chat room;;")
call message_ju("Jumin Han", "MC.........?")
call message_z("ZEN", "Wtf. How did it get in here?")
call message_s("707", "Hacker!!!!")
call message_y("Yoosung★", "Hacker!? Therae’s a hacker in ouer room!!!")
call message_y("Yoosung★", "Sevnee do somethign!!")
call message_z("ZEN", "Hey, typos. -_-;;")
call message_s("707", "Wait a sec. I’m searching.")
call message_ju("Jumin Han", "Who are you? Reveal yourself. Hey, Assistant Kang.")
call message_ja("Jaehee Kang", "Yes, I am here.")
show jaehee_icon at ja_icon_lvl
call message_z("ZEN", "You were so quiet I thought you went somewhere.")
call message_ja("Jaehee Kang", "Nothing was out of the ordinary so I was just watching")
call message_ja("Jaehee Kang", "but I see something has just happened.")
call message_y("Yoosung★", "omg")
call message_ju("Jumin Han", "Why is a stranger in our chatroom?")
call message_ja("Jaehee Kang", "No one can enter this chatroom without installing the private app we use… It seems someone has downloaded the RFA Messenger.")
call message_y("Yoosung★", "I thought Seven let only us download it?")
#confused emoji
call message_z("ZEN", "Maybe someone downloaded the app on two phones?")
call message_s("707", "Maybe?")
call message_ju("Jumin Han", "Who downloaded it twice?")
call message_y("Yoosung★", "Not me!")
call reply_message("MC", "Hello…")
call message_y("Yoosung★", "Gahhhh it’s talking!!")
#shocked emoji
call message_z("ZEN", "So it’s not two smartphones.")
call message_ju("Jumin Han", "Who is it?")
call message_s("707", "Find out what it is!")
call message_ja("Jaehee Kang", "How did you find out about this place? Where did you download the application?")
call message_s("707", "Oh… ^^; Wait.")
call message_z("ZEN", "What is it. Hurry and tell me.")
call message_s("707", "I traced the IP…")
call message_s("707", "It’s from Rika’s apartment.")
call message_y("Yoosung★", "Rika’s apartment?")
call message_ju("Jumin Han", "Where was it?")
call message_ja("Jaehee Kang", "The location is not revealed. I know it to be classified.")
call message_s("707", "Anyways, someone must have broken into her apt.")
call message_s("707", "It talked now, so it must be a person ^^;")
call message_y("Yoosung★", "So it hacked the program, Seven?")
call message_s("707", "Yup")
call message_y("Yoosung★", "Who are you?! How did you get into Rika’s apartment?!")
call message_y("Yoosung★", "How did you get this app?!")
call message_y("Yoosung★", "Gah~ So scared right now…")
#depressed emoji
call message_y("Yoosung★", "I thought the apartment has a passworh lobk?")
call message_z("ZEN", "Typo")
call message_ju("Jumin Han", "I assume it was a break in.")
call message_ja("Jaehee Kang", "Username “MC”, I recommend that you confess.")
call message_z("ZEN", "Jaehee, would you voluntarily confess to everything if it were you?")
call message_ja("Jaehee Kang", "No. But it is good to ask first.")
call message_s("707", "Lolol")
call message_ju("Jumin Han", "Quit shitting around.")
call message_ju("Jumin Han", "MC… Who are you?")
call message_ju("Jumin Han", "Reveal yourself, stranger.")
call message_ju("Jumin Han", "If you do not reveal yourself, you will pay.")
call message_z("ZEN", "Stranger you will pay? Lmfao")
call message_z("ZEN", "omg~*so scary*~")
call message_z("ZEN", "It might be a girl.")
call message_s("707", "That’s sexist lol. U should watch what u say now that ur a famous actor.")
call message_z("ZEN", "I’m not famous;; just a bit recognizable.")
call message_y("Yoosung★", "Nah~ Look at the youtube hits~")
call message_z("ZEN", "Dude. Stawp;;")
call message_s("707", "lolol")
call message_ja("Jaehee Kang", "That video is still excellent no matter how many times I watch it.")
call message_y("Yoosung★", "Zen, when do you start your next piece?")
call message_z("ZEN", ";;Don’t know. It’s up to the director.")
call message_y("Yoosung★", "He’s a celebrity lol! I’m gonna tell everyone at school.")
call message_ju("Jumin Han", "Hey.")
call message_ju("Jumin Han", "Don’t get distracted.")
call message_y("Yoosung★", "Oh, right. Username MC…")
call message_ja("Jaehee Kang", "… An abrupt stranger.")
call message_s("707", "My hands r shaking as I hack.")
call message_ju("Jumin Han", "Who are you? Reveal yourself right now.")
call message_y("Yoosung★", "Yeees! Who are u?!")
call message_z("ZEN", "Use proper english please.")
call message_s("707", "If it doesn’t say anything I’ll hack in and find out.")
call message_z("ZEN", "…Maybe")
call message_z("ZEN", "one of my fans?")
#angry jumin emoji
call screen phone_reply("I am MC. Who are you all and what is this place?","choice26","Reveal yourselves first. I’m the most confused one here…","choice27")

label choice26:
    call phone_after_menu
    #punane
    $ s_h += 1
    call message_start_m("me", "I am MC. Who are you all and what is this place?")
    call message_s("707", "Lol so awkward.")
    call message_s("707", "I thought it was a computer talking.")
    call message_z("ZEN", "Seems more normal than I thought.")
    call message_y("Yoosung★", "What were you thinking?")
    call message_z("ZEN", "… Nothing~Nothing.")

    jump aftermenu12

label choice27:
    call phone_after_menu
    #hall ja sinine
    $ ju_h += 1
    $ z_h += 1
    call message_start_m("me", "Reveal yourselves first. I’m the most confused one here…")
    call message_ju("Jumin Han", "How fierce.")
    call message_z("ZEN", "Are you a woman?")
    call message_s("707", "Zen. Be more serious, plz?")
    call message_s("707", "And wait a sec on the woman thing.")
    call message_s("707", "Looking it up.")
    #happy emoji
    call message_ja("Jaehee Kang", "Such a search violates privacy laws.")
    call message_s("707", "Ya. I’m only saying I’m looking it up.")
    call message_s("707", "No evidence that I’m actually hackginh.")
    call message_y("Yoosung★", "Seven, that’s obviously a lie. lol")
    call message_y("Yoosung★", "And I know that typo’s on purpose.")
    call message_y("Yoosung★", "Still…")
    call message_y("Yoosung★", "Won’t it tell us about itself if we tell who we are first?")
    call message_z("ZEN", "To be honest…")
    call message_z("ZEN", "I agree with Yoosung.")
    call message_ju("Jumin Han", "More like you want to show off who you are.")

    jump aftermenu12

label aftermenu12:
    call message_y("Yoosung★", "Should we… introduce ourselves?")
    call message_ju("Jumin Han", "Are you serious…?")
    call message_ja("Jaehee Kang", "I think it is a bit too early for that.")
    call message_z("ZEN", "Hi. I’m Zen. (24 yrs old) Musical actor… Don’t look me up on the internet.")
    call message_z("ZEN", "It’s embarrassing.")
    call message_y("Yoosung★", "Zen, you’re so brave!")
    call message_ju("Jumin Han", "Guess he wanted to show himself off.")
    call message_z("ZEN", "No way~!")
    call message_img_z("zen_1.png")
    call message_y("Yoosung★", "Omg… a photo too.")
    call message_ja("Jaehee Kang", "My eyes have been cleansed.")
    #Sparkly eyed Jaehee emoji
    call message_ja("Jaehee Kang", "Wait. I can’t be like this…")
    call message_ju("Jumin Han", "I see that he has zero interest in his privacy.")
    call message_s("707", "Lolol")
    call message_s("707", "My nickname’s 707.")
    call message_s("707", "Real name is a secret.")
    call message_s("707", "Fyi, Zen’s real name is Hyun Ryu.")
    call message_z("ZEN", "Your name’s a secret but not mine?;")
    call message_s("707", "U don’t care anyways lol.")
    call message_ja("Jaehee Kang", "707 does have the strangest name so I understand the secrecy.")
    call message_s("707", "The name’s too holy to be spread around~ I’m gonna pray after I finish hacking.")
    #… Zen emoji
    call message_z("ZEN", "Pray, yeah right;;")
    call message_s("707", "Just remember me as the 22yr old young hacker lol")
    call message_s("707", "Where I live is also a secret.")
    call message_z("ZEN", "So many secrets;;")
    call message_y("Yoosung★", "I’m Yoosung Kim! I’m a college student… 21 yrs old.")
    call message_ju("Jumin Han", "I don’t know why everybody’s introducing themselves. You don’t even know who that person is.")
    call message_img_y("yoosung1.jpeg")
    call message_s("707", "So warm and fuzzy here")
    call message_z("ZEN", "Lol. Seven, you don’t have any selfies to show?")
    call message_s("707", "Nothing recent.")
    call message_s("707", "Oh and also!")
    call message_s("707", "Jumin’s the heir of a pretty famous corporation and Jaehee is his assistant. 27 and 26 yrs old respectively.")
    call message_s("707", "You have a better sense of who we are now, MC?")
    call message_ju("Jumin Han", "Why did you say that…?")
    call message_s("707", "Doubted you’d do it urself.")
    call message_ju("Jumin Han", "Stop shitting around.")
    call message_s("707", "Oh, fyi, Jumin has the cutest cat.")
    call message_ju("Jumin Han", "Hey.")
    call message_ju("Jumin Han", "Why are we talking about Elizabeth the 3rd to a stranger?")
    call message_s("707", "The cat’s name is Elizabeth the 3rd.")
    call message_img_s("jumin2.png")
    call message_s("707", "Oh. U already said lol.")
    call message_y("Yoosung★", "That info’s a bit useless…")
    call message_y("Yoosung★", "We’re not even close with this MC person yet lol")
    call message_ju("Jumin Han", "Can’t believe he showed a photo of Elizabeth the 3rd to a stranger…")
    call message_ju("Jumin Han", "Idiot…")
    call message_ju("Jumin Han", "I know you came to my house the other day and harassed her. It’s all on CCTV.")
    call message_img_ju("seven1.png")
    call message_s("707", "My precious privacy!")
    call message_z("ZEN", "Yeah since you care so much about privacy.")
    call message_y("Yoosung★", "CCTV screenshots omg")
    call message_ju("Jumin Han", "And Yoosung.")
    call message_ju("Jumin Han", "Is my Elizabeth the 3rd useless?")
    #Shocked Yoosung emoji
    call message_s("707", "That was so funn~~")
    call message_s("707", "I want to see the cat again~")
    call message_ju("Jumin Han", "No.")
    call message_z("ZEN", "Stop talking about cats. Giving me goosebumps.")
    call message_ja("Jaehee Kang", "I suggest that we take care of this stranger first.")
    call message_ja("Jaehee Kang", "Could it be that we have a security breach?")
    call message_z("ZEN", "True. MC, how did you get in here?")
    call message_y("Yoosung★", "Is it really in Rika’s apartment?")
    call message_s("707", "Yup. It’s for sure…")
    call message_s("707", "How did it get the apartment password?!")
    call message_z("ZEN", "Where the hell is the apartment?")

call screen phone_reply("I am flustered too. I was connected to a stranger through a messenger app and he sent me the address.","choice28","I came here while chatting with a personal called ‘Unknown’. Do you know him by any chance?","choice29")

label choice28:
    call phone_after_menu
    #hall
    $ z_h += 1
    call message_start_m("MC", "I am flustered too. I was connected to a stranger through a messenger app and he sent me the address.")
    call message_ju("Jumin Han", "Chatting with a stranger…")
    call message_ju("Jumin Han", "How naive.")
    call message_z("ZEN", "So cute lol")
    call message_z("ZEN", "Went to an address from a chatting app lolol")
    call message_y("Yoosung★", "Don’t listen to strangers~ The world is dangerous.")
    call message_ja("Jaehee Kang", "I agree.")
    call message_s("707", "Wait.")
    call message_s("707", "Do u have that person’s username or chat record?")
    call reply_message("MC", "The username was ‘Unknown’. And the record was deleted.")
    call message_ju("Jumin Han", "Does the username not exist? Why is it ‘Unknown’?")
    call message_s("707", "I made it impossible to log in without setting a username.")
    call message_s("707", "Nothing’s in the log…")
    call message_y("Yoosung★", "What’s a log? Is it a job title for online games?")
    call message_ju("Jumin Han", "Tree trunk")
    call message_ja("Jaehee Kang", "It refers topast records;;")
    call message_z("ZEN", "Tsk tsk everyone’s so dumb")
    call message_y("Yoosung★", "Never thought I’d hear that from you")
    #Shocked Yoosung emoji
    call message_s("707", "Omg lolol can’t believe Zen just said that")
    call message_ju("Jumin Han", "The world must be coming to an end.")
    call message_ja("Jaehee Kang", "Everyone please calm down. Let’s look at the situation at hand.")
    call message_s("707", "Hmm. Good point, Jaehee.")
    call message_ja("Jaehee Kang", "Who do you think that ‘Unknown’ person is?")

    jump aftermenu13

label choice29:
    call phone_after_menu
    #sinine
    $ ju_h += 1
    call message_start_m("MC", "I came here while chatting with a personal called ‘Unknown’. Do you know him by any chance?")
    call message_ju("Jumin Han", "Unknown?")
    call message_z("ZEN", "Maybe he just didn’t set a username?")
    call message_s("707", "It’s mandatory to set a username so he must have set it that way.")

    jump aftermenu13

label aftermenu13:
    call message_s("707", "Maybe…")
    #Shocked 707 emoji
    call message_s("707", "A hacker…?!")
    call message_y("Yoosung★", "!!!")
    call message_s("707", "A hacker! No way.")
    call message_s("707", "I have everything covered!")
    call message_s("707", "Hey, MC. So he told you the password for the door lock?")

call screen phone_reply("Ya. I know nothing","choice30","Yes.","choice31")

label choice30:
    call phone_after_menu
    #hall
    $ z_h += 1
    call message_start_m("MC", "Ya. I know nothing")
    call message_ju("Jumin Han", "…Ya?")
    call message_z("ZEN", "Cute lol")

    jump aftermenu14

label choice31:
    call phone_after_menu
    #sinine
    $ ju_h += 1
    call message_start_m("MC", "Yes.")
    call message_ju("Jumin Han", "I see…")
    call message_ju("Jumin Han", "That ‘Unknown’ person could have dragged you into this.")

    jump aftermenu14

label aftermenu14:
    call message_y("Yoosung★", "But..")
    call message_y("Yoosung★", "How did you end up chatting with that person?")
    call message_ja("Jaehee Kang", "I see.")
    call message_ja("Jaehee Kang", "Where did you download this messenger app?")
    call message_ja("Jaehee Kang", "MC, you are quite strange as well.")
    call message_z("ZEN", "Do you think this person’s a creep? No way.")

call screen phone_reply3("I just wanted to chat with pretty boys…","choice32","just got it @ app store…","choice33","I just wanted to download the game and play it.","choice34")

label choice32:
    call phone_after_menu
    #kollane
    $ ja_h += 1
    call message_start_m("MC", "I just wanted to chat with pretty boys…")
    call message_z("ZEN", "Me? You wanted to chat with me?")
    call message_ju("Jumin Han", "Completely out of his mind.")
    call message_y("Yoosung★", "Ye.")
    call message_y("Yoosung★", "Oh, typo!")
    call message_ja("Jaehee Kang", "It’s true that Zen is good looking.")
    call message_z("ZEN", "Thank you, Jaehee ^^")
    #Happy 707 emoji

    jump aftermenu15

label choice33:
    call phone_after_menu
    #hall
    $ z_h += 1
    call message_start_m("MC", "just got it @ app store…")
    call message_ju("Jumin Han", "What a modern way of talking.")
    call message_z("ZEN", "So cute lol")

    jump aftermenu15

label choice34:
    call phone_after_menu
    #roheline
    $ y_h += 1
    call message_start_m("MC", "I just wanted to download the game and play it.")
    call message_y("Yoosung★", "You like games too!")
    call message_y("Yoosung★", "I love games.")
    call message_y("Yoosung★", "Do you know this game called LoLoL?")
    call message_z("ZEN", "Dude. A girl won’t play that game;")
    call message_z("ZEN", "Don’t ask stupid questions.")
    call message_y("Yoosung★", "T_T")

    jump aftermenu15

label aftermenu15:
    call message_s("707", "Anyways.")
    call message_s("707", "I should trace the person who distributed the app.")
    call message_ju("Jumin Han", "If what she is saying is true.")
    call message_ja("Jaehee Kang", "I think it would be a good idea to contact V.")
    call message_s("707", "Yeah. I think that’s a good idea.")
    call message_s("707", "I’ll call and explain everything.")
    call message_ju("Jumin Han", "I can call.")
    call message_s("707", "Already on it lol")
    call message_z("ZEN", "Fast.")
    call message_y("Yoosung★", "Seven seems talk to V pretty often.")

call screen phone_reply("What is this chat room for;;?","choice35","Who’s V?","choice36")

label choice35:
    call phone_after_menu
    #pole
    call message_start_m("MC", "What is this chat room for;;?")
    call message_ja("Jaehee Kang", "We can answer that after we have told V about this situation.")
    call message_ju("Jumin Han", "Yeah.")

    jump aftermenu16

label choice36:
    call phone_after_menu
    #pole
    call message_start_m("MC", "Who’s V?")
    call message_z("ZEN", "V is… like our boss.")
    call message_s("707", "The evil mastermind.")
    call message_ju("Jumin Han", "…or not. He’s the person who has control over this chat room and the organization we’re in.")

    jump aftermenu16

label aftermenu16:
    call message_ju("Jumin Han", "I hope V comes and takes care of all this.")
    call message_z("ZEN", "V’s too busy these days to come chat… We’ll get to talk to him because of this~")
    call message_y("Yoosung★", "We’re all busy. I don’t like that V’s the only one not coming.")
    call message_z("ZEN", "Well… that’s true…")
    call message_ja("Jaehee Kang", "V should know that MC is here so let’s just wait.")
    call message_ja("Jaehee Kang", "Seven, are you calling him?")
    call message_s("707", "Ya.")
    call message_y("Yoosung★", "But shouldn’t we tell MC what this chatroom is for first?")
    call message_y("Yoosung★", "She has to know how serious it is that she’s here!")
    call message_ju("Jumin Han", "What’s more serious is that she’s in Rika’s apartment.")
    call message_y("Yoosung★", "That’s true…")
    call message_ja("Jaehee Kang", "I am always ready to call the police.")
    call message_y("Yoosung★", "Jaehee’s scary T_T")
    call message_ju("Jumin Han", "Until we figure out who MC is")
    call message_ju("Jumin Han", "I don’t want to reveal anything.")
    call message_ja("Jaehee Kang", "I agree.")
    call message_s("707", "Wecan.")
    call message_s("707", "Sorry callingvandtypingwithonehand")
    call message_y("Yoosung★", "Type after you finish the call.")
    call message_s("707", "Lookedintoownerofdevice.")
    call message_s("707", "she’scutelol")
    call message_y("Yoosung★", "You did a background check on her!? So MC is definitely a girl?")

call screen phone_reply3("But I’m not a girl.","choice37","Where did you get that info!?","choice38","You’re not violating my…","choice39")

label choice37:
    call phone_after_menu
    #pole
    call message_start_m("MC", "But I’m not a girl.")
    call message_s("707", "thenwhydouplaythisgame")
    call message_y("Yoosung★", "???")
    call message_z("ZEN", "Are you a girl or a boy?")
    call message_s("707", "youdidntreadsweetfantasyforladies?")
    call message_y("Yoosung★", "I heard that’s just the company’s marketing scheme;")
    call message_y("Yoosung★", "Anyways, are you a girl or a boy?")
    #Confused Yoosung emoji
    call message_s("707", "girl")
    call message_ja("Jaehee Kang", "Let’s just say she’s a girl.")
    call message_z("ZEN", "Oh! A girl!")

    jump aftermenu17

label choice38:
    call phone_after_menu
    #pole
    call message_start_m("MC", "Where did you get that info!?")
    call message_z("ZEN", "He’s a hacker. He probably saw your fb page already.")
    call message_s("707", "notthereyet")
    call message_s("707", "iwillifineedtotholol")

    jump aftermenu17

label choice39:
    call phone_after_menu
    #pole
    call message_start_m("MC", "You’re not violating my…")
    call message_s("707", "Itolduimahacker.")
    call message_s("707", "Butnoevidenceididit")

    jump aftermenu17

label aftermenu17:
    call message_ju("Jumin Han", "What? It’s really a girl?")
    call message_s("707", "Ya.")
    show v_icon at v_icon_lvl
    "V has entered the chatroom."
    call message_z("ZEN", "Show me a photo")
    call message_s("707", "Nope~")
    call message_s("707", "How dare you try to violate someone’s privacy like that.")
    call message_img_s("jaehee1.png")
    call message_ju("Jumin Han", "?")
    call message_z("ZEN", "Is that MC!?")
    call message_y("Yoosung★", "omg I thought we were respecting her privacy?")
    call message_ja("Jaehee Kang", ";;;;;")
    call message_ja("Jaehee Kang", "That is a photo of me.")
    call message_y("Yoosung★", "Oh right! Sorry I was too excited;;")
    call message_z("ZEN", "So..sorry for not recognizing you;;")
    call message_ja("Jaehee Kang", "Mr. Han, you can’t recognize me either?")
    call message_ju("Jumin Han", "…")
    call message_ju("Jumin Han", "Now what are we going to do?")
    call message_s("707", "V’s coming here soon. He just hung up.")
    call message_v("V", "I’m already logged in.")
    call message_s("707", "Oh, V! You’re here ^_^")
    call message_v("V", "Yeah. I guess I’m the last one to know about this.")
    call message_ju("Jumin Han", "Oh well.")
    call message_v("V", "How is everyone? Jaehee, you’ve been well?")
    call message_ja("Jaehee Kang", "Yes. It’s been a long time, V.")
    call message_y("Yoosung★", "Hey V")
    call message_v("V", "Hey.")
    call message_v("V", "Well, I heard about a situation.")
    call message_v("V", "MC is currently in Rika’s apartment with info from a stranger and logged into this chatroom.")
    call message_s("707", "I told him everything through the phone.")
    call message_ju("Jumin Han", "Who disclosed the password for Rika’s apartment?")
    call message_v("V", "Well. No one knew the password. I don’t even know.")
    call message_y("Yoosung★", "…Thought V knew.")
    call message_y("Yoosung★", "She never invited me to her apartment.")
    call message_ju("Jumin Han", "It’s the same for everyone else.")
    call message_ju("Jumin Han", "No one’s been there before.")
    call message_y("Yoosung★", "Tell us the address. I’ll go there… I want to check who MC is myself.")
    call message_y("Yoosung★", "Seven, you know right? You traced the IP just now.")
    call message_s("707", "Uhm. Sorry but…")
    call message_s("707", "I can’t tell you that.")
    call message_y("Yoosung★", "??")
    call message_y("Yoosung★", "I’m her surviving family.")
    call message_z("ZEN", "Maybe because you’re just her cousin?")
    call message_s("707", "Not even her immediate family can go.")
    call message_s("707", "And the apartment doesn’t belong to Rika.")
    call message_y("Yoosung★", "Then who?")
    call message_v("V", "Me.")
    call message_y("Yoosung★", "You don’t even know the password!")
    call message_v("V", "I just respected her privacy.")
    call message_y("Yoosung★", "…Were you really in a relationship with her?")
    call message_ju("Jumin Han", "I can’t believe you never knew the password.")
    call message_v("V", "I’ve never even been there. I just know where it is.")
    call message_v("V", "Anyways, the apartment is in my name.")
    call message_v("V", "Rika usually worked there. There are a lot of documents in there that must not be damaged.")
    call message_v("V", "I can’t reveal the address because all the classified information about this organization is stored there, plus other sensitive materials.")
    call message_ju("Jumin Han", "I didn’t know the place contained sensitive material.")
    call message_y("Yoosung★", "You don’t trust us enough to let us go, right?")
    call message_ju("Jumin Han", "Don’t take it personally. It’s better to be ignorant sometimes.")
    call message_v("V", "Yes, for the reason that Jumin said.")
    call message_v("V", "Anyways, I can’t tell you the address. I’m sorry.")
    call message_y("Yoosung★", "Then how did Seven know that the address he traced is Rika’s apartment?")
    call message_ja("Jaehee Kang", "Since he’s responsible for the organization’s classified information.")
    call message_s("707", "Yup. That’s true, but also I’m the one who developed this app.")
    call message_s("707", "Rika wanted to take care of some work through this too.")
    call message_s("707", "I went to her place to link the app with some of the documents in her computer.")
    call message_y("Yoosung★", "Oh…")
    call message_ju("Jumin Han", "I see.")
    call message_v("V", "Only Luciel and I know the address.")
    call message_v("V", "I repeat, since the information must be protected, please do not attempt to find the apartment.")
    call message_v("V", "Do not ask MC about it and MC, please do not reveal the address.")

call screen phone_reply("Luciel?","choice40","What’s classified information?","choice41")

label choice40:
    call phone_after_menu
    #pole
    call message_start_m("MC", "Luciel?")
    call message_z("ZEN", "That’s 707’s real name. ‘Luciel Choi’")
    call message_ja("Jaehee Kang", "lol")
    call message_y("Yoosung★", "omg Jaehee just said lol")
    call message_ju("Jumin Han", "I think it’s his baptismal name?")
    call message_s("707", "I’m going to go pray for a moment.")
    #Happy 707 emoji

    jump aftermenu18

label choice41:
    call phone_after_menu
    #pole
    call message_start_m("MC", "What’s classified information?")
    call message_v("V", "All the information there is classified.")
    call message_v("V", "So MC… Is that what I call you?")
    call message_v("V", "Please do not touch anything there.")
    call message_v("V", "For example, if you try to force open one of the drawers…")
    call message_v("V", "The alarm will ring.")
    #surprised-zen

    jump aftermenu18

label aftermenu18:
    call message_y("Yoosung★", "What do we do about her apartment?")
    call message_y("Yoosung★", "Can MC stay there?")
    call message_v("V", "First…")
    call message_v("V", "No one here is going to go to Rika’s apartment, right?")
    call message_v("V", "Since the information involves everyone around us, there might be trouble if we are not careful.")
    call message_ju("Jumin Han", "Yeah yeah. You can stop explaining. Classified information. Got it.")
    call message_ju("Jumin Han", "But it is a mystery how a complete stranger could end up there.")
    call message_v("V", "If it’s someone who knows the password…")
    call message_ju("Jumin Han", "Someone Rika trusted?")
    #Confused 707 emoji
    #Confused Zen emoji
    call message_v("V", "I am only guessing…")
    call message_s("707", "So then that ‘Unknown’ person…")
    call message_s("707", "knew Rika!?")
    call message_s("707", "I can’t believe she trusted someone more than V.")
    call message_y("Yoosung★", "I don’t believe that. She couldn’t have trusted anyone more than us…")
    call message_z("ZEN", "That is… a bit surprising.")
    call message_v("V", "It’s hard to believe myself… But we shouldn’t assume that we knew everything about Rika.")
    call message_v("V", "She…")
    call message_v("V", "had a deep world of her own.")
    call message_y("Yoosung★", "…")
    call message_ju("Jumin Han", "…Anyways, V, continue.")
    call message_v("V", "If I am right.")
    call message_v("V", "MC is at her apartment right now…")
    call message_ju("Jumin Han", "Rika called in a complete stranger from up in the sky?")
    call message_v("V", "I’m not saying she wanted MC to be there… but maybe…")
    call message_v("V", "Rika wanted someone to do the work she did before.")
    call message_v("V", "At the place she worked before.")
    call message_ju("Jumin Han", "What…?")
    call message_z("ZEN", "No way…")
    call message_ja("Jaehee Kang", "The work Rika did before…")
    call message_s("707", "Hosting parties?")
    call message_z("ZEN", "You mean Rika’s party.")
    call message_y("Yoosung★", "Do you really think… that Rika planned this?")
    call message_y("Yoosung★", "If she made that decision when she was alive…")
    call message_v("V", "That’s my guess… but yes.")
    call message_v("V", "Since she didn’t leave a will.")
    call message_v("V", "According to the information Luciel provided, MC doesn’t seem dangerous.")
    call message_ju("Jumin Han", "I’m not sure about this to be honest…")
    call message_v("V", "Besides, she’s basically in the same boat now that she knows about this messenger app.")
    call message_v("V", "Whoever she might be.")
    call message_s("707", "But still…")
    call message_z("ZEN", "If that’s what V thinks…")

call screen phone_reply("Who the hell is Rika?","choice42","I just came here to find the owner of the phone… What is going on…","choice43")

label choice42:
    call phone_after_menu
    #pole
    call message_start_m("MC", "Who the hell is Rika?")
    call message_z("ZEN", "Can we tell her?")

    jump aftermenu19

label choice43:
    call phone_after_menu
    #pole
    call message_start_m("MC", "I just came here to find the owner of the phone… What is going on…")
    call message_s("707", "Owner of the phone?")
    call message_s("707", "You were phished lol")
    call message_s("707", "According to V’s guess, Rika… the person who used to live there")
    call message_s("707", "had the person ‘Unknown’ convince u to go to the apartment.")

    jump aftermenu19

label aftermenu19:
    call message_ja("Jaehee Kang", "Wait…")
    call message_ja("Jaehee Kang", "I understand… that everyone values V’s opinion.")
    call message_ja("Jaehee Kang", "But…")
    call message_ja("Jaehee Kang", "This chatroom is strictly prohibited to strangers.")
    call message_ja("Jaehee Kang", "If I may say so, I think that we must verify what MC has said.")
    call message_ja("Jaehee Kang", "For all we know, MC could have simply made up that ‘Unknown’ person.")
    call message_s("707", "I feel like Jaehee’s glasses are glinting right now.")
    call message_ja("Jaehee Kang", "?")
    call message_v("V", "Thank you for your opinion, Jaehee.")
    call message_v("V", "But right now, I would appreciate it if you could trust me.")
    call message_v("V", "If MC is not to be trusted, we can deal with it then.")
    call message_ju("Jumin Han", "Hmm.")
    call message_ju("Jumin Han", "I don't agree with you... but I'll follow your decision.")
    call message_ja("Jaehee Kang", "If that is what Mr. Han thinks, then I will accede as well.")
    call message_s("707", "Now then~")
    call message_s("707", "Shouldn't we... explain to MC about Rika and RFA?")

call screen phone_reply("Please explain.","choice44","I’m not really interested.","choice45")

label choice44:
    call phone_after_menu
    call message_start_m("MC", "Please explain.")
    call message_z("ZEN", "Okay.")

    jump aftermenu20

label choice45:
    call phone_after_menu
    #hall
    $ z_h += 1
    call message_start_m("MC", "I’m not really interested.")
    call message_z("ZEN", "How chic…")
    call message_z("ZEN", "Cute is nice but chic women have their own charms.")
    call message_ju("Jumin Han", "He’s gone insane.")
    call message_s("707", "Lol excited because she’s a girl?")
    call message_z("ZEN", "Yup.")
    call message_ju("Jumin Han", "Excited because of a stranger?")
    call message_ju("Jumin Han", "Your heart is insane.")
    call message_s("707", "Lololololol lmfao at what Jumin said.")
    call message_s("707", "Insane heart lolololol")
    call message_ja("Jaehee Kang", "Zen, isn’t it quite inappropriate to fall for someone you have never met?")
    call message_z("ZEN", "Uhm. yes.")
    call message_z("ZEN", "I can’t control myself.")
    call message_ja("Jaehee Kang", "omg")
    call message_ju("Jumin Han", "-_-")
    call message_y("Yoosung★", "MC, you may not be interested right now, but won’t you listen to what we have to say?")
    call message_y("Yoosung★", "You are involved now that you’re here.")
    call message_y("Yoosung★", "Regardless of whether you like it or not.")
    call message_s("707", "Ya. If you don’t cooperate, we can all team up to put u in trouble.")
    call message_s("707", "First, we all know that u trespassed on the apartment^^")
    #Surprised Zen emoji
    call message_z("ZEN", "Is that a threat?")
    call message_s("707", "Yup. I will threaten anyone in here who doesn’t follow V’s decision.")
    call message_s("707", "I am V’s slave.")
    call message_v("V", "…Uhm. Thank you?")
    #Depressed Yoosung emoji
    call message_y("Yoosung★", "Is that how we roll now?")
    call message_s("707", "Uhm. No lol")
    call reply_message("MC", "Oh… Alright. I’ll listen for now.")
    call message_s("707", "Thank you for ur cooperation.")

    jump aftermenu20

label aftermenu20:
    call message_z("ZEN", "Rika is…")
    call message_z("ZEN", "V’s old girlfriend, and the person who created this chatroom.")
    call message_y("Yoosung★", "Rika hosted parties regularly for a good cause.")
    call message_y("Yoosung★", "She organized a group called RFA to plan the party and manage participants.")

call screen phone_reply("A party?","choice46","Good cause?","choice47")

label choice46:
    call phone_after_menu
    #pole
    call message_start_m("MC", "A party?")
    call message_s("707", "Ya")

    jump aftermenu21

label choice47:
    call phone_after_menu
    #pole
    call message_start_m("MC", "Good cause?")
    call message_s("707", "She hosted a fundraiser to help those in need")
    call message_s("707", "and introduced the guests to one another to arrange business deals.")

    jump aftermenu21

label aftermenu21:
    call message_s("707", "Rika")
    call message_s("707", "founded the organization called RFA four years ago and hosted two parties until so far.")
    call message_s("707", "The six of us who knew her personally joined the organization and helped her host the parties.")
    call message_img_y("v1.png")
    call message_y("Yoosung★", "She was an amazing person…")
    call message_y("Yoosung★", "She always sparkled.")
    call message_z("ZEN", "And Rika…")
    call message_z("ZEN", "is no longer here with us…")
    call message_z("ZEN", "She passed away a year and a half ago.")
    call message_y("Yoosung★", "…")
    call message_s("707", "MC has to know this anyways…")
    call message_z("ZEN", "Anyways, we still haven’t gotten over that yet")
    call message_z("ZEN", "so please just keep it to yourself… MC.")
    call message_ju("Jumin Han", "I still can’t believe…")
    call message_ju("Jumin Han", "that Rika knew she’d pass away and planned all this.")
    call message_ju("Jumin Han", "But I’ll just consider it as true for now since V thinks so.")
    call message_y("Yoosung★", "…I can’t imagine… someone else taking over what Rika did.")
    call message_z("ZEN", "But if we continue on like this, there’s no need for the party or our organization to continue.")
    call message_ju("Jumin Han", "We don’t even know who she is though.")
    call message_z("ZEN", "Just the fact that she’s in this chatroom makes me trust her a bit though;;")
    call message_ju("Jumin Han", "Not because MC’s a girl?")
    call message_v("V", "Everyone… I know that this is confusing. But…")
    call message_v("V", "Maybe MC was chosen by Rika.")
    call message_v("V", "707 will look into that person called ‘Unknown’.")
    call message_v("V", "So for now, please just believe in me and wait.")
    call message_s("707", "I guess ur busy right now. Ur replies are really late.")
    call message_v("V", "Yeah, I think… I have to leave right now.")
    call message_v("V", "MC, it is best not to touch anything in the apartment.")
    call message_v("V", "It won’t be good if the alarm rings.")
    call message_v("V", "Everything that you have to do… will be linked with this app installed on your phone.")

call screen phone_reply("What do you mean?","choice48","I thought this is just a messenger app?","choice49")

label choice48:
    call phone_after_menu
    call message_start_m("MC", "What do you mean?")
    #pole
    jump aftermenu22

label choice49:
    call phone_after_menu
    #pole
    call message_start_m("MC", "I thought this is just a messenger app?")
    call message_v("V", "I know there to be other features.")
    call message_v("V", "Seven will know the details.")
    call message_s("707", "Yeah.")

    jump aftermenu22

label aftermenu22:
    call message_s("707", "This app program is not just a simple messenger.")
    call message_s("707", "All the party related emails in Rika’s computer")
    call message_s("707", "will be transferred to this app.")
    call message_s("707", "U’ll be able to automatically receive the guests’ information as well.")
    call message_s("707", "And send personal messages to other members…")
    call message_v("V", "Then there’s no need for MC to touch Rika’s old things.")
    call message_ja("Jaehee Kang", "All MC has to do is use this app.")
    call message_s("707", "I put in all those features so that Rika could work more comfortably.")
    call message_s("707", "Glad there’s a use for them lol")
    call message_z("ZEN", "Hey. My messenger doesn’t have any email checking thing?")
    call message_y("Yoosung★", "Mine neither…")
    call message_y("Yoosung★", "Can’t my messenger tell me if my LoL friends are logged in?")
    call message_s("707", "omg")
    #… Jaehee emoji
    call message_v("V", "I’m sorry…")
    call message_v("V", "But I have to leave.")
    call message_s("707", "Okay. See u later, V.")
    call message_v("V", "Jumin.")
    call message_ju("Jumin Han", "?")
    call message_v("V", "Please take care of things for me.")
    call message_ju("Jumin Han", "…Alright.")
    "V has left the chatroom."
    hide v_icon
    call message_s("707", "…V’s gone.")
    call message_z("ZEN", "Yup. What’s he so busy with?")
    call message_ju("Jumin Han", "None of your business.")
    call message_s("707", "Anyways, let’s do what V said. MC, u can log into this chatroom from time to time right?")
    call message_z("ZEN", "Yup. And come chat with us regularly.")
    call message_ju("Jumin Han", "Why doesn’t everyone stop stalking and Assistant Kang summarize everything for her.")
    call message_ju("Jumin Han", "And invite her to the organization.")
    call message_ja("Jaehee Kang", "Alright.")
    call message_ja("Jaehee Kang", "RFA is an organization Rika created so that anyone can freely make donations regardless of class or nationality.")
    call message_ja("Jaehee Kang", "At the time, she hosted quite large parties once every two years, and they were very successful.")
    call message_z("ZEN", "Those were busy days. I thought people were going to trample me.")
    call message_ja("Jaehee Kang", "This chatroom was used to discuss plans for the party.")
    call message_s("707", "I created this chatroom lol.")
    call message_y("Yoosung★", "Everyone knows that already…")
    call message_ja("Jaehee Kang", "Because this chatroom contained a lot of information that cannot be publicly released")
    call message_ja("Jaehee Kang", "the app was distributed in secret only for RFA members.")
    call message_ja("Jaehee Kang", "But ever since Rika passed away, we have not hosted a single party")
    call message_ju("Jumin Han", "Yeah… not a single one.")
    call message_ju("Jumin Han", "We wanted to, but without Rika, we couldn’t proceed.")
    call message_ja("Jaehee Kang", "…And this chatroom became a place for us to talk about personal matters.")
    call message_s("707", "We check that everyone’s alive with this chatroom and literally just chat.")
    call message_y("Yoosung★", "We shared our memories of Rika too.")
    call message_ja("Jaehee Kang", "…MC, I think you were led to that place without any explanation.")
    call message_ja("Jaehee Kang", "If V is right, it seems that someone sent you there to fill Rika’s position.")
    call message_ja("Jaehee Kang", "Considering that you knowing about the existence of that place as satisfies the conditions for joining the organization, following V’s orders…")
    call message_ju("Jumin Han", "Fyi, currently there are six members. Me, V, Zen, 707, Yoosung, and Assistant Kang. Everyone in the chatroom.")
    call message_z("ZEN", "If MC joins, it will be seven.")
    call message_y("Yoosung★", "Is she… really becoming a new member?")
    call message_ju("Jumin Han", "We didn’t hear from MC yet.")
    call message_ju("Jumin Han", "MC.")
    call message_ju("Jumin Han", "All we are trying to do is host parties, raise funds, gather people… and things like that.")
    call message_ju("Jumin Han", "Our organization has done a lot of good so far.")
    call message_ju("Jumin Han", "… You will never regret joining.")
    call message_y("Yoosung★", "I thought Jumin was against her. Why the sudden change?")
    call message_ju("Jumin Han", "I am only following V’s decision.")
    call message_z("ZEN", "If you join the organization, we’ll be able to talk more. Not everyday we meet a pretty girl.")
    call message_s("707", "Uhm. How do you know she’s pretty? I didn’t even send the photo. ")
    call message_z("ZEN", "Send the photo.")
    call message_s("707", "No.")
    call message_z("ZEN", "Damn.")
    call message_ju("Jumin Han", "Men will be men.")
    call message_z("ZEN", "And you’re not a man?")
    call message_s("707", "Heard somewhere Jumin’s gay.")
    call message_z("ZEN", "Omg…")
    call message_z("ZEN", "Go away. You scare me.")
    call message_ju("Jumin Han", "Not even worth responding to that.")
    call message_y("Yoosung★", "But Zen, you have really low standards. You still care for looks?")
    call message_ja("Jaehee Kang", "Famous people must not act that way.")
    call message_z("ZEN", "Gosh~ I’m not famous~")
    call message_ju("Jumin Han", "Everyone stop messing around.")
    call message_ju("Jumin Han", "I was talking?")
    call message_ja("Jaehee Kang", "I apologize.")
    call message_ju("Jumin Han", "MC, will you join RFA?")

call screen phone_reply3("What do I get if I join?","choice50","Alright. It looks fun. I’ll give it a go.","choice51","I'm not interested.","choice52")

label choice50:
    call phone_after_menu
    #pole
    call message_start_m("MC", "What do I get if I join?")
    call message_z("ZEN", "Whatever your heart desires.")
    call message_ju("Jumin Han", "It would be nice if you could.")
    call message_z("ZEN", "MC, are you interested in musicals?")
    call message_y("Yoosung★", "Zen, I never knew you were so into girlsss!!")
    call message_z("ZEN", "No, I just like the real deal.")
    call message_z("ZEN", "Join, MC.")
    #Winking heart Zen emoji
    call message_z("ZEN", "Do you want to talk privately? I’ll give you my number.")
    call message_s("707", "Zen, why are u being so aggressive lol?")
    call message_z("ZEN", "Haha…")
    call message_ju("Jumin Han", "Has it been 3 years since his last fling?")
    call message_z("ZEN", "It’s been longer. Damn…")
    call message_z("ZEN", "But I’ve never seen you with a woman? Ever?")
    call message_y("Yoosung★", "Stop it… Guys…")
    call message_y("Yoosung★", "I’ve never… been with anyone…")
    call message_ja("Jaehee Kang", "…")
    call message_z("ZEN", "…")
    #Crying 707 emoji
    call message_ju("Jumin Han", "Anyways.")
    call message_z("ZEN", "Ye, yeah.")
    call message_z("ZEN", "Anyways, we’re just going to think that you’re joining, MC.")

    jump aftermenu23

label choice51:
    call phone_after_menu
    #roheline ja sinine
    $ y_h += 1
    $ ju_h += 1
    call message_start_m("MC", "Alright. It looks fun. I’ll give it a go.")
    call message_y("Yoosung★", "That’s a fast decision..")
    call message_ju("Jumin Han", "Ha. I like it.")
    call message_ja("Jaehee Kang", "I wonder if you have thought this through.")
    call message_z("ZEN", "Welcome, MC. Oi, Seven. Register her info asap.")
    call message_s("707", "Ya. I have to register her before she changes her mind.")
    call message_y("Yoosung★", "Even the processing is fast…")
    call message_y("Yoosung★", "MC must be a positive person, seeing that she made her decision so fast.")
    call message_ja("Jaehee Kang", "She may not be a careful person.")
    call message_ju("Jumin Han", "Assistant Kang, is there something you do not like about her?")
    call message_y("Yoosung★", "Hey~ Jaehee, don’t be like that.")
    call message_ja("Jaehee Kang", "It is not that.")
    call message_y("Yoosung★", "…I’m glad we have a girl now! It was a hopeless sausage fest until now lol.")
    call message_y("Yoosung★", "MC! If you have any questions, I can answer them.")
    call message_y("Yoosung★", "Ask anything you need.")
    call message_y("Yoosung★", "No need to worry about anything ^^")

    jump aftermenu23

label choice52:
    call phone_after_menu
    call message_start_m("MC", "I'm not interested.")
    call message_ja("Jaehee Kang", "I understand your position.")
    call message_ju("Jumin Han", "Convince her.")
    call message_ja("Jaehee Kang", "Me?")
    call message_ju("Jumin Han", "Ya.")
    call message_ja("Jaehee Kang", "Please refrain from using abbreviations. It becomes a habit.")
    call message_ju("Jumin Han", "Stop nagging me and convince her.")
    call message_y("Yoosung★", "I'm sure even Jaehee would have refused. We might seem really suspicious.")
    call message_z("ZEN", "One vote on we seem creepy")
    call message_y("Yoosung★", "222")
    call message_ja("Jaehee Kang", "3")
    call message_ju("Jumin Han", "Don't vote on things like this.")
    call message_ja("Jaehee Kang", "MC, we may seem suspicious, but we are not strange people at all.")
    call message_ju("Jumin Han", "Except for the cat abuser 707, everyone's pretty normal.")
    call message_s("707", "I want to play with ur cat again.")
    call message_ju("Jumin Han", "Don't ever come to my house. You're prohibited. I'll notify my security.")
    call message_ja("Jaehee Kang", "If MC becomes and RFA member, we might be able to host parties again.")
    call message_s("707", "Why~")
    call message_ju("Jumin Han", "What do you mean why. I have to protect my dear family.")
    call message_s("707", "But I was so loving to her.")
    call message_ju("Jumin Han", "Get lost.")
    call message_ja("Jaehee Kang", "Please help us.")
    call message_s("707", "Ouch. That was harsh T_T")
    call message_ju("Jumin Han", "Ok then... Please disappear.")
    call message_z("ZEN", "That was nicer.")
    call message_ju("Jumin Han", "Don't come near my cat please.")
    call message_ja("Jaehee Kang", "If you do not join our organization, we will be in trouble.")
    call message_ja("Jaehee Kang", "Since even if you leak the information in Rika's apartment, there will be nothing we can do.")
    call message_ja("Jaehee Kang", "To prevent that from happening, we could sue you for trespassing on Rika's apartment and resolve everything...")
    call message_ja("Jaehee Kang", "But I think it is right to give you the choice of joining the organization and solve everything peacefully.")
    call message_s("707", "Ya. If we get to sue u, u won't be able to use this chat record as evidence. We have the ability to delete everything lol.")
    call message_s("707", "We'll delete everything and just save whatever that helps us. ^^")
    call message_ja("Jaehee Kang", "If you cooperate, I will do my very best to help you work without any confusion.")
    call message_ju("Jumin Han", "I think she gets the picture now.")
    call message_s("707", "So just register her now?")
    call message_ja("Jaehee Kang", "Then... We will consider it that you have agreed.")
    call reply_message("MC", "Wtf...")
    call message_ja("Jaehee Kang", "^^")
    call message_y("Yoosung★", "Aren't we... forcing her too much?")
    call message_s("707", "We will help her if she agrees and sue her if not, so we did give MC a choice.")
    call message_y("Yoosung★", "...I guess?")

    jump aftermenu23

label aftermenu23:
    call message_s("707", "Good. I’ve registered her as a member! Oh. We don’t really need ur signature.")
    call message_y("Yoosung★", "You’re going to collect all the info so she can’t run away, right?")
    call message_s("707", "^^… Since it’s a verbal contract.")
    call message_z("ZEN", "…Don’t collect anything without MC’s permission.")
    call message_s("707", "Ya.")
    call message_s("707", "I’m gonna leave for a sec. Need to check sth.")
    call message_z("ZEN", "Background check on MC?")
    call message_s("707", "Nah~ It’s work. I have to make a living somehow.")
    call message_y("Yoosung★", "Stop it. You get paid enough.")
    call message_s("707", "How do u know how much I get paid?")
    call message_y("Yoosung★", "I saw your new car on fb…")
    call message_img_y("seven2.png")
    call message_s("707", "Oh lol. Did u like the photo?")
    call message_y("Yoosung★", "Yup.")
    call message_s("707", "Good job lol.")
    call message_s("707", "I’m gonna peace out.")
    call message_ja("Jaehee Kang", " Well, since she has joined, I think everyone can leave if they need to.")
    call message_z("ZEN", "Yeah?")
    call message_ju("Jumin Han", "Hmm. Let me check my schedule…")
    call message_y("Yoosung★", "Okay.")
    call message_s("707", "Anyways, welcome MC.")
    call message_y("Yoosung★", "Welcome!! Good luck to us.")
    call message_z("ZEN", "Glad you joined, MC ^^")
    call message_ju("Jumin Han", "We’ll see how you do.")
    call message_ja("Jaehee Kang", "For now, I look forward to working with you.")
    ""
    hide screen phone_message9
    hide jumin_icon
    "Jumin Han has left the chatroom."
    hide seven_icon
    "707 has left the chatroom."
    hide jaehee_icon
    "Jaehee Kang has left the chatroom."
    hide yoosung_icon
    "Yoosung★ has left the chatroom."
    call message_z("ZEN", "Oh… By the way")
    call message_z("ZEN", "I had a good dream last night. I think I saw you there…")
    call message_z("ZEN", "Or not. Bye~!")
    ""
    hide screen phone_message
    hide zen_icon
    "ZEN has left the chatroom."
    hide mc_icon1

init:
    $ signlvl = Position(xpos=0.5, ypos=200, xanchor=0.5, yanchor=100)

show sign at signlvl

""
hide sign
hide phone2

jump hub

return
