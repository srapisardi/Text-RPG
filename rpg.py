import random
import time


#These are the starting stats for your character and the enemies
max_hp = 10
current_hp = 10
level = 1
current_exp = 0
next_level_exp = 10
max_enemy_hp = 10
max_damage = 10
max_enemy_damage = 10
kills = 0
potions = 0



enemies = ('Goblin', 'Skeleton', 'Orc', 'Witch', 'Demon', 'Necromancer', 'Giant Spider', 'Ghoul', 'Zombie', 'Wolf', 'Cannibal', 'Vampire', 'Mummy', 'Grizzly Bear')
choices = ['> MOVE', '> STATUS', '> USE POTION', '> QUIT']
encounter = ['> ATTACK', '> DEFEND', '> RUN', '> USE POTION', '> STATUS']


name = input("What is your character's name: ")
print("Greetings",name)
time.sleep(1)
print("Your adventure begins now. Good luck!")
time.sleep(1)
print("You have been kidnapped by an unknown entity and wake up in a desolated forest with no one in sight. \nThe stench of evil enemies surround you. \nAs you explore the forest, you see a soldier's corpse shredded into pieces.\nYou pick up his remaining equipment for protection: A sword, shield and armor.\nNow that you are equipped, there is only one objective: Survive.")
time.sleep(5)


while current_hp > 0:
    for options in choices:
        print(options)

    action = input("What would you like to do? ").lower().strip()

    if not action in('move','status','use potion','quit'):
        print("Invalid Command")
        time.sleep(1)
        continue

    if action == "quit" : break

    if action == "status":
        print("Your health is",current_hp,"out of",max_hp)
        time.sleep(1)
        print("Level:",level)
        time.sleep(1)
        print("Experience:",current_exp,"out of",next_level_exp)
        time.sleep(1)
        print("Max damage:",max_damage)
        time.sleep(1)
        print("Potions:",potions)
        time.sleep(1)

    elif action == "use potion":
        if potions == 0:
            print("You are out of potions.")
            time.sleep(1)
            continue

        if current_hp == max_hp:
            print("You are already at full health.")
            time.sleep(1)
            continue

        current_hp = current_hp + round((max_hp * .5))
        if current_hp > max_hp:
            current_hp = max_hp
            potions = potions - 1
            print("Your health has been restored to",current_hp,"out of",max_hp)
            time.sleep(1)
            continue
        elif current_hp < max_hp:
            potions = potions - 1
            print("Your health has been restored to",current_hp,"out of",max_hp)
            time.sleep(1)
            continue

    elif action == "move":

        random_encounter = random.randint(1,10)

        if random_encounter in (1,2,3):
            print("You found an empty house for safety.")
            time.sleep(1)
            continue

        if random_encounter == 4:
            print("You found wild berries.")
            time.sleep(1)
            eat_berry = input("Do you want to eat them: Yes or No?").lower().strip()
            if eat_berry == "yes":
                random_effect = random.randint(0,1)
                if random_effect == 0:
                    poison_berry = round(current_hp * .5)
                    current_hp = current_hp - poison_berry
                    print("You ate a poison berry and lose",poison_berry,"health.")
                    time.sleep(1)
                    print("Your health is",current_hp,"out of",max_hp)
                    time.sleep(1)
                    if current_hp <= 0:
                        print("You have been poisoned to death.")
                        time.sleep(1)
                        break
                    if current_hp > 0 : continue
                if random_effect == 1:
                    nutritious_berry = round(current_hp * .5)
                    if current_hp == max_hp:
                        print("You found a nutritious berry but HP already at max.")
                        time.sleep(1)
                    else:
                        current_hp = current_hp + nutritious_berry
                        if current_hp > max_hp:
                            current_hp = max_hp
                            print("You ate a nutritious berry and gain",nutritious_berry,"health.")
                            time.sleep(1)
                        else:
                            print("You ate a nutritious berry and gain",nutritious_berry,"health.")
                            time.sleep(1)
                            print("Your health is",current_hp,"out of",max_hp)
                            time.sleep(1)
                            continue
            elif eat_berry == "no":
                print("The berry looks suspicious and you choose not to eat it.")
                time.sleep(1)
                continue

        if random_encounter == 5:
            injury = round(max_damage * .25)
            max_damage = max_damage - injury
            print("You injured yourself and feel weaker. Max damage falls to",max_damage)
            time.sleep(1)
            continue

        if random_encounter == 6:
            strength = round(max_damage * .25)
            max_damage = max_damage + strength
            print("Your conditioning improves and feel stronger. Max damage increases to",max_damage)
            time.sleep(1)
            continue

        if random_encounter == 7:
            potions = potions + 1
            print("You found a potion on the ground and put it in your bag.")
            time.sleep(1)
            continue

        if random_encounter in (8,9,10):
            enemy_hp = random.randint(1,max_enemy_hp)
            print("You have encountered",random.choices(enemies))
            print("Enemy HP:",enemy_hp)
            time.sleep(1)

            while current_hp >= 0:
                if current_hp <= 0:
                    print("Your character has died.")
                    time.sleep(1)
                    break

                for battle_options in encounter:
                    print(battle_options)

                battle_action = input("What is you next move?").lower().strip()

                if not battle_action in('attack','defend','use potion','run','status'):
                    print("Invalid Command")
                    time.sleep(1)
                    continue

                if battle_action.lower().strip() == "run":
                    print("You ran away safely")
                    time.sleep(1)
                    enemy_hp = random.randint(1,max_enemy_hp)
                    break

                elif battle_action == "status":
                    print("Your health is",current_hp,"out of",max_hp)
                    time.sleep(1)
                    print("Level:",level)
                    time.sleep(1)
                    print("Experience:",current_exp,"out of",next_level_exp)
                    time.sleep(1)
                    print("Max damage:",max_damage)
                    time.sleep(1)
                    print("Potions:",potions)
                    time.sleep(1)
                    continue

                elif battle_action == "use potion":
                    if potions == 0:
                        print("You are out of potions.")
                        time.sleep(1)
                        continue

                    if current_hp == max_hp:
                        print("You are already at full health.")
                        time.sleep(1)
                        continue

                    current_hp = round(current_hp + (max_hp * .5))
                    if current_hp > max_hp:
                        current_hp = max_hp
                        potions = potions - 1
                        print("Your health has been restored to",current_hp,"out of",max_hp)
                        time.sleep(1)
                        continue
                    elif current_hp < max_hp:
                        potions = potions - 1
                        print("Your health has been restored to",current_hp,"out of",max_hp)
                        time.sleep(1)
                        continue

                elif battle_action == "defend":
                    print("You blocked an attack and take no damage")
                    time.sleep(1)
                    continue

                elif battle_action == "attack":
                    damage = random.randint(0,max_damage)
                    print("You caused",damage,"damage.","\a")
                    time.sleep(1)
                    enemy_hp = enemy_hp - damage
                    print("The enemy is at",enemy_hp,"health.")
                    time.sleep(1)

                    if enemy_hp <= 0:
                        print("The enemy has been defeated!")
                        time.sleep(1)
                        kills = kills + 1
                        gained_exp = random.randint(1,10)
                        print("You gained",gained_exp,"XP.")
                        time.sleep(1)
                        current_exp = current_exp + gained_exp
                        print("Experience:",current_exp,"out of",next_level_exp)
                        time.sleep(1)
                        if current_exp >= next_level_exp:
                            level = level + 1
                            print("You are now level",level)
                            time.sleep(1)
                            next_level_exp = next_level_exp + 15
                            max_hp = max_hp + random.randint(1,5)
                            print("Your maximum health is now",max_hp)
                            time.sleep(1)
                            max_damage = max_damage + random.randint(1,5)
                            print("Your maximum damage is now",max_damage)
                            time.sleep(1)
                            max_enemy_damage = max_enemy_damage + random.randint(1,5)
                            max_enemy_hp = max_enemy_hp + random.randint(1,5)
                            current_hp = max_hp
                            print("Your health has been restored to",current_hp,"out of",max_hp)
                            time.sleep(1)
                        potion_chance = random.randint(1,10)
                        if potion_chance == 1:
                            potions = potions + 1
                            print("The enemy has dropped a potion. You place the potion in your bag")
                            time.sleep(1)
                        break

                    else:
                        enemy_damage = random.randint(0,max_enemy_damage)
                        print("The enemy does",enemy_damage,"damage.","\a")
                        time.sleep(1)
                        current_hp = current_hp - enemy_damage
                        print("You are at",current_hp,"out of",max_hp)
                        time.sleep(1)
                        continue




print("Game Over!")
time.sleep(1)
print("Your character finished at level:",level)
time.sleep(1)
print("Number of kills:",kills)




#This is a test


# Current Bugs
# None...so far

# Ideas
# Drop item upgrades from enemies to improve characters stats
# Make defend option better. Still thinking of ideas.
# Chance enemy attacks first.
# When player reaches level 100, player battles the final boss. The final boss will be the toughest enemy in the game.
