from asyncio.tasks import wait
from io import BufferedIOBase
from os import name
from sys import prefix
from turtle import color
import discord
from discord import colour
from discord import emoji
from discord import message
from discord import member
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
import json
from pixqrcode import PixQrCode
from validators import url

with open("config.json") as e:
    infos = json.load(e)
    TOKEN = infos["token"]
    prefixo2 = infos["prefix"]
    owner = infos["owenerbot"]
    ticket = infos["ticketid"]
    img = infos["authorimage"]
    logcanal = infos["log"]
    logpunicao = infos["logpunicao"]
    entrou = infos["entrada"]
    saida = infos["saida"]
    estrela = infos["estrela"]
    adm = infos["adm"]
    menage = infos["menage"]
    mod = infos["mod"]
    estrela = infos["estrela"]
    ceo = infos["ceo"]


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefixo2, case_insensitive=True, intents=intents)


@client.event
async def on_ready():

    await client.change_presence(
        status=discord.Status.dnd, activity=discord.Game('dev by "Porto#4255')
    )

    print("Name of the bot: ", client.user.name)
    print("bot user id: ", client.user.id)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
      return
    msg_content = message.content.lower()

    links = ['https://', '.com', 'discord.gg']

    if any(word in msg_content for word in links):
        await message.delete()
        await message.channel.send("Não pode enviar links aqui não zé!")

    await client.process_commands(message)

@client.event
async def on_member_join(member):
    rank = discord.utils.get(member.guild.roles, name= "Roça Evolved 2022")  # name do cargo
    rank2 = discord.utils.get(member.guild.roles, name="・Liberação")  # name do cargo
    entroulog = client.get_channel(entrou)
    embed2 = discord.Embed(
        title = "Entrou no sv",
        description= "Bem Vindo <@!{}>".format(member.id)
    ) 
    embed2.set_image(url = member.avatar_url)
    await entroulog.send(embed = embed2)
    await member.add_roles(rank,rank2)



@client.event
async def on_member_remove(member):
    saidalog = client.get_channel(saida)
    embed = discord.Embed(
        title = "Saiu do sv",
        description="<@!{}> saiu do servidor".format(member.id))
    await saidalog.send(embed = embed)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
      return
    msg_content = message.content.lower()

    bots = [f'<@!{client.user.id}>']

    if any(word in msg_content for word in bots):
        await message.delete()
        await message.channel.send(f"meu prefixo e {prefixo2}")

    await client.process_commands(message)


@client.command()
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def ajudastaff(ctx):
    embed = discord.Embed(
        title="Comandos staff",
        description="{0}anuncio \n {0}say \n {0}kick \n {0}ban \n {0}clear ".format(prefixo2),
    )

    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command(name="staff")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def comando_staff(ctx):
        embed1 = discord.Embed(
            title="ajuda staff",
            description="Aqui você pode pedir ajuda ao <@!{}>".format(owner),
        )
        embed1.set_author(name="Porto", icon_url=img)
        await ctx.send(embed=embed1)
        await ctx.message.delete()


@client.command(name="kick")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def kick(ctx, membro: discord.Member, *, motivo=None):
        embed1 = discord.Embed(
            title = "Punições",
            description = f'Quem kickou{ctx.author.mention} \membro kickado: {membro.mention} \nMotivo do kick: **{motivo}**'
        )
        canal = client.get_channel(id=logpunicao)
        await canal.send(embed = embed1)
        await membro.kick()
        await ctx.message.delete()


@client.command(name = "ban")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def ban(ctx, membro : discord.Member, *, motivo=None):
        embed1 = discord.Embed(
            title = "Punições",
            description = f'Quem baniu{ctx.author.mention} \nbanido: {membro.mention} \nMotivo do ban: **{motivo}**'
        )
        canal = client.get_channel(id=logpunicao)
        await canal.send(embed = embed1)
        await membro.ban()
        await ctx.message.delete()


@client.command(name="clear")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        embedclear = discord.Embed(
            title="Log apagou mensagens",
            description=f"{ctx.author.mention} apagou {amount} mensagens no canal <#{ctx.channel.id}>",
        )
        canalembed = client.get_channel(id=logcanal)
        await canalembed.send(embed=embedclear)


@client.command(name="say")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def say(ctx, *, arg):
        argss = arg
        msgg = argss
        embedsay = discord.Embed(
            title="Log say",
            description=f"{ctx.author.mention} usou o comando say no <#{ctx.channel.id}>\n\nescreveu: **{arg}**",
        )
        canalembed = client.get_channel(id=logcanal)
        await canalembed.send(embed=embedsay)
        await ctx.send(msgg)
        await ctx.message.delete()


@client.command(name="anuncio")
@commands.has_any_role(ceo,mod,estrela,adm,menage)
async def anuncio(ctx, *, args):
        embedanun = discord.Embed(
                title="Anuncio",
                description=f"**{args}**",
            )
        embedanun.set_image(url ='https://cdn.discordapp.com/icons/838317146512687124/926457e72e222d8cd69120029fa88c56.png?size=2048')
        await ctx.send("@everyone", embed=embedanun)
        await ctx.message.delete()

@client.command(name = "avatar")
async def avatar(ctx, member : discord.Member = None):
            if member is None:
                embed = discord.Embed(title="Marque uma pessoa exemplo: ```{prefixo2}avatar [member]```", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            else:
                embed2 = discord.Embed(title=f"{member}'s Avatar! ", colour=0x0000ff, timestamp=ctx.message.created_at, 
                description = f"comando executado por {ctx.author.mention}"
                )
                msglog = f"comando {prefixo2}avatar {member} foi executado pelo{ctx.author.mention} no canal <#{ctx.channel.id}>"
                embed2.set_image(url=member.avatar_url)
                await ctx.send(embed=embed2)
                logg = client.get_channel(id=logcanal)
                await logg.send(msglog)
""" @client.command(name = "pix")
async def pix(ctx,*,args):
    nome = "ARTHUR PORTO CAMBOA" 
    telefone = "XXXXXXXXX"
    cidade = "SAO PAULO"
    valor = args
    pix = PixQrCode(nome,telefone,cidade,valor)
    await ctx.send(pix.export_base64()) """
     

""" @client.command(name = "serverinfo")
async def serverinfo(ctx):
    embed = discord.Embed(title = "Informações do server", color =12092939)
    embed.add_file(name = "Nome do server", value= ctx.message.guild.name, inline=True)
    embed.add_file(name = "Membros", value=len(ctx.message.guild.members))
    await ctx.send(embed = embed) """

client.run(TOKEN)
