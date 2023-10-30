import dominate
from dominate.tags import *


def createPlayerPage(player):
    doc = dominate.document(title='Player Page: '+player.username)

    with doc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')

        with div():
            attr(cls='body')
            with doc:
                with div(id='user'):
                    h1(player.username)
                with div(id='gamesPlayed').add(ol()):
                        li("Total games played:" +str(player.totalGames()))
                        li("Total zerg games played: " +str(player.zergGames))
                        li("Total Protoss Games Played: "+ str(player.protossGames))
                        li("Total Terran Games Played: "+ str(player.terranGames))            

                with div(id='buildOrders'):
                     for race in ['zerg', 'protoss', 'terran']:
                        for buildOrder in player.buildOrders[race]:
                            h3(buildOrder + " - " + str(player.buildOrders[race][buildOrder]['percent']) +"%")
                            replays = player.buildOrders[race][buildOrder]['replays']
                            with div(id='replays').add(ol()):
                                for replay in replays:
                                    replayName = replay.strip('.rep')
                                    li(a(replayName, href='https://repmastered.app/game/'+replayName))

    with open("output/players/"+player.username+".html", "w") as text_file:
        text_file.write(doc.render())