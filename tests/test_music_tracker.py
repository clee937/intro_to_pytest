from lib.music_tracker import *
from lib.track import *

""" When we initialise a new music tracker, the playlist should be empty """
def test_empty_playlist_on_initialisation():
    mt = MusicTracker()
    assert mt.playlist == []

""" When we add a track, it should be added to the playlist """
def test_that_a_track_can_be_added_to_music_player():
    mt = MusicTracker()
    mt.add(Track("Waterloo", "ABBA"))
    assert mt.get_playlist() == ["Waterloo - ABBA"]

""" We should be able to view a list of all the tracks in the playlist, using get_playlist() """
def test_that_all_tracks_can_be_listed():
    mt = MusicTracker()
    mt.add(Track("Waterloo", "ABBA"))
    mt.add(Track("Dancing Queen", "ABBA"))
    assert mt.get_playlist() == ["Waterloo - ABBA", "Dancing Queen - ABBA"], "Should return: ['Waterloo - ABBA', 'Dancing Queen - ABBA']" # --> ["Waterloo - ABBA", "Dancing Queen - ABBA"]

""" When there are no tracks in the playlist, an empty playlist should be returned when get_playlist() is called"""
def test_empty_list_is_returned_when_no_tracks_have_been_added():
    mt = MusicTracker()
    assert mt.get_playlist() == []

# """ When we remove a track, it should be removed from the playlist """
# def test_that_a_track_can_be_removed():
#     mt = MusicTracker()
#     mt.add(Track("Waterloo", "ABBA"))
#     mt.add(Track("Shape of You", "Ed Sheeran"))
#     mt.add(Track("Dancing Queen", "ABBA"))
#     mt.remove(Track("Dancing Queen", "ABBA"))
#     assert mt.get_playlist() == ["Waterloo - ABBA", "Shape of You - Ed Sheeran"], "Should return: ['Waterloo - ABBA', 'Shape of You - Ed Sheeran']" # --> ["Waterloo - ABBA", "Shape of You - Ed Sheeran"]
