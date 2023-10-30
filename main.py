import time
from analyzer import *
from crawler import *
from html_exporter import *

run2v2Crawler(players=["progamermatt"])
players = analyzeReplays()

for playerName, player in players.items():
    player.buildUsageStats()
    createPlayerPage(player)


