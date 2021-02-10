# historical-data-uploader
Download a stock's historical data
```
Usage:

csv_data = handle_data('AAPL', start=datetime(2014, 1, 2), end=datetime(2021, 2, 5))
```

```
# Adding data to csv file
csv_data.to_csv(csv_file_path)
```

```
# Uploading csv file to mediafire
upload_media()
```

```
# Removing file to prevent duplication / glitches
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)

```

