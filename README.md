# VCDS (VagCom) Interface

## Purpose of this repository:

This repository is meant to create a multiple line chart for sensor data coming from the VCDS(VagCom) software. You can use the VagCom program to record data coming from the CAN bus and generate a CSV file from that recorded session.

In my case, I had a misfire problem on my car and I wanted to see if that coincided with any other factors such as a big change in RPM.

I also wanted to illustrate the process of storing data in a db, fetching it with SQLAlchemy, and creating an html file to show it in the browser.

## How this repository is set up:
 
The data in the CSV file is read in and stored in the `Database.db` file and becomes queryable through `backend.py`

`session_reader.py` lets you specify a csv file you would like to read in - these files should exist in the `Sessions` folder

`graph.py` allows you to look into the db, create a new chart, save it in the `Charts` folder as an html file, and open it up in the browser

You can delete the contents of the db file to start over with a new session.

## Some things that can be done to improve this repository:

- allow unique sessions in the backend
- a user interface to read in new sessions and view existing data

### Dependencies:

- SQLAlchemy
- plotly
- pandas