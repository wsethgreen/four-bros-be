from flask import Blueprint
from src.controllers.PlayersController import PlayersController

players_bp = Blueprint('players', __name__)
PlayersController = PlayersController()

@players_bp.route('', methods=['GET'])
def get_all():
    return PlayersController.get_all_players()

@players_bp.route('/<player_id>', methods=['GET'])
def get_by_player_id(player_id: str) -> dict:
    return PlayersController.get_player_by_player_id(player_id)


@players_bp.route('/player_of_the_week', methods=['GET'])
def get_player_of_the_week() -> dict:
    return PlayersController.get_player_of_the_week()

@players_bp.route('hof', methods=['GET'])
def get_hof() -> dict:
    return PlayersController.get_hof()
