choice1 = input('\nWelcome to Butterfly Island! You wake up on the beach, unsure of how you found yourself here covered in sand. No time to ponder this though, you can see a storm brewing and need to move quickly. You look around and see that you have two options. You can traverse your way along the seashore to look for any wrecked or docked ships you can climb onto or make your way into the forest farther inland to see shelter. Type "forest" or "seashore".')

if choice1 == " forest" or "forest":
  choice2 = input('\n You pick yourself up and make your way into the dense foliage. You walk for what feels like hours, hoping that the canopy of trees will shield you from the rain when it finally falls. Finally, you find yourself at what appears to be a trampled road of grass and follow it. It leads to a crossroads post with two signs, one of which you can\'t quite make out the first part of: Bramble ruins and ___ castle. Type "bramble ruins" or "castle".')
  if choice2 == " bramble ruins" or "bramble ruins":
    choice3 = input('\nYou don\'t like the sound of a castle you don\'t know the name of or its owner so you turn and make your way to bramble ruins. The walk is shorter than you expected. You\'re here. There\'s a small lagoon and a large stone wall that appears to be overran with foliage. All of a sudden a dog springs up to you. He appears excited to see you. Do you pet the dog? Type "yes" or "no".')
    if (choice3 == " yes" or "yes"):
      print("\nYou pet the dog and he bounds away in appreciation.")
      print("\nNow back to the task at hand. You survey your surroundings more closely. The stone wall has a door on its side. In order to reach it, you will have to cross a wooden bridge that appears that it will collapse after one trip across it. If the door on the other side is locked, you would be stuck on that side of the bridge.")
      choice4 = input('\nAs you assess the situation, a glint of silver catches your eye in the water of the lagoon. You can\'t see very far down to make it out but it could be a key to that door. What do you do? Type "go to the water" or "cross the bridge".')
      if choice4 == " go to the water" or "go to the water":
        print("\nYou go investigate the glimmer of silver in the lagoon. You lean in closer and reach your hand out to grab whatever the object is. All of a sudden arms are wrapping themselves around your back and you're dragged into the water.")
        print("\nTurns out the silver you were seeing was apart of a mermaid's diadem as she was resting on a rock close to the surface and she awoke to someone reaching for it.")
        print("\nShe drowns you for your attempted theft..")
        print('\nGame over.')
      if choice4 == " cross the bridge" or "cross the bridge":
        print("\nYou avoid the lagoon. You don't know what that object is but the water is way too murky to consider touching. You decide to take a risk and cross the bridge. With the wind picking up from the impending storm, it's beginning to sway. You cross it, careful not to put your full weight on any one step. Once you've made it about 3/4 of the way there, the posts holding the bridge together begin to lean and you run to reach the other side just before the posts give out! With a collapsed bridge and raindrops beginning to fall, there's no way but forward.")
        print('\nAs you near the door, you consider how you will attempt to open it if it really is locked. You ponder various stances to throw your full weight on it when you reach the door.')
        print("\nYou try the knob... ")
        print("\nIt's unlocked.")
        print("\nGood.")
        choice5 = input('\nYou enter into a stone room. You can hear the heavy rainfall outside which makes you all the more grateful to have entered when you did. You can see three doors ahead. Through the left door you can hear what sounds like gentle playing of a piano, through the gap under the middle door you can smell roasted turkey, and through the right door appears to be torch light. You are hungry but whoever is playing the piano could help you to learn more about this place and following the torch light could lead somewhere warm you could rest. Where will you go? Type "left", "middle", or "right".')
        if choice5 == " left" or "left":
          print("\nYou open the left door and find a staircase which you descend, preparing to meet whoever is playing such a melancholy song.")
          print("\nThere's no one here. Only a damp room with a piano underneath a single barred window from which droplets of rain are pouring in. Some of the raindrops pelt the keys of the piano emitting a soft uneven tune.")
          print("\nYou're disappointed that you weren't able to speak to someone and turn back to the staircase to try the other doors.")
          print("\n... You can hear the sound of the door close.")
          print("\nYou race back up the stairs but the door is locked! Someone's locked you in!")
          print("\nYou step back to the piano, thoughts racing, when suddenly you can hear the sound of keys jangling. The dog from earlier appears at the window holding a ring of keys!")
          print("\nThe dog recognizes you instantly and bows its head towards the bars affectionately.")
          print("\nYou reach through the bars to grab the keys and give the dog a good pat for his help. No questions needed for how he got them. You're just hoping that one of them will unlock the door.")
          print("\nYou try them on the lock, growing increasingly worried when you hear a click as it unlocks. You're out and stop to ground your nerves.")
          choice6 = input('\nThe storm isn\'t letting up outside any time soon. Time to try the other doors. Your adventure in the piano room has left you even more hungry and needing of rest but you\'ve grown more wary of these rooms. Which door will you try next? Type "middle" or "right".')
          if choice6 == " middle" or "middle":
            print("You're too hungry to continue further and you make your way through the middle door. After that nasty trick in the last room, you're more than a little wary of whatever you smell roasting but when you finally enter what appears to be a small kitchen, you're met with..")
            print("AN ACTUAL TURKEY!")
            print("Slowly roasting over a small fire...")
            choice7 = input('It smells good but can you trust it? You are now starving and starting to move more sluggishly from the lack of food but there\'s no one around. Whoever locked you in that last room could have done something to it in another attempt on your life. What do you do? Type "eat the turkey" or "leave the room".')
            if choice7 == " eat the turkey" or "eat the turkey":
              print("You take a hesitant bite of the turkey and chew slowly just in case.")
              print("...")
              print("It tastes fine. Huh.")
              print("...")
              print("You wolf down the rest of the turkey, feeling more energized with every bite. You make your way back to the three doors and look outside.")
              print("The rain has been reduced to a subtle drizzle.")
              print("You survey your surroundings when out of the corner of your eye you can see a figure standing a few yards away outside. They appear to be staring at you.")
              print("You don't recognize who it is...")
              print("...The figure isn't moving...")
              choice8 = input('It\'s starting to creep you out. What do you do? Type "confront the figure" or "continue on through the right door".')
              if choice8 == " confront the figure" or "confront the figure":
                print("If that person is the one that locked you in the piano room, you're going to give them a piece of your mind. You storm outside, demanding to know what their problem is. As you grow closer, you become increasingly nervous when you're no closer to making out their features than when you first viewed them from the window.")
                print("It has no features?...")
                print("Suddenly, confronting this figure doesn't seem so appealing.")
                print("Even worse, the hairs on the end of your arms are beginning to stand up and you feel an overwhelming sense of dread.")
                print("You turn to walk back to the stone wall when suddenly, the figure is in front of you!")
                print("It grabs you and a struggle ensues. Luckily, you've just eaten and you feel fantastic. You shove off the figure and sprint back to the door and slam it behind you. You need to lock it. You quickly try each of the keys on your ring and one of them appears to go to the door because as soon as the lock turns, you can hear the figure try the knob.")
                print("It doesn't attempt to force entry, but you can hear its knocks slowly and evenly against the door. You take a moment to catch your breath.")
                print("Now your only chance at escape is whatever is through that right door. The torch light is beginning to die in the hall so you need to move quickly.")
              if choice8 == " continue on through the right door" or "continue on through the right door":
                print("You know better than to confront the looming figure. If that person is what locked you in the piano room, it does not like you.. or your will to live. Best to continue on through the right door and avoid it altogether. But first, you remember the keys that you obtained from the dog. You don't want whoever is outside to follow you deeper inside the ruins.")
                print("You lock the door and carry on into the torch-lit hall.")
            if choice7 == " leave the room" or "leave the room":
              print("A warm kitchen with a roasting turkey over a freshly-lit fire in an otherwise abandoned ruin is way too suspicious. You may be hungry but even you know poison doesn't settle a stomach very well.")
              print("You make your way back to the three doors and look outside.")
              print("The rain has been reduced to a subtle drizzle.")
              print("You survey your surroundings when out of the corner of your eye you can see a figure standing a few yards away outside. They appear to be staring at you.")
              print("You don't recognize who it is...")
              print("...The figure isn't moving...")
              choice9 = input('It\'s starting to creep you out. What do you do? Type "confront the figure" or "continue on through the right door".')
              if choice9 == " confront the figure" or "confront the figure":
                print("If that person is the one that locked you in the piano room, you're going to give them a piece of your mind. You storm outside, demanding to know what their problem is. As you grow closer, you become increasingly nervous when you're no closer to making out their features than when you first viewed them from the window.")
                print("It has no features?...")
                print("Suddenly, confronting this figure doesn't seem so appealing.")
                print("Even worse, the hairs on the end of your arms are beginning to stand up and you feel an overwhelming sense of dread.")
                print("You turn to walk back to the stone wall when suddenly, the figure is in front of you!")
                print("It grabs you and a struggle ensues. Unfortunately, your lack of energy makes you weaker. The figure easily overpowers you.")
                print("You are strangled. Game over.")
          if choice6 == " right" or "right":
            choice10 = input('You start through the torch-lit hallway. The flames are still burning bright and the torches look like they could easily be taken off the wall. Do you take a torch? Type "yes" or "no".')
        if choice5 == " middle" or "middle":
          print("You're too hungry to continue further and you'd rather converse with whoever occupies these ruins over dinner than music. You make your way through the middle door and into a small kitchen and you're met with...")
          print("AN ACTUAL TURKEY!")
          print("Slowly roasting over a small fire...")
          choice12 = input('It smells good but can you trust it? You are hungry but there\'s no one around. What do you do? Type "eat the turkey" or "leave the room".')
          if choice12 == " eat the turkey" or "eat the turkey":
            print("You take a hesitant bite of the turkey and chew slowly just in case.")
            print("...")
            print("It tastes fine. Huh.")
            print("...")
            print("You wolf down the rest of the turkey, feeling more energized with every bite. You make your way back to the three doors and look outside.")
            print("The rain has been reduced to a subtle drizzle.")
            choice13 = input('You have two doors left to try. You can attempt to ask whoever is in the piano room about the ruins or continue further through the right door. Type "left" or "right".')
            if choice13 == " left" or "left":
              print("You try the left doorknob but the door is locked. Whoever's inside must be hard at practice or just doesn't want to talk right now.")
              print("Nothing left to try but the right door then.")
              print("...")
              print("You spare a glance outside as you make your way to the right door and out of the corner of your eye you spot a figure standing a few yards away outside. They appear to be staring at you.")
              print("You don't recognize who it is...")
              print("...The figure isn't moving...")
              choice14 = input('It\'s starting to creep you out but that person could know more about this place. What do you do? Type "approach the figure" or "continue".')
              if choice14 == " approach the figure" or "approach the figure":
                print("You travel back outside intending to confront the figure about where you are and what all of this is. Having just having eaten renewed your strength and you march with determination towards the person. 'Hey!', you call out. 'Where are..?' You stop when it swivels its head? around to stare? at you. You can\'t really tell... because it has no facial features... It has no features at all. Its entire body is seemingly one giant shadow.")
                print("This doesn't seem like that grand of an idea anymore. You don\'t understand what scares you about it but you take a few steps back.")
                print("You begin walking backwards towards the door as the rain begins to pick up. Suddenly, the figure breaks out into a sprint towards you.")
                print("Panic! You find yourself stumbling over your own feet running as fast as you can back to the door!")
                print("You reach the door and close it behind you. You go to lock it but it needs a key!")
                print("A key??")
                print("...")
                print("You don\'t have a key!")
                print("...")
                choice15 = input("The only place left to go is through the right door or to stand your ground and fight. What do you do? Type 'stand your ground' or 'through the right door!'")
                if choice15 == "stand your ground" or " stand your ground":
                  print("It would just follow you through the right door anyway. Best to save your energy and confront this thing head-on. You can hear quick and light footsteps interwining with the heavy rainfall outside as you try to choose the best stance for when it smashes through that door.")
                  print("You rock back and forth on your haunches waiting for it to burst in.")
                  print("The door bursts open and you swing but it\'s on you before your arm can finish the wind-up. The figure chokes you and you die.")
                if choice15 == " through the right door!" or "through the right door!":
                  print("You have no weapon and you\'re out of breath. You need some more time to think and one more door between you and that thing seems like the best way to achieve that. You race through the right door and shut it just as you hear footsteps approach the ruins' door.")
                  print("You look around and find yourself in a dimly-lit hallway.")
                  print("There's a torch on the wall. You could use it to defend yourself.")
                  print("However, you\'re unsure of that thing\'s strength.")
                  choice16 = input("You could also continue running down the hallway and hope you find a better solution up ahead. What do you do? Type 'grab the torch' or 'run!")
                  if choice16 == "grab the torch" or " grab the torch":
                    print("You snatch the torch off the stone wall just as the figure busts down the first door into the atrium. You\'re alarmed by its display of strength as you hear the door fall off its hinges and decide to rethink your strategy.")
                    print("You quickly step behind the door of the hallway. Best to avoid direct on-sight confrontation and utilize the element of surprise against this thing.")
                    print("As it bursts through the door to the hallway, you swing the torch against its head hard!")
                    print("It goes down!")
                    print("Keep swinging!")
                    print("While your blows land, it appears to be more distressed by the torch\'s firelight than the hard metal of the torch\'s handle.")
                    print("Nevertheless, you make sure it stays down before you even consider dropping your newfound weapon.")
                    print("As you catch your breath, the figure appears to dissipate under the light of the flickering flame until where there once was the shape of a man is nothing but dark whisps of shadow.")
                    print("Okay. Now you really need to figure out what\'s going on here.")
                    print("You just ate turkey from a ghost kitchen and fought a shadow.")
                    print("Add it to your resume I guess but there don\'t appear to be any job fairs out here.")
                    print("Now all that you can do is continue onward. You travel down the hallway, torch in hand.")
              if choice14 == " continue" or "continue":
                print("The way the figure is staring at you doesn\'t seem friendly.")
                print("Best to not draw its attention anymore than necessary.")
                choice17 = input("You continue through the right door and are met by a dimly-lit hallway and torch softly flickering on the stone wall next to you. Do you take it? Type 'yes' or 'no'.")
                if choice17 == " yes" or "yes":
                  print("You take the torch off the stone wall and continue on down the hallway.")
                  print("Down a little ways is a door that opens into a small library. A large chair and coffee table sit in front of a hearth that blazes with a steady flame. You\'re exhausted and need a break.")
                  choice18 = input("Do you sit down and rest for a little while? Type 'yes' or 'no'.")
                  if choice18 == "yes" or " yes":
                    print("You drag your feet over to the hearth and slump into the chair.")
                    print("The heat from the fire fights away the chill from the rain outside.")
                    print("After eating all that turkey, you start to feel thirsty.")
                    print("A cup of tea drops down and floats right above the coffee table.")
                    print("...")
                    print("Now where the heck did that come from?")
                    choice19 = input("Do you drink it?")
                    if choice19 == "yes" or " yes":
                      print("You\'re too thirsty to question it and take a sip.")
                      print("...")
                      print("Chamomile. Lovely.")
                      print("You finish your tea, refreshed, and spring up from the chair.")
                      print("You need to find a way out of here.")
                      print("You progress through the opposite door out of the library and find yourself in a small room. The ceiling drips through cracks in the walls overrun by the torrential downpour continuing outside.")
                      print("In the middle of the room is a stone platform with three books on it.")
                      choice20 = input("You move close enough to read their titles: 'Herbs and Other Types of Vegetation', 'Potions and their Properties', 'A Beginner's Guide to Traps'. Which do you read? Type 'plants', 'potions' or 'traps'.")
                      if choice20 == "traps" or " traps":
                        print("This place has already proved the potential to be dangerous. You want to equip yourself with any knowledge you can find on what you could encounter next.")
                        print("You open the book on traps and begin to read.")
                        print(
                          "As you read, the rain steadily begins to let up. You finish the last chapter after it\'s already become a drizzle.")
                        print("You continue on with your journey through the next door.")
                        print(
                          "It opens into another long hallway but this one is darker. Luckily, you have your torch with you.")
                        print(
                          "You use it to light your line of sight but you still can\'t make out much so you turn it to the ground to hopefully guide your walking path.")
                        print(
                          "You can discern leaves on the ground which is odd. This hallway is a ways away from the entrance of the ruins.")
                        print(
                          "Any leaves somebody could have tracked in would have been left in that first hallway you passed through at the latest.")
                        choice21 = input(
                          "Step through the leaves, to the side of the leaves, or jump over the leaves? Type 'step', 'side' or 'jump'.")
                        if choice21 == "step" or " step":
                          print(
                            "You step through the leaves. 'Oh, those leaves were covering a pit',you think briefly as you fall to your demise into a pit of spikes.")
                          print("You die.")
                        if choice21 == "jump" or " jump":
                          print(
                            "Those leaves are most likely covering something. With your torch you still can\'t make out how far it goes on but you don\'t want to slip on the space on the sides of the pile.")
                          print("You choose to jump across.")
                          print(
                            "As you sail forward, however, your torchlight briefly illuminates the space you couldn\'t see further into the hallway.")
                          print("The leaf pile went on for a little longer than you thought.")
                          print("You fall through the leaves and into a spike pit.")
                          print("You die.")
                        if choice21 == "side" or " side":
                          print(
                            "Those leaves are most likely covering something. However, you can make out a space of solid stone surrounding the leaves and you use your torch to guide your way around the leaf pile.")
                          print(
                            "You\'ve successfully navigated what could have been a trap and pat yourself on the back before forging onward.")
                      if choice20 == "potions" or " potions":
                        print("By now you'\ve discerned that this place has some sort of magical presence. Best to be equipped with some knowledge against it.")
                        print("You open the potions book and read.")
                        print("As you read, the rain steadily begins to let up. You finish the last chapter after it\'s already become a drizzle.")
                        print("You continue on with your journey through the next door.")
                        print(
                          "It opens into another long hallway but this one is darker. Luckily, you have your torch with you.")
                        print(
                          "You use it to light your line of sight but you still can\'t make out much so you turn it to the ground to hopefully guide your walking path.")
                        print(
                          "You can discern leaves on the ground which is odd. This hallway is a ways away from the entrance of the ruins.")
                        print(
                          "Any leaves somebody could have tracked in would have been left in that first hallway you passed through at the latest.")
                        choice21 = input(
                          "Step through the leaves, to the side of the leaves, or jump over the leaves? Type 'step', 'side' or 'jump'.")
                        if choice21 == "step" or " step":
                          print(
                            "You step through the leaves. 'Oh, those leaves were covering a pit',you think briefly as you fall to your demise into a pit of spikes.")
                          print("You die.")
                        if choice21 == "jump" or " jump":
                          print(
                            "Those leaves are most likely covering something. With your torch you still can\'t make out how far it goes on but you don\'t want to slip on the space on the sides of the pile.")
                          print("You choose to jump across.")
                          print(
                            "As you sail forward, however, your torchlight briefly illuminates the space you couldn\'t see further into the hallway.")
                          print("The leaf pile went on for a little longer than you thought.")
                          print("You fall through the leaves and into a spike pit.")
                          print("You die.")
                        if choice21 == "side" or " side":
                          print(
                            "Those leaves are most likely covering something. However, you can make out a space of solid stone surrounding the leaves and you use your torch to guide your way around the leaf pile.")
                          print(
                            "You\'ve successfully navigated what could have been a trap and pat yourself on the back before forging onward.")
                      if choice20 == "plants" or " plants":
                        print("With so much vegetation growing in and around the ruins, you consider it best to study up on various types of plants you could encounter.")
                        print("As you read, the rain steadily begins to let up. You finish the last chapter after it\'s already become a drizzle.")
                        print("You continue on with your journey through the next door.")
                        print("It opens into another long hallway but this one is darker. Luckily, you have your torch with you.")
                        print("You use it to light your line of sight but you still can\'t make out much so you turn it to the ground to hopefully guide your walking path.")
                        print("You can discern leaves on the ground which is odd. This hallway is a ways away from the entrance of the ruins.")
                        print("Any leaves somebody could have tracked in would have been left in that first hallway you passed through at the latest.")
                        choice21 = input("Step through the leaves, to the side of the leaves, or jump over the leaves? Type 'step', 'side' or 'jump'.")
                        if choice21 == "step" or " step":
                          print("You step through the leaves. 'Oh, those leaves were covering a pit',you think briefly as you fall to your demise into a pit of spikes.")
                          print("You die.")
                        if choice21 == "jump" or " jump":
                          print(
                            "Those leaves are most likely covering something. With your torch you still can\'t make out how far it goes on but you don\'t want to slip on the space on the sides of the pile.")
                          print("You choose to jump across.")
                          print(
                            "As you sail forward, however, your torchlight briefly illuminates the space you couldn\'t see further into the hallway.")
                          print("The leaf pile went on for a little longer than you thought.")
                          print("You fall through the leaves and into a spike pit.")
                          print("You die.")
                        if choice21 == "side" or " side":
                          print("Those leaves are most likely covering something. However, you can make out a space of solid stone surrounding the leaves and you use your torch to guide your way around the leaf pile.")
                          print("You\'ve successfully navigated what could have been a trap and pat yourself on the back before forging onward.")



                
                  