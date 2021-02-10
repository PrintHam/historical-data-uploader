from pandas_datareader import data
from mediafire import MediaFireApi, MediaFireUploader
import os
import random


# Returns the stock's historical data from "x" to "y" date
def handle_data(symbol, start, end):
    stock_data = data.DataReader(
        symbol,
        'yahoo',
        start,
        end)

    return stock_data


def upload_media(csv_file_path, ticker):
    # Authentication
    api = MediaFireApi()
    session = api.user_get_session_token(
        email=os.environ['EMAIL'],
        password=os.environ['PASSWORD'],
        app_id=os.environ['app_id']
    )
    api.session = session

    try:

        uploader = MediaFireUploader(api=api)
        csv_file = open(csv_file_path, 'rb')
        result = uploader.upload(csv_file,
                                 f'{ticker}\'s Historical Data {random.randint(2000, 38410875)}).csv')

        upload_dict = api.file_get_info(result.quickkey)
        dict(upload_dict)
        link = upload_dict['file_info']['links']

        print(*link.values())

        return link['normal_download']

    except:

        return False
