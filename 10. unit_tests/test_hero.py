from unittest import TestCase, main
from hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Ivakata", 1, 100, 50)
        self.enemy_hero = Hero("Drago", 2, 100, 70)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "Ivakata")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_battle_with_yourself_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_hero_health_equal_or_below_zero_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_enemy_hero_health_equal_or_below_zero_raise_value_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ve.exception), "You cannot fight Drago. He needs to rest")

    def test_hero_damage_correct_expect_multiply_damage_and_level(self):
        result = self.hero.damage * self.hero.level
        self.hero.battle(self.enemy_hero)

        self.assertEqual(result, 50)

    def test_enemy_hero_damage_correct_expect_multiply_damage_and_level(self):
        result = self.enemy_hero.damage * self.enemy_hero.level
        self.hero.battle(self.enemy_hero)

        self.assertEqual(result, 140)

    def test_hero_health_expect_decrease_after_battle(self):
        result = self.hero.health - self.enemy_hero.damage
        self.hero.battle(self.enemy_hero)

        self.assertEqual(result, 30)

    def test_enemy_hero_health_expect_decrease_after_battle(self):
        result = self.enemy_hero.health - self.hero.damage
        self.hero.battle(self.enemy_hero)

        self.assertEqual(result, 50)

    def test_both_players_health_equal_or_below_zero_after_battle_expect_to_return_draw(self):
        self.hero.damage = 100
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(result, "Draw")

    def test_enemy_hero_with_less_or_equal_to_zero_health_after_battle_expect_hero_to_win_and_increase_stats(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 10
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 85)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_hero_with_less_or_equal_to_zero_health_after_battle_expect_hero_to_lose_and_increase_enemy_stats(self):
        self.hero.damage = 10
        self.enemy_hero.damage = 100
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(self.enemy_hero.level, 3)
        self.assertEqual(self.enemy_hero.health, 95)
        self.assertEqual(self.enemy_hero.damage, 105)
        self.assertEqual(result, "You lose")

    def test_string_method_correct(self):
        result = self.hero.__str__()
        text = f"Hero Ivakata: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 50\n"

        self.assertEqual(result, text)


if __name__ == '__main__':
    main()
