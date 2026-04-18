from lib.track import *

""" When the track is instantiated, it should be given a name """

def test_track_title_on_instantiation():
    track = Track("Waterloo", "ABBA")
    assert track.title == "Waterloo - ABBA", "should return 'Waterloo - ABBA'"