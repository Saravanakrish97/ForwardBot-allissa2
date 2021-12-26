from os import environ
class Config(object):
    API_ID = "12416481"
    API_HASH = "80f3fa70039ffda055dcf94fe97e75fb"
    BOT_TOKEN = "5009748966:AAH_7XseUnx8lfWx6e8wcw9dYmmQP6r4D14"
    STRING_SESSION = "1AZWarzoBu4fVfgme6Jwv06oYdbNH33fZjnpAcsXBqALDEUFochgSOyx4oobacuunDVNRJ9SXNYxOdqiCptsgwNmv2Y7Mqv9AjeX0iYt9inSBZ04bk15EvtMgCpWtdwU0DDSuAN_U1hVbFPvHGNaDxAlf1Eytw6M16nbA7OhIqDzWL9u1B465gMDJPRyWv3vfJVk1HA5iegbklQJ--WYSa86L3q52PrNs15NOGP4f1ueQGVwDdGXwiNRjGe2kOSareN3LwYEJ6Y0hIYgGkTSAMcG023l0UXjxlyOw91lgFFYiRVME-on2vIN_XtRwKo4YI-atrUF5alM8_mpJrtbcryLy6VkPwOg="
    SUDO_USERS = "5011421350"
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
