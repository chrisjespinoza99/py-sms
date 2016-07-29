def response_handler(body):
    message = ""
    if body == 'start':
        message = "Your friend texts you asking you to cruise with him and go to the bird sanctuary. Do you 'go with him' or 'stay in the dorm'?"
    elif body == 'stay in the dorm':
        message = "Congratulations! You are a sane person who knows a thing or two about surviving horror movies! You actually want to stay in (MS)**2 !!! Now what, though? I have to give you something to do. Do you want to bounce a 'tennis ball' around the room or just 'go to bed'?"
    elif body == 'tennis ball':
        message = "You remain in your dorm and decide to bounce a tennis ball around your room. Your dorm counselor across the hall walks into your room at 12:30 am and gives you dorm restriction for making 'too much noise'. He emails Mrs. Burgos, who then assigns you cleaning duty at Commons the next day. The lady in charge of you is named Juana. Juana makes you scrub the tables to make sure they are shiny clean. You finally finish an hour later and ponder why you didn't just cruise with your friend. You could've avoided all this. But then again, you aren't stupid and you want to live. I guess you somewhat made a right choice. The end."
    elif body == 'go to bed':
        message = "You go to bed and get the best eight hours of sleep in your life! You start off your day great and ace your physics exam! Congrats! You are doing something right! You are a model example of an (MS)**2 student!! The end! Do you want to 'start' over?"
    elif body == 'go with him':
        message = "You have arrived outside the bird sanctuary and your friend is 20 minutes late. Do you 'wait' or 'go in' without him?"
    elif body == 'wait':
        message = "You decide to wait a few minutes more when you see a creepy hooded figure standing a few feet away from you watching you. You should probably get away. Do you 'run to your dorm' or 'into the sanctuary'?"
    elif body == 'run to your dorm':
        message = "You decide to run to your dorm and keep running for a few minutes and end up by the cemetery. Do you 'hide in the cemetery' or 'keep running to your dorm'?"
    elif body == 'into the sanctuary':
        message = "You go into the sanctuary, worried about whether you are being followed or not. You continue running and eventually find a fork in the path. Do you take the 'left path' or the 'right path'?"
    elif body == 'go in':
        message = "You go into the sanctuary, wondering where your friend is. You continue walking and eventually find a fork in the path. Do you take the 'left path' or the 'right path'?"
    elif body == 'hide in the cemetery':
        message = "You go into the cemetery and look frantically for somewhere to hide. You begin hearing footsteps. Do you 'hide in a coffin' or 'behind a tombstone'?"
    elif body == 'hide in a coffin':
        message = "You climb into an empty coffin and close the lid, praying that the man didn't see you. You begin dozing off when suddenly you get a call. Your phone isn't on silent!! You silence it quickly. Do you 'wait it out' in the coffin or do you 'leave the coffin'?"
    elif body == 'wait it out':
        message = "You wait it out for a minute or so, only to hear scraping noises outside the coffin. Suddenly, a knife plunges through the coffin, piercing your body. You try to get out of the coffin only to realize it's locked. You keep getting stabbed and scream in pain. After a few minutes, you are finally resting in peace. You just DIED! Maybe you should have put your phone on vibrate as soon as you left the dorm, so you wouldn't get caught by campus security...or the hooded figure that killed you. Well, too late for that. Shame on you!!! Do you want to 'start' over?"
    elif body == 'leave the coffin':
        message = "You carefully sneak out of the coffin only to find the hooded figure standing a few feet away...with his back towards you. Do you 'sneak out of the cemetery' or 'attack the hooded figure'?"
    elif body == 'behind a tombstone':
        message = "You quickly hide behind a tombstone. You look up to find the hooded figure in the cemetery, searching for you. Do you 'sneak out of the cemetery' or wait and 'attack the hooded figure'?"
    elif body == 'sneak out of the cemetery':
        message = "You maneuver around the cemetery, hiding behind tombstones and moving your way towards the exit. You make it out of the cemetery alive and continue to your dorm when you see campus security. Do you 'talk to security' or 'continue running to your dorm'?"
    elif body == 'attack the hooded figure':
        message = "You quickly attack the figure and knock him to the ground...only to realize it's your friend! He was trying to scare you! Do you 'help him up' or leave him and 'get out of the cemetery'?"
    elif body == 'help him up':
        message = "You give your friend a hand and pull him up. He thanks you.....and then pulls out a knife and literally stabs you in the back!!! He pushes you to the ground and continues to stab you until you finally bleed to death. You are now DEAD! THE END! Do you want to 'start' over?"
    elif body == 'get out of the cemetery':
        message = "You storm off angrily and leave your friend behind. You then keep walking and make it back to your dorm. You finally go to bed, oblivious to the fact that your friend was just attacked and killed by someone else. But that doesn't matter, right? YOU survived!! Who needs friends anyways?? THE END. Do you want to 'start' over?"
    elif body == 'keep running to your dorm':
        message = "You keep running to your dorm only to see a campus security car parked outside of GW. Do you 'talk to security' and tell him about what you saw or do you 'continue running to your dorm'?"
    elif body == 'talk to security':
        message = "You go towards the car and knock on the window. The campus security guy comes out of the car and asks you what you are doing. You tell him everything and then decides to go back to the sanctuary and check it out. Do you 'go with security' or do you 'wait in the car'?"
    elif body == 'go with security':
        message = "You're too frightened to be alone, so you stick with the campus security guy and head back to the sanctuary. Do you 'go in with him' or 'wait for him outside'?"
    elif body == 'go in with him':
        message = "You go in with him. After a few minutes, you start to feel safer and relieved. Maybe you just imagined the figure......Or maybe not because he's right there!!! He runs to the campus security guy and slits his throat, killing him. You try to run, but the hooded figure grabs you by the arm and pulls you to the ground. He then stabs you repeatedly until you finally pass out and bleed to death! Your body is found the next morning hanging from a tree by your intestines. You were just brutally murdered! The END! Do you want to 'start' over?"
    elif body == 'wait for him outside':
        message = "WHY????!!!!! Are you CRAZY?!!!!! Rule #1 of horror movies: NEVER be ALONE!!! You wait outside the sanctuary for a few minutes when you hear someone get closer. The hooded figure emerges from the sanctuary, with a knife in one hand and the decapitated head of the campus security guy in the other. You remain where you are, frozen in fear. The hooded figure then grabs you and drags you into the sanctuary, where no one can hear you scream. Your decapitated head is found the next day at the top of the flagpole outside of Commons while your body is at the base of the flagpole. You just DIED!!! Maybe you should watch more horror movies!!! Do you want to 'start' over?"
    elif body == 'wait in the car':
        message = "You wait in the car for a few minutes. You begin to fall asleep in the driver's seat. THUD!! You wake up to find the dead body of the campus security guy on top of the windshield!!! You hear a scraping noise outside. The hooded figure is outside the car, scraping his knife against the car door. Do you 'stay in the car' or 'try to get out'?"
    elif body == 'try to get out':
        message = "You quickly run out of the car through the paseenger's door. The figure is nowhere to be seen. Do you try to get into 'GW' or 'continue running to your dorm'?"
    elif body == 'stay in the car':
        message = "You stay in the car and lock all the doors. Hopefully, he can't get in. After all, he doesn't have the car keys. The campus security guy does...oh wait.. The figurestands outside the window taunting you with the car keys. He begins unlocking random doors and you frantically try to lock them back. He then seems to disappear...until you see the back door of the car!! It's open and the killer is inside the car! He grabs you by the throat and slams your face in the windshield. You groan in pain... and then yell as he begins to stab you. You finally die and your body is found the next morning, with your limbs and head scattered throughout the campus. The END! Do you want to 'start' over?"
    elif body == 'continue running to your dorm':
        message = "You continue running to your dorm and then realize you have to cross Main Street! Do you 'wait for the crosswalk' or do you 'run the crosswalk'?"
    elif body == 'wait for the crosswalk':
        message = "You wait for the walk signal to turn on, worrying if you are really safe. Thankfully, the walk signal turns on and you make it to your dorm in one piece. You are abou to sleep....when you get a text from your friend. He's outside your dorm and needs your help for something urgent. Do you 'go help' your friend or 'go to bed'?"
    elif body == 'run the crosswalk':
        message = "Unfortunately, due to your impatience, you are hit by a car! Your ribs break and  your body is crushed. You die instantly! The end! Do you want to 'start over?"
    elif body == 'left path':
        message = "You choose the left path. The mooonlight is hard to see in this path and as a result, you end up walking in a bear trap. You start bleeding profusely and wonder why you didn't wait for your friend. You bleed out and die. The end."
    elif body == 'right path':
        message = "You walk on the right path for a few minutes when you start to get a little frustrated. Do you 'call your friend' or 'keep going'?"
    elif body == 'call your friend':
        message = "You try to call your friend, but you have no signal. Dang it!!! Stupid MetroPCS!!! I guess you should 'keep going'."
    elif body == 'keep going':
        message = "You eventually find yourself at the log cabin. You hear voices and yelling next to it and see people wearing masks and costumes surrounding a campfire. Suddenly, someone yells and points in your direction. Do you 'try to hide' or 'run away'?"
    elif body == 'bush':
        message = "Really??? A BUSH??!!! You are found easily and then dragged to the campfire. It seems like you've found some sort of secret cult. The cult leader then gives you an ultimatum. Do you 'join the cult' or 'refuse to join'?"
    elif body == 'tree':
        message = "You climb a tree and try to wait it out up there. However, you eventually slip and fall to the ground. You are found easily and then dragged to the campfire. It seems like you've found some sort of secret cult. The cult leader then gives you an ultimatum. Do you 'join the cult' or 'refuse to join'?"
    elif body == 'join the cult':
        message = "The cult leader smiles and then tells you that you must go through initiation to prove you are worthy. He then brings out your friend, who is tied up and gagged. The cult leader demands that you kill him. Do you 'kill your friend' or 'refuse'?"
    elif body == 'refuse to join':
        message = "The cult leader gets angry and orders the rest of the cult to tie you up. You are then tied to a wooden pole and lit on fire. You burn to death. The end. Do you want to 'start' over?"
    elif body == 'kill your friend':
        message = "You are given an axe. You look your friend in the eyes and tell him sorry before you swing the axe and hit his face, killing him instantly. The cult leader smiles and says congratulations. You are now part of the cult. There is just one catch...you cannont leave the cult ever. Now, every Saturday night, you are forced to meet and kill other friends and stangers. What a life....Maybe you should've stayed in your dorm....The end. Do you want to 'start' over?"
    elif body == 'refuse':
        message = "You refuse to kill your friend. The cult leader is furious and demands that both of you be executed. Your friend is then tied to a wooden pole and burnt to a crisp. THen, you are hung from a tree. Why didn't you just stay in your dorm? You'd still be alive. Oh well... Do you want to 'start' over?"
    elif body == 'run away':
        message = "You try to run away, but you are eventually caught by someone and dragged towards the campfire. It seems like you've found some sort of secret cult. The cult leader then gives you an ultimatum. Do you 'join the cult' or 'refuse to join'?"
    elif body == 'try to hide':
        message = "You decide to hide. Do you hide behind a 'bush' or climb up a 'tree'?"
    elif body == 'go help':
        message = "You go see what your friend wants. You angrily ask him what you want, oblivious to the fact that the hooded figure is behind you. You get stabbed in the beack by the killer. You beg your friend to help you, but he just stands there with a big smile on his face, enjoying your pain and murder. You've just been stabbed in the back! Both literally and figuratively!!! You DIE!!! The END!!! Do you want to 'start' over?"
    elif body == 'go to sleep':
        message = "You get a somewhat good sleep. Six hours of sleep isn't much, but at least you're alive!!! The end! Do you want to 'start' over?"
    elif body == 'GW':
        message = "You try to go into GW, but the doors are locked. You try to use your ID, but it doesn't work either. You wasted so much time that you could've been using to run away! The killer grabs your head and smashes it through the glass on the doors. He repeatedly does this until your face is covered in cuts and bruises. He then stabs you in the neck, killing you!! Your body is found hanging in front of Samuel Phillips the next day! The end! Do you want to 'start' over?"
    else:
        message = "Invalid command.  Text 'start' to restart the game."
    return message


#elif body == 'into the sanctuary':
        #message = "Unfortunately, this game is incomplete...please come back later for more!  Do you want to 'start' over?"