import requests
import os
import zipfile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

dir = 'downloads'
parent_dir = '/app/'


def create_dir(new_dir, parent_dir):
    path = os.path.join(parent_dir, new_dir)

    try:
        os.mkdir(path)
    except OSError as error:
        print(error)


def get_filename(inp):
    url = inp
    if url.find('/'):
        filename = url.rsplit('/', 1)
        return filename[1]


def unzip_file(inp):
    with zipfile.ZipFile(f'downloads/{inp}', 'r') as zip_ref:
        zip_ref.extractall('downloads/')


def main():
    create_dir(dir, parent_dir)

    for url in download_uris:
        filename = get_filename(url)
        print(filename)
        r = requests.get(url)
        if r.status_code == 200:
            open(f'downloads/{filename}', 'wb').write(r.content)
            print('file downloaded', r.status_code)
            unzip_file(filename)
            os.remove(f'downloads/{filename}')
        else:
            print(f'file not found for url {url}')
    # unzip_file(filename)
    # os.remove(f'downloads/{filename}')
    print('done')


if __name__ == '__main__':
    main()
