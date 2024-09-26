import tkinter as tk
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

    def flip(self):
        self.is_face_up = not self.is_face_up

    def __str__(self):
        return f"{self.rank} of {self.suit}" if self.is_face_up else "Card"

    class Deck:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    ranks = ['Ach', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


class SpiderSolitaire:
    def __init__(self, root):
        self.root = root
        self.root.title("Spider Solitaire")

        self.deck = Deck()
        self.build_table()

    def build_table(self):

        pass

        if __name__ == "__main__":
            root = tk.Tk()
            game = SpiderSolitaire(root)
            root.mainloop()

            def move_card(self, card, from_pile, to_pile):

    if self.valid_move(card, to_pile):
        from_pile.remove(card)
        to_pile.append(card)