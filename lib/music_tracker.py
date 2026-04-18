class MusicTracker():
    def __init__(self):
        self.playlist = []

    def add(self, Track):
        self.playlist.append(Track)

    def get_playlist(self):
        return [track.title for track in self.playlist]

    def remove(self, track):
        self.playlist = [song for song in self.playlist if song.title != track.title]
