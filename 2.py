# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import os
import sys
from chatterbot.conversation import Statement, Response
from chatterbot.utils import print_progress_bar

bot = ChatBot(
    "Kenzo",
    read_only = True,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

print("HI. I'm Kenzo.")

while True:
    try:
        bot_input = bot.get_response(None)
    # Type clear and enter to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

print("How can I help you?")