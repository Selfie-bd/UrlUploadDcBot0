import logging
import math
import os
import time


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    chat_id = self._mess.chat.id
    mes_id = self._mess.message_id
    from_user = self._from_user
    now = time.time()
    diff = now - start
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Cancel 🚫",
                    callback_data=(
                        f"gUPcancel/{chat_id}/{mes_id}/{from_user}"
                    ).encode("UTF-8"),
                )
            ]
        ]
    )
    
        if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "<b>╭────── ⌊__UploadinG: 〘{2}%〙 📤__⌉</b>\n│ \n<b>├〖{0}{1}〗</b>\n".format(
            ''.join(["▣" for i in range(math.floor(percentage / 10))]),
            ''.join(["□" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress +"│" + "\n**├Total 📀:**   〘<code>{1}</code>〙\n**├Done ✓ :** 〘<code>{0}</code>〙\n**├Speed** 🚀 :  〘<code>{2}/s</code>〙\n**├ETA** ⏳ :  〘<code>{3}</code>〙\n**│**\n**╰── ⌊ @All_Movie_Rockers ⌉**".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n{}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
