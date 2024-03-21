from a2_support import *


class Card:
    """An abstract base class representing a card in the game.

    This class has attributes for name, description, damage, block, energy
    cost, status modifiers and whether or not the card requires a target.

    Attributes:
        card (str): The name of the card.
        damage (int): The amount of damage this card does to its target
        block (int): The amount of block this card gives to its target 
        energy_cost (int): The amount of energy this card costs to play
        status_modifiers (dict): A dictionary describing each status modifier
        applied when this card is played.
        description (str): A description of the card.
        requires_target (bool): True if playing this card requires a target,
        False otherwise.
    """

    def __init__(
        self,
        card: str = 'Card',
        damage: int = 0,
        block: int = 0,
        energy_cost: int = 1,
        status_modifiers: dict = {},
        description: str = 'A card.',
        requires_target: bool = True,
    ) -> None:
        """Initialize the Card instance with the given attribute values."""
        self._damage = damage
        self._block = block
        self._energy_cost = energy_cost
        self._status_modifiers = status_modifiers
        self._name = card
        self._description = description
        self._requires_target = requires_target

    def get_damage_amount(self) -> int:
        """Returns the amount of damage this card does to its target (i.e. the
        opponent it is played on). By default, the damage done by a card is 0.

        Returns:
            int: The damage amount of the card.

        Example:
            >>> card = Card()
            >>> card.get_damage_amount()
            0
        """
        return self._damage

    def get_block(self) -> int:
        """Returns the amount of block this card gives to its target.
        The default block value is 0.

        Returns:
            int: The block value of the card.

        Example:
            >>> card = Card(card="Defend", block=3)
            >>> card.get_block()
            3
        """
        return self._block

    def get_strength(self) -> int:
        """Returns the amount of strength this card gives to its target.
        The default strength value is 0.

        Returns:
            int: The strength value of the card.

        Example:
            >>> card = Card(card="Harden", status_modifiers={"strength": 2})
            >>> card.get_strength()
            2
        """
        self._strength = 0
        if "strength" in self._status_modifiers:
            self._strength = self._status_modifiers["strength"]
        return self._strength

    def get_energy_cost(self) -> int:
        """Returns the amount of energy this card costs to play.
        The default energy cost is 1.

        Returns:
            int: The energy cost of the card.

        Example:
            >>> card = Card(card="Strike", energy_cost=1)
            >>> card.get_energy_cost()
            1
        """
        return self._energy_cost

    def get_status_modifiers(self) -> dict[str, int]:
        """Returns a dictionary describing each status modifier applied.

        Returns:
            Dict[str, int]: The status modifiers dictionary of the card.

        Example:
            >>> card = Card(card="card_name", status_modifiers={"weak": 2})
            >>> card.get_status_modifiers()
            {'weak': 2}
        """
        return self._status_modifiers

    def get_name(self) -> str:
        """Returns the name of the card. 

        In the Card superclass, this is just thestring 'Card'. 

        Returns:
            str: The name of the card.

        Example:
            >>> card = Card()
            >>> card.get_name() 
            'Card'
        """
        return self._name

    def get_description(self) -> str:
        """Returns a description of the card.

        In the Card superclass, this is just the string 'A card'. 

        Returns:
            str: A description of the card.

        Example:
            >>> card = Card()
            >>> card.get_description() 
            'A card.'
        """
        return self._description

    def requires_target(self) -> bool:
        """Returns a boolean indicating whether a card requires a target.

        Returns True if playing this card requires a target, and False if it
        does not. By default, a card does require a target. 

        Returns:
            bool: True, if the card requires a target. False, if the card does
            not require a target

        Example:
            >>> card = Card()
            >>> card.requires_target() 
            True
        """
        return self._requires_target

    def __str__(self) -> str:
        """Returns a string representation of this card.

        Returns the string in the format '{Card name}: {Card description}'. 

        Returns:
            str: The card name and the card description in the format
            '{Card name}: {Card description}'

        Example:
            >>> card = Card()
            >>> str(card)
            'Card: A card.'
        """
        return f"{self._name}: {self._description}"

    def __repr__(self) -> str:
        """Returns the text that would be required to create
        a new instance of this class identical to self.

        This method is inherited by all subclasses of Card.

        Returns:
            str: A copy of the text required to recreate this class instance.

        Example:
            >>> strike = Strike()
            >>> strike
            Strike()
        """
        return f"{self._name}()"


class Strike(Card):
    """A subclass of Card representing a Strike card in the game.

    A Strike card deals 6 damage to its target and costs 1 energy point to play.

    Attributes inherited from Card:
        name (str): The name of the card, set to "Strike".
        description (str): A description of the card, set to "Deal 6 damage.".
        damage (int): The amount of damage this card does to its target,
            set to 6.
        block (int): The amount of block this card gives to its target,
            set to 0.
        energy_cost (int): The amount of energy this card costs to play,
            set to 1.
        status_modifiers (Dict[str, int]): A dictionary describing each status
            modifier applied when this card is played,
            set to an empty dictionary.
        requires_target (bool): True if playing this card requires a target,
            False otherwise, set to True.

    Example:
        >>> strike = Strike()
        >>> print(strike.get_damage_amount(), 
        strike.get_block(), strike.get_energy_cost())
        6 0 1
        >>> strike.get_name()
        'Strike'
        >>> strike.get_description()
        'Deal 6 damage.'
        >>> strike.requires_target()
        True
        >>> str(strike)
        'Strike: Deal 6 damage.'
        >>> strike
        Strike()
    """

    def __init__(self) -> None:
        super().__init__(card="Strike", damage=6, block=0,
                         energy_cost=1, status_modifiers={},
                         description="Deal 6 damage.", requires_target=True)


class Defend(Card):
    """A subclass of Card representing a Defend card in the game.

    Defend is a type of Card that adds 5 block to its user. Defend does not
    require a target. It costs 1 energy point to play. 

    Attributes inherited from Card:
        name (str): The name of the card, set to "Block".
        description (str): A description of the card, set to "Gain 5 block.".
        damage (int): The amount of damage this card does to its target,
            set to 0.
        block (int): The amount of block this card gives to its target,
            set to 5.
        energy_cost (int): The amount of energy this card costs to play,
            set to 1.
        status_modifiers (Dict[str, int]): A dictionary describing each status
            modifier applied when this card is played,
            set to an empty dictionary.
        requires_target (bool): True if playing this card requires a target,
            False otherwise, set to False.

    Example:
        >>> defend = Defend() 
        >>> print(defend.get_damage_amount(), defend.get_block(),
        defend.get_energy_cost()) 
        0 5 1 
        >>> defend.get_name() 
        'Defend' 
        >>> defend.get_description() 
        'Gain 5 block.' 
        >>> defend.requires_target() 
        False
        >>> str(defend) 
        'Defend: Gain 5 block.' 
        >>> defend 
        Defend()
    """

    def __init__(self) -> None:
        super().__init__(card="Defend", damage=0, block=5, energy_cost=1,
                         status_modifiers={},
                         description="Gain 5 block.",
                         requires_target=False)


class Bash(Card):
    """A subclass of Card representing a Bash card in the game.

    Bash is a type of Card that adds 5 block to its user and
    causes 7 damage to its target. It costs 2 energy points to play. 

    Attributes inherited from Card:
        name (str): The name of the card, set to "Bash".
        description (str): A description of the card, set to "Deal 7 damage.
            Gain 5 block.".
        damage (int): The amount of damage this card does to its target,
            set to 7.
        block (int): The amount of block this card gives to its target,
            set to 5.
        energy_cost (int): The amount of energy this card costs to play,
            set to 2.
        status_modifiers (Dict[str, int]): A dictionary describing each status
            modifier applied when this card is played,
            set to an empty dictionary.
        requires_target (bool): True if playing this card requires a target,
            False otherwise, set to True.

    Example:
        >>> bash = Bash() 
        >>> print(bash.get_damage_amount(), bash.get_block(),
        bash.get_energy_cost()) 
        7 5 2 
        >>> bash.get_name() 
        'Bash' 
        >>> bash.get_description() 
        'Deal 7 damage. Gain 5 block.' 
        >>> bash.requires_target() 
        True 
        >>> str(bash) 
        'Bash: Deal 7 damage. Gain 5 block.' 
        >>> bash Bash()
    """

    def __init__(self) -> None:
        super().__init__(card="Bash", damage=7, block=5, energy_cost=2,
                         status_modifiers={},
                         description="Deal 7 damage. Gain 5 block.",
                         requires_target=True)


class Neutralize(Card):
    """A subclass of Card representing a Neutralize card in the game.

    Neutralize is a type of card that deals 3 damage to its
    target. It also applies status modifiers to its target; namely, it applies 1
    weak and 2 vulnerable. Neutralize does not cost any energy points to play.

    Attributes inherited from Card:
        name (str): The name of the card, set to "Neutralize".
        description (str): A description of the card, set to "Deal 3 damage.".
        damage (int): The amount of damage this card does to its target,
            set to 3.
        block (int): The amount of block this card gives to its target,
            set to 0.
        energy_cost (int): The amount of energy this card costs to play,
            set to 0.
        status_modifiers (Dict[str, int]): A dictionary describing each status
            modifier applied when this card is played,
            set to an {'weak': 1, 'vulnerable': 2}.
        requires_target (bool): True if playing this card requires a target,
            False otherwise, set to True.

    Example:
        >>> neutralize = Neutralize() 
        >>> print(neutralize.get_damage_amount(),
        neutralize.get_block(), neutralize.get_energy_cost())
        3 0 0 
        >>> neutralize.get_status_modifiers()
        {'weak': 1, 'vulnerable': 2} 
        >>> neutralize.get_name()
        'Neutralize' 
        >>> neutralize.get_description() 
        'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.' 
        >>> str(neutralize) 
        'Neutralize: Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.' 
        >>> neutralize
        Neutralize()
    """

    def __init__(self) -> None:
        super().__init__(card="Neutralize", damage=3, block=0,
                         energy_cost=0,
                         status_modifiers={'weak': 1, 'vulnerable': 2},
                         description="Deal 3 damage. "
                         "Apply 1 weak. Apply 2 vulnerable.",
                         requires_target=True)


class Survivor(Card):
    """A subclass of Card representing a Survivor card in the game.

    Survivor is a type of card that adds 8 block and applies
    1 strength to its user. Survivor does not require a target.

    Attributes inherited from Card:
        name (str): The name of the card, set to "Survivor".
        description (str): A description of the card, set to "Gain 8 block 
            and 1 strength.".
        damage (int): The amount of damage this card does to its target,
            set to 0.
        block (int): The amount of block this card gives to its target,
            set to 8.
        energy_cost (int): The amount of energy this card costs to play,
            set to 1.
        status_modifiers (Dict[str, int]): A dictionary describing each status
            modifier applied when this card is played,
            set to an {'strength': 1}.
        requires_target (bool): True if playing this card requires a target,
            False otherwise, set to False. 

    Example:
        >>> survivor = Survivor() 
        >>> print(survivor.get_damage_amount(), survivor.get_block(),
        survivor.get_energy_cost())
        0 8 1 
        >>> survivor.get_status_modifiers()
        {'strength': 1} 
        >>> survivor.requires_target() 
        False 
        >>> survivor.get_name()
        'Survivor' 
        >>> survivor.get_description() 
        'Gain 8 block and 1 strength.' 
        >>> str(survivor)
        'Survivor: Gain 8 block and 1 strength.'
        >>> survivor
        Survivor()
    """

    def __init__(self) -> None:
        super().__init__(card="Survivor", damage=0, block=8,
                         energy_cost=1, status_modifiers={'strength': 1},
                         description="Gain 8 block and 1 strength.",
                         requires_target=False)


class Entity:
    """An abstract base class representing an entity in the game.

    This class has attributes for max hp, block, strength, weak, and vulnerable.

    Attributes:
        - Health points (HP): This starts at the maximum HP for
            the entity, and may decrease over the course of one or 
            more encounters. An entity is defeated when its
            HP is reduced to 0. 
        - Block: This is the
            amount of defense the entity has. When an entity is attacked,
            damage is applied to the block first. 
            Only once the block has been reduced to 0 will any remaining 
            damage be caused to the entity's HP. 
        - Strength: The amount of additional strength this entity has. 
            When an entity plays a card that causes damage to a target, 
            the damage caused will increase by 1 for each strength point 
            the entity has. Strength does not wear off until 
            the end of an encounter. 
        - Weak: The number of turns for which
            this entity is weak. If an entity is weak on a given turn, 
            all cards played by the entity that cause damage 
            will cause 25% less damage. 
        - Vulnerable: The number of turns for which this entity 
            is vulnerable. If an entity is vulnerable on a turn, 
            damage caused to it will be increased by 50%.
    """

    def __init__(self,
                 max_hp: int,
                 ) -> None:
        """Initialize the Entity instance with the given attribute values.

        Sets up a new entity with the given max_hp. An entity starts with the
        maximum amount of HP it can have. Block, strength, weak, and vulnerable
        all start at 0. 

        Args:
            max_hp (int): The maximum HP for this entity.
        """
        block = 0
        strength = 0
        weak = 0
        vulnerable = 0
        self._max_hp = max_hp
        self._hp = max_hp
        self._block = block
        self._strength = strength
        self._weak = weak
        self._vulnerable = vulnerable

    def get_hp(self) -> int:
        """Returns the current HP for this entity. 

        Returns:
            int: The current HP for this entity.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_hp() 
            20
            >>> entity.reduce_hp(2)
            >>> entity.get_hp()
            18
        """
        return self._hp

    def get_max_hp(self) -> int:
        """Returns the maximum possible HP for this entity. 

        Returns:
            int: The maximum possible HP for this entity.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_max_hp()
            20
        """
        return self._max_hp

    def get_block(self) -> int:
        """Returns the amount of block for this entity. 

        Returns:
            int: The amount of block for this entity.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_block() 
            0
        """
        return self._block

    def get_strength(self) -> int:
        """Returns the amount of strength for this entity. 

        Returns:
            int: The amount of strength for this entity.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_strength()
            0
        """
        return self._strength

    def get_weak(self) -> int:
        """Returns the amount of turns for which this entity is weak.

        Returns:
            int: The amount of turns for which this entity is weak.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_weak()
            0
        """
        return self._weak

    def get_vulnerable(self) -> int:
        """Returns the number of turns for which this entity is vulnerable.

        Returns:
            int: The number of turns for which this entity is vulnerable.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_vulnerable()
            0
        """
        return self._vulnerable

    def get_name(self) -> str:
        """Returns the name of the entity.

        Returns:
            str: The name of the most specific class the entity belongs to.

        Example:
            >>> entity = Entity(20)
            >>> entity.get_name()
            'Entity'
        """
        return self.__class__.__name__

    def reduce_hp(self, amount: int) -> None:
        """Reduces the HP of a given entity.

        Attacks the entity with a damage of amount. This involves reducing block
        until the amount of damage has been done or until block has reduced to
        zero, in which case the HP is reduced by the remaining amount. For
        example, if an entity has 20 HP and 5 block, calling reduce_hp with an
        amount of 10 would result in 15 HP and 0 block. HP cannot go below 0.

        Args:
            amount (int): The number of HP that will be taken away.

        Example:
            >>> entity = Entity(20)
            >>> entity.reduce_hp(2)
            >>> entity.get_hp()
            18
        """
        self._block -= amount
        if self._block > 0:
            return None
        else:
            self._hp += self._block
        if self._hp < 0:
            self._hp = 0
        if self._block < 0:
            self._block = 0

    def is_defeated(self) -> bool:
        """ Returns a boolean value to determine if the entity is defeated.

        Returns True if the entity has been defeated, and False otherwise. An
        entity is defeated if it has no HP remaining. 

        Returns:
            bool: True if the entity has been defeated, False otherwise.

        Example:
            >>> entity = Entity(20)
            >>> entity.is_defeated()
            False
        """
        return self._hp == 0

    def add_block(self, amount: int) -> None:
        """Adds the given amount to the total block this entity has. 

        Args:
            amount (int): The amount that will be added to the total block.

        Example:
            >>> entity = Entity(20)
            >>> entity.add_block(5)
            >>> entity.get_block()
            5
        """
        self._block = self._block + amount

    def add_strength(self, amount: int) -> None:
        """Adds the given amount to the amount of strength this entity has. 

        Args:
            amount (int): The amount that will be added to strength.

        Example:
            >>> entity = Entity(20)
            >>> entity.add_strength(2)
            >>> entity.get_strength()
            2
        """
        self._strength = self._strength + amount

    def add_weak(self, amount: int) -> None:
        """Adds the given amount to the amount of weak this entity has. 

        Args:
            amount (int): The amount that will be added to weak.

        Example:
            >>> entity = Entity(20)
            >>> entity.add_weak(3)
            >>> entity.get_weak()
            3
        """
        self._weak = self._weak + amount

    def add_vulnerable(self, amount: int) -> None:
        """Adds the given amount to the amount of vulnerable this entity has.

        Args:
            amount (int): The amount that will be added to vulnerable.

        Example: 
            >>> entity = Entity(20)
            >>> entity.add_vulnerable(4)
            >>> entity.get_vulnerable()
            4
        """
        self._vulnerable = self._vulnerable + amount

    def new_turn(self) -> None:
        """Starts a new turn in the encounter.

        Applies any status changes that occur when a new turn begins. For the
        base Entity class, this involves setting block back to 0, and reducing
        weak and vulnerable each by 1 if they are greater than 0. 

        Example:
            >>> entity = Entity(20)
            >>> entity.new_turn()
        """
        self._block = 0
        if self._weak >= 1:
            self._weak -= 1
        if self._vulnerable >= 1:
            self._vulnerable -= 1
        return None

    def __str__(self) -> str:
        """Returns a string which represents the current entity.

        Returns the string representation for the entity in the format '{entity
        name} ({current HP}/{max HP})'. If called from the abstract base class
        will only return a string representation of the class object.

        Returns:
            str: Represents the entity in the format of '{entity
                name} ({current HP}/{max HP})'.

        Example:
            >>> player = Player(20)
            >>> str(player)
            'Player: 20/20 HP'
        """
        return f"{self.get_name()}: {self.get_hp()}/{self.get_max_hp()} HP"

    def __repr__(self) -> str:
        """Returns the command required to recreate the instance.

        Returns the text that would be required to create a new instance of this
        class identical to self.

        Returns:
            str: Command required to recreate a copy of the given instance.

        Example:
            >>> entity = Entity(20)
            >>> repr(entity)
            'Entity(20)'

        """
        return f"{self.__class__.__name__}({self.get_max_hp()})"


class Player(Entity):
    """A subclass of Entity representing the Player instance in the game.

    A Player is a type of entity that the user controls. In addition to regular
    entity functionality, a player also has energy and cards. Player's must
    manage three sets of cards; the deck (cards remaining to be drawn), their
    hand (cards playable in the current turn), and a discard pile (cards that
    have been played already this encounter).

    Attributes inherited from Entity:
        max_hp (int): The maximum HP for this entity.
        hp (int): The current Health points (HP) for the entity.
        block (int): The amount of block for this entity.
        strength (int): The amount of strength for this entity.
        weak (int): The number of turns for which this entity is weak.
        vulnerable (int): The number of turns for which this
             entity is vulnerable.


    """

    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """Initializes the Player subclass and its parent class. 

        In addition to executing the initializer for the Entity superclass, this
        method initializes the player's energy which starts at 3, as well as
        three lists of cards (deck, hand, and discard pile). If the cards
        parameter is not None, the deck is initialized to be cards. Otherwise,
        it is initialized as an empty list. The players hand and discard
        piles start as empty lists.

        Args:  
            max_hp: The maximum HP for the player. This value is 
                constant for the duration of the game.
            cards: A list of cards that will be used to initialize 
                the player's deck. If this parameter is None, the deck will be 
                initialized as an empty list.
        """
        super().__init__(max_hp)
        self._max_hp = max_hp
        self._energy = 3
        self._hand = []
        self._discard = []
        self._cards = cards
        if cards != None:
            self._deck = cards
        else:
            self._deck = []

    def get_energy(self) -> int:
        """Returns the amount of energy the player has remaining.

        Returns:
            int: The amount of energy the player has remaining.

        Example:
            >>> player = Player(20, 3)
            >>> player.get_energy()
            3
        """
        return self._energy

    def get_hand(self) -> list[Card]:
        """Returns the players current hand.

        Returns:
            list[Card]: A list of Cards that exist in the players current hand.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            print(player.get_hand())
            []
            >>> player.new_turn()
            >>> player.get_hand()
            [Strike(), Defend(), Strike(), Strike(), Bash()]
        """
        return self._hand

    def get_deck(self) -> list[Card]:
        """Returns the players current deck.

        Returns:
            list[Card]: The cards that are in the players current deck.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            >>> player.get_deck()
            [Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Bash()]
            >>> player.new_turn()
            >>> player.get_deck()
            [Defend(), Defend()]   
        """
        return self._deck

    def get_discarded(self) -> list[Card]:
        """Returns the players current discard pile.

        Returns:
            list[Card]: The cards that are in the discared pile.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            >>> player.play_card('Bash')
            Bash()
            >>> player.get_discarded()
            [Bash()]   
        """
        return self._discard

    def start_new_encounter(self) -> None:
        """Starts a new encounter, puts discard pile back 
        into deck. Only if hand is empty.

        This method adds all cards from the player's discard pile to the end of 
        their deck, and sets the discard pile to be
        an empty list. A pre-condition to this method is that the player's hand 
        should be empty when it is called.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            >>> player.get_deck()
            [Defend(), Defend()]
            >>> player.start_new_encounter()
            >>> player.get_deck()
            [Defend(), Defend(), Strike(), Defend(), Strike(), Strike(), Bash()]
        """
        if not self._hand == []:
            return None
        self._deck.extend(self._discard)
        self._discard = []
        return None

    def end_turn(self) -> None:
        """Ends players turn, discards hand.

        This method adds all remaining cards from the player's hand to the end
        of their discard pile, and sets their hand back to an empty list.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            >>> player.new_turn()
            >>> player.get_hand()
            [Strike(), Defend(), Strike(), Strike(), Bash()]
            >>> player.end_turn()
            >>> player.get_hand()
            []
            >>> player.get_discarded()
            [Strike(), Defend(), Strike(), Strike(), Bash()]
        """
        self._discard.extend(self._hand)
        self._hand = []
        return None

    def new_turn(self) -> None:
        """Starts new player turn, deals a new hand and resets energy levels.

        This method sets the player up for a new turn. This involves everything
        that a regular entity requires for a new turn, but also requires that
        the player be dealt a new hand of 5 cards, and energy be reset to 3.
        Uses the draw_cards function from a2_support.py to achieve
        dealing the player new cards. 

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(), 
                Defend(), Defend(), Defend(), Bash()])
            >>> player.get_hand()
            []
            >>> player.new_turn()
            >>> player.get_hand()
            [Strike(), Defend(), Strike(), Strike(), Bash()]

        """
        super().new_turn()
        self._energy = 3
        draw_cards(self._deck, self._hand, self._discard)
        return None

    def play_card(self, card_name: str) -> Card | None:
        """Attempts to play a card from the player's hand.

        If a card with the given name exists in the player's 
        hand and the player has enough energy to
        play said card, the card is removed from the player's hand and added to
        the discard pile, the required energy is deducted from the player's
        energy, and the card is returned. If no card with the given name exists
        in the player's hand, or the player doesn't have enough energy to play
        the requested card, this function returns None.

        Returns:
            Card | None: The played Card if the card is found and able to be
                played, otherwise None if the card is not found in the hand.

        Example:
            >>> player = Player(50, [Strike(), Strike(), Strike(),
                Defend(), Defend(), Defend(), Bash()])
            >>> player.new_turn()
            >>> player.get_hand()
                [Strike(), Defend(), Strike(), Strike(), Bash()]
            >>> player.play_card('Bash')
                Bash()
            >>> player.get_hand()
                [Strike(), Defend(), Strike(), Strike()]
        """

        for card in self._hand:
            if Card.get_name(card) == card_name:
                if Card.get_energy_cost(card) <= self.get_energy():
                    self._energy -= Card.get_energy_cost(card)
                    self._hand.remove(card)
                    self._discard.append(card)
                    return card
                else:
                    return None
        return None

    def __repr__(self) -> str:
        """Returns the command required to recreate the instance.

        Returns the text that would be required to create a new instance of this
        class identical to self. This method is overwritten by the instantiable
        subclasses of Player as predefined subclasses have set attributes, 
        thus no args are needed to create a copy of the instance.

        Returns:
            str: Command required to recreate a copy of the given instance.

        Example:
            >>> player = Player(20)
            >>> repr(player)
            'Player(20, None)'

        """
        return f"{self.__class__.__name__}({self.get_max_hp()}, {self._cards})"


class IronClad(Player):
    """A subclass of Player with predefined attributes representing the IronClad
    game character.

    IronClad is a type of player that starts with 80 HP.
    IronClad's deck contains 5 Strike cards, 4 Defend cards, and 1 Bash card. 
    The __init__ method for IronClad does not take any arguments beyond self. 
    """

    def __init__(self) -> None:
        """
        Initialize an IronClad instance with the pre-set attribute values.
        """
        super().__init__(80)
        if self._deck == []:
            self._deck = [Strike(), Strike(), Strike(), Strike(), Strike(),
                          Defend(), Defend(), Defend(), Defend(),
                          Bash()]
        else:
            self._deck = self._cards

    def __repr__(self) -> str:
        """Returns the command required to recreate the instance.

        Returns the text that would be required to create a new instance of this
        class identical to self. This is manually defined for each subclass of 
        player as predefined subclasses have set attributes, thus no args are
        needed to create a copy of the instance.

        Returns:
            str: Command required to recreate a copy of the given instance.

        Example:
            >>> ironclad = IronClad()
            >>> repr(ironclad)
            'IronClad()'

        """
        return f"{self.__class__.__name__}()"


class Silent(Player):
    """A subclass of Player with predefined attributes representing the Silent
    game character.

    Silent is a type of player that starts with 70 HP. 
    Silent's deck contains 5 Strike cards, 5 Defend cards, 1 Neutralize card, 
    and 1 Survivor card. 
    The __init__ method for Silent does not take any arguments beyond self.
    """

    def __init__(self) -> None:
        """
        Initialize a Silent instance with the pre-set attribute values.
        """
        super().__init__(70)
        if self._deck == []:
            self._deck = [Strike(), Strike(), Strike(), Strike(), Strike(),
                          Defend(), Defend(), Defend(), Defend(), Defend(),
                          Neutralize(), Survivor()]
        else:
            self._deck = self._cards

    def __repr__(self) -> str:
        """Returns the command required to recreate the instance.

        Returns the text that would be required to create a new instance of this
        class identical to self. This is manually defined for each subclass of 
        player as predefined subclasses have set attributes, thus no args are
        needed to create a copy of the instance.

        Returns:
            str: Command required to recreate a copy of the given instance.

        Example:
            >>> silent = Silent()
            >>> repr(silent)
            'Silent()'

        """
        return f"{self.__class__.__name__}()"


class Monster(Entity):
    """A subclass of Entity representing a Monster instance in the game.

    A Monster is a type of entity that the user battles during encounters. 
    In addition to regular entity functionality, each monster also has a 
    unique id, and an action method that handles the effects of the monster's 
    action on itself, and describes the effect the monster's 
    action would have on its target.

    Attributes inherited from Entity:
        max_hp (int): The maximum HP for this entity.
        hp (int): The current Health points (HP) for the entity.
        block (int): The amount of block for this entity.
        strength (int): The amount of strength for this entity.
        weak (int): The number of turns for which this entity is weak.
        vulnerable (int): The number of turns for which this
             entity is vulnerable.

    """

    # Initialises the id variable of monster to allow iteration.
    _instance_id = 0

    def __init__(self, max_hp: int) -> None:
        """Initializes the Monster subclass and its parent class. 

        Sets up a new monster with the given maximum HP and a unique id number. 
        The first monster created has an id of 0, 
        the second monster created has an id of 1, etc.
        So each monster is technically unique to its encounter.

        Args:  
            max_hp: The maximum HP for the monster. This value is 
                constant for the duration of the game.
        """

        super().__init__(max_hp)
        self._id = Monster._instance_id
        Monster._instance_id += 1

    def get_id(self) -> int:
        """Returns the unique id number of this monster.

        Returns:
            int: The unique id number of this monster instance.
        """
        return self._id

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster and returns its effects.

        Performs the current action for this monster, and returns a dictionary 
        describing the effects this monster's action should cause to its target.
        In the abstract Monster superclass, this method should just raise a 
        NotImplementedError. This method is overwritten by the instantiable
        subclasses of Monster, with the strategies specific
        to each type of monster. In this abstract Monster superclass, 
        this method just raises a NotImplementedError.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        """Returns the command required to recreate the instance.

        Returns the text that would be required to create a new instance of this
        class identical to self.

        Returns:
            str: Command required to recreate a copy of the given instance.

        Example:
            >>> monster = Monster(20)
            >>> repr(monster)
            'Monster(20)'

        """
        return f"{self.__class__.__name__}({self.get_max_hp()})"


class Louse(Monster):
    """A subclass of Monster which represents the Louse monster type in-game.

    The Louse has a unique action method which randomly generated a damage
    amount between 5 and 7 (inclusive). This is set for each instance of Louse
    and is not dynamic after initialisation.
    """

    def __init__(self, max_hp: int) -> None:
        """Initialises the Louse subclass and its parent classes. 

        As well as initialising the Louse subclass and its parent classes. This
        function utilises the random_louse_amount 
        function from a2_support.py to generate the damage amount each
        louse will attack. The random_louse_amount function is only called once 
        for each Louse instance, when the louse is created.

        Args:
            max_hp (int): The maximum hp value which will be given to
                this Louse instance.
        """
        super().__init__(max_hp)
        self.amount = random_louse_amount()

    def action(self) -> dict[str, int]:
        """Returns a dictionary with a randomly generated damage amount.

        The Louse's action method simply returns a dictionary of 
        {'damage': amount}, where amount is an amount between 5 
        and 7 (inclusive), randomly generated when the Louse instance 
        is created.

        Returns:
            dict[str, int]: A random amount of damage in the 
                format of {'damage': amount}.

        Example:
            >>> louse = Louse(20)
            >>> louse.get_id()
            0
            >>> louse.action()
            {'damage': 6}
            >>> another_louse = Louse(30)
            >>> another_louse.action()
            {'damage': 7}
            >>> another_louse.get_id()
            1
        """
        amount = self.amount
        return {'damage': amount}


class Cultist(Monster):
    """A subclass of Monster which represents the Cultist monster type in-game.

    The Cultist subclass is unique because the more instances of the class that
    exist, the higher the damage each instance will do. For attack that occurs,
    as identified by the _num_calls variable, the Cultists will deal
    1 extra damage. With the exception of the second attack which
    deals sets the base damage to 6 + number of calls. There is also a 50%
    chance that a weak status modifier will be applied to the player on attack.

    """
    # Initialises the number of calls variable of Cultist to allow iteration.
    _num_calls = 0

    def __init__(self, max_hp: int) -> None:
        """Initialises the Cultist subclass and its parent classes. 

        Args:
            max_hp (int): The maximum hp value which will be given to
                this Cultist instance.
        """
        super().__init__(max_hp)

    def action(self) -> dict[str, int]:
        """Returns a dictionary containing damage and weak amount, damage will
        increase by 1 for each attack of Cultist that occurs. 
        Weak iterates between 0 and 1.

        This method returns a dictionary of {'damage': damage_amount,
        'weak': weak_amount}. For each Cultist instance, 
        damage_amount is 0 the first time action is called. 
        For each subsequent call to action, damage_amount = 6 + num_calls, 
        where num_calls is the number of times the action method 
        has been calledon this specific Cultist instance. 
        The weak_amount alternates between 0 and 1 each time the action method 
        is called on a specific Cultist instance, 
        starting at 0 for the first call.

        Returns:
            dict[str, int]: Damage and weak amount generated by the method, in
                the format of {'damage': damage_amount,'weak': weak_amount}.

        Example:
            >>> cultist = Cultist(20)
            >>> cultist.action()
            {'damage': 0, 'weak': 0}
            >>> cultist.action()
            {'damage': 7, 'weak': 1}
            >>> cultist.action()
            {'damage': 8, 'weak': 0}
            >>> cultist.action()
            {'damage': 9, 'weak': 1}
        """
        if self._num_calls == 0:
            self.damage_amount = 0
        if self._num_calls == 1:
            self.damage_amount = 6 + 1
        if self._num_calls > 1:
            self.damage_amount += 1
        if self._num_calls == 0:
            self.weak_amount = 1
        if self.damage_amount % 2 != 0:
            self.weak_amount = 1
        elif self.damage_amount % 2 == 0:
            self.weak_amount = 0
        self._num_calls += 1
        damage_amount = self.damage_amount
        weak_amount = self.weak_amount
        return {'damage': damage_amount, 'weak': weak_amount}


class JawWorm(Monster):
    """A subclass of Monster which represents the JawWorm monster type in-game.

    The JawWorm subclass is unqiue because its action method is based off how
    much health it has lost. Half of the health lost is rounded up and returned
    as damage. And half is rounded down and applied as block to itself.
    """

    def __init__(self, max_hp: int) -> None:
        """Initialises the JawWorm subclass and its parent classes.

        Args:
            max_hp (int): The maximum hp value which will be given to
                this JawWorm instance.
        """
        super().__init__(max_hp)

    def action(self) -> dict[str, int]:
        """Returns a dictionary of a damage amount equal to half of its health
        lost so far (rounded up), and applies block amount (to itself)
        also equal to half of its health lost (rounded down).

        Each time action is called on a JawWorm instance,
        the following effects occur:
        - Half of the amount of damage the jaw worm has taken so far 
        (rounding up) is added to the jaw worm's own block amount.
        - Half of the amount of damage the jaw worm has taken so far 
        (rounding down) is used for damage to the target.
        - The amount of damage taken so far is the difference between 
        the jaw worm's maximum HP and its current HP.

        Returns:
            dict[str, int]: The generated damage amount in the format of
                {'damage': damage_to_deal}.

        Example:
            >>> jaw_worm = JawWorm(20)
            >>> jaw_worm.get_block()
            0
            >>> jaw_worm.action()
            {'damage': 0}
            >>> jaw_worm.get_block()
            0
            >>> jaw_worm.reduce_hp(11)
            >>> jaw_worm.action()
            {'damage': 5}
            >>> jaw_worm.get_block()
            6
        """
        self.damage_amount = -(super().get_hp() - super().get_max_hp()) / 2
        block_to_add = self.damage_amount.__ceil__()
        super().add_block(block_to_add)
        damage_to_deal = self.damage_amount.__floor__()
        return {'damage': damage_to_deal}


class Encounter:
    """
    Each encounter in the game is represented as an instance of the Encounter 
    class. This class manages one player and a set of 1 to 3 monsters, and 
    facilitates the interactions between the player and monsters.
    """

    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        The initializer for an encounter takes the player instance,
        as well as a list of tuples describing the monsters in the encounter. 
        Each tuple contains the name (type) of monster and the monster's max HP.
        The initializer should use these tuples to construct monster instances 
        in the order in which they are described. The initializer should also 
        tell the player to start a new encounter 
        (see Player.start_new_encounter), and should also start a new turn 
        (see start_new_turn below for a description)

        Args:
            player (Player): Identifies the player subclass to be used.
            monsters (list[tuple[str, int]]): List of tuples which identify 
                the monsters. The tuples should be in the format of 
                ('monster_name', monster_max_hp).

        """
        # Initialises a variable which will be used to determine whether its the
        # player or the monster turn.       'p' = player, 'm' = monster
        self._whos_turn = ''
        if player == 'ironclad':
            self.player = IronClad()
        if player == 'silent':
            self.player = Silent()
        else:
            self.player = player
        self.start_monsters = []
        for items in monsters:
            monster_name, monster_max_hp = items
            self.start_monsters.append(globals()[monster_name](monster_max_hp))
        player.start_new_encounter()
        self.start_new_turn()
        return None

    def start_new_turn(self) -> None:
        """Starts new turn, sets to player's turn.

        This method sets it to be the player's turn (i.e. 
        the player is permitted to attempt to apply cards) and calls
        new_turn on the player instance.

        Example:
            >>> player = Silent()
            >>> monsters = [('Louse', 10)]
            >>> encounter = Encounter(player, monsters)
            >>> encounter.start_new_turn()
        """
        self._whos_turn = 'p'
        self.player.new_turn()
        return None

    def end_player_turn(self) -> None:
        """Ends the player's turn and starts the monster's turn.

        This method sets it to not be the player's turn (i.e. the player is not 
        permitted to attempt to apply cards), and ensures all cards remaining 
        in the player's hand move into their discard pile. This method also 
        calls the new_turn method on all monster instances remaining in the 
        encounter.

        Example:
            >>> player = Silent()
            >>> monsters = [('Louse', 10)]
            >>> encounter = Encounter(player, monsters)
            >>> encounter.start_new_turn()
            >>> encounter.end_player_turn()
        """
        self._whos_turn = 'm'
        self.player.end_turn()
        for monster in self.get_monsters():
            monster.new_turn()
        return None

    def get_player(self) -> Player:
        """Returns the player in this encounter.

        Returns:
            Player: The Player Class that exists in this encounter.

        Example:
            >>> player = Silent()
            >>> monsters = [('Louse', 10)]
            >>> encounter = Encounter(player, monsters)
            >>> encounter.get_player()
            Silent()
        """
        return self.player

    def get_monsters(self) -> list[Monster]:
        """Returns the monsters remaining in this encounter.

        Returns:
            list[Monster]: A list of the Monsters that exist and are not
                defeated in this encounter.

        Example:
            >>> player = Silent()
            >>> monsters = [('Louse', 10)]
            >>> encounter = Encounter(player, monsters)
            >>> encounter.get_monsters()
            [Louse(10)]

        """
        self.monsters_remaining = []
        for monster in self.start_monsters:
            if monster.is_defeated() == False:
                self.monsters_remaining.append(monster)
        return self.monsters_remaining

    def is_active(self) -> bool:
        """Returns True if there are monsters remaining in this encounter, 
        and False otherwise.

        Returns:
            bool: True if monsters are still alive in this encounter, 
                false otherwise.

        Example:
            >>> player = Silent()
            >>> monsters = [('Louse', 10)]
            >>> encounter = Encounter(player, monsters)
            >>> encounter.is_active() == True
            True
            >>> another_encounter = Encounter(Silent(), [])
            >>> another_encounter.is_active() == False
            True
        """
        if self.get_monsters() != []:
            return True
        else:
            return False

    def player_apply_card(self, card_name: str,
                          target_id: int | None = None) -> bool:
        """Attempts to play card from hand.

        This method attempts to apply the first card with the given name from 
        the player's hand (where relevant, the target for the card is 
        specified by the given target_id).

        Args:
            card_name (str): The name of the card to be played.
            target_id (int | None, optional): The id of the target of the card.
                Defaults to None.

        Returns:
            bool: True if card is played successfully, False otherwise.

        Example:
        >>> player = Silent()
        >>> monsters = [('Louse', 10)]
        >>> encounter = Encounter(player, monsters)
        >>> player.get_hand()
        [Survivor(), Strike(), Strike(), Neutralize(), Defend()]
        >>> encounter.player_apply_card("Survivor", 0)
        True
        """
        # Check to see if its the player's turn.
        if self._whos_turn != 'p':
            return False

        # Check to see if player has the card in their hand.
        for cards in self.player.get_hand():
            if cards.get_name() == card_name:
                card = cards
                break
        else:
            return False

        # Assign requires_target result to prevent calling again
        requires_target = card.requires_target()

        # Check if the Card requires a target. If it does,
        # ensure a valid target_id is provided.
        if requires_target:
            if target_id == None:
                return False
            else:
                for monster in self.get_monsters():
                    if monster.get_id() == target_id:
                        break
                else:
                    return False

        # Attempt to play the card.
        if self.player.play_card(card.get_name()) != card:
            return False

        # Add any block and strength from the card to the player.
        self.player.add_block(card.get_block())
        self.player.add_strength(card.get_strength())

        # Get any vulnerable or weakness effects the card may have.
        weak_effect = card.get_status_modifiers().get("weak")
        vuln_effect = card.get_status_modifiers().get("vulnerable")
        if weak_effect == None:
            weak_effect = 0
        if vuln_effect == None:
            vuln_effect = 0

        # Apply any vulnerable or weakness effects to the target.
        if requires_target:
            for mon in self.get_monsters():
                if mon.get_id() == target_id:
                    mon.add_vulnerable(vuln_effect)
                    mon.add_weak(weak_effect)
                    target = mon
                    break
            else:
                return False

        # Calculate and apply damage amount.
        if requires_target:
            damage_multi = 1
            if target.get_vulnerable() > 0:
                damage_multi *= 1.5
            if self.player.get_weak() > 0:
                damage_multi *= 0.75
            damage_amount = (int((card.get_damage_amount()
                                  + self.player.get_strength()) * damage_multi))
            target.reduce_hp(int(damage_amount))

            # Update list of remaining monsters.
            if target.is_defeated():
                self.get_monsters()

        return True

    def enemy_turn(self) -> None:
        """Plays monsters turns.

        This method attempts to allow all remaining monsters 
        in the encounter to take an action. This method
        immediately returns if it is the player's turn. 

        Example:
        >>> player = Silent()
        >>> monsters = [('Louse', 10)]
        >>> encounter = Encounter(player, monsters)
        >>> encounter.get_player().get_hp()
        70
        >>> encounter.end_player_turn()
        >>> encounter.enemy_turn()
        >>> encounter.get_player().get_hp()
        64 
        """
        if self._whos_turn == 'p':
            return None
        for mon in self.get_monsters():
            action = mon.action()
            per_mon_damage = action.get("damage", 0)
            if "weak" in action:
                self.player.add_weak(action.get("weak", 0))
            if "vulnerable" in action:
                self.player.add_vulnerable(action.get("vulnerable", 0))
            if "strength" in action:
                mon.add_strength(action.get("strength", 0))
            if mon.get_strength() > 0:
                per_mon_damage += mon.get_strength()
            if self.player.get_vulnerable() > 0:
                per_mon_damage *= 1.5
            if mon.get_weak() > 0:
                per_mon_damage *= 0.75
            self.player.reduce_hp(per_mon_damage)
        self.start_new_turn()
        return None


def main():
    """Runs the main logic of the program."""

    def mv_get_description(user_input: str) -> None:
        """
        When the user enters this command, the description for the card
        with the given card_name should be printed. The description of the card
        will be printed even if the player does
        not have an instance of the requested card. 

        Args:
            user_input (str): The input that will be interpreted.
        """
        card = user_input.split()[1]
        if card in cards:
            selected_card = cards.get(card)
            print(f"\n{selected_card.get_description()}", end="\n\n")
        return None

    def mv_end_turn(user_input: str) -> None:
        """
        When the user enters this command, the player's turn will end,
        and the enemy turn will run. If the player is defeated after the
        enemy turn, the game will terminate with the game lose message.
        Otherwise the resulting encounter state is displayed.

        Args: 
            user_input (str): This is not used here and is only implemented so 
            the same command can be used for all move types.
        """
        encounter.end_player_turn()
        encounter.enemy_turn()
        if player.get_hp() == 0:
            return None
        display_encounter(encounter)
        return None

    def mv_inspect(user_input: str) -> None:
        """Plays the inspect move.

        When the user enters 'inspect deck', the player's deck should be
        printed. When the user enters 'inspect discard', the player's discard
        pile should be printed.

        Args:
            user_input (string): The input that will be interpreted.
        """
        if user_input.split()[1] == "deck":
            print(f"\n{encounter.player.get_deck()}", end="\n\n")
        if user_input.split()[1] == "discard":
            print(f"\n{encounter.player.get_discarded()}", end="\n\n")
        return None

    def mv_play(user_input: str) -> None:
        """Tries to convert the user input into a play card command.

        Attempts to play a card. If the card application fails for any
        reason, the card failure message is printed. Otherwise if
        the card is successfully applied, the resulting encounter state is
        printed. It is assumed that if a target_id is entered it will
        be an integer, but not that a monster with that ID exists in the
        encounter.

        Args:
            user_input (string): The input that will be interpreted.
        """
        input = user_input.split()
        if len(input) == 2:
            card_name = input[1]
            if (not encounter.player_apply_card(card_name)
                    and encounter.is_active()):
                print(CARD_FAILURE_MESSAGE)
            else:
                display_encounter(encounter)
        if len(input) == 3:
            card_name = input[1]
            target_id = int(input[2])
            if encounter.player_apply_card(card_name, target_id):
                display_encounter(encounter)
            else:
                if encounter.is_active():
                    print(CARD_FAILURE_MESSAGE)
        return None

    # List of all the cards avaliable in the game. For mv_get_description.
    cards = {
        "Strike": Strike(),
        "Defend": Defend(),
        "Bash": Bash(),
        "Survivor": Survivor(),
        "Neutralize": Neutralize()
    }

    # Dictionary of the possibles user input moves.
    moves = {
        "describe": mv_get_description,
        "end": mv_end_turn,
        "inspect": mv_inspect,
        "play": mv_play
    }

    # Get player type and game file from user. Get encounters from game file.
    player = input("Enter a player type: ")
    game_file = input("Enter a game file: ")
    encounters = read_game_file(game_file)

    # Init the persistent player class.
    if player == "silent":
        player = Silent()
    if player == "ironclad":
        player = IronClad()

    # Play through all encounters manually.
    for enc_mons in encounters:
        if player.get_hp() == 0:
            break
        print("New encounter!\n")
        encounter = Encounter(player, enc_mons)
        display_encounter(encounter)

        # Continually prompt for and play user moves.
        while encounter.is_active() and player.get_hp() > 0:
            user_input = input("Enter a move: ")
            if user_input.split()[0] in moves:
                moves.get(user_input.split()[0])(user_input)
            if not encounter.is_active():
                player.end_turn()
                print(f"{ENCOUNTER_WIN_MESSAGE}", end="\n")

    # Print if the player won or lost.
    if player.get_hp() == 0:
        print(f"{GAME_LOSE_MESSAGE}", end="\n")
    if player.get_hp() > 0:
        print(f"{GAME_WIN_MESSAGE}", end="\n")


if __name__ == "__main__":
    main()
