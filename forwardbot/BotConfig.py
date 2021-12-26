from os import environ
class Config(object):
    API_ID = "9821348"
    API_HASH = "c03b8a9b7724e7acd4635cf9e9a33b10"
    BOT_TOKEN = "5006516736:AAGhNGMsDKKoIl2hSnxiwsiNNiBl5IFSQnc"
    STRING_SESSION = "1AZWarzoBuydNVtKKs9YTgKuz2h4SDgq_dn53v2hKoFIjCi8_qZlGz4UvX6xC_ha-PUbWbWxn6lELikEV3QhA-eMPU6MS7hgFPAkxGpU30D3da18TnFfmRsnIydv-0ZPxx-auRNAdv5cQNhrZ2IgaCRhAonHCZuZHVBp5_Xk2iqzfbOqWD9xXS-9ty_oa3m-_NniYJj38akJD65Cypb6E8GdB330XevlaISzmJj4qSe-afZwFUPAXNa6EJun7wHpjsoIAcx4JqPPrmztvISs1QWNZNGblWrcpeRH66DjnIyEdoO5ts_SPyKFx26f8nJwLf5Pb-nsEWnJsi8TMidJGLqrwTuKEf1I="
    SUDO_USERS = "5051794395"
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
