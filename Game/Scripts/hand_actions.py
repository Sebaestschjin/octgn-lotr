Discard = "Discard"

def discard_card(card):
    mute()
    card.moveTo(me.piles[Discard])
    notify("{} discards {}.".format(me, card))


def discard_card_at_random(group, x=0, y=0):
    mute()
    card = group.random()
    if card is None:
        return
    card.moveTo(me.piles[Discard])
    notify("{} randomly discards {}.".format(me, card))
