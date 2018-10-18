import apb.config as config
import titlecase

class Base:
    _max_similar_tracks = config.read('general', 'max_similar_tracks')
    _max_top_tracks = config.read('general', 'max_top_tracks')
    _max_top_tags = config.read('general', 'max_top_tags')

    def __init__(self, artist=None, track=None):
        if artist and track:
            self.artist = titlecase(artist)
            self.track = titlecase(track)
            self.full_track = (self.artist, self.track)
            self.full_track_read = f'{self.artist} - {self.track}'
            self.track_url = None
            self.track_id = None
            self.similar_track_list = []
        elif artist and not track:
            self.artist = titlecase(artist)
            self.artist_id = None
            self.similar_artist_list = []

        self.tag_list = []
