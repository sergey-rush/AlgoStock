from threading import Thread

from Data.DataProvider import DataProvider


class DataManager:
    class __DataManager:
        def __init__(self):
            self.data_provider = DataProvider()
            self.prob_dict = {}

        def get_stock_by_stock_id(self, stock_id):
            return self.data_provider.get_stock_by_stock_id(stock_id)

        def insert_stock(self, stock):
            return self.data_provider.insert_stock(stock)

        def get_stocks(self):
            return self.data_provider.get_stocks()

        def get_probs(self):
            if len(self.prob_dict) == 0:
                probs = self.data_provider.get_probs()
                for prob in probs:
                    keyword = prob[0]
                    ratio = prob[1]
                    discount = float(prob[2])
                    self.prob_dict[(keyword, ratio)] = discount
                return self.prob_dict
            else:
                return self.prob_dict

        def insert_prob(self, keyword, ratio, discount):
            return self.data_provider.insert_prob(keyword, ratio, discount)

        def save_temp_probs(self):
            if len(self.prob_dict) > 0:
                self.prob_dict = {}
            return self.data_provider.save_temp_probs()

        def copy_probs_from_file(self):
            return self.data_provider.copy_probs_from_file()

        def get_players_by_game_id(self, game_id):
            return self.data_provider.get_players_by_game_id(game_id)

        def get_player_by_player_id(self, player_id):
            return self.data_provider.get_player_by_player_id(player_id)

        def insert_player(self, game_id, player_name, keyword, landlord, winner, stock_id, seat, total, set_count):
            return self.data_provider.insert_player(game_id, player_name, keyword, landlord, winner, stock_id, seat, total, set_count)

        def update_player(self, winner, player_id):
            return self.data_provider.update_player(winner, player_id)

        def get_game_by_game_id(self, game_id):
            return self.data_provider.get_game_by_game_id(game_id)

        def get_games_by_stock_id(self, stock_id):
            return self.data_provider.get_games_by_stock_id(stock_id)

        def insert_game(self, stock_id):
            return self.data_provider.insert_game(stock_id)

        def update_game(self, stock_id, game_id):
            self.data_provider.update_game(stock_id, game_id)

        def get_plays_by_game_id(self, game_id):
            return self.data_provider.get_plays_by_game_id(game_id)

        def get_plays_by_limit(self, limit):
            return self.data_provider.get_plays_by_limit(limit)

        def insert_play(self, game_id, attack_set, defend_set, result, attacker_id, defender_id, attack_hand, defend_hand, stock_id, attacker_name, defender_name):
            return self.data_provider.insert_play(game_id, attack_set, defend_set, result, attacker_id, defender_id, attack_hand, defend_hand, stock_id, attacker_name, defender_name)

    instance = None

    def __init__(self):
        if not DataManager.instance:
            DataManager.instance = DataManager.__DataManager()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_instance(self):
        return self.instance
