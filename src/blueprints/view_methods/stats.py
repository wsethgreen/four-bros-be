from typing import List

from src.constants import session
from src.data_models.DefensiveStats import DefensiveStats
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.WeekYear import WeekYear
from src.helpers import(
    _get_player_defensive_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_rushing_stats
)
from src.models.Stats import(
    PlayerDefensiveStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerRushingStats
)
from src.responses.Stats import(
    PlayerDefensiveStatsSchema,
    PlayerPassingStatsSchema,
    PlayerReceivingStatsSchema,
    PlayerRushingStatsSchema
)


# Schemas to deserialize objects
defensive_stat_schema = PlayerDefensiveStatsSchema()
defensive_stats_schema = PlayerDefensiveStatsSchema(many=True)
passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)
receiving_stat_schema = PlayerReceivingStatsSchema()
receiving_stats_schema = PlayerReceivingStatsSchema(many=True)
rushing_stat_schema = PlayerRushingStatsSchema()
rushing_stats_schema = PlayerRushingStatsSchema(many=True)


def get_season_defense_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and DefensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, DefensiveStats).filter(
            PlayerInfo.id == DefensiveStats.player_id,
            DefensiveStats.year == week_year.year
            ).all()
    
    player_objects: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in players]

    # Sort players based on passing stat categories
    long_int_ret_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.long_int_ret, reverse=True)[:10]
    sacks_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.sacks, reverse=True)[:10]
    forced_fumbles_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.forced_fumbles, reverse=True)[:10]
    solo_tkls_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.solo_tkls, reverse=True)[:10]
    safeties_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.safeties, reverse=True)[:10]
    pass_def_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.pass_def, reverse=True)[:10]
    blocked_kicks_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.blocked_kicks, reverse=True)[:10]
    tfl_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.tfl, reverse=True)[:10]
    ints_made_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.ints_made, reverse=True)[:10]
    fumbles_rec_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.fumbles_rec, reverse=True)[:10]
    half_a_sack_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.half_a_sack, reverse=True)[:10]
    asst_tkls_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.asst_tkls, reverse=True)[:10]
    def_tds_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.def_tds, reverse=True)[:10]
    fum_rec_yards_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.fum_rec_yards, reverse=True)[:10]
    int_ret_yards_leaders = sorted(player_objects, key=lambda p: p.defensive_stats.int_ret_yards, reverse=True)[:10]
    # Convert top ten lists into json
    long_int_ret_leaders_json = defensive_stats_schema.dump(long_int_ret_leaders)
    sacks_leaders_json = defensive_stats_schema.dump(sacks_leaders)
    forced_fumbles_leaders_json = defensive_stats_schema.dump(forced_fumbles_leaders)
    solo_tkls_leaders_json = defensive_stats_schema.dump(solo_tkls_leaders)
    safeties_leaders_json = defensive_stats_schema.dump(safeties_leaders)
    pass_def_leaders_json = defensive_stats_schema.dump(pass_def_leaders)
    blocked_kicks_leaders_json = defensive_stats_schema.dump(blocked_kicks_leaders)
    tfl_leaders_json = defensive_stats_schema.dump(tfl_leaders)
    ints_made_leaders_json = defensive_stats_schema.dump(ints_made_leaders)
    fumbles_rec_leaders_json = defensive_stats_schema.dump(fumbles_rec_leaders)
    half_a_sack_leaders_json = defensive_stats_schema.dump(half_a_sack_leaders)
    asst_tkls_leaders_json = defensive_stats_schema.dump(asst_tkls_leaders)
    def_tds_leaders_json = defensive_stats_schema.dump(def_tds_leaders)
    fum_rec_yards_leaders_json = defensive_stats_schema.dump(fum_rec_yards_leaders)
    int_ret_yards_leaders_json = defensive_stats_schema.dump(int_ret_yards_leaders)

    response = {
        'long_int_ret_leaders': long_int_ret_leaders_json,
        'sacks_leaders': sacks_leaders_json,
        'forced_fumbles_leaders': forced_fumbles_leaders_json,
        'solo_tkls_leaders': solo_tkls_leaders_json,
        'safeties_leaders': safeties_leaders_json,
        'pass_def_leaders': pass_def_leaders_json,
        'blocked_kicks_leaders': blocked_kicks_leaders_json,
        'tfl_leaders': tfl_leaders_json,
        'ints_made_leaders': ints_made_leaders_json,
        'fumbles_rec_leaders': fumbles_rec_leaders_json,
        'half_a_sack_leaders': half_a_sack_leaders_json,
        'asst_tkls_leaders': asst_tkls_leaders_json,
        'def_tds_leaders': def_tds_leaders_json,
        'fum_rec_yards_leaders': fum_rec_yards_leaders_json,
        'int_ret_yards_leaders': int_ret_yards_leaders_json
    }

    return response


def get_season_passing_stats(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            OffensiveStats.player_id == PlayerInfo.id,
            OffensiveStats.year == week_year.year
        ).all()

    converted_players: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]

    players_json = passing_stats_schema.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_season_passing_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()

    # Convert players to PlayerPassingStats model so they can be sorted
    player_objects: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]
    # Sort players based on passing stat categories
    completions_leaders = sorted(player_objects, key=lambda p: p.passing_stats.completions, reverse=True)[:10]
    pass_att_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_att, reverse=True)[:10]
    longest_pass_leaders = sorted(player_objects, key=lambda p: p.passing_stats.longest_pass, reverse=True)[:10]
    pass_yards_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_yards, reverse=True)[:10]
    pass_td_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_tds, reverse=True)[:10]
    int_leaders = sorted(player_objects, key=lambda p: p.passing_stats.ints, reverse=True)[:10]
    # Convert top ten lists into json
    completions_leaders_json = passing_stats_schema.dump(completions_leaders)
    pass_att_leaders_jason = passing_stat_schema.dump(pass_att_leaders)
    longest_pass_leaders_jason = passing_stat_schema.dump(longest_pass_leaders)
    pass_yard_leaders_json = passing_stats_schema.dump(pass_yards_leaders)
    pass_td_leaders_json = passing_stats_schema.dump(pass_td_leaders)
    int_leaders_json = passing_stats_schema.dump(int_leaders)


    response = {
        'completions': completions_leaders_json,
        'pass_att': pass_att_leaders_jason,
        'longest_pass': longest_pass_leaders_jason,
        'pass_yards': pass_yard_leaders_json,
        'pass_tds': pass_td_leaders_json,
        'interceptions': int_leaders_json
    }

    return response


def get_season_receiving_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()
    # Convert players to PlayerReceivingStats model so they can be sorted
    player_objects: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in players]

    # Sort by category
    reception_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.receptions, reverse=True)[0:10]
    rec_yards_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.rec_yards, reverse=True)[0:10]
    rec_tds_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.rec_tds, reverse=True)[0:10]
    yac_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.yac, reverse=True)[0:10]
    drops_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.drops, reverse=True)[0:10]

    # Convert top ten lists to json
    reception_leaders_json = receiving_stats_schema.dump(reception_leaders)
    rec_yards_leaders_json = receiving_stats_schema.dump(rec_yards_leaders)
    rec_tds_leaders_json = receiving_stats_schema.dump(rec_tds_leaders)
    yac_leaders_json = receiving_stats_schema.dump(yac_leaders)
    drops_leaders_json = receiving_stats_schema.dump(drops_leaders)

    response = {
        'receptions': reception_leaders_json,
        'rec_yards': rec_yards_leaders_json,
        'rec_tds': rec_tds_leaders_json,
        'yac': yac_leaders_json,
        'drops': drops_leaders_json
    }

    return response


def get_season_rushing_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()

    # Convert players to PlayerPassingStats model so they can be sorted
    player_objects: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in players]

    # Sort
    rush_att_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.rush_att, reverse=True)[:10]
    rush_yards_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.rush_yards, reverse=True)[:10]
    ya_contact_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.ya_contact, reverse=True)[:10]
    broke_tkls_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.broke_tkls, reverse=True)[:10]
    fumbles_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.fumbles, reverse=True)[:10]
    twenty_plus_yd_runs_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.twenty_plus_yd_runs, reverse=True)[:10]
    # Convert top ten lists to json
    rush_att_leaders_json = rushing_stats_schema.dump(rush_att_leaders)
    rush_yards_leaders_json = rushing_stats_schema.dump(rush_yards_leaders)
    ya_contact_leaders_json = rushing_stats_schema.dump(ya_contact_leaders)
    broke_tkls_leaders_json = rushing_stats_schema.dump(broke_tkls_leaders)
    fumbles_leaders_json = rushing_stats_schema.dump(fumbles_leaders)
    twenty_plus_yd_runs_leaders_json = rushing_stats_schema.dump(twenty_plus_yd_runs_leaders)

    response = {
        'rush_att': rush_att_leaders_json,
        'rush_yards': rush_yards_leaders_json,
        'ya_contact': ya_contact_leaders_json,
        'broken_tackles': broke_tkls_leaders_json,
        'fumbles': fumbles_leaders_json,
        'twenty_plus_runs': twenty_plus_yd_runs_leaders_json
    }

    return response
