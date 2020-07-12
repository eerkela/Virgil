import json
import os
import random
import sys
import statistics


def pick_random(list, size=1):
    if (size > len(list)):
        size = len(list)
    sample = random.sample(list, size)
    if len(sample) == 1:
        return sample[0]
    return sample

def add_alias(id, name, value):
    path = os.path.join('Aliases', id + '.json')
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write('{}')
    with open(path, 'r') as f:
        j = json.load(f)
    j[name.title()] = value.title()
    with open(path, 'w') as f:
        json.dump(j, f)

def get_aliases(id):
    path = os.path.join('Aliases', id + '.json')
    with open(path) as f:
        j = json.load(f)
    return j

def remove_alias(id, name):
    path = os.path.join('Aliases', id + '.json')
    with open(path, 'r') as f:
        j = json.load(f)
    if (name in j.keys()):
        value = j.pop(name)
        with open(path, 'w') as f:
            json.dump(j, f)
        return value
    raise Exception('Alias not found: ' + str(name))

def source_map():
    generators = {
        'Historical' : {
            'Cornish' : lambda s, lim: HistoricalGenerator(s, lim),
            'Irish' : lambda s, lim: HistoricalGenerator(s, lim),
            'Welsh' : lambda s, lim: HistoricalGenerator(s, lim),
            'Armenian' : lambda s, lim: HistoricalGenerator(s, lim),
            'Dutch' : lambda s, lim: HistoricalGenerator(s, lim),
            'Finnish' : lambda s, lim: HistoricalGenerator(s, lim),
            'French' : lambda s, lim: HistoricalGenerator(s, lim),
            'German' : lambda s, lim: HistoricalGenerator(s, lim),
            'Norwegian' : lambda s, lim: HistoricalGenerator(s, lim),
            'Portuguese' : lambda s, lim: HistoricalGenerator(s, lim),
            'Spanish' : lambda s, lim: HistoricalGenerator(s, lim),
            'Italian' : lambda s, lim: HistoricalGenerator(s, lim),
            'Irish_Medieval' : lambda s, lim: PersonalGenerator(s, lim),
            'Gaelic' : lambda s, lim: PersonalGenerator(s, lim),
            'Welsh_Medieval' : lambda s, lim: PersonalGenerator(s, lim),
            'Aztec' : lambda s, lim: PersonalGenerator(s, lim),
            'Sanskrit' : lambda s, lim: PersonalGenerator(s, lim),
            'German_Medieval' : lambda s, lim: PersonalGenerator(s, lim),
            'Norse' : lambda s, lim: PersonalGenerator(s, lim),
            'Russian_Medieval' : lambda s, lim: PersonalGenerator(s, lim),
            'Greek_Hellenic' : lambda s, lim: PersonalGenerator(s, lim),
            'Italian_Medieval' : lambda s, lim: PersonalGenerator(s, lim),
            'Hebrew' : lambda s, lim: PersonalGenerator(s, lim),
            'Brittanic_Old_Welsh' : lambda s, lim: BinaryGenerator(s, lim),
            'Incan' : lambda s, lim: BinaryGenerator(s, lim),
            'Dutch_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Finnish_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Hungarian_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Norwegian_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Polish_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Portuguese_Medieval' : lambda s, lim: BinaryGenerator(s, lim),
            'Anglo-Saxon' : lambda s, lim: AngloSaxonGenerator(s, lim),
            'English' : lambda s, lim: EnglishGenerator(s, lim),
            'English_Aristocratic' : lambda s, lim: AltEnglishGenerator(s, lim),
            'English_Rustic' : lambda s, lim: AltEnglishGenerator(s, lim),
            'English_Medieval' : lambda s, lim: MedievalEnglishGenerator(s, lim),
            'Scottish' : lambda s, lim: ScottishGenerator(s, lim),
            'Scottish_Medieval' : lambda s, lim: MedievalScottishGenerator(s, lim),
            'African_Tribal' : lambda s, lim: AfricanTribalGenerator(s, lim),
            'North_African_Berber' : lambda s, lim: NorthAfricanBerberGenerator(s, lim),
            'Egyptian_Ancient' : lambda s, lim: AncientEgyptianGenerator(s, lim),
            'Amerindian_Tribal' : lambda s, lim: AmerindianTribalGenerator(s, lim),
            'Mayan' : lambda s, lim: MayanGenerator(s, lim),
            'Chinese' : lambda s, lim: ChineseGenerator(s, lim),
            'Indian' : lambda s, lim: IndianGenerator(s, lim),
            'Japanese' : lambda s, lim: JapaneseGenerator(s, lim),
            'Japanese_Medieval' : lambda s, lim: MedievalJapaneseGenerator(s, lim),
            'Korean' : lambda s, lim: KoreanGenerator(s, lim),
            'Mongol' : lambda s, lim: MongolGenerator(s, lim),
            'Tibetan' : lambda s, lim: TibetanGenerator(s, lim),
            'French_Medieval' : lambda s, lim: MedievalFrenchGenerator(s, lim),
            'Celtic_Gaulish' : lambda s, lim: CelticGaulishGenerator(s, lim),
            'Germanic' : lambda s, lim: GermanicGenerator(s, lim),
            'Gypsy' : lambda s, lim: GypsyGenerator(s, lim),
            'Hungarian' : lambda s, lim: HungarianGenerator(s, lim),
            'Polish' : lambda s, lim: PolishGenerator(s, lim),
            'Russian' : lambda s, lim: RussianGenerator(s, lim),
            'Spanish_Medieval' : lambda s, lim: MedievalSpanishGenerator(s, lim),
            'Arabic' : lambda s, lim: ArabicGenerator(s, lim),
            'Greek' : lambda s, lim: GreekGenerator(s, lim),
            'Roman' : lambda s, lim: RomanGenerator(s, lim),
            'Jewish' : lambda s, lim: JewishGenerator(s, lim),
            'Phoenician' : lambda s, lim: PhoenicianGenerator(s, lim),
            'Aboriginal' : lambda s, lim: AboriginalGenerator(s, lim),
            'Papuan' : lambda s, lim: PapuanGenerator(s, lim),
            'Polynesian' : lambda s, lim: PolynesianGenerator(s, lim)
        },
        'Fantasy' : {
            'Generic_Fantasy' : lambda s, lim: FantasyGenerator(s, lim),
            'Goblin' : lambda s, lim: CrudeGenerator('goblin', lim),
            'Orc' : lambda s, lim: CrudeGenerator('orc', lim),
            'Ogre' : lambda s, lim: CrudeGenerator('ogre', lim),
            'Elf_High' : lambda s, lim: ElfGenerator('high elf', lim),
            'Elf_Wood' : lambda s, lim: ElfGenerator('wood elf', lim),
            'Drow' : lambda s, lim: ElfGenerator('drow', lim),
            'Dwarf' : lambda s, lim: DoughtyGenerator('dwarf', lim),
            'Halfling' : lambda s, lim: DoughtyGenerator('halfling', lim),
            'Gnome' : lambda s, lim: DoughtyGenerator('gnome', lim),
            'Fey_Seelie' : lambda s, lim: FeyGenerator('seelie', lim),
            'Fey_Unseelie' : lambda s, lim: FeyGenerator('unseelie', lim),
            'Nymph' : lambda s, lim: NymphGenerator('nymph', lim),
            'Siren' : lambda s, lim: NymphGenerator('siren', lim),
            'Dragon' : lambda s, lim: DragonGenerator('normal', lim),
            'Evil_Dragon' : lambda s, lim: DragonGenerator('evil', lim),
            'Faerie_Dragon' : lambda s, lim: DragonGenerator('faerie', lim),
            'Serpent' : lambda s, lim: SerpentGenerator(lim),
            'Demon_Small' : lambda s, lim: InfernalGenerator('small demon', lim),
            'Demon_Medium' : lambda s, lim: InfernalGenerator('medium demon', lim),
            'Demon_Large' : lambda s, lim: InfernalGenerator('large demon', lim),
            'Devil_Small' : lambda s, lim: InfernalGenerator('small devil', lim),
            'Devil_Medium' : lambda s, lim: InfernalGenerator('medium devil', lim),
            'Devil_Large' : lambda s, lim: InfernalGenerator('large devil', lim),
            'Ooze' : lambda s, lim: InfernalGenerator('ooze', lim),
            'Angel' : lambda s, lim: AngelGenerator(lim),
        },
        'Description' : {
            'Description' : lambda s, lim: SyllabicGenerator(s, lim)
        }
    }
    '''

    'Demon_Small' : ,
    'Demon_Hordling' : ,
    'Demon_Brute' : ,
    'Demon_Lord' : ,
    'Devil_Small' : ,
    'Devil_Hordling' : ,
    'Devil_Brute' : ,
    'Devil_Lord' : ,
    '''
    return generators

def get_generator(source, duplicate_limit=20):
    generators = source_map()
    if source in generators['Historical'].keys():
        return generators['Historical'][source](source, duplicate_limit)
    elif source in generators['Fantasy'].keys():
        return generators['Fantasy'][source](source, duplicate_limit)
    elif source in generators['Description'].keys():
        return generators['Description'][source](source, duplicate_limit)
    else:
        raise Exception('Invalid Source: ' + str(source))
    return False


class Generator:

    def __init__(self, id: str, sources: str, duplicate_limit: int = 20):
        self.id = id
        self.duplicate_limit = duplicate_limit
        self.generators = self.assign_generators(sources)

    def assign_generators(self, sources):
        aliases = get_aliases(self.id)
        expanded = []
        for source in sources.split('+'):
            if (source.title() in aliases.keys()):
                expanded.extend(aliases[source.title()].split('+'))
            else:
                expanded.append(source)
        generators = {}
        for source in expanded:
            lim = self.duplicate_limit
            generators[source] = get_generator(source, lim)
        return generators

    def generate(self, gender, amount=10, *args):
        names = []
        for g in self.generators.values():
            names += g.generate(gender, amount, *args)
        return pick_random(names, amount)

    def get_description(self):
        descriptions = {}
        for (k, v) in self.generators.items():
            descriptions[k] = v.get_description()
        return descriptions

    def get_pronunciation(self):
        pronunciation_guides = {}
        for (k, v) in self.generators.items():
            pronunciation_guides[k] = v.get_pronunciation()
        return pronunciation_guides

    def print_structure(self):
        for g in self.generators.values():
            g.print_structure()
            print()

    def valid_args(self):
        options = {}
        for g in self.generators.values():
            options = {**options, **g.valid_args()}
        return options


class HistoricalGenerator:

    def __init__(self, source: str, duplicate_limit: int = 20):
        valid_sources = source_map()['Historical'].keys()
        if source not in valid_sources:
            raise Exception('invalid source: ' + str(source))
        self.source = source
        self.duplicate_limit = duplicate_limit
        list_path = os.path.join('Names', 'Historical', source + '.json')
        with open(list_path) as f:
            self.list = json.load(f)

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

    def get_description(self):
        return self.list['Description']

    def get_pronunciation(self):
        return self.list['Pronunciation']

    def print_structure(self):
        print('%s = {' % self.source)
        self.print_structure_helper(self.list, '\t')
        print('}')
        return True

    def print_structure_helper(self, my_dict, indentation):
        if isinstance(my_dict, dict):
            for k in my_dict.keys():
                print(indentation + '\'%s\'' % k)
                self.print_structure_helper(my_dict[k], indentation + '\t')
        return True

class PersonalGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))
        names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                names = self.list['Male']['Common']
            else:
                names = self.list['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                names = self.list['Female']['Common']
            else:
                names = self.list['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class BinaryGenerator(HistoricalGenerator):

    def valid_args(self):
        return {}

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))
        names = []
        if (gender.lower() == 'male'):
            names = self.list['Male']
        elif (gender.lower() == 'female'):
            names = self.list['Female']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class AngloSaxonGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'most common name elements only',
            'single-element' : 'single-element names only',
            'two-element' : 'two-element names only'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather single-element names:
        single_element = self.list['Single-element']
        if ('single-element' in args):
            return pick_random(single_element, amount)

        # Gather two-element names:
        first_element = []
        second_element = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                first_element = self.list['Two-element']['Male']['First']['Common']
                second_element = self.list['Two-element']['Male']['Second']['Common']
            else:
                first_element = self.list['Two-element']['Male']['First']['Standard']
                second_element = self.list['Two-element']['Male']['Second']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                first_element = self.list['Two-element']['Female']['First']['Common']
                second_element = self.list['Two-element']['Female']['Second']['Common']
            else:
                first_element = self.list['Two-element']['Female']['First']['Standard']
                second_element = self.list['Two-element']['Female']['Second']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            r = random.random()
            if (r > 0.9 or 'two-element' in args):   #name is two-element
                name = pick_random(first_element) \
                     + pick_random(second_element)
            else:
                name = pick_random(single_element)

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class EnglishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'standard' : 'only choose names from "Standard" list',
            'other' : 'only choose names from "Other" list',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            elif ('other' in args):
                personal_names = self.list['Personal']['Male']['Other']
            elif ('standard' in args):
                personal_names = self.list['Personal']['Male']['Standard']
            else:
                personal_names = self.list['Personal']['Male']['Standard'] \
                               + self.list['Personal']['Male']['Other']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            elif ('other' in args):
                personal_names = self.list['Personal']['Female']['Other']
            elif ('standard' in args):
                personal_names = self.list['Personal']['Female']['Standard']
            else:
                personal_names = self.list['Personal']['Female']['Standard'] \
                               + self.list['Personal']['Female']['Other']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class AltEnglishGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = self.list['Family']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class MedievalEnglishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'standard' : 'only choose names from "Standard" list',
            'other' : 'only choose names from "Other" list'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))
        names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                names = self.list['Male']['Common']
            elif ('standard' in args):
                names = self.list['Male']['Standard']
            elif ('other' in args):
                names = self.list['Male']['Other']
            else:
                names = self.list['Male']['Standard'] \
                      + self.list['Male']['Other']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                names = self.list['Female']['Common']
            elif ('standard' in args):
                names = self.list['Female']['Standard']
            elif ('other' in args):
                names = self.list['Female']['Other']
            else:
                names = self.list['Female']['Standard'] \
                      + self.list['Female']['Other']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class ScottishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'highland' : 'limit names to those found in highlands region',
            'lowland' : 'limit names to those found in lowlands region'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        elif ('highland' in args):
            family_names = self.list['Family']['Highland']
        elif ('lowland' in args):
            family_names = self.list['Family']['Lowland']
        else:
            family_names = self.list['Family']['Standard'] \
                         + self.list['Family']['Highland'] \
                         + self.list['Family']['Lowland']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class MedievalScottishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'highland' : 'limit names to those found in highland region',
            'lowland' : 'limit names to those found in lowland region'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))
        names = []
        if (gender.lower() == 'male'):
            if ('highland' in args):
                if ('common' in args):
                    names = self.list['Male']['Highland']['Common']
                else:
                    names = self.list['Male']['Highland']['Standard']
            elif ('lowland' in args):
                if ('common' in args):
                    names = self.list['Male']['Lowland']['Common']
                else:
                    names = self.list['Male']['Lowland']['Standard']
            elif ('common' in args):
                names = self.list['Male']['Highland']['Common'] \
                      + self.list['Male']['Lowland']['Common']
            else:
                names = self.list['Male']['Highland']['Standard'] \
                      + self.list['Male']['Lowland']['Standard']
        elif (gender.lower() == 'female'):
            if ('highland' in args):
                if ('common' in args):
                    names = self.list['Female']['Highland']['Common']
                else:
                    names = self.list['Female']['Highland']['Standard']
            elif ('lowland' in args):
                if ('common' in args):
                    names = self.list['Female']['Lowland']['Common']
                else:
                    names = self.list['Female']['Lowland']['Standard']
            elif ('common' in args):
                names = self.list['Female']['Highland']['Common'] \
                      + self.list['Female']['Lowland']['Common']
            else:
                names = self.list['Female']['Highland']['Standard'] \
                      + self.list['Female']['Lowland']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class AfricanTribalGenerator(HistoricalGenerator):

    def valid_tribes(self):
        tribes = ['benin', 'efe', 'ewe', 'fante', 'ibo',  'kikuyu', 'kisii', \
                  'luo', 'ngoni', 'nyakyusa', 'sesotho', 'shona', 'swahili', \
                  'tswana', 'xhosa', 'yao', 'yoruba', 'zulu', 'other']
        return tribes

    def valid_args(self):
        valid_args = {
            'family' : 'family names only (no first names)',
            'tribe' : 'generate tribe names (no personal names)',
            'east' : '(for use with "tribe" option only) - generate east \
                      african tribe names',
            'west' : '(for use with "tribe" option only) - generate west \
                      african tribe names',
            'south' : '(for use with "tribe" option only) - generate south \
                       african tribe names',
        }
        for t in self.valid_tribes():
            valid_args[t] = 'limit names to %s tribe' % t.title()
        return valid_args

    def generate(self, gender, amount=10, *args):
        tribes = self.valid_tribes()
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('benin' in args):
            family_names = self.list['Family']['Benin']
        elif ('Kikuyu' in args):
            family_names = self.list['Family']['Kikuyu']
        else:
            for k, v in self.list['Family'].items():
                family_names += v
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather tribe names
        tribe_names = []
        if ('east' in args):
            tribe_names = self.list['Tribe']['East Africa']
        elif ('south' in args):
            tribe_names = self.list['Tribe']['South Africa']
        elif ('west' in args):
            tribe_names = self.list['Tribe']['West Africa']
        else:
            for k, v in self.list['Tribe'].items():
                tribe_names += v
        if ('tribe' in args):
            return pick_random(tribe_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if (any([a in tribes for a in args])):
                for a in args:
                    if a in tribes:
                        personal_names += self.list['Personal']['Male'][a.title()]
            else:
                for k, v in self.list['Personal']['Male'].items():
                    personal_names += v
        elif (gender.lower() == 'female'):
            if (any([a in tribes for a in args])):
                for a in args:
                    if a in tribes:
                        personal_names += self.list['Personal']['Female'][a.title()]
            else:
                for k, v in self.list['Personal']['Female'].items():
                    personal_names += v
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(personal_names, amount)

class NorthAfricanBerberGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'tuareg' : 'limit names to Tuareg origin',
            'other' : 'limit names to non-Tuareg origin',
            'romanized' : 'roman transliterations of Berber names',
            'ruler' : '(for use with "romanized" option) - only generate \
                       names of recognized Berber rulers'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather Romanized names
        if ('romanized' in args):
            if ('ruler' in args):
                romanized_names = self.list['Romanized']['Rulers']
            elif ('other' in args):
                romanized_names = self.list['Romanized']['Other']
            else:
                romanized_names = self.list['Romanized']['Rulers'] \
                                + self.list['Romanized']['Other']
            return pick_random(romanized_names, amount)

        # Gather native Berber names
        names = []
        if (gender.lower() == 'male'):
            if ('tuareg' in args):
                names = self.list['Male']['Tuareg']
            elif ('other' in args):
                names = self.list['Male']['Other']
            else:
                names = self.list['Male']['Tuareg'] \
                      + self.list['Male']['Other']
        elif (gender.lower() == 'female'):
            if ('tuareg' in args):
                names = self.list['Female']['Tuareg']
            elif ('other' in args):
                names = self.list['Female']['Other']
            else:
                names = self.list['Female']['Tuareg'] \
                      + self.list['Female']['Other']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class AncientEgyptianGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'stand-alone' : 'only generate stand-alone names',
            'theophoric' : 'only generate theophoric names',
            'simple' : 'only use simple theophoric elements (does not affect \
                        stand-alone names)',
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather stand-alone names
        standalone_names = []
        theo_prefixes = []
        theo_deities = []
        theo_suffixes = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                standalone_names = self.list['Stand-alone']['Male']['Common']
                theo_prefixes = self.list['Theophoric']['Prefix']['Common']
                theo_deities = self.list['Theophoric']['Deity']['Common']
                theo_suffixes = self.list['Theophoric']['Suffix']['Common']
            elif ('simple' in args):
                standalone_names = self.list['Stand-alone']['Male']['Standard']
                theo_prefixes = self.list['Theophoric']['Prefix']['Simple']
                theo_deities = self.list['Theophoric']['Deity']['God'] \
                             + self.list['Theophoric']['Deity']['Goddess']
                theo_suffixes = self.list['Theophoric']['Suffix']['Simple']
            else:
                standalone_names = self.list['Stand-alone']['Male']['Standard']
                theo_prefixes = self.list['Theophoric']['Prefix']['Simple'] \
                              + self.list['Theophoric']['Prefix']['Compound']
                theo_deities = self.list['Theophoric']['Deity']['God'] \
                             + self.list['Theophoric']['Deity']['Goddess']
                theo_suffixes = self.list['Theophoric']['Suffix']['Simple'] \
                              + self.list['Theophoric']['Suffix']['Compound']
            theo_prefixes.remove('Sit-')
            theo_suffixes.remove('-irdis')
            theo_suffixes.remove('-nefert')
            theo_suffixes.remove('-nodjmet')
            theo_suffixes.remove('-nofret')
        elif (gender.lower() == 'female'):
            if ('common' in args):
                standalone_names = self.list['Stand-alone']['Female']['Common']
                theo_prefixes = self.list['Theophoric']['Prefix']['Common']
                theo_deities = self.list['Theophoric']['Deity']['Common']
                theo_suffixes = self.list['Theophoric']['Suffix']['Common']
            elif ('simple' in args):
                standalone_names = self.list['Stand-alone']['Female']['Standard']
                theo_prefixes = self.list['Theophoric']['Prefix']['Simple']
                theo_deities = self.list['Theophoric']['Deity']['God'] \
                             + self.list['Theophoric']['Deity']['Goddess']
                theo_suffixes = self.list['Theophoric']['Suffix']['Simple']
            else:
                standalone_names = self.list['Stand-alone']['Female']['Standard']
                theo_prefixes = self.list['Theophoric']['Prefix']['Simple'] \
                              + self.list['Theophoric']['Prefix']['Compound']
                theo_deities = self.list['Theophoric']['Deity']['God'] \
                             + self.list['Theophoric']['Deity']['Goddess']
                theo_suffixes = self.list['Theophoric']['Suffix']['Simple'] \
                              + self.list['Theophoric']['Suffix']['Compound']
            theo_prefixes.remove('Si-')
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('stand-alone' in args):
            return pick_random(standalone_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            r1 = random.randrange(1, 2)
            if (r1 == 1 or 'theophoric' in args):  #name is theophoric
                r2 = random.randrange(1, 4)
                if (r2 == 1):   #name is of form: deity + suffix
                    r3 = random.randrange(1, 30)
                    if (r3 == 1):   #1 in 30 to have 2 dieities
                        option_1 = pick_random(theo_deities) \
                                 + '-' + pick_random(theo_deities) \
                                 + pick_random(theo_suffixes)
                        option_2 = pick_random(theo_deities) \
                                 + pick_random(theo_suffixes) \
                                 + '-' + pick_random(theo_deities)
                        name = pick_random([option_1, option_2])
                    else:   #name has only 1 deity
                        name = pick_random(theo_deities) \
                             + pick_random(theo_suffixes)
                else:   #name is of form: prefix + deity
                    r3 = random.randrange(1, 30)
                    if (r3 == 1):   #1 in 30 to have 2 dieities
                        option_1 = pick_random(theo_prefixes) \
                                 + pick_random(theo_deities) \
                                 + '-' + pick_random(theo_deities)
                        option_2 = pick_random(theo_deities) \
                                 + '-' + pick_random(theo_prefixes) \
                                 + pick_random(theo_deities)
                        name = pick_random([option_1, option_2])
                    else:   #name has only 1 deity
                        name = pick_random(theo_prefixes) \
                             + pick_random(theo_deities)
            else:   #name is stand-alone
                r2 = random.randrange(1, 20)
                if (r2 == 1):   #name is part theophoric
                    std = pick_random(standalone_names)
                    theo1 = self.generate('male', 1, 'theophoric', 'simple')[0]
                    r3 = random.randrange(1, 20)
                    if (r3 == 1):   #name is even longer
                        theo2 = self.generate('male', 1, 'theophoric', 'simple')[0]
                        opt1 = ' '.join([std, theo1, theo2])
                        opt2 = ' '.join([std, theo2, theo1])
                        opt3 = ' '.join([theo1, std, theo2])
                        opt4 = ' '.join([theo1, theo2, std])
                        opt5 = ' '.join([theo2, std, theo1])
                        opt6 = ' '.join([theo2, theo1, std])
                        name = pick_random([opt1, opt2, opt3, opt4, opt5, opt6])
                    else:   #name has only 1 theophoric element
                        opt1 = ' '.join([std, theo1])
                        opt2 = ' '.join([theo1, std])
                        name = pick_random([opt1, opt2])
                else:   #name is solely stand-alone
                    name = pick_random(standalone_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class AmerindianTribalGenerator(HistoricalGenerator):

    def valid_tribes(self):
        tribes = ['algonquin', 'apache', 'cherokee', 'chippewa', 'choctaw', \
                  'delaware', 'eskimo', 'iroquois', 'nez perce', 'navaho', \
                  'sioux', 'other']
        return tribes

    def valid_args(self):
        valid_args = {
            'family' : 'family names only (no personal names)',
            'tribe' : 'generate tribe names (no personal names)',
        }
        for t in self.valid_tribes():
            valid_args[t] = 'limit names to %s tribe' % t.title()
        return valid_args

    def generate(self, gender, amount=10, *args):
        tribes = self.valid_tribes()
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        if ('family' in args):
            family_names = self.list['Family']['Eskimo']
            return pick_random(family_names, amount)

        # Gather tribe names
        if ('tribe' in args):
            tribe_names = self.list['Tribe']
            return pick_random(tribe_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if (any([a in tribes for a in args])):
                for a in args:
                    if a in tribes:
                        personal_names = self.list['Personal']['Male'][a.title()]
            else:
                for k, v in self.list['Personal']['Male'].items():
                    personal_names += v
        elif (gender.lower() == 'female'):
            if (any([a in tribes for a in args])):
                for a in args:
                    if a in tribes:
                        personal_names += self.list['Personal']['Female'][a.title()]
            else:
                for k, v in self.list['Personal']['Female'].items():
                    personal_names += v
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(personal_names, amount)

class MayanGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'noprefix' : 'removes gender prefix (Ah-/Ix-) from name'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))
        if (gender.lower() not in ['male', 'female']):
            raise Exception('gender not recognized: ' + str(gender))

        # Gather common names and append appropriate prefix
        if ('common' in args):
            common_names = self.list['Common']
            if ('noprefix' in args):
                return pick_random(common_names, amount)
            names = []
            i = 0
            while (len(names) < amount and i < self.duplicate_limit):
                name = ''
                if (gender.lower() == 'male'):
                    name = 'Ah-' + pick_random(common_names)
                else:
                    name = 'Ix-' + pick_random(common_names)
                if name in names:
                    i += 1
                else:
                    names.append(name)
            return names

        numbers = self.list['Numbers']
        days = self.list['Days']
        months = self.list['Months']
        standard = self.list['Standard']
        if (gender.lower() == 'male'):
            standard.remove('Colel')           # female only
            standard.remove('Ciuatl')
        else:
            standard.remove('Yum')             # male only
            standard.remove('Tecutli')
        all = numbers + days + months + standard

        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            # Append appropriate prefix:
            name = ''
            if ('noprefix' in args):
                pass
            elif (gender.lower() == 'male'):
                name = 'Ah-'
            else:
                name = 'Ix-'

            # Construct name
            r = random.randrange(1, 20)
            if (r <= 3):   #name has 1 element
                name += pick_random(standard)
            elif (r >= 4 and r <= 14):   #name has 2 elements
                first = pick_random(all)
                second = pick_random(all)
                name += '-'.join([first, second])
            elif (r >= 15 and r <= 19):   #name has 3 elements
                first = pick_random(all)
                second = pick_random(all)
                third = pick_random(all)
                name += '-'.join([first, second, third])
            else:   #name has 4 elements
                first = pick_random(all)
                second = pick_random(all)
                third = pick_random(all)
                fourth = pick_random(all)
                name += '-'.join([first, second, third, fourth])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class ChineseGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'standard' : 'choose names from "Standard" list',
            'other' : 'choose names from "Other" list',
            'revolutionary' : 'allows names with elements associated with the \
                              Chinese Communist Revolution'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names:
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        elif ('standard' in args):
            family_names = self.list['Family']['Standard']
        elif ('other' in args):
            family_names = self.list['Family']['Other']
        else:
            family_names = self.list['Family']['Standard'] + self.list['Family']['Other']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names:
        first_element = []
        second_element = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                first_element = self.list['Personal']['Male']['Common']
                second_element = self.list['Personal']['Male']['Second']
            else:
                first_element = self.list['Personal']['Male']['First']
                second_element = self.list['Personal']['Male']['Second']
            if ('revolutionary' not in args):
                # remove elements with revolutionary context
                revolutionary_elements = ['gwo', 'gwun', 'hwa', 'min']
                for element in revolutionary_elements:
                    first_element.remove(element.title())
                    second_element.remove(element)
        elif (gender.lower() == 'female'):
            if ('common' in args):
                first_element = self.list['Personal']['Female']['Common']
                second_element = self.list['Personal']['Female']['Second']
            else:
                first_element = self.list['Personal']['Female']['First']
                second_element = self.list['Personal']['Female']['Second']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            r = random.randrange(1, 20)
            name = ''
            if (r == 20):   #name contains only a single element
                if ('common' in args):
                    if ('personal' in args):
                        name = pick_random(first_element)
                    else:
                        first = pick_random(first_element)
                        family = pick_random(family_names)
                        name = family + ' ' + first
                else:
                    if ('personal' in args):
                        name = pick_random(first_element)
                    else:
                        first = pick_random(first_element)
                        second = pick_random(second_element).title()
                        family = pick_random(family_names)

                        choice = pick_random([first, second])
                        name = family + ' ' + choice
            else:   #name is standard two-element
                if ('personal' in args):
                    first = pick_random(first_element)
                    second = pick_random(second_element)

                    # Remove duplicates
                    while (first.lower() == second):
                        second = pick_random(second_element)
                    name = '-'.join([first, second])
                else:
                    first = pick_random(first_element)
                    second = pick_random(second_element)
                    family = pick_random(family_names)

                    # Remove duplicates
                    while (first.lower() == second):
                        second = pick_random(second_element)
                    name = family + ' ' + '-'.join([first, second])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class IndianGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'theophoric' : 'generate theophoric names only'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Gather theophoric names
        theo_gods = self.list['Theophoric']['Gods']
        theo_second = self.list['Theophoric']['Neutral']
        if (gender.lower() == 'male'):
            theo_second += self.list['Theophoric']['Male']
        elif (gender.lower() == 'female'):
            theo_second += self.list['Theophoric']['Female']

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            r = random.randrange(1, 20)
            if (r == 1 or 'theophoric' in args):   # name is theophoric
                name = pick_random(theo_gods) + ' ' + pick_random(theo_second)
            else:
                name = pick_random(personal_names) + ' ' + pick_random(family_names)

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class JapaneseGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(family_names) \
                 + ' ' \
                 + pick_random(personal_names)
            if (name in names):
                i += 1
            else:
                names.append(name)
        return names

class MedievalJapaneseGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'family' : 'family names only (no first names)',
            'noble' : '(for use with "family" option only) - limit family \
                       names to those historically associated with nobility',
            'warrior' : '(for use with "family" option only) - limit family \
                         names to those historically associated with warrior \
                         clans'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('noble' in args and 'warrior' not in args):
            family_names = self.list['Family']['Noble']
        elif ('warrior' in args and 'noble' not in args):
            family_names = self.list['Family']['Warrior']
        else:
            family_names = self.list['Family']['Noble'] \
                         + self.list['Family']['Warrior']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        first_element = []
        second_element = []
        one_syllable = self.list['Personal']['First']['One Syllable']
        female_first_element = self.list['Personal']['First']['Female']
        if (gender.lower() == 'male'):
            if ('common' in args):
                first_element = self.list['Personal']['First']['Common']
                second_element = self.list['Personal']['Second']['Common']
            else:
                first_element = self.list['Personal']['First']['Standard']
                second_element = self.list['Personal']['Second']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                first_element = female_first_element
                second_element = self.list['Personal']['Second']['Common']
            else:
                first_element = female_first_element \
                              + self.list['Personal']['First']['Standard']
                second_element = self.list['Personal']['Second']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            if (gender.lower() == 'male'):
                first = ''
                second = pick_random(second_element)
                r = random.randrange(1, 100)
                if (r == 100):  #name uses a one-syllable first element
                    first = pick_random(one_syllable)
                elif (r == 99):   #name has an extra syllable in first element
                    first = pick_random(first_element) \
                          + pick_random(one_syllable).lower()
                else:
                    first = pick_random(first_element)
                if (first.lower() == second.lower()):
                    second = ''
                name = first + second
            else:
                first = pick_random(first_element)
                second = pick_random(second_element)
                r1 = random.randrange(1, 6)
                if (r1 == 1):   # name is of form: first + '-ko'
                    second = 'ko'
                else:
                    if (first in female_first_element):
                        r2 = random.randrange(1, 10)
                        if (r2 == 10): # female first element by itself
                            second = ''
                    if (second.endswith('u')):
                        second += 'ko'
                name = first + second

            if ('noble' in args or 'warrior' in args):
                family = pick_random(family_names)
                name = ' '.join([family, name])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class KoreanGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names:
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names:
        first_element = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                first_element = self.list['Personal']['Male']['Common']
                second_element = self.list['Personal']['Male']['Second']
            else:
                first_element = self.list['Personal']['Male']['First']
                second_element = self.list['Personal']['Male']['Second']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                first_element = self.list['Personal']['Female']['Common']
                second_element = self.list['Personal']['Female']['Second']
            else:
                first_element = self.list['Personal']['Female']['First']
                second_element = self.list['Personal']['Female']['Second']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names:
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            family = pick_random(family_names)
            name = ''
            if (gender.lower() == 'male'):
                first = pick_random(first_element)
                second = pick_random(second_element)
                r = random.randrange(1, 20)
                if (r == 1):   # name has only one element
                    second = ''
                if ('personal' in args):
                    name = ' '.join([first, second])
                else:
                    name = ' '.join([family, first, second])
            else:
                first = pick_random(first_element)
                second = ''
                if (random.random() < 0.3):   # name ends with Ae, Hy, Ja, Ok, or Sook
                    second = pick_random(['Ae', 'Hy', 'Ja', 'Ok', 'Sook'])
                else:
                    second = pick_random(second_element)

                r1 = random.randrange(1, 20)
                if (r1 == 1):   # name contains one element
                    r2 = random.randrange(1, 10)
                    if (r2 == 1):   # name contains 3 elements instead of 1
                        opt1 = pick_random(first_element)
                        opt2 = pick_random(second_element)
                        choice = pick_random([opt1, opt2])
                        if ('personal' in args):
                            name = ' '.join([first, second, choice])
                        else:
                            name = ' '.join([family, first, second, choice])
                    else:   # name only contains 1 element (for real this time)
                        if ('personal' in args):
                            name = first
                        else:
                            name = ' '.join([family, first])
                else:   # name is standard 2 element
                    if ('personal' in args):
                        name = ' '.join([first, second])
                    else:
                        name = ' '.join([family, first, second])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class MongolGenerator(HistoricalGenerator):

    #TODO: change 'title' option to append titles to name

    def valid_args(self):
        valid_args = {
            'tribe' : 'generate tribe names only (no personal names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather tribe names
        if ('tribe' in args):
            tribe_names = self.list['Tribe']
            return pick_random(tribe_names, amount)

        # Gather titles
        if ('title' in args):
            titles = self.list['Titles']
            return pick_random(titles, amount)

        # Gather personal names
        names = []
        if (gender.lower() == 'male'):
            names = self.list['Personal']['Male']
        elif (gender.lower() == 'female'):
            names = self.list['Personal']['Female']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class TibetanGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'clan' : 'generate clan names (no personal names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather clan names
        if ('clan' in args):
            clan_names = self.list['Clan']
            return pick_random(clan_names, amount)

        # Gather personal names
        weekdays = self.list['Personal']['Weekdays']
        others = self.list['Personal']['Other']
        if (gender.lower() == 'male'):
            female_only = ['Jangmu', 'Jetsun', 'Lhamo']
            for f in female_only:
                others.remove(f)
        elif (gender.lower() == 'female'):
            male_only = ['Jangbu']
            for f in male_only:
                others.remove(f)
        else:
            raise Exception('gender not recognized: ' + str(gender))

        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            day = pick_random(weekdays)
            other = pick_random(others)

            r = random.randrange(1, 30)
            if (r == 1):   # name is prefixed with another name element
                prefixed_elements = ['Da', 'Nur', 'Phu']
                other = pick_random(prefixed_elements) + other.lower()

            name = ' '.join([day, other])
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class MedievalFrenchGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'french' : 'only generate names from french heartland',
            'norman' : 'only generate names from norman france',
            'provencal' : 'only generate names from french region of Provence'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather personal names
        names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                names = self.list['Male']['Common']
            elif ('french' in args):
                names = self.list['Male']['French']
            elif ('norman' in args):
                names = self.list['Male']['Norman']
            elif ('provencal' in args):
                names = self.list['Male']['Provencal']
            else:
                names = self.list['Male']['Common'] \
                      + self.list['Male']['French'] \
                      + self.list['Male']['Provencal']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                names = self.list['Female']['Common']
            elif ('french' in args):
                names = self.list['Female']['French']
            elif ('norman' in args):
                names = self.list['Female']['Norman']
            elif ('provencal' in args):
                names = self.list['Female']['Provencal']
            else:
                names = self.list['Female']['Common'] \
                      + self.list['Female']['French'] \
                      + self.list['Female']['Provencal']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class CelticGaulishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'tribe' : 'generate tribe names (no personal names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather tribe names
        if ('tribe' in args):
            tribes = s['Tribe']
            return pick_random(tribes, amount)

        # Gather personal names
        names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                names = self.list['Personal']['Male']['Common']
            else:
                names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                names = self.list['Personal']['Female']['Common']
            else:
                names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class GermanicGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'most common name elements only',
            'single-element' : 'single-element names only',
            'two-element' : 'two-element names only'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather tribe names
        if ('tribe' in args):
            return pick_random(s['Tribe'], amount)

        # Gather name elements
        pet_names = self.list['Single-element']['Common']
        single_element_endings = []
        single_element = []
        first_element = []
        second_element = []
        if (gender.lower() == 'male'):
            single_endings = self.list['Single-element']['Endings']['Masculine']
            if ('common' in args):
                single_element = self.list['Two-element']['Male']['First']['Common'] \
                               + pet_names
                first_element = self.list['Two-element']['Male']['First']['Common']
                second_element = self.list['Two-element']['Male']['Second']['Common']
            else:
                single_element = self.list['Two-element']['Male']['First']['Standard'] \
                               + pet_names
                first_element = self.list['Two-element']['Male']['First']['Standard']
                second_element = self.list['Two-element']['Male']['Second']['Standard']
        elif (gender.lower() == 'female'):
            single_endings = self.list['Single-element']['Endings']['Feminine']
            if ('common' in args):
                single_element = self.list['Two-element']['Female']['First']['Common'] \
                               + pet_names
                first_element = self.list['Two-element']['Female']['First']['Common']

                male_converted = self.list['Two-element']['Male']['Second']['Common']
                male_converted = [e + 'a' for e in male_converted]
                second_element = self.list['Two-element']['Female']['Second']['Common'] \
                               + male_converted

            else:
                single_element = self.list['Two-element']['Female']['First']['Standard'] \
                               + pet_names
                first_element = self.list['Two-element']['Female']['First']['Standard']
                male_converted = self.list['Two-element']['Male']['Second']['Standard']
                male_converted = [e + 'a' for e in male_converted]
                second_element = self.list['Two-element']['Female']['Second']['Common'] \
                               + male_converted
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            vowels = ['a', 'e', 'i', 'o', 'u']
            name = ''
            r1 = random.random()
            if ('two-element' in args):
                first = pick_random(first_element)
                second = pick_random(second_element)
                r2 = random.random()
                if (r2 < 0.5 and not first.endswith(tuple(vowels))
                    and not second.startswith(tuple(vowels))):
                    name = first + 'i' + second
                else:
                    name = first + second
            elif (r1 < 0.2 or 'single-element' in args):  # name is single-element
                name = pick_random(single_element)
                ending = ''
                if (name not in pet_names):
                    for v in vowels:
                        if (name.endswith(v)):
                            ending = single_endings[0]
                        else:
                            ending = single_endings[1]
                name = name + ending
            else:   # name is two-element
                first = pick_random(first_element)
                second = pick_random(second_element)
                r2 = random.random()
                if (r2 < 0.5 and not first.endswith(tuple(vowels))
                    and not second.startswith(tuple(vowels))):
                    name = first + 'i' + second
                else:
                    name = first + second

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class GypsyGenerator(HistoricalGenerator):

    #TODO: change 'title' option to append a title to a name

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'tribe' : 'generate tribe names (no personal names)',
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather tribe names
        if ('tribe' in args):
            tribes = self.list['Tribe']
            return pick_random(tribes, amount)

        # Gather titles
        if ('titles' in args):
            titles = self.list['Titles']
            return pick_random(titles, amount)

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class HungarianGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names
        personal_names = []
        diminutives = []
        if (gender.lower() == 'male'):
            diminutives = self.list['Personal']['Male']['Diminutive']
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            diminutives = self.list['Personal']['Female']['Diminutive']
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            first_name = pick_random(personal_names)
            last_name = pick_random(family_names)
            r = random.random()
            if (r < 0.5 and first_name in diminutives.keys()):
                dim = pick_random(diminutives[first_name])
                first_name += ' \"' + dim + '\"'

            if ('personal' in args):
                name = first_name
            else:
                last_name = pick_random(family_names)
                name = ' '.join([first_name, last_name])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class PolishGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather name elements
        personal_names = []
        family_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
                family_names = self.list['Family']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
                family_names = self.list['Family']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
                family_names = self.list['Family']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
                family_names = self.list['Family']['Standard']
            ending_map = {
                'ski' : 'ska',
                'cki' : 'cka',
                'dzki' : 'dzka'
            }
            modified_endings = []
            for f in family_names:
                for (k, v) in ending_map.items():
                    if f.endswith(k):
                        modified_endings.append(f[:-len(k)] + v)
            family_names = modified_endings
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)
        if ('family' in args):
            return pick_random(family_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class RussianGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        vowels = ['a', 'e', 'i', 'o', 'u', 'y']

        # Gather family names
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        else:
            family_names = self.list['Family']['Standard']

        # Gather personal names
        personal_names = []
        diminutives = []
        patronymic_ending = ''
        if (gender.lower() == 'male'):
            patronymic_ending = 'ovich'
            diminutives = self.list['Personal']['Male']['Diminutive']
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            patronymic_ending = 'ovna'
            diminutives = self.list['Personal']['Female']['Diminutive']
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']

            family_names_modified = []
            for f in family_names:
                if (f.endswith(('sky', 'ski'))):
                    family_names_modified.append(f[:-3] + 'skaya')
                elif (not f.endswith(tuple(vowels))):
                    family_names_modified.append(f + 'a')
            family_names = family_names_modified
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            first_name = pick_random(personal_names)
            r1 = random.random()
            if (r1 < 0.5 and first_name in diminutives.keys()):
                dim = pick_random(diminutives[first_name])
                first_name += ' \"' + dim + '\"'

            if ('personal' in args):
                name = first_name
            else:
                last_name = ''
                r2 = random.random()
                if (r2 < 0.25):   # family name is patronymic
                    father = pick_random(self.list['Personal']['Male']['Standard'])
                    while (father.endswith(tuple(vowels))):
                        father = father[:-1]
                    last_name = father + patronymic_ending
                else:
                    last_name = pick_random(family_names)

                if ('family' in args):
                    name = last_name
                else:
                    name = ' '.join([first_name, last_name])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class MedievalSpanishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'spanish' : 'limit names to typical spanish',
            'basque' : 'limit names to basque region of Spain'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather personal names
        names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                names = self.list['Male']['Common']
            elif ('spanish' in args):
                names = self.list['Male']['Spanish']
            elif ('basque' in args):
                names = self.list['Male']['Basque']
            else:
                names = self.list['Male']['Common'] \
                      + self.list['Male']['Spanish'] \
                      + self.list['Male']['Basque']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                names = self.list['Female']['Common']
            elif ('spanish' in args):
                names = self.list['Female']['Spanish']
            elif ('basque' in args):
                names = self.list['Female']['Basque']
            else:
                names = self.list['Female']['Common'] \
                      + self.list['Female']['Spanish'] \
                      + self.list['Female']['Basque']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class ArabicGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'standard' : 'choose names from "Standard" list (no personal \
                          bynames)',
            'bynames' : 'choose names from "Bynames" list (no "standard" \
                         personal names)',
            'religious' : 'choose family names from "Religious Epithets" list \
                           (no bynames as family names)'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather name elements
        personal_names = []
        bynames = self.list['Bynames']['Beasts'] \
                + self.list['Bynames']['Occupations'] \
                + self.list['Bynames']['Qualities']
        religious_epithets = self.list['Religious Epithets']['Faith']
        if ('religious' in args):
            r = []
            for e in self.list['Religious Epithets']['Attribute']:
                r.append('Abd-' + e)
            religious_epithets += r
        else:
            religious_epithets += self.list['Religious Epithets']['Attribute']

        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            elif ('standard' in args):
                personal_names = self.list['Personal']['Male']['Standard']
            elif ('bynames' in args):
                personal_names = self.list['Personal']['Male']['Bynames']
            else:
                personal_names = self.list['Personal']['Male']['Standard'] \
                               + self.list['Personal']['Male']['Bynames']
            personal_bynames = []
            for b in self.list['Personal']['Male']['Bynames']:
                personal_bynames.append('al-' + b)
            bynames += personal_bynames
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            elif ('standard' in args):
                personal_names = self.list['Personal']['Female']['Standard']
            elif ('bynames' in args):
                personal_names = self.list['Personal']['Female']['Bynames']
            else:
                personal_names = self.list['Personal']['Female']['Standard'] \
                               + self.list['Personal']['Female']['Bynames']
            personal_bynames = []
            for b in self.list['Personal']['Female']['Bynames']:
                personal_bynames.append('al-' + b)
            bynames += personal_bynames + self.list['Bynames']['Female']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        if ('personal' in args):
            return pick_random(personal_names, amount)
        if ('family' in args):
            return pick_random(bynames + religious_epithets, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            first = pick_random(personal_names)
            last = pick_random(bynames + religious_epithets)

            name = ' '.join([first, last])
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class GreekGenerator(HistoricalGenerator):

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather name elements:
        personal_names = []
        family_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
                family_names = self.list['Family']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
                family_names = self.list['Family']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
                family_names = self.list['Family']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
                family_names = self.list['Family']['Standard']
            endings_to_modify = ['as', 'es', 'is', 'ou']
            modified_endings = []
            for f in family_names:
                if (f.endswith(tuple(endings_to_modify))):
                    modified_endings.append(f[:-1])
            family_names = modified_endings
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)
        if ('family' in args):
            return pick_random(family_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class RomanGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'ordinal' : 'force names to include an ordinal (number) element'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather name elements
        praenomina = []
        nomina = []
        cognomina = []
        ordinals = []
        if (gender.lower() == 'male'):
            ordinals = self.list['Male']['Cognomina']['Ordinal']
            if ('common' in args):
                praenomina = self.list['Male']['Praenomina']['Common']
                nomina = self.list['Male']['Nomina']['Common']
                if ('ordinal' in args):
                    cognomina = ordinals
                else:
                    cognomina = self.list['Male']['Cognomina']['Common']
            else:
                praenomina = self.list['Male']['Praenomina']['Standard']
                nomina = self.list['Male']['Nomina']['Standard']
                if ('ordinal' in args):
                    cognomina = ordinals
                else:
                    cognomina = self.list['Male']['Cognomina']['Standard'] \
                              + self.list['Male']['Cognomina']['Ordinal']
        elif (gender.lower() == 'female'):
            feminine_ending_map = {
                'a' : 'ina',
                'us' : 'a',
                'o' : 'a'
            }
            for f in self.list['Male']['Cognomina']['Ordinal']:
                for (k, v) in feminine_ending_map.items():
                    if (f.endswith(k)):
                        ordinals.append(f[:-len(k)] + v)
            if ('common' in args):
                for f in self.list['Male']['Nomina']['Common']:
                    for (k, v) in feminine_ending_map.items():
                        if (f.endswith(k)):
                            nomina.append(f[:-len(k)] + v)
                for f in self.list['Male']['Cognomina']['Common']:
                    for (k, v) in feminine_ending_map.items():
                        if (f.endswith(k)):
                            cognomina.append(f[:-len(k)] + v)
            else:
                for f in self.list['Male']['Nomina']['Standard']:
                    for (k, v) in feminine_ending_map.items():
                        if (f.endswith(k)):
                            nomina.append(f[:-len(k)] + v)
                for f in self.list['Male']['Cognomina']['Standard']:
                    for (k, v) in feminine_ending_map.items():
                        if (f.endswith(k)):
                            cognomina.append(f[:-len(k)] + v)
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            if (gender.lower() == 'male'):
                praenomin = pick_random(praenomina)
                nomin = pick_random(nomina)
                cognomin = ''
                if ('ordinal' in args):
                    cognomin = pick_random(ordinals)
                else:
                    cognomin = pick_random(cognomina)

                r1 = random.randrange(1, 30)
                if (r1 == 1):   # name has 2 cognomin elements
                    cognomin2 = pick_random(cognomina)
                    while (cognomin2 == cognomin):
                        cognomin2 = pick_random(cognomina)

                    r2 = random.randrange(1, 20)
                    if (r2 == 1):
                        cognomin3 = pick_random(cognomina)
                        while (cognomin3 in [cognomin, cognomin2]):
                            cognomin3 = pick_random(cognomina)

                            name = ' '.join([praenomin, nomin, cognomin, \
                                             cognomin2, cognomin3])
                    else:
                        name = ' '.join([praenomin, nomin, cognomin, cognomin2])
                else:
                    name = ' '.join([praenomin, nomin, cognomin])
            else:
                nomin = pick_random(nomina)
                cognomin = pick_random(cognomina)
                name = ' '.join([nomin, cognomin])

                r1 = random.random()
                if (r1 < 0.33 or 'ordinal' in args):   # name has an ordinal
                    ordinal = pick_random(ordinals + ['maior', 'minor'])
                    name += ' ' + ordinal

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class JewishGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'standard' : 'choose names from "Standard" list only',
            'old' : 'old (pre-hebrew revival) family names only',
            'new' : 'new (post-hebrew revival) family names only'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather last names:
        family_names = []
        if ('common' in args):
            family_names = self.list['Family']['Common']
        elif ('standard' in args):
            family_names = self.list['Family']['Standard']
        elif ('old' in args):
            family_names = self.list['Family']['Old']
        elif ('new' in args):
            family_names = self.list['Family']['New']
        else:
            family_names = self.list['Family']['Standard'] \
                         + self.list['Family']['Old'] \
                         + self.list['Family']['New']
        if ('family' in args):
            return pick_random(family_names, amount)

        # Gather personal names:
        personal_names = []
        if (gender.lower() == 'male'):
            if ('common' in args):
                personal_names = self.list['Personal']['Male']['Common']
            else:
                personal_names = self.list['Personal']['Male']['Standard']
        elif (gender.lower() == 'female'):
            if ('common' in args):
                personal_names = self.list['Personal']['Female']['Common']
            else:
                personal_names = self.list['Personal']['Female']['Standard']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('personal' in args):
            return pick_random(personal_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(personal_names) \
                 + ' ' \
                 + pick_random(family_names)
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class PhoenicianGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'stand-alone' : 'limit names to stand-alone only',
            'theophoric' : 'limit names to theophoric only'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather name elements:
        stand_alone = []
        theo_prefixes = []
        theo_deities = []
        theo_suffixes = []
        if (gender.lower() == 'male'):
            stand_alone = self.list['Stand-alone']['Male'] \
                        + self.list['Stand-alone']['Neutral']
            if ('common' in args):
                theo_prefixes = self.list['Theophoric']['Common']['Prefix']
                theo_deities = self.list['Theophoric']['Common']['Deity']
                theo_suffixes = self.list['Theophoric']['Common']['Suffix']
            else:
                theo_prefixes = self.list['Theophoric']['Prefix']['Male'] \
                              + self.list['Theophoric']['Prefix']['Neutral']
                theo_deities = self.list['Theophoric']['Deity']['Phoenician'] \
                             + self.list['Theophoric']['Deity']['Titles'] \
                             + self.list['Theophoric']['Deity']['Other']
                theo_suffixes = self.list['Theophoric']['Suffix']
        elif (gender.lower() == 'female'):
            stand_alone = self.list['Stand-alone']['Female'] \
                        + self.list['Stand-alone']['Neutral']
            if ('common' in args):
                theo_prefixes = self.list['Theophoric']['Common']['Prefix']
                theo_deities = self.list['Theophoric']['Common']['Deity']
                theo_suffixes = self.list['Theophoric']['Common']['Suffix']
            else:
                theo_prefixes = self.list['Theophoric']['Prefix']['Female'] \
                              + self.list['Theophoric']['Prefix']['Neutral']
                theo_deities = self.list['Theophoric']['Deity']['Phoenician'] \
                             + self.list['Theophoric']['Deity']['Titles'] \
                             + self.list['Theophoric']['Deity']['Other']
                theo_suffixes = self.list['Theophoric']['Suffix']
        else:
            raise Exception('gender not recognized: ' + str(gender))
        if ('stand-alone' in args):
            return pick_random(stand_alone, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            r1 = random.randrange(1, 6)
            if (r1 <= 4 or 'theophoric' in args):  # name is theophoric
                r2 = random.randrange(1, 4)
                if (r2 == 4):   # name is of form: deity + suffix
                    deity = pick_random(theo_deities)
                    suffix = pick_random(theo_suffixes)
                    name = deity + suffix
                else:   # name is of form: prefix + deity
                    prefix = pick_random(theo_prefixes)
                    deity = pick_random(theo_deities).lower()
                    name = prefix + deity
            else:   # name is stand-alone
                name = pick_random(stand_alone)

            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class AboriginalGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'family' : 'family names only (no first names)',
            'languages' : 'generate names of native Aboriginal languages'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names:
        if ('family' in args):
            family_names = self.list['Family']
            return pick_random(family_names, amount)

        # Gather languages:
        if ('languages' in args):
            languages = self.list['Languages']
            return pick_random(languages, amount)

        # Gather personal names
        names = []
        if (gender.lower() == 'male'):
            names = self.list['Personal']['Male']
            for f in self.list['Family']:
                if (f.endswith('o')):
                    names.append(f)
        elif (gender.lower() == 'female'):
            names = self.list['Personal']['Female']
            for f in self.list['Family']:
                if (f.endswith('a')):
                    names.append(f)
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class PapuanGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'common' : 'limit generated names to those that are most common',
            'tribe' : 'generate names of native Papuan tribes',
            'languages' : 'generate names of native Papuan languages'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather family names:
        if ('tribe' in args):
            tribe_names = self.list['Tribe and Clan']
            return pick_random(tribe_names, amount)

        # Gather languages:
        if ('languages' in args):
            languages = self.list['Languages']
            return pick_random(languages, amount)

        # Gather personal names
        names = []
        feminine_endings = ['a', 'e', 'i', 'y']
        if (gender.lower() == 'male'):
            names = self.list['Personal']['Male']
            for f in self.list['Languages']:
                if (not f.endswith(tuple(feminine_endings))):
                    names.append(f)
        elif (gender.lower() == 'female'):
            names = self.list['Personal']['Female']
            for f in self.list['Languages']:
                if (f.endswith(tuple(feminine_endings))):
                    names.append(f)
        else:
            raise Exception('gender not recognized: ' + str(gender))
        return pick_random(names, amount)

class PolynesianGenerator(HistoricalGenerator):

    def valid_args(self):
        valid_args = {
            'personal' : 'personal names only (no last names)',
            'family' : 'family names only (no first names)',
            'tribe' : 'generate names of native Polynesian tribes',
            'hawaiian' : 'only generate Hawaiian names',
            'maori' : 'only generate Maori names',
            'samoan' : 'only generate Samoan names',
            'tahitian' : 'only generate Tahitian names',
            'tongan' : 'only generate Tongan names'
        }
        return valid_args

    def generate(self, gender, amount=10, *args):
        for a in args:
            if a and a not in self.valid_args().keys():
                raise Exception('Invalid argument: ' + str(a))

        # Gather tribes:
        if ('tribe' in args):
            tribes = self.list['Tribe']
            return pick_random(tribes, amount)

        # Gather name elements:
        personal_names = []
        family_names = []
        if (gender.lower() == 'male'):
            if ('hawaiian' in args):
                personal_names = self.list['Hawai\'ian']
                family_names = []
            elif ('maori' in args):
                personal_names = self.list['Personal']['Male']['Maori']
                family_names = self.list['Family']['Maori']
            elif ('samoan' in args):
                personal_names = self.list['Personal']['Male']['Samoan']
                family_names = self.list['Family']['Samoan']
            elif ('tahitian' in args):
                personal_names = self.list['Personal']['Male']['Tahitian']
                family_names = []
            elif ('tongan' in args):
                personal_names = self.list['Personal']['Male']['Tongan']
                family_names = self.list['Family']['Tongan']
            else:
                personal_names = self.list['Hawai\'ian'] \
                               + self.list['Personal']['Male']['Maori'] \
                               + self.list['Personal']['Male']['Samoan'] \
                               + self.list['Personal']['Male']['Tahitian'] \
                               + self.list['Personal']['Male']['Tongan']
                family_names = self.list['Hawai\'ian'] \
                             + self.list['Family']['Maori'] \
                             + self.list['Family']['Samoan'] \
                             + self.list['Family']['Tongan']
        elif (gender.lower() == 'female'):
            if ('hawaiian' in args):
                personal_names = self.list['Hawai\'ian']
                family_names = []
            elif ('maori' in args):
                personal_names = self.list['Personal']['Female']['Maori']
                family_names = self.list['Family']['Maori']
            elif ('samoan' in args):
                personal_names = self.list['Personal']['Female']['Samoan']
                family_names = self.list['Family']['Samoan']
            elif ('tahitian' in args):
                personal_names = self.list['Personal']['Female']['Tahitian']
                family_names = []
            elif ('tongan' in args):
                personal_names = self.list['Personal']['Female']['Tongan']
                family_names = self.list['Family']['Tongan']
            else:
                personal_names = self.list['Hawai\'ian'] \
                               + self.list['Personal']['Female']['Maori'] \
                               + self.list['Personal']['Female']['Samoan'] \
                               + self.list['Personal']['Female']['Tahitian'] \
                               + self.list['Personal']['Female']['Tongan']
                family_names = self.list['Hawai\'ian'] \
                             + self.list['Family']['Maori'] \
                             + self.list['Family']['Samoan'] \
                             + self.list['Family']['Tongan']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        if ('personal' in args):
            return pick_random(personal_names, amount)
        if ('family' in args):
            return pick_random(family_names, amount)

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            first = pick_random(personal_names)
            last = pick_random(family_names)
            name = ' '.join([first, last])

            if name in names:
                i += 1
            else:
                names.append(name)
        return names


class SyllabicGenerator:

    def __init__(self, source=None, duplicate_limit=20):
        self.duplicate_limit= duplicate_limit
        self.list = {
            'harsh' : self.load_json('Strange_Syllables')['Harsh'],
            'neutral' : self.load_json('Strange_Syllables')['Neutral'],
            'smooth' : self.load_json('Strange_Syllables')['Smooth'],
            'various' : self.load_json('Strange_Syllables')['Various'],
            'crude_small' : self.load_json('Vile_And_Crude')['Small'],
            'crude_medium' : self.load_json('Vile_And_Crude')['Medium'],
            'crude_large' : self.load_json('Vile_And_Crude')['Large'],
            'primitive' : self.load_json('Primitive')['Standard'],
            'doughty' : self.load_json('Doughty_And_Homely')['Doughty']['Prefix'],
            'homely' : self.load_json('Doughty_And_Homely')['Homely']['Prefix'],
            'fair' : self.load_elvish(self.load_json('Fair_And_Noble')),
            'noble' : self.load_elvish(self.load_json('Fair_And_Noble')),
            'small' : self.load_json('Small_And_Spry')['Small']['Prefix'],
            'spry' : self.load_json('Small_And_Spry')['Spry']['Prefix'],
            'sinister' : self.load_elvish(self.load_json('Evil_But_Elegant')),
            'nasty' : self.load_json('Malevolent')['Prefix'],
            'draconic' : self.load_json('Draconic')['Prefix'],
            'soft' : self.load_json('Infernal')['Soft & Spongy'],
            'spongy' : self.load_json('Infernal')['Soft & Spongy'],
            'dull' : self.load_json('Infernal')['Dull & Heavy'],
            'heavy' : self.load_json('Infernal')['Dull & Heavy'],
            'sharp' : self.load_json('Infernal')['Sharp & Spiky'],
            'spiky' : self.load_json('Infernal')['Sharp & Spiky'],
            'angelic' : self.load_json('Angelic')['Prefix'],
            'comical_short' : self.load_json('Comical')['Short'],
            'comical_long' : self.load_json('Comical')['Long'],
            'ape' : self.load_json('Animal')['Mammals']['Apes'],
            'rat' : self.load_json('Animal')['Mammals']['Rats'],
            'squirrel' : self.load_json('Animal')['Mammals']['Squirrels'],
            'dog' : self.load_json('Animal')['Mammals']['Dogs'],
            'hyena' : self.load_json('Animal')['Mammals']['Hyenas'],
            'cat' : self.load_json('Animal')['Mammals']['Cats'],
            'big_cat' : self.load_json('Animal')['Mammals']['Great Cats'],
            'horse' : self.load_json('Animal')['Mammals']['Horses'],
            'pig' : self.load_json('Animal')['Mammals']['Pigs'],
            'crustacean' : self.load_json('Animal')['Arthropods']['Crustaceans'],
            'spider' : self.load_json('Animal')['Arthropods']['Spiders'],
            'insect' : self.load_json('Animal')['Arthropods']['Insects'],
            'octopus' : self.load_json('Animal')['Molluscs']['Octopus'],
            'squid' : self.load_json('Animal')['Molluscs']['Squid'],
            'slug' : self.load_json('Animal')['Molluscs']['Slugs'],
            'bird_cry' : self.load_json('Animal')['Birds']['Cries'],
            'bird_croak' : self.load_json('Animal')['Birds']['Croaks'],
            'bird_tweet' : self.load_json('Animal')['Birds']['Tweets'],
            'bird_chirp' : self.load_json('Animal')['Birds']['Chirps'],
            'bird_hoot' : self.load_json('Animal')['Birds']['Hoots'],
            'fish' : self.load_json('Animal')['Fish']['Fish'],
            'shark' : self.load_json('Animal')['Fish']['Sharks'],
            'eel' : self.load_json('Animal')['Fish']['Eels'],
            'turtle' : self.load_json('Animal')['Reptiles']['Turtles'],
            'lizard' : self.load_json('Animal')['Reptiles']['Lizards'],
            'snake' : self.load_json('Animal')['Reptiles']['Snakes'],
            'frog' : self.load_json('Animal')['Amphibians']['Frogs'],
            'toad' : self.load_json('Animal')['Amphibians']['Toads']
        }

    def generate(self, desc, amount=10):
        descriptors = desc.split('+')
        for d in descriptors:
            if d not in self.list.keys():
                raise Exception('invalid descriptor: ' + str(d))

        names = []
        for _ in range(amount):
            name = ''
            for d in descriptors:
                name += pick_random(self.list[d])
            lim = 0
            while (name in names and lim < self.duplicate_limit):
                name = ''
                for d in descriptors:
                    name += pick_random(self.list[d])
                if name in names:
                    lim += 1
            names.append(name.title())
        return names

    def get_descriptors(self):
        descriptors = {
            'Standard' : sorted(['harsh', 'neutral', 'smooth', 'various',
                          'crude_small', 'crude_medium', 'crude_large',
                          'primitive', 'doughty', 'homely', 'fair', 'noble',
                          'small', 'spry', 'sinister', 'nasty', 'draconic',
                          'soft', 'spongy', 'dull', 'heavy', 'sharp', 'spiky',
                          'angelic', 'comical_short', 'comical_long']),
            'Animal' : sorted(['ape', 'rat', 'squirrel', 'dog', 'hyena', 'cat',
                        'big_cat', 'horse', 'pig', 'crustacean', 'spider',
                        'insect', 'octopus', 'squid', 'slug', 'bird_cry',
                        'bird_croak', 'bird_tweet', 'bird_chirp', 'bird_hoot',
                        'fish', 'shark', 'eel', 'turtle', 'lizard', 'snake',
                        'frog', 'toad'])
        }
        return descriptors

    def load_json(self, list):
        path = os.path.join('Names', 'Fantasy', list + '.json')
        with open(path) as f:
            list = json.load(f)
        return list

    def load_elvish(self, source_dict):
        prefixes = source_dict['Prefix']['A'] + source_dict['Prefix']['B']
        middle = source_dict['Middle']
        all = []
        for p in prefixes:
            for m in middle:
                component = p + m
                if component not in all:
                    all.append(component)
        return all

class FantasyGenerator:

    def __init__(self, source: str, duplicate_limit: int = 20):
        valid_sources = source_map()['Fantasy'].keys()
        if source not in valid_sources:
            raise Exception('invalid source: ' + str(source))
        self.source = source
        self.duplicate_limit = duplicate_limit
        list_path = os.path.join('Names', 'Fantasy', source + '.json')
        with open(list_path) as f:
            self.list = json.load(f)

    def generate(self, length, amount=10):
        names = []
        if (length.lower() == 'one-syllable'):
            names = self.list['One-syllable']
        elif (length.lower() == 'two-syllable'):
            names = self.list['Two-syllable']
        elif (length.lower() == 'three-syllable'):
            names = self.list['Three-syllable']
        elif (length.lower() == 'multi-syllable'):
            names = self.list['Multi-syllable']
        else:
            names = self.list['One-syllable'] + self.list['Two-syllable'] \
                  + self.list['Three-syllable'] + self.list['Multi-syllable']
        return pick_random(names, amount)

    def print_structure(self):
        print('%s = {' % self.source)
        self.print_structure_helper(self.list, '\t')
        print('}')
        return True

    def print_structure_helper(self, my_dict, indentation):
        if isinstance(my_dict, dict):
            for k in my_dict.keys():
                print(indentation + '\'%s\'' % k)
                self.print_structure_helper(my_dict[k], indentation + '\t')
        return True

class CrudeGenerator:

    def __init__(self, race, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Vile_And_Crude.json')
        with open(path) as f:
            if (race.lower() == 'goblin'):
                self.list = json.load(f)['Small']
            elif (race.lower() == 'orc'):
                self.list = json.load(f)['Medium']
            elif (race.lower() == 'ogre'):
                self.list = json.load(f)['Large']
            else:
                raise Exception('invalid race: ' + str(race))

    def generate(self, gender=None, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            first = pick_random(self.list)
            r1 = random.randrange(1, 20)
            if (r1 == 1 or True):   # name has only one element
                vowels = ['a', 'e', 'i', 'o', 'u']
                if (first[0] not in vowels and first[-1] not in vowels):
                    prefixes = ['a', 'i', 'o', 'u']
                    name = pick_random(prefixes) + first
                else:
                    if (first[0] in vowels):
                        prefixes = ['b', 'g', 'h', 'k', 'z',
                                    'br', 'gr', 'hr', 'kr', 'zr',
                                    'bl', 'gl', 'kl']
                        name = pick_random(prefixes) + first
                    else:
                        suffixes = ['b', 'g', 'h', 'k', 'z',
                                    'rg', 'rk', 'rz',
                                    'lg', 'lk', 'lz']
                        name = first + pick_random(suffixes)
            else:
                second = pick_random(self.list)
                while (first == second):
                    second = pick_random(self.list)
                name = first + second

            r2 = random.random()
            if (r2 < 0.2):
                name = 'G\'' + name

            name = name.title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class ElfGenerator:

    def __init__(self, race: str, duplicate_limit: int = 20):
        self.duplicate_limit = duplicate_limit
        self.race = race
        if (race.lower() == 'high elf'):
            path = os.path.join('Names', 'Fantasy', 'Fair_And_Noble.json')
            with open(path) as f:
                self.list = json.load(f)
                self.list['Prefix'] = self.list['Prefix']['A']
        elif (race.lower() == 'wood elf'):
            path = os.path.join('Names', 'Fantasy', 'Fair_And_Noble.json')
            with open(path) as f:
                self.list = json.load(f)
                self.list['Prefix'] = self.list['Prefix']['B']
        elif (race.lower() == 'drow'):
            path = os.path.join('Names', 'Fantasy', 'Evil_But_Elegant.json')
            with open(path) as f:
                self.list = json.load(f)
                self.list['Prefix'] = self.list['Prefix']['A'] \
                                    + self.list['Prefix']['B']
        else:
            raise Exception('invalid race: ' + str(race))

    def generate(self, gender, amount=10):
        prefixes = self.list['Prefix']
        middle = self.list['Middle']
        suffixes = []
        if (gender.lower() == 'male'):
            suffixes = self.list['Suffix']['Male']
        elif (gender.lower() == 'female'):
            suffixes = self.list['Suffix']['Female']
        else:
            raise Exception('gender not recognized: ' + str(gender))

        # Compile names
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            pref = pick_random(prefixes)
            mid = pick_random(middle)
            suff = pick_random(suffixes)

            # Remove duplicate letters
            if (pref[-1] == mid[0]):
                pref = pref[:-1]
            if (mid[-1] == suff[0]):
                suff = suff[1:]

            # Add glue where necessary
            vowels = ['a', 'e', 'i', 'o', 'u']
            vowel_glue = ''
            if (self.race.lower() == 'drow'):
                if (gender.lower() == 'male'):
                    vowel_glue = 'i'
                else:
                    vowel_glue = 'i'
            else:
                if (gender.lower() == 'male'):
                    vowel_glue = 'a'
                else:
                    vowel_glue = 'e'

            if (mid[-1] not in vowels and suff[0] not in vowels):
                mid += vowel_glue

            name = ''.join([pref, mid, suff]).title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class DoughtyGenerator:

    #TODO: move gnome into its own generator -> comical_long+comical_short

    def __init__(self, race, duplicate_limit=20):
        self.race = race
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Doughty_And_Homely.json')
        with open(path) as f:
            if (race.lower() == 'dwarf'):
                self.list = json.load(f)['Doughty']
            elif (race.lower() == 'halfling'):
                self.list = json.load(f)['Homely']
            elif (race.lower() == 'gnome'):
                list = json.load(f)
                self.list = {
                    'Prefix' : list['Doughty']['Prefix'],
                    'Suffix' : {
                        'Male' : list['Homely']['Suffix']['Male'],
                        'Female' : list['Homely']['Suffix']['Female']
                    }
                }

    def generate(self, gender, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            root = pick_random(self.list['Prefix'])
            ending = ''
            if (gender.lower() == 'male'):
                ending = pick_random(self.list['Suffix']['Male'])
            elif (gender.lower() == 'female'):
                ending = pick_random(self.list['Suffix']['Female'])
            else:
                raise Exception('gender not recognized: ' + str(gender))

            vowels = ['a', 'e', 'i', 'o', 'u']
            if (self.race.lower() == 'gnome'):
                if (root[-1] in vowels):
                    root += 'l'
            elif (self.race.lower() == 'dwarf'):
                r = random.randrange(1, 8)
                if (r == 1):
                    if (gender.lower() == 'male'):
                        if (root[-1] in vowels):
                            ending = 'r'
                        else:
                            ending = 'i'
                    elif (gender.lower() == 'female'):
                        if (root[-1] in vowels):
                            ending = 'ra'
                        else:
                            ending = 'a'


            name = (root + ending).title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class FeyGenerator:

    def __init__(self, type, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Small_And_Spry.json')
        with open(path) as f:
            if (type.lower() == 'seelie'):
                self.list = json.load(f)['Small']
            elif (type.lower() == 'unseelie'):
                self.list = json.load(f)['Spry']
            else:
                raise Exception('type not recognized: ' + str(type))

    def generate(self, gender, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            root = pick_random(self.list['Prefix'])
            if (gender.lower() == 'male'):
                name = root + pick_random(self.list['Suffix']['Male'])
            elif (gender.lower() == 'female'):
                name = root + pick_random(self.list['Suffix']['Female'])

            name = name.title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class NymphGenerator:

    def __init__(self, type, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Nymphs_And_Sirens.json')
        with open(path) as f:
            if (type.lower() == 'nymph'):
                self.list = json.load(f)['Nymphs']
            elif (type.lower() == 'siren'):
                self.list = json.load(f)['Sirens']
            else:
                raise Exception('invalid creature type: ' + str(type))

    def generate(self, gender, amount=10):
        return pick_random(self.list, amount)

class DragonGenerator:

    def __init__(self, type, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Draconic.json')
        with open(path) as f:
            dragons = json.load(f)
            if (type.lower() == 'faerie'):
                path2 = os.path.join('Names', 'Fantasy', 'Small_And_Spry.json')
                with open(path2) as f2:
                    sprites = json.load(f2)['Spry']
                dragons['Suffix'] = sprites['Suffix']
                self.list = dragons
            elif (type.lower() == 'evil'):
                path2 = os.path.join('Names', 'Fantasy', 'Infernal.json')
                with open(path2) as f2:
                    sharp = json.load(f2)['Sharp & Spiky']
                dragons['Suffix']['Male'] = sharp
                dragons['Suffix']['Female'] = sharp
                self.list = dragons
            elif (type.lower() == 'normal'):
                self.list = dragons
            else:
                raise Exception('invalid dragon type: ' + str(type))

    def generate(self, gender, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = ''
            root = pick_random(self.list['Prefix'])
            if (gender.lower() == 'male'):
                name = root + pick_random(self.list['Suffix']['Male'])
            elif (gender.lower() == 'female'):
                name = root + pick_random(self.list['Suffix']['Female'])

            name = name.title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class SerpentGenerator:

    def __init__(self, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Serpents.json')
        with open(path) as f:
            self.list = json.load(f)

    def generate(self, gender=None, amount=10):
        return pick_random(self.list, amount)

class InfernalGenerator:

    def __init__(self, type, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Infernal.json')
        with open(path) as f:
            roots = json.load(f)
            if (type.lower() == 'small demon'):
                self.list = {
                    'first' : roots['Dull & Heavy'],
                    'second' : []
                    }
            elif (type.lower() == 'medium demon'):
                self.list = {
                    'first' : roots['Dull & Heavy'],
                    'second' : roots['Soft & Spongy']
                }
            elif (type.lower() == 'large demon'):
                self.list = {
                    'first' : roots['Dull & Heavy'],
                    'second' : roots['Sharp & Spiky']
                }
            elif (type.lower() == 'small devil'):
                self.list = {
                    'first' : roots['Sharp & Spiky'],
                    'second' : []
                }
            elif (type.lower() == 'medium devil'):
                p2 = os.path.join('Names', 'Fantasy', 'Malevolent.json')
                with open(p2) as f2:
                    nasty = json.load(f2)
                self.list = {
                    'first' : nasty['Prefix'],
                    'second' : roots['Sharp & Spiky']
                }
            elif (type.lower() == 'large devil'):
                p2 = os.path.join('Names', 'Fantasy', 'Malevolent.json')
                with open(p2) as f2:
                    nasty = json.load(f2)
                p3 = os.path.join('Names', 'Fantasy', 'Strange_Syllables.json')
                with open(p3) as f3:
                    harsh = json.load(f3)['Harsh']
                self.list = {
                    'first' : harsh,
                    'second' : nasty['Suffix']
                }
            elif (type.lower() == 'ooze'):
                p2 = os.path.join('Names', 'Fantasy', 'Strange_Syllables.json')
                with open(p2) as f2:
                    smooth = json.load(f2)['Smooth']
                self.list = {
                    'first' : roots['Soft & Spongy'],
                    'second' : smooth
                }
            else:
                raise Exception('fiend type not recognized: ' + str(type))

    def generate(self, gender, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(self.list['first'])
            if (isinstance(self.list['second'], dict)):
                if (gender.lower() == 'male'):
                    name += pick_random(self.list['second']['Male'])
                elif (gender.lower() == 'female'):
                    name += pick_random(self.list['second']['Female'])
                else:
                    raise Exception('gender not recognized: ' + str(gender))
            elif (self.list['second']):
                vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                second = pick_random(self.list['second'])
                if (name[-1] not in vowels and second[0] not in vowels):
                    glue = ['u', 'u', 'u', 'o', 'o', 'i', 'i', 'a', 'a', 'e']
                    name += pick_random(glue) + second
                elif (name[-1] in vowels and second[0] in vowels):
                    glue = ['z', 'y', 'v', 'r', 'l', 'j']
                    name += pick_random(glue) + second
                else:
                    name += second

            name = name.title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names

class AngelGenerator:

    def __init__(self, duplicate_limit=20):
        self.duplicate_limit = duplicate_limit
        path = os.path.join('Names', 'Fantasy', 'Angelic.json')
        with open(path) as f:
            self.list = json.load(f)

    def generate(self, gender, amount=10):
        names = []
        i = 0
        while (len(names) < amount and i < self.duplicate_limit):
            name = pick_random(self.list['Prefix'])
            if (gender.lower() == 'male'):
                ending = pick_random(self.list['Suffix']['Male'])
                if (name[-2:] == ending[-2:]):
                    title = pick_random(self.list['Titles'])
                    name = title + name
                else:
                    name += ending
            elif (gender.lower() == 'female'):
                ending = pick_random(self.list['Suffix']['Female'])
                if (name[-2:].replace('a', 'e') == ending[-2:]):
                    title = pick_random(self.list['Titles'])
                    name = title + name
                else:
                    name += ending

            name = name.title()
            if name in names:
                i += 1
            else:
                names.append(name)
        return names


class StochasticAnalyzer:

    #TODO: make this behave with names containing spaces (e.g. first + last)

    def __init__(self, list):
        self.list = list
        (self.mean_length, self.stdev_length) = self.get_length_distribution()
        self.window_size = int(self.mean_length / 2)
        if (self.window_size < 2):
            self.window_size = 2

        self.counts = self.get_counts(self.list)
        self.probabilities = self.get_probabilities()
        self.thresholds = self.get_thresholds()

    def get_counts(self, list):
        counts = {
            'start' : {},
            'middle' : {},
            'end' : {}
        }

        for name in list:
            #for name_element in name.split():
            for i in range(len(name) - self.window_size + 1):
                element = name[i:i+self.window_size]
                starting_letter = element[0]
                if i == 0:
                    if element in counts['start'].keys():
                        counts['start'][element] += 1
                    else:
                        counts['start'][element] = 1
                elif i == len(name) - self.window_size:
                    if starting_letter not in counts['end'].keys():
                        counts['end'][starting_letter] = {}
                        counts['end'][starting_letter][element] = 1
                    else:
                        if element in counts['end'][starting_letter].keys():
                            counts['end'][starting_letter][element] += 1
                        else:
                            counts['end'][starting_letter][element] = 1
                else:
                    if starting_letter not in counts['middle'].keys():
                        counts['middle'][starting_letter] = {}
                        counts['middle'][starting_letter][element] = 1
                    else:
                        if element in counts['middle'][starting_letter].keys():
                            counts['middle'][starting_letter][element] += 1
                        else:
                            counts['middle'][starting_letter][element] = 1
        return counts

    def get_probabilities(self):
        counts = self.counts

        # Starting element probabilities:
        start_total = sum([count for count in counts['start'].values()])
        for (element, count) in counts['start'].items():
            counts['start'][element] = count / start_total

        # Middle element probabilities:
        for (letter, elements) in counts['middle'].items():
            total = sum([c for c in elements.values()])
            for (element, count) in elements.items():
                elements[element] = count / total

        # Ending element probabilities:
        for (letter, elements) in counts['end'].items():
            total = sum([c for c in elements.values()])
            for (element, count) in elements.items():
                elements[element] = count / total
        return counts

    def get_thresholds(self):
        probs = self.probabilities

        # Starting element thresholds:
        start_threshold = 0
        for (element, probability) in probs['start'].items():
            start_threshold += probability
            probs['start'][element] = start_threshold

        # Middle element thresholds:
        for (letter, elements) in probs['middle'].items():
            threshold = 0
            for (element, probability) in elements.items():
                threshold += probability
                elements[element] = threshold

        # Ending element thresholds:
        for (letter, elements) in probs['end'].items():
            threshold = 0
            for (element, probability) in elements.items():
                threshold += probability
                elements[element] = threshold
        return probs

    def get_length_distribution(self):
        lengths = [len(name) for name in self.list]
        mean = statistics.mean(lengths)
        stdev = statistics.stdev(lengths)
        return (mean, stdev)

    def get_length(self):
        length = int(random.gauss(self.mean_length, self.stdev_length))
        return length

    def print_matrix(self, matrix):
        # Print starting elements:
        print('start:')
        for (element, value) in matrix['start'].items():
            print('\t' + element + '\t' + str(value))

        print('middle:')
        for (letter, elements) in matrix['middle'].items():
            print('\t' + letter)
            for (element, value) in elements.items():
                print('\t\t' + element + '\t' + str(value))

        print('end:')
        for (letter, elements) in matrix['end'].items():
            print('\t' + letter)
            for (element, value) in elements.items():
                print('\t\t' + element + '\t' + str(value))

    def construct_name(self, elements=False):
        thresholds = self.thresholds
        length = self.get_length()

        r = random.random()
        name = ''
        chosen_elements = []
        # Get random start:
        for (element, thresh) in thresholds['start'].items():
            if (r < thresh):
                name += element
                chosen_elements.append(element)
                break

        # Build middle:
        while (len(name) < length - (self.window_size - 1)):
            last_char = name[-1]
            r = random.random()
            if last_char in thresholds['middle'].keys():
                for (element, thresh) in thresholds['middle'][last_char].items():
                    if (r < thresh):
                        name += element[1:]
                        chosen_elements.append(element)
                        break
            else:
                all_elements = []
                for elements in thresholds['middle'].values():
                    all_elements += elements.keys()
                element = pick_random(all_elements)
                name += element
                chosen_elements.append(element)

        # Get random ending:
        last_char = name[-1]
        # if last character not in recorded endings, append one that is
        while (last_char not in thresholds['end'].keys()):
            r = random.random()
            if last_char in thresholds['end'].keys():
                for (element, thresh) in thresholds['middle'][last_char].items():
                    if (r < thresh):
                        name += element[1:]
                        chosen_elements.append(element)
                        break
            else:
                all_endings = []
                for elements in thresholds['end'].values():
                    all_endings += elements.keys()
                element = pick_random(all_endings)
                name += element
                chosen_elements.append(element)
            last_char = name[-1]

        r = random.random()
        for (element, thresh) in thresholds['end'][last_char].items():
            if (r < thresh):
                name += element[1:]
                chosen_elements.append(element)
                break

        while (not self.is_grammatical(name)):
            (name, chosen_elements) = self.construct_name(elements=True)
        if elements:
            return (name, chosen_elements)
        return name

    def is_grammatical(self, name):
        vowels = ['a', 'à', 'á', 'â', 'ã', 'ä',
                  'e', 'è', 'é', 'ê', 'ë',
                  'i', 'ì', 'í', 'î', 'ï',
                  'o', 'ò', 'ó', 'ô', 'õ', 'ö',
                  'u', 'ù', 'ú', 'û', 'ü',
                  'y', 'ý', 'ÿ']
        consecutive_consonants = 0
        for char in name:
            if char.lower() not in vowels:
                consecutive_consonants += 1
            else:
                consecutive_consonants = 0
            if (consecutive_consonants == 3):
                return False
        return True

    def score_name(self, name_elements):
        start = name_elements[0]
        end = name_elements[-1]

        start_prob = self.probabilities['start'][start]
        end_prob = self.probabilities['end'][end[0]][end]
        middle_probs = [self.probabilities['middle'][e[0]][e] for e in name_elements[1:-1]]
        return sum([start_prob, *middle_probs, end_prob]) / len(name_elements)


if __name__ == '__main__':
    #sources = source_map()['Historical'].keys()

    '''
    g = Generator('Italian')
    list1 = g.generate('male', sys.maxsize, 'personal')
    list2 = g.generate('male', sys.maxsize, 'family')
    a1 = StochasticAnalyzer(list1)
    a2 = StochasticAnalyzer(list2)
    name = ' '.join([a1.construct_name(), a2.construct_name()])
    print(name)
    '''

    default_id = 'Arkaden#6050'
    arguments = sys.argv[1:]
    if (len(arguments) < 3):
        print('Need at least 3 arguments:')
        print()
        print('python namegen.py <source_list> <gender> <amount>')
        print()
        print('<source_list> (str): source list to use (from Names/)')
        print('<gender> (str): gender for which to generate names')
        print('<amount> (int): amount of names to generate')
        print()
        print('Further arguments are passed directly to Generator.generate')
    elif (str(arguments[0]) == 'alias'):
        name = arguments[1]
        value = arguments[2]
        add_alias(default_id, name, value)
    else:
        source_list = str(arguments[0])
        gender = str(arguments[1])
        amount = int(arguments[2])

        g = Generator(default_id, source_list)
        names = g.generate(gender, amount, *arguments[3:])

        for name in names:
            print(name)
