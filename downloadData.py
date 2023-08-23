from kaggle.api.kaggle_api_extended import KaggleApi

location = "dubradave/nfl-draft-history-1990-present"
csv = "NFLDraftHistory.csv"

api = KaggleApi()
api.authenticate()

api.dataset_download_file(location, csv)