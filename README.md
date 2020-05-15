# SQL Airline Project

See available routes between two cities with Everest Travels.

Another simple quarantine project to learn some web dev and databases and to act as a reference for future project using similar technologies.

![demo image](/demo/demo.png)

## Technologies Used

* Flask 1.1.2
* Python 3.6
* Postgres 10.12
* SQLAlchemy 1.3
* Ruby Sass 3.7
* Jinja 2.11
* Bootstrap

## Use

This requires a postgres database to be setup before it will work

### Database Setup

Setup a postgres database and use this to generate a URI. Place the URI in a file called config.py in the top directory. Use the sql files to create the necessary tables in the database. Then ``` import.py ``` can be used to fill the database.

``` import.py ``` used to import data into the tables set up with the sql files using sqlalchemy.
Requires:
1. database is setup with tables
2. database is active
3. URI is properly configured in ``` config.py ```
4. data files are in the data directory

This script has an extremely long output (because it is in debug mode) so suggested to run as:
```
python import.py > output.txt
```
Or:
```
python import.py | less
```

### Web Setup

The file ``` setup.sh ``` can be sourced to set environment variable necessary for setup. Please check if these will conflict with your environment (for example, the display variable).
Source with 
```
. source.sh
```

### Run

To run the website, make sure the Postgres database is running.
This can be done using the ``` enter_pg.sh ``` script.

Then, start flask using
```
run flask 
```
and open a browser to the specified address.

When finished, make sure to stop the Postgres database using
```
sudo service postgresql stop
```

### Develop

When developing, it is useful to run ``` watch_css.sh ``` to have sass automatically update ``` style.css ``` based on changes to the sass file. 

## Data

All data is from OpenFlights and is historical. 
https://openflights.org/data.html

## Logo

Logo was made by me in Adobe Illustrator