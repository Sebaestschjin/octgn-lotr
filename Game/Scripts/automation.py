def onPGV(args):
    startingPlayer()

def deck_loaded(args):
    if args.player == me:
        me.setGlobalVariable("deckLoaded", "Yes")
        if all(player.getGlobalVariable("deckLoaded") == "Yes" for player in getPlayers()):
            twilight = table.create("fb909fa6-1ed7-44f7-a214-77b9bf5ce90d", -200, -31, 1, persist = True)
            twilight.anchor = True
        
def startingPlayer():
    if all(player.getGlobalVariable("burdenBid") != "999" for player in getPlayers()):
        notify("{} has bid {} burden token(s).".format(me,int(me.getGlobalVariable("burdenBid"))))
        

def notBid(group, x=0, y=0):
    if me.getGlobalVariable("burdenBid") == "999":
        return True
    else: return False