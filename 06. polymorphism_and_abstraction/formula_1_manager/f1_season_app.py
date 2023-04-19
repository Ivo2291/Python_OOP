from formula_1_manager.formula_teams.mercedes_team import MercedesTeam
from formula_1_manager.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self, red_bull_team: RedBullTeam = None, mercedes_team: MercedesTeam = None):
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        better_pos = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. " \
               f"{better_pos} is ahead at the {race_name} race."
