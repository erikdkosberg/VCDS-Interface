# VCDS (VagCom) Interface

USAGE:

This program works by running log.py via python log.py

It assumes that you have generated a 'session' csv file

What it does is load the session into SQL Alchemy (Database.db) via 'backend.py'; it then utilizes 'graph.py' to create a combined line chart of all the data.

PURPOSE:
 
To be able to drill down on correlated data.

ENHANCEMENTS:

Converting the scaling based on tolerances

DEPENDENCIES:

python3+

pip install SQLAlchemy

pip install plotly
