# Scrape-Crossfit-Gyms

This is a commissioned scraping project to scrape the crossfit gym data.

## Data

Encoded: UTF-8

**Note**: Not all data is reported on every gym (most gyms have all the data). The only fields that may not be reported are the following fields: state, full_state, lat, long, zipcode, city, and address.

## Installation

You need requests run 
```
pip install -r requirements.txt
```

or
```
pip install requests
```

## Running

Run
```
python main.py
```

## Output

Outputs to [output.csv](output.csv). Example is [here](output.csv)


**Headers**:
```
website,photo,ready_to_link,ordernum,lat,lon,city,name_search,photo_version,zip,country_short_code,bad_standing,effective_date,status,address,active,state_code,show_on_map,kids,name,country,org_type,aid,full_state
```