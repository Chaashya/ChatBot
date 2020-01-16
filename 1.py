# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
#import logging
#logging.basicConfig(level=logging.INFO)

from chatterbot.response_selection import get_random_response
bot = ChatBot(
    "Kenzo",
    response_selection_method=get_random_response,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.LowConfidenceAdapter"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training1")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

print("Hey there! I'm Kenzo. How can I help you today?")

while True:
    try:
        bot_input = bot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break