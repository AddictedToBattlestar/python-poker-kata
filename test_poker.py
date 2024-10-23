from constants import CardValue, CardSuit
from poker import Card, Deck

def test_card_comparison():
    ace_spades = Card(CardValue.ACE, CardSuit.SPADES)
    two_diamonds = Card(CardValue.TWO, CardSuit.DIAMONDS)
    assert ace_spades > two_diamonds

def test_new_deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert deck.cards[0] == Card(CardValue.TWO, CardSuit.SPADES)
    assert deck.cards[1] == Card(CardValue.THREE, CardSuit.SPADES)
    assert deck.cards[50] == Card(CardValue.KING, CardSuit.CLUBS)
    assert deck.cards[51] == Card(CardValue.ACE, CardSuit.CLUBS)

def test_shuffle_deck():
    deck = Deck()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    assert len(deck.cards) == 52
    assert deck.cards[0] != Card(CardValue.TWO, CardSuit.SPADES)
    assert deck.cards[1] != Card(CardValue.THREE, CardSuit.SPADES)
    assert deck.cards[50] != Card(CardValue.KING, CardSuit.CLUBS)
    assert deck.cards[51] != Card(CardValue.ACE, CardSuit.CLUBS)

def test_deal_hand():
    deck = Deck()
    hand = deck.deal_hand()
    assert len(hand) == 5
    assert len(deck.cards) == 47

def test_deal_hand_repeatedly():
    deck = Deck()
    hand1 = deck.deal_hand()
    hand2 = deck.deal_hand()
    assert len(hand1) == 5
    assert len(hand2) == 5
    assert len(deck.cards) == 42