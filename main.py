# DCC level 0 character generator

from random import randint, choice
import csv

# TABLES

# Lucky Sign table
lucky_signs = {
    '1': 'Harsh winter: All attack rolls', 
    '2': 'The bull: Melee attack rolls', 
    '3': 'Fortunate date: Missile fire attack rolls', 
    '4': 'Raised by wolves: Unarmed attack rolls', 
    '5': 'Conceived on horseback: Mounted attack rolls', 
    '6': 'Born on the battlefield: Damage rolls', 
    '7': 'Path of the bear: Melee damage rolls', 
    '8': 'Hawkeye: Missile fire damage rolls', 
    '9': 'Pack hunter: Attack and damage rolls for -level starting weapon', 
    '10': 'Born under the loom: Skill checks (including thief skills)', 
    '11': "Fox's cunning: Find/disable traps", 
    '12': 'Four-leafed clover: Find secret doors', 
    '13': 'Seventh son: Spell checks', 
    '14': 'The raging storm: Spell damage', 
    '15': 'Righteous heart: Turn unholy checks', 
    '16': 'Survived the plague: Magical healing*', 
    '17': 'Lucky sign: Saving throws', 
    '18': 'Guardian angel: Savings throws to escape traps', 
    '19': 'Survived a spider bite: Saving throws against poison', 
    '20': 'Struck by lightning: Reflex saving throws', 
    '21': 'Lived through famine: Fortitude saving throws', 
    '22': 'Resisted temptation: Willpower saving throws', 
    '23': 'Charmed house: Armor Class', 
    '24': 'Speed of the cobra: Initiative', 
    '25': 'Bountiful harvest: Hit points (applies at each level)', 
    '26': "Warrior's arm: Critical hit tables**", 
    '27': 'Unholy house: Corruption rolls', 
    '28': 'The Broken Star: Fumbles**', 
    '29': 'Birdsong: Number of languages', 
    '30': 'Wild child: Speed (each +1/-1 = +5ft/-5ft speed)'}

# Occupation table
occupations = {
        '1': {'Occupation': 'Alchemist', 'Trained Weapon': 'Staff', 'Trade Goods': 'Oil, 1 flask'}, 
        '2': {'Occupation': 'Animal trainer', 'Trained Weapon': 'Club', 'Trade Goods': 'Pony'}, 
        '3': {'Occupation': 'Armorer', 'Trained Weapon': 'Hammer (as club)', 'Trade Goods': 'Iron helmet'}, 
        '4': {'Occupation': 'Astrologer', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Spyglass'}, 
        '5': {'Occupation': 'Barber', 'Trained Weapon': 'Razor (as dagger)', 'Trade Goods': 'Scissors'}, 
        '6': {'Occupation': 'Beadle', 'Trained Weapon': 'Staff', 'Trade Goods': 'Holy symbol'}, 
        '7': {'Occupation': 'Beekeeper', 'Trained Weapon': 'Staff', 'Trade Goods': 'Jar of honey'}, 
        '8': {'Occupation': 'Blacksmith', 'Trained Weapon': 'Hammer (as club)', 'Trade Goods': 'Steel tongs'}, 
        '9': {'Occupation': 'Butcher', 'Trained Weapon': 'Cleaver (as axe)', 'Trade Goods': 'Side of beef'}, 
        '10': {'Occupation': 'Caravan guard', 'Trained Weapon': 'Short sword', 'Trade Goods': 'Linen, 1 yard'}, 
        '11': {'Occupation': 'Cheesemaker', 'Trained Weapon': 'Cudgel (as staff)', 'Trade Goods': 'Stinky cheese'}, 
        '12': {'Occupation': 'Cobbler', 'Trained Weapon': 'Awl (as dagger)', 'Trade Goods': 'Shoehorn'}, 
        '13': {'Occupation': 'Confidence artist', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Quality cloak'}, 
        '14': {'Occupation': 'Cooper', 'Trained Weapon': 'Crowbar (as club)', 'Trade Goods': 'Barrel'}, 
        '15': {'Occupation': 'Costermonger', 'Trained Weapon': 'Knife (as dagger)', 'Trade Goods': 'Fruit'}, 
        '16': {'Occupation': 'Cutpurse', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Small chest'}, 
        '17': {'Occupation': 'Ditch digger', 'Trained Weapon': 'Shovel (as staff)', 'Trade Goods': 'Fine dirt, 1 lb.'}, 
        '18': {'Occupation': 'Dock worker', 'Trained Weapon': 'Pole (as staff)', 'Trade Goods': '1 late RPG book'}, 
        '19': {'Occupation': 'Dwarven apothecarist', 'Trained Weapon': 'Cudgel (as staff)', 'Trade Goods': 'Steel vial'}, 
        '20': {'Occupation': 'Dwarven blacksmith', 'Trained Weapon': 'Hammer (as club)', 'Trade Goods': 'Mithril, 1 oz.'}, 
        '21': {'Occupation': 'Dwarven chest-maker', 'Trained Weapon': 'Chisel (as dagger)', 'Trade Goods': 'Wood, 10 lbs.'}, 
        '22': {'Occupation': 'Dwarven herder', 'Trained Weapon': 'Staff', 'Trade Goods': 'Sow**'}, 
        '23': {'Occupation': 'Dwarven miner', 'Trained Weapon': 'Pick (as club)', 'Trade Goods': 'Lantern'}, 
        '24': {'Occupation': 'Dwarven miner', 'Trained Weapon': 'Pick (as club)', 'Trade Goods': 'Lantern'}, 
        '25': {'Occupation': 'Dwarven mushroom-farmer', 'Trained Weapon': 'Shovel (as staff)', 'Trade Goods': 'Sack'}, 
        '26': {'Occupation': 'Dwarven rat-catcher', 'Trained Weapon': 'Club', 'Trade Goods': 'Net'}, 
        '27': {'Occupation': 'Dwarven stonemason', 'Trained Weapon': 'Hammer', 'Trade Goods': 'Fine stone, 10 lbs.'}, 
        '28': {'Occupation': 'Dwarven stonemason', 'Trained Weapon': 'Hammer', 'Trade Goods': 'Fine stone, 10 lbs.'}, 
        '29': {'Occupation': 'Elven artisan', 'Trained Weapon': 'Staff', 'Trade Goods': 'Clay, 1 lb.'}, 
        '30': {'Occupation': 'Elven barrister', 'Trained Weapon': 'Quill (as dart)', 'Trade Goods': 'Book'}, 
        '31': {'Occupation': 'Elven chandler', 'Trained Weapon': 'Scissors (as dagger)', 'Trade Goods': 'Candles, 20'}, 
        '32': {'Occupation': 'Elven falconer', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Falcon'}, 
        '33': {'Occupation': 'Elven forester', 'Trained Weapon': 'Staff', 'Trade Goods': 'Herbs, 1 lb.'}, 
        '34': {'Occupation': 'Elven forester', 'Trained Weapon': 'Staff', 'Trade Goods': 'Herbs, 1 lb.'}, 
        '35': {'Occupation': 'Elven glassblower', 'Trained Weapon': 'Hammer (as club)', 'Trade Goods': 'Glass beads'}, 
        '36': {'Occupation': 'Elven navigator', 'Trained Weapon': 'Shortbow', 'Trade Goods': 'Spyglass'}, 
        '37': {'Occupation': 'Elven sage', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Parchment and quill pen'}, 
        '38': {'Occupation': 'Elven sage', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Parchment and quill pen'}, 
        '39': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '40': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '41': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '42': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '43': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '44': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '45': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '46': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '47': {'Occupation': 'Farmer*', 'Trained Weapon': 'Pitchfork (as spear)', 'Trade Goods': 'Hen**'}, 
        '48': {'Occupation': 'Fortune-teller', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Tarot deck'}, 
        '49': {'Occupation': 'Gambler', 'Trained Weapon': 'Club', 'Trade Goods': 'Dice'}, 
        '50': {'Occupation': 'Gongfarmer', 'Trained Weapon': 'Trowel (as dagger)', 'Trade Goods': 'Sack of night soil'}, 
        '51': {'Occupation': 'Grave digger', 'Trained Weapon': 'Shovel (as staff)', 'Trade Goods': 'Trowel'}, 
        '52': {'Occupation': 'Grave digger', 'Trained Weapon': 'Shovel (as staff)', 'Trade Goods': 'Trowel'}, 
        '53': {'Occupation': 'Guild beggar', 'Trained Weapon': 'Sling', 'Trade Goods': 'Crutches'}, 
        '54': {'Occupation': 'Guild beggar', 'Trained Weapon': 'Sling', 'Trade Goods': 'Crutches'}, 
        '55': {'Occupation': 'Halfling chicken butcher', 'Trained Weapon': 'Hand axe', 'Trade Goods': 'Chicken meat, 5 lbs.'}, 
        '56': {'Occupation': 'Halfling dyer', 'Trained Weapon': 'Staff', 'Trade Goods': 'Fabric, 3 yards'}, 
        '57': {'Occupation': 'Halfling dyer', 'Trained Weapon': 'Staff', 'Trade Goods': 'Fabric, 3 yards'}, 
        '58': {'Occupation': 'Halfling glovemaker', 'Trained Weapon': 'Awl (as dagger)', 'Trade Goods': 'Gloves, 4 pairs'}, 
        '59': {'Occupation': 'Halfling gypsy', 'Trained Weapon': 'Sling', 'Trade Goods': 'Hex doll'}, 
        '60': {'Occupation': 'Halfling haberdasher', 'Trained Weapon': 'Scissors (as dagger)', 'Trade Goods': 'Fine suits, 3 sets'}, 
        '61': {'Occupation': 'Halfling mariner', 'Trained Weapon': 'Knife (as dagger)', 'Trade Goods': 'Sailcloth, 2 yards'}, 
        '62': {'Occupation': 'Halfling moneylender', 'Trained Weapon': 'Short sword', 'Trade Goods': '5 gp, 10 sp, 200 cp'}, 
        '63': {'Occupation': 'Halfling trader', 'Trained Weapon': 'Short sword', 'Trade Goods': '20 sp'}, 
        '64': {'Occupation': 'Halfling vagrant', 'Trained Weapon': 'Club', 'Trade Goods': 'Holy water, 1 vial'}, 
        '65': {'Occupation': 'Healer', 'Trained Weapon': 'Club', 'Trade Goods': 'Holy water, 1 vial'}, 
        '66': {'Occupation': 'Herbalist', 'Trained Weapon': 'Club', 'Trade Goods': 'Herbs, 1 lb.'}, 
        '67': {'Occupation': 'Herder', 'Trained Weapon': 'Staff', 'Trade Goods': 'Herding dog**'}, 
        '68': {'Occupation': 'Hunter', 'Trained Weapon': 'Shortbow', 'Trade Goods': 'Deer pelt'}, 
        '69': {'Occupation': 'Hunter', 'Trained Weapon': 'Shortbow', 'Trade Goods': 'Deer pelt'}, 
        '70': {'Occupation': 'Indentured servant', 'Trained Weapon': 'Staff', 'Trade Goods': 'Locket'}, 
        '71': {'Occupation': 'Jester', 'Trained Weapon': 'Dart', 'Trade Goods': 'Silk clothes'}, 
        '72': {'Occupation': 'Jeweler', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Gem worth 20 gp'}, 
        '73': {'Occupation': 'Locksmith', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Fine tools'}, 
        '74': {'Occupation': 'Mendicant', 'Trained Weapon': 'Club', 'Trade Goods': 'Cheese dip'}, 
        '75': {'Occupation': 'Mercenary', 'Trained Weapon': 'Longsword', 'Trade Goods': 'Hide armor'}, 
        '76': {'Occupation': 'Merchant', 'Trained Weapon': 'Dagger', 'Trade Goods': '4 gp'}, 
        '77': {'Occupation': 'Miller/baker', 'Trained Weapon': 'Club', 'Trade Goods': 'Flour'}, 
        '78': {'Occupation': 'Minstrel', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Ukulele'}, 
        '79': {'Occupation': 'Noble', 'Trained Weapon': 'Longsword', 'Trade Goods': 'Gold ring worth 10 gp'}, 
        '80': {'Occupation': 'Orphan', 'Trained Weapon': 'Club', 'Trade Goods': 'Rag doll'}, 
        '81': {'Occupation': 'Ostler', 'Trained Weapon': 'Staff', 'Trade Goods': 'Bridle'}, 
        '82': {'Occupation': 'Outlaw', 'Trained Weapon': 'Short sword', 'Trade Goods': 'Leather armor'}, 
        '83': {'Occupation': 'Rope maker', 'Trained Weapon': 'Knife (as dagger)', 'Trade Goods': 'Rope'}, 
        '84': {'Occupation': 'Scribe', 'Trained Weapon': 'Dart', 'Trade Goods': 'Parchment'}, 
        '85': {'Occupation': 'Shaman', 'Trained Weapon': 'Feathered bone club', 'Trade Goods': 'Com badge'}, 
        '86': {'Occupation': 'Slave', 'Trained Weapon': 'Club', 'Trade Goods': 'Strange-looking rock'}, 
        '87': {'Occupation': 'Smuggler', 'Trained Weapon': 'Sling', 'Trade Goods': 'Waterproof sack'}, 
        '88': {'Occupation': 'Soldier', 'Trained Weapon': 'Spear', 'Trade Goods': 'Shield'}, 
        '89': {'Occupation': 'Squire', 'Trained Weapon': 'Longsword', 'Trade Goods': 'Steel helmet'}, 
        '90': {'Occupation': 'Squire', 'Trained Weapon': 'Longsword', 'Trade Goods': 'Steel helmet'}, 
        '91': {'Occupation': 'Tax collector', 'Trained Weapon': 'Longsword', 'Trade Goods': '100 cp'}, 
        '92': {'Occupation': 'Trapper', 'Trained Weapon': 'Sling', 'Trade Goods': 'Badger pelt'}, 
        '93': {'Occupation': 'Trapper', 'Trained Weapon': 'Sling', 'Trade Goods': 'Badger pelt'}, 
        '94': {'Occupation': 'Urchin', 'Trained Weapon': 'Stick (as club)', 'Trade Goods': 'Begging bowl'}, 
        '95': {'Occupation': 'Wainwright', 'Trained Weapon': 'Club', 'Trade Goods': 'Pushcart***'}, 
        '96': {'Occupation': 'Weaver', 'Trained Weapon': 'Dagger', 'Trade Goods': 'Fine suit of clothes'}, 
        '97': {'Occupation': "Wizard's apprentice", 'Trained Weapon': 'Dagger', 'Trade Goods': 'Black grimoire'}, 
        '98': {'Occupation': 'Woodcutter', 'Trained Weapon': 'Handaxe', 'Trade Goods': 'Bundle of wood'},
        '99': {'Occupation': 'Woodcutter', 'Trained Weapon': 'Handaxe', 'Trade Goods': 'Bundle of wood'},
        '100': {'Occupation': 'Woodcutter', 'Trained Weapon': 'Handaxe', 'Trade Goods': 'Bundle of wood'}
    }

# Equipment table
equipment = [
    ['1', 'Backpack', '2 gp'],
    ['2', 'Candle', '1 cp'],
    ['3', 'Chain, 10ft', '30 gp'],
    ['4', 'Chalk, 1 piece', '1 cp'],
    ['5', 'Chest, empty', '2 gp'],
    ['6', 'Crowbar', '2 gp'],
    ['7', 'Flask, empty', '3 cp'],
    ['8', 'Flint & steel', '15 cp'],
    ['9', 'Grappling hook', '1 gp'],
    ['10', 'Hammer, small', '5 sp'],
    ['11', 'Holy symbol', '25 gp'],
    ['12', 'Holy water, 1 vial**', '25 gp'],
    ['13', 'Iron spikes, each', '1 sp'],
    ['14', 'Lantern', '10 gp'],
    ['15', 'Mirror, hand-sized', '10 gp'],
    ['16', 'Oil, 1 flask***', '2 sp'],
    ['17', 'Pole, 10-foot', '15 cp'],
    ['18', 'Rations, per day', '5 cp'],
    ['19', 'Rope, 50ft', '25 cp'],
    ['20', 'Sack, large', '12 cp'],
    ['21', 'Sack, small', '8 cp'],
    ['22', 'Thieves tools', '25 gp'],
    ['23', 'Torch, each', '1 cp'],
    ['24', 'Waterskin', '5 sp']
]

# FUNCTIONS
def get_mod(score):
    # Determine modifier for each stat and assign it
            if score == 3:
                return -3
            elif score == 4 or score == 5:
                return -2
            elif score >= 6 and score <= 8:
                return -1
            elif score >= 9 and score <= 12:
                return 0
            elif score >= 13 and score <= 15:
                return 1
            elif score == 16 or score == 17:
                return 2
            elif score == 18:
                return 3

def create_character(number_of_characters):
    i = 0
    while i < number_of_characters:

        i += 1

        print(f'--------------Character {i}--------------\n')

        # 1 Determine ability scores; 3d6 in order for each. Note ability modifiers on Table 1-1. The abilities are: Strength, Agility, Stamina, Intelligence, Personality, Luck.
        stat_block = {
            'strength': {
                'score': 0,
                'modifier': 0
            },
            'agility': {
                'score': 0,
                'modifier': 0
            },
            'stamina': {
                'score': 0,
                'modifier': 0
            },
            'personality': {
                'score': 0,
                'modifier': 0
            },
            'intelligence': {
                'score': 0,
                'modifier': 0
            },
            'luck': {
                'score': 0,
                'modifier': 0,
                'sign': ''
            },
        }
        
        print('*** STATS ***')

        # Loop through each stat
        for stat in stat_block:
            # Assign random value (3d6) to the score
            stat_block[stat]['score'] = randint(3, 18)

            stat_block[stat]['modifier'] = get_mod(stat_block[stat]['score'])

            # Print results
            print(f'{stat.title()}: {stat_block[stat]["score"]} ({stat_block[stat]["modifier"]})')

        print('\n*** AC, HIT POINTS AND INITIATIVE ***')

        # 2 Determine hit points; roll 1d4, adjusted by Stamina modifier.
        ac = 10 + stat_block['agility']['modifier']
        print(f'AC: {ac}')

        hit_points = 0
        while hit_points <= 0:    
            hit_points = randint(1, 4) + stat_block['stamina']['modifier']
        print(f'Hit points: {hit_points}')

        print(f'Initiative: {stat_block["agility"]["modifier"]}')

        # TODO 3 Determine Lucky Sign; roll 1d30, adjusted by Luck modifier on Table 1-2. The resultant Lucky Roll modifier associated with that Lucky Sign is permanent and does not change later when Luck is spent.
        print('\n*** LUCKY SIGN ***')

        # Generate 1d30+luck mod roll
        lucky_sign_d30 = randint(1, 30)
        lucky_sign_roll = lucky_sign_d30 + stat_block['luck']['modifier']
        print(f"Lucky sign roll: {lucky_sign_roll} ({lucky_sign_d30} + {stat_block['luck']['modifier']})")
        
        # Alter roll if less than 0 or greater than 30 to avoid index error
        if lucky_sign_roll <= 0:
            lucky_sign_roll = 1
        elif lucky_sign_roll >= 31:
            lucky_sign_roll = 30 

        # Assign roll to sign attribute
        stat_block['luck']['sign'] = lucky_sign_roll

        # Use lucky sign roll as index to query table
        random_lucky_sign = list(lucky_signs.items())
        lucky_sign_output = str(random_lucky_sign[lucky_sign_roll-1]).replace("(", "").replace(")", "").replace("'", "")
        print(f'Lucky Sign: {lucky_sign_output}')


        print('\n*** OCCUPATION ***')

        # 4 Determine 0-level occupation; roll 1d100 on Table 1-3. This result will tell include the character’s 0-level starting weapon and trade goods.
        random_occupation = choice(list(occupations.keys()))
        occupation_output = str(occupations[random_occupation]).replace("{", "").replace("}", "").replace("'", "")
        print(f'{occupation_output}')

        # 5 Choose an alignment.
        alignments = ['Law', 'Neutral', 'Chaos']
        print(f'Alignment: {choice(alignments)}')

        # TODO 6 Determine starting money; roll 5d12 copper pieces. Roll for a random gear item.
        starting_money = randint(5, 60)
        print(f'Starting money: {starting_money} copper pieces')

        starting_gear = choice(equipment)
        print(f'Starting equipment: {starting_gear[1]}')

        print('')

no_of_chars = input('How many characters do you want to generate? ')

create_character(int(no_of_chars))

input('Press enter to exit...')