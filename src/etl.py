import pandas as pd
import numpy as np
import mysql.connector
import MySQLdb as my
from src.sql_queries import *
import requests
import json
from src.config import KEY
from src.functions import *

def open_xl_file(file_path):
    """
    Function that receives a path and opens the excel file...
    args:
        file_path: file to be open
    returns: dataframe
    """
    try:
        """function to open a file with param keep_default_na=False: to prevent identify NA as NaN
            args:
                file_path: file to be opened and trasnformed to dataframe
            return: a dataframe with all the file content"""

        df = pd.read_excel(
            file_path, index_col=None, header=0, keep_default_na=False
        )  # keep_default_na=False: to prevent identify NA as NaN
        df = df.replace("", None)
        df = df.replace(np.nan, None)

        return df
    except PermissionError as error:
        print(
            "The file {} might be opened, please close it: {}".format(file_path, error)
        )


def get_countries(df):
    """
    Receives countries dataframe  file (https://data.europa.eu/euodp/en/data/dataset/cordisref-data)
    args:
        dataframe with all the data related to countries
    returns: dataframe with id, acronym and country name
    """
    try:
        df.insert(0, "id", range(1, 1 + len(df["acronym"])))
        df.set_index("id")
        df.columns = ["id", "acronym", "name"]
        return df
    except mysql.connector.Error as error:
        print("Unexpected error in database in get_countries(): {}".format(error))
        raise


def process_countries(cur, conn, df):
    """
    Function that inserts countries in the database
    Args:
        cur: current cursor
        conn: current connection
        df: countries dataframe    
    """
    try:
        # open countries file
        df = get_countries(df)
        country_data = df[["id", "acronym", "name"]].values.tolist()
        cur.executemany(countries_table_insert, country_data)
        conn.commit()
        print("process_countries()")

    except mysql.connector.Error as error:
        print(
            "Failed to insert record into table countries, in process_countries()".format(
                error
            )
        )
        raise
    except TypeError as error:
        print("TypeError: UnexpectedError in process_countries(): {}".format(error))
        raise
    except KeyError as error:
        print("Failed to retrieve records in process_countries(): {}".format(error))
        raise
    except ValueError as error:
        print("Failed to retrieve records in process_countries(): {}".format(error))
        raise

def process_airlines():
    
    url = 'https://api.instantwebtools.net/v1/airlines'
    json_file = requests.get(url)

    my_dict=json.loads(json_file.text)
    return my_dict

def execute_queries(cur, conn):
    try:
        #########################################################################################################
        # paths
        #########################################################################################################
        countries_path = "C:/Users/rosalia/OneDrive - BARRABES/Escritorio/JEFF/data/countries.xls"
        process_countries(cur, conn, open_xl_file(countries_path))
        #process_airlines(cur, conn)

    except NameError as error:
        print("Failed to open file {}".format(error))

def process_etl():
    conn = mysql.connector.connect(
        host=KEY.get('host'),
        user=KEY.get('user'),
        password=KEY.get('password'),
        auth_plugin="mysql_native_password",
    )

    cur = conn.cursor()
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    print("Tables created")

    execute_queries(cur, conn)

    conn.close()
    print("Tables created")
