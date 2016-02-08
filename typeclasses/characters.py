"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.
"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    The Character defaults to implementing some of its hook methods with the
    following standard functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead)
    at_after_move - launches the "look" command
    at_post_puppet(player) -  when Player disconnects from the Character, we
                    store the current location, so the "unconnected" character
                    object does not need to stay on grid but can be given a
                    None-location while offline.
    at_pre_puppet - just before Player re-connects, retrieves the character's
                    old location and puts it back on the grid with a "charname
                    has connected" message echoed to the room
    """
    pass

    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character 
        generation step instead.
        """
        
        #set persistent attributes
        self.db.alignment = 0
        
        #set start skill dictionary
        self.db.skills = {'Combat': 0}
        
        self.db.baseStrength = 5
        self.db.baseDexterity = 4
        self.db.baseWisdom = 2
        self.db.modStrength = 0
        self.db.modDexterity = 0
        self.db.modWisdom = 0

    def get_score(self):
        return self.db.baseStrength, self.db.baseDexterity, self.db.baseWisdom, self.db.modStrength, self.db.modDexterity, self.db.modWisdom, self.db.alignment
    
    
        