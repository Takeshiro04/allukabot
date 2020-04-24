import html
import random
import time
from typing import List
from alluka import dispatcher, OWNER_ID, DEV_USERS, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS
from telegram import Bot, Update, ParseMode
from telegram.ext import CommandHandler, run_async
import alluka.modules.fun_strings as fun_strings
from alluka import dispatcher
from alluka.modules.disable import DisableAbleCommandHandler
from alluka.modules.helper_funcs.chat_status import is_user_admin
from alluka.modules.helper_funcs.extraction import extract_user
from alluka.modules.helper_funcs.chat_status import user_admin, sudo_plus
from alluka.modules.log_channel import loggable



@run_async
def runs(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


@run_async
def slap(bot: Bot, update: Update, args: List[str]):

    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_ALLUKA_TEMPLATES)
         

        if type(temp) == list:
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):

                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(chat.id, message.from_user.id, until_date=mutetime, can_send_messages=False)
                
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)



@run_async
def roll(bot: Bot, update: Update):
    update.message.reply_text(random.choice(range(1, 7)))


@run_async
def toss(bot: Bot, update: Update):
    update.message.reply_text(random.choice(fun_strings.TOSS))

@run_async
@sudo_plus
def insult(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.ALLUKA_INSULT))

@run_async
@sudo_plus
def abuse(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.ABUSE_STRINGS),parse_mode=ParseMode.MARKDOWN)

@run_async
@sudo_plus
def gay(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.GAY),parse_mode=ParseMode.MARKDOWN)

@run_async
@sudo_plus
def rape(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.RAPE_STRINGS),parse_mode=ParseMode.MARKDOWN)

@run_async
def pro(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.PRO_STRINGS),parse_mode=ParseMode.MARKDOWN)

@run_async
@sudo_plus
def send(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    message = update.effective_message
    text = message.text[len('/send '):]
    reply_text(text,parse_mode=ParseMode.MARKDOWN)
    message.delete()

@run_async
def shrug(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(r"¯\_(ツ)_/¯")


@run_async
def bluetext(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS")


@run_async
def rlg(bot: Bot, update: Update):

    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)
    
    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    
    update.message.reply_text(repl)


@run_async
def decide(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))

    
@run_async
def table(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))


__help__ = """
 - /runs: reply a random string from an array of replies.
 - /slap: slap a user, or get slapped if not a reply.
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /toss : Tosses A coin
 - /abuse : Abuses the cunt
 - /bluetext : check urself :V
 - /roll : Roll a dice.
 - /rlg : Join ears,nose,mouth and create an emo ;-;
"""

RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
ABUSE_HANDLER = CommandHandler("abuse", abuse)
INSULT_HANDLER = CommandHandler("insult", insult)
GAY_HANDLER = CommandHandler("gay", gay)
PRO_HANDLER = DisableAbleCommandHandler("pro", pro)
SEND_HANDLER = DisableAbleCommandHandler("send", send)
RAPE_HANDLER = CommandHandler("rape", rape)


dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(INSULT_HANDLER)
dispatcher.add_handler(GAY_HANDLER)
dispatcher.add_handler(PRO_HANDLER)
dispatcher.add_handler(SEND_HANDLER)
dispatcher.add_handler(RAPE_HANDLER)

__mod_name__ = "Fun"
__command_list__ = ["runs", "slap", "roll", "toss", "shrug", "bluetext", "rlg", "decide", "table" , "abuse", "insult", "gay", "pro", "rape"]
__handlers__ = [RUNS_HANDLER, SLAP_HANDLER, ROLL_HANDLER, TOSS_HANDLER, SHRUG_HANDLER, BLUETEXT_HANDLER, RLG_HANDLER, DECIDE_HANDLER, TABLE_HANDLER,ABUSE_HANDLER,INSULT_HANDLER,GAY_HANDLER,PRO_HANDLER,RAPE_HANDLER]
