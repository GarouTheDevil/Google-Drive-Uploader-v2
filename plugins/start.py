from pyrogram import Client, Filters, StopPropagation,InlineKeyboardButton, InlineKeyboardMarkup
from bot.helper.check_channel import inChannel
from bot.helper.send_join import sendJoinmsg


@Client.on_message(Filters.command(["start"] ), group=-2)
async def start(client, message):
    
    joinButton=InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton("Report Bugs 😊", url="https://t.me/aryanvikash")],
        
        
        ])
        
        
    welcomemsg = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomemsg, reply_markup = joinButton)
    raise StopPropagation
