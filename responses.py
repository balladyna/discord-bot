import messages
from harvester import *

URL = 'https://pl.wikiquote.org/wiki/Specjalna:Losowa_strona'


def handle_response(user_message) -> str:
    p_message = user_message.lower()

    if p_message == 'hej':
        return messages.greetings
    elif p_message == '!cytat':
        return get_reply()
    elif p_message == '!życie':
        return messages.special_message
    elif p_message == '!help':
        return messages.help_message
    return messages.unknown_command


def get_reply():
    url = Harvester(URL)
    return Harvester.get_quote(url)
