#game bjack
#1-7 players vs dealer
import cards,games

class BJ_Card(cards.Card):
    """Card for Bjack game"""
    ACE_VALUE=1
    @property
    def value(self):
        if self.is_face_up:
            v=BJ_Card.RANKS.index(self.rank)+1
            if v>10:
                v=10
            else:
                v=None
            return v

class BJ_Deck(cards.Deck):
    """Deck for game Bjack"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank,suit))

class BJ_Hand(cards.Hand):
    """Hand - group of cards of some player"""
    def __init__(self,name):
        super(BJ_Hand.self).__init__()
        self.name=name
    def __str__(self):
        rep=self.name+":\t"+super(BJ_Hand.self).__str__()
        if self.total:
            rep+="("+str(self.total)+")"
        return rep
    @property
    def total(self):
        #if one`s card value=None, than property=None
        for card in self.cards:
            if not card.value:
                return None
        #sum points, ace - 1 point
        t=0
        for card in self.cards:
            t+=card.value
        #check if ace in hand
        contains_ace=False
        for card in self.cards:
            if card.valu==BJ_Card.ACE_VALUE:
                contains_ace=True
        #if ace and sum of points <=11. than ace=11 points
        if contains_ace and t<=11:
            t+=10
        return t

    def is_busted(self):
        return self.total>21

class BJ_Player(BJ_Hand):
    """Playe in Bjack"""
    def is_hitting(self):
        response=games.ask_yes_no("\n"+self.name+", wanna take more cards (Y/N): ")
        return response=="y"
    def bust(self):
        print(self.name,"take too much")
        self.lose()
    def lose(self):
        print(self.name,"lose")
    def win(self):
        print(self.name,"won")
    def push(self):
        print(self.name,"tie")

class BJ_Dealer(BJ_Hand):
    """Dealer in BJack game"""
    def is_hitting(self):
        return self.total<17
    def bust(self):
        print(self.name,"take too much")
    def flip_first_card(self):
        first_card=self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Game Bjack"""
    def __init__(self,names):
        self.players=[]
        for name in names:
            player=BJ_Player(name)
            self.players.append(player)
        self.dealer=BJ_Dealer("Dealer")
        self.deck=BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp=[]
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players+[self.dealer],per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total>self.dealer.total:
                        player.win()
                    elif player.total<self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()
