from bs4 import BeautifulSoup
import requests


class ExtractData():
    def __init__(self):
        self.MATCH_TITLE = ""
        self.TEAM_1 = ""
        self.SCORE_1 = ""
        self.TEAM_2 = ""
        self.match_completed = []
        self.SCORE_2 = ""
        self.COMMENT = ""

        try:
            self.response = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
            soup = BeautifulSoup(self.response.text, "html.parser")
            team1_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div",
                                                                                         class_="cb-hmscg-bat-txt cb-ovr-flo")
            team2_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_="cb-hmscg-bwl-txt")
            comment = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_='cb-text-live')
            match_title = soup.find("div", class_="cb-col-100 cb-col cb-schdl cb-billing-plans-text").find_all(
                "h3", class_="cb-lv-scr-mtch-hdr inline-block")

            if not team1_score or not team2_score:
                team1_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all(
                    "div", class_="cb-hmscg-bwl-txt cb-ovr-flo")
                team2_score = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div",
                                                                                             class_="cb-hmscg-bat-txt")

            for tit in match_title:
                title = tit.get_text(strip=True)
                self.MATCH_TITLE = title.replace(",", " ")

            for match in team1_score:
                self.TEAM_1 = match.find("div", class_="cb-ovr-flo cb-hmscg-tm-nm").get_text(strip=True)
                self.SCORE_1 = match.find("div", style="display:inline-block; width:140px").get_text(strip=True)

            for match in team2_score:
                self.TEAM_2 = match.find("div", class_="cb-ovr-flo cb-hmscg-tm-nm").get_text(strip=True)
                self.SCORE_2 = match.find("div", style="display:inline-block; width:140px").get_text(strip=True)

            if not comment:
                comment = soup.find("div", class_="cb-col-100 cb-col cb-schdl").find_all("div", class_='cb-text-complete')
            for c in comment:
                self.COMMENT = c.get_text(strip=True)

        except Exception as a:
            print(a)
