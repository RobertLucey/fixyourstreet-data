import os


BASE_DIR = '/opt/fixyourstreet_data/' if os.getenv('TEST_ENV', 'False') == 'False' else '/tmp/fixyourstreet_data'

DATA_FILE_PATH = os.path.join(BASE_DIR, 'data.csv')
