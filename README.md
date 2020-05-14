# SQL dev project

config.py is ignored


import.py

This script is used to import data into the tables set up with the sql files using sqlalchemy.
Requires:
    1. database is setup with tables
    2. database is active
    3. URI is properly configured in config.py
    4. data files are in the data directory

This script has an extremely long output so suggested to run as:
```
python import.py > output.txt
```
Or:
```
python import.py | less
```
