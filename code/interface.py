import tkinter as tk
from PIL import Image, ImageTk

class PlanningPokerApp:
    def __init__(self, master):
        self.master = master
        master.title("Planning Poker")

        self.card_mapping = {
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_0.jpg": 0,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_1.jpg": 1,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_2.jpg": 2,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_3.jpg" : 3,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_5.jpg" : 5,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_8.jpg" : 8,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_13.jpg": 13,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_20.jpg": 20,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_40.jpg": 40,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_100.jpg": 100,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_cafe.jpg": 0,
            "C:/Users/rayen/Documents/M1_lyon2/M1_Lyon2/M1Manar/Conception_agile/projet/cartes/cartes_interro.jpg": 0
        }

        self.card_width = 150
        self.card_height = 175

        self.card_images = [Image.open(path).resize((self.card_width, self.card_height)) for path in self.card_mapping.keys()]
        self.current_card_index = 0

        self.card_frame = tk.Frame(master)
        self.card_frame.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.selected_cards = set()

        for i, (card_path, card_number) in enumerate(self.card_mapping.items()):
            row_index = i // 5
            col_index = i % 5

            image_tk = ImageTk.PhotoImage(self.card_images[i])
            button = tk.Button(self.card_frame, image=image_tk, command=lambda num=card_number: self.toggle_card_selection(num))
            button.image = image_tk
            button.grid(row=row_index, column=col_index, padx=10, pady=10)

        self.label_score = tk.Label(master, text="Score:")
        self.label_score.grid(row=0, column=0, pady=7)

        self.label_average = tk.Label(master, text="Moyenne des numéros sélectionnés: ")
        self.label_average.grid(row=0, column=1, pady=7)

        self.entry_mission = tk.Entry(master)
        self.entry_mission.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="we")
        self.entry_mission.bind("<Return>", self.submit_mission)

        self.button_submit = tk.Button(master, text="Soumettre l'estimation", command=self.show_estimate)
        self.button_submit.grid(row=3, column=0, pady=10, columnspan=2)

        self.label_selected_card = tk.Label(master, text="Mission : Aucune")
        self.label_selected_card.grid(row=4, column=0, columnspan=2, pady=10)

    def toggle_card_selection(self, card_number):
        if card_number in self.selected_cards:
            self.selected_cards.remove(card_number)
        else:
            self.selected_cards.add(card_number)

        if self.selected_cards:
            average_selected = sum(self.selected_cards) / len(self.selected_cards)
            self.label_average.config(text=f"Moyenne des numéros sélectionnés: {average_selected:.2f}")
        else:
            self.label_average.config(text="Moyenne des numéros sélectionnés: N/A")

        selected_card_path = next(iter(self.selected_cards), None)
        if selected_card_path:
            self.label_selected_card.config(text=f"Mission : {selected_card_path}")
        else:
            self.label_selected_card.config(text="Mission : Aucune")

        self.update_card_button_appearance()

    def update_card_button_appearance(self):
        for button in self.card_buttons:
            card_path = next(path for path, num in self.card_mapping.items() if num == int(button.cget("command").split()[-1]))
            if card_path in self.selected_cards:
                button.config(bordercolor="red")
            else:
                button.config(bordercolor="black")

    def submit_mission(self, event=None):
        mission_text = self.entry_mission.get()
        self.label_selected_card.config(text=f"Mission : {mission_text}")

    def show_estimate(self):
        estimate = self.label_score.cget("text")
        mission = self.label_average.cget("text")

        print(f"Estimation : {estimate}, Mission : {mission}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanningPokerApp(root)
    root.mainloop()
