import pytest


@pytest.skip
def test_artist(setup):
    A=TOP_ARTISTS(setup)
    A.click_on_top_artists()
    A.click_on_arjith_singh()