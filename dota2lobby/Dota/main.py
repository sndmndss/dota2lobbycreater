from steam.client import SteamClient
from dota2.client import Dota2Client

#client = steam operations, dota = dota client operations
client = SteamClient()
dota = Dota2Client(client)

#starts dota client
@client.on('logged_on')
def start_dota():
    dota.launch()

#creates lobby and make bot join spec
@dota.on('ready')
def create_practice_lobby():
    dota.destroy_lobby()
    dota.wait_event(dota.create_practice_lobby(password='5454',
                               options=dict(game_name='test', pass_key='5454', server_region=5, game_mode=2, pause_setting=0,)))
    dota.wait_event(dota.join_practice_lobby_broadcast_channel(channel=1))
    dota.sleep(20)
    dota.destroy_lobby()



def init():
    dota.on('ready',create_practice_lobby)
    client.cli_login()
    client.run_forever()