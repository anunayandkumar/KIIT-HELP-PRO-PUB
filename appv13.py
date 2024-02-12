<<<<<<< HEAD
import telegram.ext
import json
import datetime
import pytz
import kiit

def main():
    TOKEN = "BOT TOKEN"

    def start(update, context):
        update.message.reply_text(f"Hello . Welcome to KIIT HELP . Enter /help to explore accepted commands .")

    def help(update, context):
        help_message = f"You can access the features using the following commands:\n\n"
        help_message = help_message + f"/start : Starts the bot .\n"
        help_message = help_message + f"/help : Help Command. \n"
        help_message = help_message + f"/get_timetable: Access Personalized Time Table. \n"
        update.message.reply_text(help_message)

    def get_timetable(update, context):
        get_timetable_message = f"To get your today's Time table , \nEnter : /timetable <your roll number>. \n\n"
        get_timetable_message = get_timetable_message + f"For example your roll number is 21052142 . Your message should be /timetable 21052142 . \n"
        update.message.reply_text(get_timetable_message)

    def timetable(update, context):
        roll = int(context.args[0])
        finalString = kiit.result(roll)
        update.message.reply_text(finalString)

    updater = telegram.ext.Updater(TOKEN, use_context=True)
    dispatch = updater.dispatcher

    dispatch.add_handler(telegram.ext.CommandHandler("start", start))
    dispatch.add_handler(telegram.ext.CommandHandler("help", help))
    dispatch.add_handler(telegram.ext.CommandHandler("get_timetable", get_timetable))
    dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()



=======
import telegram.ext
import json
import datetime
import pytz
import kiit

def main():
    TOKEN = "BOT TOKEN"

    def start(update, context):
        update.message.reply_text(f"Hello . Welcome to KIIT HELP . Enter /help to explore accepted commands .")

    def help(update, context):
        help_message = f"You can access the features using the following commands:\n\n"
        help_message = help_message + f"/start : Starts the bot .\n"
        help_message = help_message + f"/help : Help Command. \n"
        help_message = help_message + f"/get_timetable: Access Personalized Time Table. \n"
        update.message.reply_text(help_message)

    def get_timetable(update, context):
        get_timetable_message = f"To get your today's Time table , \nEnter : /timetable <your roll number>. \n\n"
        get_timetable_message = get_timetable_message + f"For example your roll number is 21052142 . Your message should be /timetable 21052142 . \n"
        update.message.reply_text(get_timetable_message)

    def timetable(update, context):
        roll = int(context.args[0])
        finalString = kiit.result(roll)
        update.message.reply_text(finalString)

    updater = telegram.ext.Updater(TOKEN, use_context=True)
    dispatch = updater.dispatcher

    dispatch.add_handler(telegram.ext.CommandHandler("start", start))
    dispatch.add_handler(telegram.ext.CommandHandler("help", help))
    dispatch.add_handler(telegram.ext.CommandHandler("get_timetable", get_timetable))
    dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()




