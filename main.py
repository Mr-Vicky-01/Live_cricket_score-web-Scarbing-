from bs4 import BeautifulSoup
import requests

MATCH_TITLE = ""
TEAM_1 = ""
SCORE_1 = ""
TEAM_2 = ""
SCORE_2 = ""
COMMENT = ""
match_completed = []

try:
    response = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
    soup = BeautifulSoup(response.text, "html.parser")
    team1_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div",
                                                                                 class_="cb-hmscg-bwl-txt cb-ovr-flo")
    team2_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_="cb-hmscg-bat-txt")
    comment = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_='cb-text-live')
    match_title = soup.find("div", class_="cb-col-100 cb-col cb-schdl cb-billing-plans-text").find_all(
        "h3", class_="cb-lv-scr-mtch-hdr inline-block")

    for tit in match_title:
        title = tit.get_text(strip=True)
        MATCH_TITLE = title.replace(",", " ")

    for match in team1_score:
        TEAM_1 = match.find("div", class_="cb-ovr-flo cb-hmscg-tm-nm").get_text(strip=True)
        SCORE_1 = match.find("div", style="display:inline-block; width:140px").get_text(strip=True)

    for match in team2_score:
        TEAM_2 = match.find("div", class_="cb-ovr-flo cb-hmscg-tm-nm").get_text(strip=True)
        SCORE_2 = match.find("div", style="display:inline-block; width:140px").get_text(strip=True)

    if comment == match_completed:
        comment = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_='cb-text-complete')
    for c in comment:
        COMMENT = c.get_text(strip=True)

    print(MATCH_TITLE)
    print("~" * len(COMMENT))
    print(TEAM_1, SCORE_1)
    print(TEAM_2, SCORE_2)
    print("~" * len(COMMENT))
    print(COMMENT)

except Exception as a:
    print(a)

