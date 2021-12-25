from os import environ
class Config(object):
    API_ID = "15086115"
    API_HASH = "5ad000f8ad2b24dabda4d8ffb912c688"
    BOT_TOKEN = "5069286089:AAF46kj7Drxp8B0GnfXhvuEQ-5rZNn_Oq8s"
    STRING_SESSION = "1AZWarzkBu6Ab8txZ3qxNx3HsNfapXMJBQroA3h48fJsyTM3MCunSjiWywgCunLt4mXPE0_3cz3jGgRm1FEQ8y7ieEWggHEJIX7acQ6yi-5DsvJrntlHojc92jp0qHvuD_1ijp6Mv7K5a87aaxfw8XxsKduwgJgrTAZkE4RaEtDydGp8fY4v2InFmAkxGrVy9i10HbONdSIf7vDPxeYByAG7UIskUCmXXX_AmiYhqN6JU-J2f9p_Fw_S2HyzZs5MomT2TSPCy7r3-YyP2kV_yjDpyh8bNBTVG9pPWJVX_CqiLvd-3QSt4toAezYH7-WzkhQDonihnVjkswXEPTz_ykfJmXhv39N4="
    SUDO_USERS = "5040791858"
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
