#ANOTHER STORY PROULOGE

define v = Character("V")
define r = Character("Ray")
define u = Character("???")
define m = Character("MC")
define d = Character("Driver")
image as_v_closed_eyes = Transform("as_v_closed_eyes.png", zoom=1.4)
image as_v_sad = Transform("as_v_sad.png", zoom=1.4)
image as_v_surprised = Transform("as_v_surprised.png", zoom=1.4)
image as_v_tavaline = Transform("as_v_tavaline.png", zoom=1.4)

init:
    $ asv_lvl = Position(xpos=0.5, ypos=100, xanchor=0.5, yanchor=50)
    $ ray_lvl = Position(xpos=0.5, ypos=190, xanchor=0.5, yanchor=50)

label another_story:

menu:

    "Watch intro-video?"

    "Yes":
        jump intro2


    "No":
        jump start_as

label intro2:
    $ renpy.movie_cutscene("as_intro.mpg")

label start_as:

    stop music
    "(One month after Rika's death.)"
    voice "asv01.ogg"
    v "Rika..."
    voice "asv02.ogg"
    v "If I could go back to the past, I would have made a different choice..."
    "....."
    show as_sm_grave
    show as_v_closed_eyes at asv_lvl
    voice "asv03.ogg"
    v "It's already been 1 month since you left."
    voice "asv04.ogg"
    hide as_v_closed_eyes
    show as_v_tavaline at asv_lvl
    v "Seems you absence is still grave within the members. Everyone's deeply grieving since you left."
    voice "asv05.ogg"
    hide as_v_tavaline
    show as_v_sad at asv_lvl
    v "Feels like it's my fault that you left... from where did it go wrong...?"
    voice "asv06.ogg"
    hide as_v_sad
    show as_v_closed_eyes at asv_lvl
    v "Guess blaming myself won't solve anything... I was determined to do anything to undo the past.. but... will it happen how I want it to happen?"
    voice "asv07.ogg"
    v "Every time my eyes pain me, I am reminded of you... If this were your light-hearted way of testing me... I'd rather prefer that."
    voice "asv08.ogg"
    hide as_v_closed_eyes
    show as_v_surprised at asv_lvl
    v "Ah... This flower... I wonder who left it here."
    hide as_v_surprised
    show as_v_sad at asv_lvl
    voice "asv09.ogg"
    v "Narcissus... Maybe Yoosung?..."
    voice "asv10.ogg"
    v "We talked of a flower shop yesterday, maybe this was why. He purposely got the one you like."
    hide as_v_sad
    show as_v_closed_eyes at asv_lvl
    voice "asv11.ogg"
    v "I'll give this to you in person."
    hide as_v_closed_eyes

    hide as_sm_grave

    "*Insert chatroom between Unknown and MC, which I haven't written yet here*"

    show as_sm_street

    voice "phone.ogg"
    "(Cellphone vibrating)."
    voice "phone.ogg"
    "(Incoming Call.)"
    # menu:
    voice "asu01.ogg"
    u "Hey. It's me, the one who was just chatting with you."
    #menu
    m "Unknown?"
    voice "asu02.ogg"
    u "(Sorry for the clipping) Yeah, it's me."
    voice "asu03.ogg"
    u "Your voice over the phone is cute. I can't wait to see you..."
    voice "asu04.ogg"
    u "As I mentioned in the chatroom, I called to explain to you about this app."
    voice "asu05.ogg"
    u "And also thought that talking while you hear my voice will be more credible."
    voice "asu06.ogg"
    u "In truth, a tutorial within the game was supposed to explain everything,"
    voice "asu07.ogg"
    u "but it's still being modified."
    voice "asu08.ogg"
    u "Do you remember the characters I sent you?"
    #menu
    m "Yes, I remember."
    voice "asu09.ogg"
    u "Yeah, the image I sent you of the game characters I'm currently developing."
    voice "asu10.ogg"
    u "Those characters will be your chatting partners."
    voice "asu11.ogg"
    u "All five characters in the image are part of an association called RFA."
    #menu
    m "RFA?"
    voice "asu12.ogg"
    u "RFA is a closed organization with the purpose of holding fundraising parties."
    voice "asu13.ogg"
    u "The plot is set to open a fundraising party with your help."
    voice "asu14.ogg"
    u "You've been set as the party coordinator, in charge of inviting guests."
    voice "asu15.ogg"
    u "Just think that you are the one choosing whom to invite to the party."
    #menu
    m "I can just choose guests however I like?"
    voice "asu16.ogg"
    u "The characters inside the game will recommend you the guests."
    voice "asu17.ogg"
    u "Depending on how you answer them, the guest may or may not come."
    voice "asu18.ogg"
    u "Of course it'll be a disappointment if it's only inviting guests."
    voice "asu19.ogg"
    u "You will find out their secrets by chatting/answering phone calls with the characters."
    voice "asu20.ogg"
    u "It'll be much faster to understand by playing, instead of listening to all this."
    #menu
    m "Alright, fine. I'll do it."
    voice "asu21.ogg"
    u "Thanks! I was terrified that you'll refuse."
    voice "asu22.ogg"
    u "Right. But this game hasn't been released yet and cannot be revealed to the market."
    voice "asu23.ogg"
    u "So to perform the tests, you have to come over here."
    #menu
    m "Where's here?"
    voice "asu24.ogg"
    u "You probably won't know even if I told you. It's in the mountains and doesn't appear on the map."
    voice "asu25.ogg"
    u "To maintain confidentiality before the release, it's being developed in a sparsely populated area."
    voice "asu26.ogg"
    u "Of course, you don't have to come here yourself as it's troublesome."
    voice "asu27.ogg"
    u "I'll send a car over to your place if you tell me your address."
    voice "asu28.ogg"
    u "Hop onto that and head this way."
    #menu
    m "Umm... Alright."
    voice "asu29.ogg"
    u "Wow, I didn't expect an okay at one go. You trust me, right? Thanks!"
    "(Send address)"
    voice "asu30.ogg"
    u "I'll send a car right now to the address you've sent me. Please be there."
    voice "asu31.ogg"
    u "Oh. I'm telling you this in advance, so don't freak out."
    voice "asu32.ogg"
    u "The location I'm at is also confidential and it can't be revealed."
    voice "asu33.ogg"
    u "You won't be able to see the road to this place. Don't be scared and do as I tell you."
    voice "asu34.ogg"
    u "I should hang up now. I should also get ready."
    #menu
    m "Get ready?"
    voice "asu35.ogg"
    u "Yes. Get ready to greet you."
    voice "asu36.ogg"
    u "My heart's fluttering from the thought that I can meet you soon..."
    voice "asu37.ogg"
    u "Everything will be complete once you're here."
    voice "asu38.ogg"
    u "Then... I'll see you later."
    voice "phone_hungup.ogg"
    "Phone disconnected."
    "......"
    hide as_sm_street

    show as_sm_auto
    voice "asd01.ogg"
    d "Are you MC? I've been ordered to pick you up."
    voice "asd02.ogg"
    d "The location is confidential, can you put on these sleep masks?"
    #menu
    m "Yes. Thank you."
    voice "asd03.ogg"
    d "Thank you for being considerate."
    voice "asd04.ogg"
    d "We should get going."
    hide as_sm_auto
    voice "auto1.ogg"
    "(Moving...)"
    "..."
    "......"
    voice "auto2.ogg"
    "(Car stopped)"
    voice "asd05.ogg"
    d "We have arrived. Please don't get off yet."
    voice "asd06.ogg"
    d "And I'm sorry, but you have to wear the sleeping mask again."
    voice "asd07.ogg"
    d "...Mr. Ray has arrived."
    voice "auto3.ogg"
    "(Car door opened)"
    voice "asu39.ogg"
    "Welcome. I've been waiting. Welcome to this wonderful place."
    voice "asu40.ogg"
    "It wouldn't have been an easy decision to come here... Thanks for trusting me."
    #menu
    m "Unknown?"
    voice "asu41.ogg"
    u "You knew who I was by just listnening to my voice?"
    # voice "asu42.ogg"
    u "(I lost the voice clip)Yeah, it's me. Username Unknown."
    voice "asu43.ogg"
    u "Didn't you think Unknown was a funny name? It was a default name because I didn't set up a username. No special meaning."
    voice "asu44.ogg"
    u "My name is Ray."
    voice "asr01.ogg"
    r "Thanks for coming all this way."
    voice "asr02.ogg"
    r "I really want to show you around, I prepped up this and that while waiting for you."
    voice "asr03.ogg"
    r "Oh, don't take off the mask yet. You can't take it off until we reach your room."
    #menu
    m "That's shady."
    voice "asr04.ogg"
    r "There's nothing shady here. This place is like my spiritual hometown."
    voice "asr05.ogg"
    r "Trust me... There's no way I'm going to hurt you."
    voice "asr06.ogg"
    r "You're my priceless guest. It was tough bringing you here, girl."
    voice "asr07.ogg"
    r "I'll hold your hand on your way down the car."
    m "Thank you."
    voice "asr08.ogg"
    r "You're thanking me?"
    voice "asr09.ogg"
    r "No, thank you. You are doing what I tell you to do."
    voice "auto4.ogg"
    "(Car door closed)"
    voice "asr10.ogg"
    r "Shall we go? Just trust me and follow me."
    voice "asr11.ogg"
    r "Hold on to my hand."
    voice "sammud.ogg"
    "(Walking...)"
    "...."
    "..."
    ".."
    "(After walking about 5 minutes.)"
    voice "asr12.ogg"
    r "You have no idea what a relief it was when you said you'll help."
    voice "asr13.ogg"
    r "What a relief, thanks to you."
    voice "asr14.ogg"
    r "You'll be a big help."
    #menu
    m "What were you going to do if I said no?"
    voice "asr15.ogg"
    r "...well."
    voice "asr16.ogg"
    r "I don't want to think about it."
    voice "asr17.ogg"
    r "We could have delayed the game's release date."
    voice "asr18.ogg"
    r "Or it could have been a disaster, nobody knows."
    voice "asr19.ogg"
    r "We're here. Come, I'll remove your mask."

    show as_sm_meroom
    show as_ray_happy at ray_lvl
    voice "asr20.ogg"
    r "Hi!"
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr21.ogg"
    r "First time seeing each other face-to-face, isn't it?"
    #menu
    m "Hello... Nice to meet you."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr22.ogg"
    r "Yeah. It feels great to talk to you in person, eye-to-eye."
    hide as_ray_happy
    show as_ray_closed_eyes at ray_lvl
    voice "asr23.ogg"
    r "Thanks for trusting me and coming here."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr24.ogg"
    r "This is your room."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr25.ogg"
    r "I've tried my best in preparing all this... still, let me know of any inconvenience"
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr26.ogg"
    r "and you're free to roam this floor, but for other floors you'll have to tell me first."
    hide as_ray_neutral
    show as_ray_creepy1 at ray_lvl
    voice "asr27.ogg"
    r "The reason... you know why, right?"
    m "Because it's confidential?"
    hide as_ray_creepy1
    show as_ray_happy at ray_lvl
    voice "asr28.ogg"
    r "Correct. You know very well. You have good memory."
    hide as_ray_happy
    show as_ray_creepy1 at ray_lvl
    voice "asr29.ogg"
    r "I don't hate smart people."
    hide as_ray_creepy1
    show as_ray_neutral at ray_lvl
    voice "asr30.ogg"
    r "I get the feeling that you'll pull this off quite well."
    hide as_ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr31.ogg"
    r "We still have some time left. I'll explain a bit about the game."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr32.ogg"
    r "As I mentioned before, the purpose of the game is to hold a party with RFA"
    voice "asr33.ogg"
    r "All the characters that appear there are AIs that I've designed."
    hide as__ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr34.ogg"
    r "There's one problem as I've tried to make it super-realitic with the AI."
    #menu
    m "What problem?"
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr35.ogg"
    r "It's... Umm..."
    hide as_ray_neutral
    show as_ray_creepy1 at ray_lvl
    voice "asr36.ogg"
    r "The AIs turn super-suspicious when a new person comes in."
    hide as_ray_creepy1
    show as_ray_neutral at ray_lvl
    voice "asr37.ogg"
    r "Your concept is that someone hacked your messenger and that's how you got into the RFA chatroom."
    hide as_ray_neutral
    show as_ray_creepy1 at ray_lvl
    voice "asr38.ogg"
    r "Quite suspicious, isn't it?"
    #menu
    m "Someone hacked the messenger?"
    hide as_ray_creepy1
    show as_ray_happy at ray_lvl
    voice "asr39.ogg"
    r "Yes. And then you join the chatroom."
    hide as_ray_happy
    show as_ray_closed_eyes at ray_lvl
    voice "asr40.ogg"
    r "So, everyone will be cautious of you."
    hide as_ray_closed_eyes
    show as_ray_creepy1 at ray_lvl
    voice "asr41.ogg"
    r "That's the setting of the game. It's no fun when everyone likes you from the start, is it?"
    hide as_ray_creepy1
    show as_ray_closed_eyes at ray_lvl
    voice "asr42.ogg"
    r "They'll ask you about the hacker. But you can't answer them because you know nothing..."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr43.ogg"
    r "They'll try to find out how you got to download this app, where you currently are..."
    voice "asr44.ogg"
    r "and might even try to pry out about the creator, me."
    hide as_ray_neutral
    show as_ray_oh at ray_lvl
    voice "asr45.ogg"
    r "At that, you can't reveal the truth. You must keep the secret to the end."
    hide as_ray_oh
    show as_ray_closed_eyes at ray_lvl
    voice "asr46.ogg"
    r "Can you promise me that you won't reveal what we've been talking about to the AIs?"
    #menu
    m "What happens if I speak the truth?"
    voice "asr47.ogg"
    r "Game... Over?"
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr48.ogg"
    r "I'll also be devastated when you finish as game over... So never ever tell the truth."
    hide as_ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr49.ogg"
    r "Don't forget -"
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr50.ogg"
    r "How you got this app, your current location... it's all a secret."
    voice "asr51.ogg"
    r "and who I am, the fact they're AIs are obviously a secret."
    hide as_ray_neutral
    show as_ray_oh at ray_lvl
    voice "asr52.ogg"
    r "You have to be careful, if the game goes through forced shutdown, you have to start all over again from the beginning."
    hide as_ray_oh
    show as_ray_closed_eyes at ray_lvl
    voice "asr53.ogg"
    r "There are slight difference depending on how you talk to them."
    hide as_ray_closed_eyes
    show as_ray_creepy1 at ray_lvl
    voice "asr54.ogg"
    r "but if they don't accept you into the association easily, say, 'Someone called Rika sent me to hold the party.'"
    #menu
    m "Who's Rika?"
    hide as_ray_creepy1
    show as_ray_neutral at ray_lvl
    voice "asr55.ogg"
    r "She's a character within the game."
    hide as_ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr56.ogg"
    r "The other characters will tell you what kind of character she is, but simply put, she's the one who founded the group in the game."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr57.ogg"
    r "And as I mentioned through the phone, your role in the game is party coordinator."
    voice "asr58.ogg"
    r "Depending on how you talk to your potential guests, they will either come to the party or decline."
    #menu
    m "Can I choose a different role?"
    hide as_ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr59.ogg"
    r "Oh - that function doesn't exist yet."
    hide as_ray_closed_eyes
    show as_ray_happy at ray_lvl
    voice "asr60.ogg"
    r "But that's a great idea. Playing from a different role... great idea."
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr61.ogg"
    r "Inviting the guests is more crucial than you think, try to invite them with your best effort."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr62.ogg"
    r "Don't forget that there might be more interesting events than the RFA party, depending on what choices you make."
    hide as_ray_happy
    show as_ray_closed_eyes at ray_lvl
    voice "asr63.ogg"
    r "And last of all, this is the most important thing."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr64.ogg"
    r "You have to tell me what you think as you play the game."
    voice "asr65.ogg"
    r "Even the smallest thing is okay. Tell me everything, how the party went, what the characters said to you..."
    hide as_ray_neutral
    show as_ray_creepy1 at ray_lvl
    voice "asr66.ogg"
    r "That way, I'll know how well the game is going... Your role is important."
    #menu
    m "I think it'll end with hosting parties and no chance to build a relationship."
    hide as_ray_creepy1
    show as_ray_happy at ray_lvl
    voice "asr67.ogg"
    r "Hahaha, you don't have to worry about that."
    voice "asr68.ogg"
    r "You're already truly attractive, the AIs will notice your charm."
    hide as_ray_happy
    show as_ray_creepy1 at ray_lvl
    voice "asr69.ogg"
    r "Just keep the secrets well, okay?"
    hide as_ray_creepy1
    show as_ray_neutral at ray_lvl
    voice "asr70.ogg"
    r "Well then, can you give me your phone for a sec? I'll install the game."
    #menu
    m "Here."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr71.ogg"
    r "Thanks, I only need it for a few minutes."
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr72.ogg"
    r "A few moments, please."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr73.ogg"
    r "It's done. Here, it'll finish installing in a few minutes."
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr74.ogg"
    r "Do you have any other questions about the game?"
    #menu
    m "How do I pursue you, Ray?"
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr75.ogg"
    r "Me? Hahaha..."
    voice "asr76.ogg"
    r "Though I'm not a character inside the game."
    hide as_ray_happy
    show as_ray_neutral at ray_lvl
    voice "asr77.ogg"
    r "I've always dreamed of someone who's a good listener to what I say."
    hide as_ray_neutral
    show as_ray_closed_eyes at ray_lvl
    voice "asr78.ogg"
    r "My voice is quite small... most people don't seem to listen very well."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr79.ogg"
    r "Oh, and lastly... I know I keep emphasizing this but... don't forget to keep the secret."
    hide as_ray_neutral
    show as_ray_mad at ray_lvl
    voice "asr80.ogg"
    r "Don't ever... try to get the game over easily. Promise me that, please?"
    #menu
    m "Umm, they're really AIs, right?"
    hide as_ray_mad
    show as_ray_neutral at ray_lvl
    voice "asr81.ogg"
    r "No doupt."
    hide as_ray_neutral
    show as_ray_creepy1 at ray_lvl
    voice "asr82.ogg"
    r "You'll find out right away that they're not as interesting as me..."
    hide as_ray_creepy1
    show as_ray_closed_eyes at ray_lvl
    voice "asr83.ogg"
    r "I want to talk to you a bit more, but I have to get going now."
    hide as_ray_closed_eyes
    show as_ray_neutral at ray_lvl
    voice "asr84.ogg"
    r "The plot is that when you start the game, the messenger has been hacked and they're all surprised that you suddenly entered the chatroom."
    hide as_ray_neutral
    show as_ray_happy at ray_lvl
    voice "asr85.ogg"
    r "Okay then, give it your best, coordinator."
    "....."
    "There is a game application on the screen I've never seen before."
    "(Start the game)"
    "Insert chatroom which I'm too lazy to write here."
    "das it"

return
