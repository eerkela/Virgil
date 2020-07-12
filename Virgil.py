import json
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from tabulate import tabulate

import namegen


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

def format_list(list, max_length=10):
    columns = []
    for i in range(0, len(list), max_length):
        columns.append(list[i:i+max_length])

    rows = []
    for i in range(len(columns[0])):
        row = []
        for c in columns:
            try:
                row.append(c[i])
            except:
                row.append('')
        rows.append(row)

    table = '```' + tabulate(rows, tablefmt='plain') + '```'
    return table


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def help(ctx, *requests):
    id = str(ctx.guild)
    if (id == 'None'):
        id = str(ctx.author)

    embed = discord.Embed(title='Help', type='rich')
    source_map = namegen.source_map()
    sources = []
    for k in source_map['Historical'].keys():
        sources.append(k)
    for k in source_map['Fantasy'].keys():
        sources.append(k)

    if ('names' in requests):
        helpstring = '''```!names <source> <gender> <amount> [options]```
        **Where:**
        <source> = one of the available sources from !list sources
        <gender> = male, female, or (if left blank) both
        <amount> = integer > 0. Responses are limited to 1024 characters
        [options] = an space-separated list of options to be supplied to the name generator

        **Notes:**
        To get a list of available sources, use:
        ```!list sources```Multiple sources can be selected at once by joining them with '+', e.g.:
        ```!names French+German+English+... male 10 [options]```For a list of valid options for a given name source, use:
        ```!help <source>```

        **Description Names:**
        Rather than using an established name source like above, you can also select the "Description" source instead.  This source, rather than building a name from a predetermined list like the others, allows you to build your own by combining syllables with a particular emotional tone.  This method works particularly well for monsters, where you can mix and match syllables to represent a particular origin/creature type.  A soft+smooth name might work particularly well for an ooze, for example, or a harsh+sharp name for a devil, etc.

        To generate a description name, use the following command structure:
        ```!names Description [descriptors] <amount>```Descriptors, like sources above, must be separated by '+' characters, with the order corresponding to the order elements will appear in the generated names.  To get a list of available descriptors, use:
        ```!list descriptors```
        '''
        embed.description = helpstring
    elif ('list' in requests):
        helpstring = '''```!list sources```Lists all available standard name sources for use with Virgil
        ```!list descriptors```Lists all descriptors that can be used with !names Description
        ```!list aliases```Lists all custom aliases and their values that are associated with this server
        '''
        embed.description = helpstring
    elif ('alias' in requests):
        helpstring = '''```!alias <operation> <alias_name> <value>```Where:
        <operation> = add | remove | list
        <alias_name> = name of alias on storage
        <value> = expanded value of alias

        **Usage:**
        Aliasing allows you to define custom names for source lists that are unique to your world.  Think of them as a shorthand way to refer to an expanded value.  For instance, I can use the following command to add an alias called 'Morn' to my world:
        ```!alias add Morn French+German+Dutch```From then onwards, I can use the keyword 'Morn' in place of a default source, and Virgil will expand it into its lengthened form ('French+German+Dutch') during interpretation.  As such, running the following command,
        ```!names Morn female 10```will return a list of 10 female names that are randomly selected from the French, German, and Dutch name lists.  This behavior is very useful for defining regions within your individual fantasy world, which may draw upon several different historical or fantastic name sources at once.  Aliases can additionally be appended together using the '+' operator just like default sources.

        **Updating Aliases:**
        If I were to decide that I wanted the 'Morn' alias to point to a different list of sources than French+German+Dutch, I would call the add command once more with my preferred value:
        ```!alias add Morn Italian+Spanish+Greek```The 'Morn' alias will now point to the Italian, Spanish, and Greek name lists instead of French, German, and Dutch.

        **Removing aliases:**
        To remove an alias, run the following command:
        ```!alias remove <alias_name>```
        **Listing aliases:**
        To receive a list of all current aliases and their values, use the following command:
        ```!list aliases```
        '''
        embed.description = helpstring
    elif any([s in sources for s in requests]):
        helpstring = '''In order to use any of the following otions, no field in the following formula can be left blank:
        ```!names <source> <gender> <amount> [your_options]```
        If this is not done first, the chosen option will be interpreted as one of the required fields, and name generation will fail.

        You can use multiple options at once by separating them with spaces.
        '''
        embed.description = helpstring
        for s in sources:
            if (s in requests):
                g = namegen.Generator(id, s)
                options = g.valid_args()
                matrix = [[k, v] for (k, v) in options.items()]
                helpstring = '```' + tabulate(matrix, tablefmt='plain') + '```'
                if (helpstring == '``````'):
                    helpstring = 'None'
                embed.add_field(name=s + ' Options',
                                value=helpstring,
                                inline=False)
    else:
        helpstring = '''Virgil is a random name generator that allows players and game masters to quickly and easily generate names from a wide variety of sources, both fantasy and historical.  Names can be mixed and matched as desired by appending multiple lists, and custom aliases can be saved in order to store namelists that are unique to your world.

        **General Use:**
        ```!names <source> <gender> <amount> [options]```Where:
        <source> = one of the sources from !list sources
        <gender> = male, female, or, (if left blank), both
        <amount> = integer > 0, number of names to generate

        **Description Names:**
        ```!names Description <descriptors> <amount>```Where:
        <descriptors> = a + separated list of descriptors (!list descriptors)
        <amount> = integer > 0, number of names to generate

        For more information on general use and description names, see:
        ```!help names```
        **Custom Aliases:**
        ```!alias <operation> <alias_name> <value>```Where:
        <operation> = add | remove | list
        <alias_name> = name of alias on storage
        <value> = expanded value of alias

        For more information on aliases and their use, see:
        ```!help alias```
        '''
        embed.description = helpstring

    await ctx.send(embed=embed)


@bot.command()
async def names(ctx, source: str, gender: str = '', amount: int = 10, *args):
    id = str(ctx.guild)
    if (id == 'None'):
        id = str(ctx.author)
    g = namegen.Generator(id, source.title())

    names = {}
    if (not gender):
        names['Male'] = g.generate('male', amount, *args)
        names['Female'] = g.generate('female', amount, *args)
    else:
        names[gender.title()] = g.generate(gender.lower(), amount, *args)

    title = ' '.join([source.title(), 'Names'])
    response = discord.Embed(title=title, type='rich')
    for (k, v) in names.items():
        response.add_field(name=k, value='\n'.join(v))
    await ctx.send(embed=response)


@bot.command()
async def list(ctx, specifier: str):
    id = str(ctx.guild)
    if (id == 'None'):
        id = str(ctx.author)

    if (specifier.lower() == 'sources'):
        custom_sources = sorted(namegen.get_aliases(id).keys())
        custom_values = format_list(custom_sources, 10)

        historical_sources = sorted(namegen.source_map()['Historical'].keys())
        historical_values = format_list(historical_sources, 30)

        fantasy_sources = sorted(namegen.source_map()['Fantasy'].keys())
        fantasy_values = format_list(fantasy_sources, 10)

        description = '**Historical**\n' + historical_values \
                    + '\n**Fantasy**\n' + fantasy_values \
                    + '\n**Custom**\n' + custom_values

        response = discord.Embed(title='Available Name Sources',
                                 type='rich',
                                 description=description)
        await ctx.send(embed=response)
    elif (specifier.lower() == 'descriptors'):
        g = namegen.SyllabicGenerator()
        descriptors = g.get_descriptors()
        description = '**Standard**\n' + format_list(descriptors['Standard']) \
                    + '\n**Animals**\n' + format_list(descriptors['Animal'])

        response = discord.Embed(title='Available Descriptors',
                                 type='rich',
                                 description=description)
        await ctx.send(embed=response)
    elif (specifier.lower() == 'aliases'):
        aliases = namegen.get_aliases(id)

        embed = discord.Embed(title='Custom Aliases', type='rich')
        matrix = [[k, v] for (k, v) in sorted(aliases.items())]
        table = '```' + tabulate(matrix, headers=['Name', 'Value']) + '```'
        embed.description = table
        await ctx.send(embed=embed)
    else:
        raise Exception('list specifier not recognized: ' + str(specifier))


@bot.command()
async def alias(ctx, operation: str, *args):
    id = str(ctx.guild)
    if (id == 'None'):
        id = str(ctx.author)

    if (operation.lower() == 'add'):
        if (len(args) < 2):
            raise Exception('at least 1 field missing from alias, see \
                             !help alias for more information')
        matrix = []
        for i in range(0, len(args), 2):
            name = str(args[i]).title()
            value = str(args[i+1]).title()
            namegen.add_alias(id, name, value)
            matrix.append([name, value, '✓'])

        embed = discord.Embed(title='Alias Added', type='rich')
        table = '```' + tabulate(matrix, headers=['Name', 'Value', '']) + '```'
        embed.description = table
        await ctx.send(embed=embed)
    elif (operation.lower() == 'remove'):
        if (len(args) < 1):
            raise Exception('must give name of alias to remove, see !help \
                             alias for more information')
        matrix = []
        for name in args:
            name = str(name).title()
            namegen.remove_alias(id, name)
            matrix.append([name, '✗'])

        embed = discord.Embed(title='Alias Removed', type='rich')
        table = '```' + tabulate(matrix, headers=['Name', '']) + '```'
        embed.description = table
        await ctx.send(embed=embed)
    else:
        raise Exception('invalid operation: ' + str(operation) + '\nsee !help \
                         alias for more information')



bot.run(TOKEN)
