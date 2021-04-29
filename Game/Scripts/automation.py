TwilightCard = "fb909fa6-1ed7-44f7-a214-77b9bf5ce90d"
BidVariable = "burdenBid"
BidDefault = 999
DeckLoaded = "deckLoaded"


def on_player_global_variable_changed(_):
    determine_starting_player()


def on_deck_loaded(args):
    if args.player == me:
        set_deck_loaded(me)

        if all_players(is_deck_loaded):
            twilight = table.create(TwilightCard, -200, -31, 1, persist=True)
            notify("{}".format(twilight))
            twilight.anchor = True


def determine_starting_player():
    if all_players(has_bid):
        notify("{} has bid {} burden token(s).".format(me, get_bid(me)))


def get_bid(player):
    return int(player.getGlobalVariable(BidVariable))


def set_bid(player, value):
    player.setGlobalVariable(BidVariable, str(value))


def has_bid(player):
    return get_bid(player) != BidDefault


def has_not_bid(group, x=0, y=0):
    return not has_bid(me)


def all_players(test):
    return all(test(player) for player in getPlayers())


def is_deck_loaded(player):
    return player.getGlobalVariable(DeckLoaded) == "Yes"


def set_deck_loaded(player):
    player.setGlobalVariable(DeckLoaded, "Yes")
