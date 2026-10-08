import allure
from pages.kids import KidsPage


@allure.title("verify kids products navigation")
@allure.description("verify that the user can navigate through kids prducts page")
@allure.feature("kids")
@allure.story("product navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.id("001")
@allure.label("team","QA")
@allure.parent_suite("canvazo")
@allure.suite("kids")
@allure.sub_suite("Navigation")
@allure.issue("https://jira.example.com/browse/BUG-123",name="BUG-123")
@allure.tag("smoke")
def test_kids(setup):
    kids = KidsPage(setup)
    with allure.step("navigate to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to drawing colouring page"):
        kids.go_to_drawing_coloring()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to kids painting page"):
        kids.go_to_kids_painting()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    # kids.go_to_drawing_book()
    with allure.step("navigate to poster colour page"):
        kids.go_to_poster_colour()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to tempera colour page"):
        kids.go_to_tempera_colour()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to gift set page"):
        kids.go_to_gift_set()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to crayons set page"):
        kids.go_to_crayons()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to colour pencil set page"):
        kids.go_to_colour_pencil()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to sketch pens page"):
        kids.go_to_sketch_pens()
    with allure.step("return to kids page"):
        kids.go_to_kids()
    with allure.step("navigate to drawing colouring page"):
        kids.go_to_drawing_book()

