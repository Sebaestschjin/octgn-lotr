DamageMarker = ('Damage', 'ca152f06-41cc-476a-be27-0bdd57f4b710')
BurdenMarker = ('Burden', 'ad150c1d-4534-456b-a4bd-58bf67a26c3b')
TwilightMarker = ('Twilight', 'e4fe7c68-73f2-4ea6-a311-f537088965eb')
HighlightColor = "#ff0000"


def add_default_marker(card, x=0, y=0):
    marker_type = determine_default_marker(card)
    if marker_type:
        add_marker(card, marker_type)


def add_damage(card, x=0, y=0):
    add_marker(card, DamageMarker)


def add_burden(card, x=0, y=0):
    add_marker(card, BurdenMarker)


def add_twilight(card, x=0, y=0):
    add_marker(card, TwilightMarker)


def add_other(card, x=0, y=0):
    mute()
    marker, qty = askMarker()
    if qty != 0:
        card.markers[marker] = qty


def add_marker(card, marker):
    mute()
    name = marker[0]
    card.markers[marker] += 1
    notify("{} adds a {} to {}.".format(me, name, card))


def remove_default_marker(card, x=0, y=0):
    marker_type = determine_default_marker(card)
    if marker_type:
        remove_marker(card, marker_type)


def remove_damage(card, x=0, y=0):
    remove_marker(card, DamageMarker)


def remove_burden(card, x=0, y=0):
    remove_marker(card, BurdenMarker)


def remove_twilight(card, x=0, y=0):
    remove_marker(card, TwilightMarker)


def remove_marker(card, marker):
    mute()
    name = marker[0]
    if card.markers[marker] < 1:
        return
    card.markers[marker] -= 1
    notify("{} removes a {} from {}.".format(me, name, card))


def determine_default_marker(card):
    if is_character(card):
        return DamageMarker
    elif is_twilight_tracker(card):
        return TwilightMarker
    return None


def rotate_cards(cards, x=0, y=0):
    mute()
    for card in cards:
        card.orientation ^= Rot90
        if card.orientation & Rot90 == Rot90:
            notify('{} turns {} sideways'.format(me, card))
        else:
            notify('{} turns {} upright'.format(me, card))


def flip_cards(cards, x=0, y=0):
    mute()
    for card in cards:
        if card.isFaceUp:
            notify("{} flips {} face down.".format(me, card))
            card.isFaceUp = False
        else:
            card.isFaceUp = True
            notify("{} flips {} face up.".format(me, card))


def highlight_cards(cards, x=0, y=0):
    mute()
    for card in cards:
        if card.highlight == HighlightColor:
            card.highlight = None
            notify('{} removes highlight from {}'.format(me, card))
        else:
            card.highlight = HighlightColor
            notify('{} highlights {}'.format(me, card))


def flip_coin(group, x=0, y=0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))


def roll_d6(group, x=0, y=0):
    mute()
    n = rnd(1, 6)
    notify("{} rolls {} on a 6-sided die.".format(me, n))


def bid_burdens(group, x=0, y=0):
    if did_not_bid(me):
        bid = askInteger("How much burden would you like to bid?", 0)
        if bid:
            set_bid(me, bid)
    else:
        whisper("You've already bid for this game.")


def is_character(card):
    return 'Ally' in card.type or 'Companion' in card.type or 'Minion' in card.type


def is_twilight_tracker(card):
    return "Twilight Pool" in card.name
