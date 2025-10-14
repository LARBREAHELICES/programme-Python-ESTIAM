import random

# ===============================
# 1. Définition des classes
# ===============================

class Character:
    """Base class representing any character in the game."""

    def __init__(self, name: str, health: int, attack: int, defense: int):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self) -> bool:
        """Return True if the character still has health points."""
        return self.health > 0

    def take_damage(self, amount: int):
        """Reduce health when the character takes damage."""
        self.health = max(0, self.health - amount)

    def heal(self, amount: int):
        """Heal the character (used by the Knight)."""
        self.health += amount


class Knight(Character):
    """The player-controlled character."""

    def choose_action(self) -> str:
        """Display available actions and return the player's choice."""
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Heal")
        choice = input("Choose your action: ")
        return choice.strip()


class Dragon(Character):
    """The enemy, controlled by the computer."""
    pass


# ===============================
# 2. Game logic functions
# ===============================

def compute_damage(attacker: Character, defender: Character) -> int:
    """Compute the damage dealt by one character to another.
    A small random variation is applied to simulate luck."""
    base_damage = attacker.attack - defender.defense
    variation = random.randint(-3, 3)  # Adds randomness
    damage = max(0, base_damage + variation)
    defender.take_damage(damage)
    return damage


def player_turn(player: Knight, enemy: Dragon):
    """Handle the player's turn: attack or heal."""
    choice = player.choose_action()

    if choice == "1":
        damage = compute_damage(player, enemy)
        print(f"{player.name} attacks and deals {damage} damage to {enemy.name}.")
    elif choice == "2":
        heal_amount = random.randint(10, 20)
        player.heal(heal_amount)
        print(f"{player.name} heals for {heal_amount} HP.")
    else:
        print("Invalid action! You lose your turn.")


def dragon_turn(dragon: Dragon, player: Knight):
    """Handle the dragon's automatic attack."""
    print("\n--- Dragon's Turn ---")
    damage = compute_damage(dragon, player)
    print(f"{dragon.name} attacks and deals {damage} damage to {player.name}.")


# ===============================
# 3. Main game loop
# ===============================

def main():
    """Main function controlling the game loop."""

    # Initialize characters
    player = Knight(name="Knight", health=100, attack=20, defense=10)
    dragon = Dragon(name="Dragon", health=120, attack=18, defense=8)

    print("=== Dragon vs Knight ===")
    print("A terrible dragon challenges your courage!")

    # Main game loop
    while player.is_alive() and dragon.is_alive():
        print(f"\n{player.name} HP: {player.health} | {dragon.name} HP: {dragon.health}")

        # Player's turn
        player_turn(player, dragon)
        if not dragon.is_alive():
            print(f"\n{dragon.name} is defeated. You win!")
            break

        # Dragon's turn
        dragon_turn(dragon, player)
        if not player.is_alive():
            print(f"\n{player.name} has fallen. Game over.")
            break

    print("\n=== End of the battle ===")


# ===============================
# 4. Program entry point
# ===============================

if __name__ == "__main__":
    main()