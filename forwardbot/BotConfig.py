from os import environ
class Config(object):
    API_ID = "17760593"
    API_HASH = "5427e1cec6e213dc3f9b4123a2f59d64"
    BOT_TOKEN = "5007386358:AAF-PxQr4ipnri83EtMucIHXiFF4i71ZskM"
    STRING_SESSION = "1AZWarzoBuxT1R4SV-_aY2eEV5tlSLxKQ03BOObHNk6eZSKQ04tT2P49ojnD69BSAVQRTB-BDajxKkMbcko_xUgPChp9PUi0AqHprTlBUN4MKTVqKu3lfVOZRxF4GMq4SO1Z7HJ3SaBvCXGdvsiCt1875iQI7vBzxmNdOQaWJXHo4CH9Nby71ce0lKQDiOgCO9bIp3yR7Kx5LSJSo57vO7kCMlgXUMqfep2pFn5cGzknz3A9yzOQbyQkvFjCv2ScMYhl1EwTzE3tjMuxECQG0h81sAt5MoxODxWtQzmXE6cwNeHpCFa3o6PW0GaOja9UYJ2U8F_yMJSR2HhXk4oEebjA9hjoa6BA="
    SUDO_USERS = "5002918737"
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
