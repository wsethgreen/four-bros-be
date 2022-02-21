from typing import List
from sqlalchemy import LABEL_STYLE_DISAMBIGUATE_ONLY
from sqlalchemy.sql import exists

from data import(
    def_stats,
    player_info,
    off_stats,
    team_info,
    week_year
)
from constants import(
    Base,
    engine,
    session
)
from data_models.DefensiveStats import DefensiveStatsData
from data_models.PlayerInfo import PlayerInfoData
from data_models.OffensiveStats import OffensiveStatsData
from data_models.TeamInfo import TeamInfoData

from responses.Stats import PassingStatsSchema
from responses.Players import PlayerSchema


passing_stat_schema = PassingStatsSchema()
passing_stats_schema = PassingStatsSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


jared_yates = session.query(PlayerInfoData).filter(PlayerInfoData.id == 8106).one()
print(jared_yates)
jared_yates_off_stats = session.query(OffensiveStatsData).filter(OffensiveStatsData.player_id == jared_yates.id).one()
print(jared_yates_off_stats)

players = PlayerInfoData.query.join(OffensiveStatsData, PlayerInfoData.id == OffensiveStatsData.player_id)

players_json = passing_stats_schema.dump(players)

print(players_json)


### 
# Check for length of dictionary records compared to DB records
###

# print(f'Team Dict Records: {len(team_info)}')
# print(f'Team DB Records: {len(teams)}')
# print(f'Player Info Dict Records: {len(player_info)}')
# print(f'Player Info DB Records: {len(players)}')
# print(f'Player Def Stats Dict Records: {len(def_stats)}')
# print(f'Player Def Stats DB Records: {len(defensive_stats_all)}')
# print(f'Player Off Stats Dict Records: {len(off_stats)}')
# print(f'Player Off Stats DB Records: {len(offensive_stats_all)}')
