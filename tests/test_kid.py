from pages.kids import KidsPage

import pytest
@pytest.mark.skip
def test_kids(driver):
    driver.get("https://canvazo.com/")
    kids = KidsPage(driver)
    kids.go_to_kids()
    kids.go_to_drawing_coloring()
    kids.go_to_kids()
    kids.go_to_kids_painting()
    kids.go_to_kids()
    # kids.go_to_drawing_book()
    kids.go_to_kids()
    kids.go_to_poster_colour()
    kids.go_to_kids()
    kids.go_to_tempera_colour()
    kids.go_to_kids()
    kids.go_to_gift_set()
    kids.go_to_kids()
    kids.go_to_crayons()
    kids.go_to_kids()
    kids.go_to_colour_pencil()
    kids.go_to_kids()
    kids.go_to_sketch_pens()
    kids.go_to_kids()

