from pages.top_artists_page import TOP_ARTISTS

def test_artist(setup):
    A=TOP_ARTISTS(setup)
    A.click_on_top_artists()
    A.click_on_arjith_singh()