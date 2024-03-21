from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
import datetime
import pytz

import jobs
import kiit
import openaiprompt


def main():
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f"Hello . Welcome to KIIT HELP . Enter /help to explore accepted commands .")

    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        help_message = f"You can access the features using the following commands:\n\n"
        help_message = help_message + f"1. /start : Starts the bot .\n"
        help_message = help_message + f"2. /help : Help Command. \n"
        help_message = help_message + f"3. /get_timetable: Access Personalized Time Table.\n"
        help_message = help_message + f"4. /chat : Enter Command followed by prompt to get any help . Ex : /chat Describe Bhubaneshwar. \n"
        help_message = help_message + f"5. /job : Enter Command followed by Job Title . Ex: /job Web Developer. \n"
        await update.message.reply_text(help_message)

    async def get_timetable(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        get_timetable_message = f"To get your today's Time table , \nEnter : /timetable <your roll number>. \n\n"
        get_timetable_message = get_timetable_message + f"For example your roll number is 21052142 . Your message should be /timetable 21052142 . \n"
        await update.message.reply_text(get_timetable_message)

    async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        roll = int(context.args[0])
        finalString = kiit.result(roll)
        await update.message.reply_text(finalString)

    async def job(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        title = " ".join(context.args)
        final =jobs.jobSearch(title)
        finalString1 = final[0]
        finalString2 = final[1]
        finalString3 = final[2]
        await update.message.reply_text(finalString1)
        await update.message.reply_text(finalString2)
        await update.message.reply_text(finalString3)




    async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        prompt = " ".join(context.args)
        generated_query = openaiprompt.generate_text(prompt)
        await update.message.reply_text(generated_query)

    app = ApplicationBuilder().token("KEY").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("get_timetable", get_timetable))
    app.add_handler(CommandHandler("timetable", timetable))
    app.add_handler(CommandHandler("chat", chat))
    app.add_handler(CommandHandler("job", job))

    app.run_polling()


if __name__ == "__main__":
    main()
