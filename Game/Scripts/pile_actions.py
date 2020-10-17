DrawCardsDefault = 5


def draw_card(group, x=0, y=0):
    mute()
    if len(group) < 1:
        return
    card = group.top()
    card.moveTo(card.owner.hand)
    notify("{} draws a card from {}.".format(me, group.name))


def draw_cards(group, x=0, y=0):
    mute()
    if len(group) < 1:
        return
    global DrawCardsDefault
    count = askInteger("Draw how many cards?", DrawCardsDefault)
    DrawCardsDefault = count
    for card in group.top(count):
        card.moveTo(card.owner.hand)
    notify("{} draws {} cards from {}.".format(me, count, group.name))


def shuffle(group, x=0, y=0):
    mute()
    group.shuffle()
    notify("{} shuffles their {}.".format(me, group.name))
