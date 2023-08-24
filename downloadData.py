from kaggle.api.kaggle_api_extended import KaggleApi

location = "cviaxmiwnptr/nfl-team-stats-20022019-espn"
csv = "nfl_team_stats_2002-2022.csv"

api = KaggleApi()
api.authenticate()

api.dataset_download_file(location, csv)