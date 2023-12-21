from tkinter import *
from extract_data import ExtractData


class Interface():
    def __init__(self, extract_data: ExtractData):
        self.data = extract_data
        self.window = Tk()
        self.window.title("Live Cricket Score")
        self.window.config(pady=20, padx=20)

        self.title = Canvas(width=300, height=50, bg="lightgreen", highlightthickness=0)
        self.match_title = self.title.create_text(150,25, text=self.data.MATCH_TITLE, fill="red", font=("ariel", 10, "bold"))
        self.title.grid(row=1, column=1, columnspan=2, pady=15)

        self.team1 = Label(text=self.data.TEAM_1, font=("ariel", 10, "bold"))
        self.team1.grid(row=2, column=1)

        self.team1_score = Label(text=self.data.SCORE_1, font=("ariel", 10, "bold"), bg="lightgrey")
        self.team1_score.grid(row=2, column=2, pady=2)

        self.team2 = Label(text=self.data.TEAM_2, font=("ariel", 10, "bold"))
        self.team2.grid(row=3, column=1)

        self.team2_score = Label(text=self.data.SCORE_2, font=("ariel", 10, "bold"), bg="lightgrey")
        self.team2_score.grid(row=3, column=2,pady=2)

        self.commentry = Canvas(width=300, height=40, bg="lightgreen", highlightthickness=0)
        self.comment = self.commentry.create_text(150,20, text=self.data.COMMENT, fill="black", font=("ariel", 10, "normal"))
        self.commentry.grid(row=4, column=1, columnspan=2, pady=10)

        refresh_png = PhotoImage(file="refresh.png")
        refresh_png_resized = refresh_png.subsample(13, 13)
        self.button = Button(image=refresh_png_resized, highlightthickness=0, bg="grey", command=self.get_score)
        self.button.grid(row=0, column=3)

        self.window.mainloop()

    def get_score(self):
        self.data = ExtractData()  # Refresh data
        self.update_ui()

    def update_ui(self):
        self.title.itemconfig(self.match_title, text=self.data.MATCH_TITLE)
        self.team1.config(text=self.data.TEAM_1)
        self.team1_score.config(text=self.data.SCORE_1)
        self.team2.config(text=self.data.TEAM_2)
        self.team2_score.config(text=self.data.SCORE_2)
        self.commentry.itemconfig(self.comment, text=self.data.COMMENT)
