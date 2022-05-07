import hikari
import lightbulb

bot = lightbulb.BotApp(token='OTcwOTk1ODM3NTMyNTEyMjU3.YnEEVw.SGFlwuP0G5b_etypvPjqPNV7SPc', default_enabled_guilds=(970995837532512257))

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Я работаю!")

@bot.command
@lightbulb.command('abra', 'kadabra')
@lightbulb.implements(lightbulb.SlashCommand)
async def abra(ctx):
    await ctx.respond('kadabra')

@bot.command
@lightbulb.command('ping', 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('pong')

@bot.command
@lightbulb.command('new', 'york')
@lightbulb.implements(lightbulb.SlashCommand)
async def new(ctx):
    await ctx.respond('york')

@bot.command
@lightbulb.command('life', 'is great')
@lightbulb.implements(lightbulb.SlashCommand)
async def life(ctx):
    await ctx.respond('is great')

@bot.command
@lightbulb.command('real', 'life')
@lightbulb.implements(lightbulb.SlashCommand)
async def real(ctx):
    await ctx.respond('life')

@bot.command
@lightbulb.command('yandex', 'lyceum')
@lightbulb.implements(lightbulb.SlashCommand)
async def yandex(ctx):
    await ctx.respond('lyceum')

@bot.command
@lightbulb.command('best', 'yandex')
@lightbulb.implements(lightbulb.SlashCommand)
async def best(ctx):
    await ctx.respond('yandex')


bot.run()