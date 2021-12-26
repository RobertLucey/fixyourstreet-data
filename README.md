# Fixyourstreet data

Tools for working with fixyourstreet.ie data

## Usage

Before working with any data you must first pull. Do this by running `update_fixyourstreet_data`. Do this every now and then to keep the data fresh,


```python
>>> from fixyourstreet_data.utils import get_reports
>>> reports = get_reports()
>>> reports[0].serialize()
{
    'incident': {
        'incidentid': 1,
        'incidentactive': 1,
        'incidentdate': '2021-12-25 01:00:00',
        'incidentdescription': 'Household rubbish dumped Submitted via EPA/NIECE Smartphone App. #Waste/IllegalDumping -- posted via the fixyourstreet.ie public api',
        'incidentmode': 1,
        'incidenttitle': 'Waste/Illegal Dumping',
        'incidentverified': 0,
        'incidentlocation': {
            'locationid': 1,
            'locationlatitude': 52.00000,
            'locationlongitude': -7.00000,
            'locationname': 'Near the building entrance',
            'geo': {
                'lat': '52.15139',
                'lon': '-6.98611',
                'name': 'Dunmore East',
                'admin1': 'Munster',
                'admin2': 'Waterford',
                'cc': 'IE'
            }
        }
    },
    'media': {
        'id': 123,
        'type': 1,
        'link': '111111_1_1111111111.jpg',
        'thumb': '111111_1_1111111111_t.jpg'
    },
    'categories': [
        {
            'category': {
                'id': 6,
                'title': 'Litter and Illegal Dumping',
                'label': 'litter_and_illegal_dumping'
            }
        }
    ]
}
```
