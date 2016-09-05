import spotipy
import spotipy.util as util

class scraper:

    def __init__(self):
        self.interface = spotipy.Spotify()
        self.is_config = False

    def config_user(self, my_username, my_scope, my_client_id, my_client_secret):
        token = util.prompt_for_user_token(my_username, my_scope, my_client_id, my_client_secret, "http://www.megsradio.fm")
        if token:
            self.interface = spotipy.Spotify(auth=token)
            self.is_config = True
        else:
            raise Exception("Invalid user conf!")

    def get_featured_playlists(self):
        playlists = self.interface.featured_playlists()
        for list in playlists:
            print(list)