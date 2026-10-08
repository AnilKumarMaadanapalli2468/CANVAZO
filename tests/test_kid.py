from pages.kids import KidsPage


def test_kids(driver):

    driver.get("https://canvazo.com/")
    kids = KidsPage(driver)
    kids.go_to_kids()
    kids.go_to_drawing_coloring()




