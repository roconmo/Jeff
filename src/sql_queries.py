#!/usr/bin/env python3

# DROP TABLES
airlines_table_drop = "DROP TABLE IF EXISTS jeff.airline"
countries_table_drop = "DROP TABLE IF EXISTS jeff.country"

########################################################################################
# CREATE TABLES
########################################################################################
airlines_table_create = """CREATE TABLE jeff_assign.airlines (
                            id int NOT NULL, 
                            name varchar(100) NOT NULL,
                            fk_country_id int,
                            logo varchar(150),
                            slogan varchar(200),
                            head_quarters varchar(200),
                            website varchar(150),
                            established int,
                            PRIMARY KEY(id),
                            FOREIGN KEY (fk_country_id) REFERENCES jeff_assign.countries(fk_country_id),
                            INDEX (id)
                        )"""

countries_table_create = """CREATE TABLE jeff_assign.countries (
                            fk_country_id int NOT NULL,
                            acronym varchar(2) NOT NULL,
                            name varchar(50) NOT NULL,
                            PRIMARY KEY(fk_country_id),
                            INDEX (fk_country_id)
                        )"""

######################################################################################
# INSERT RECORDS #####################################################################
######################################################################################

airlines_table_insert = """INSERT INTO jeff_assign.airlines ( 
                            id, 
                            name, 
                            fk_country_id, 
                            logo, 
                            slogan, 
                            head_quarters,
                            website,
                            established)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """

countries_table_insert = """INSERT INTO jeff_assign.countries ( 
                            fk_country_id,
                            acronym,
                            name)
                        VALUES (%s, %s, %s); """



create_table_queries = [
    countries_table_create,
    airlines_table_create
    
]

drop_table_queries = [
    airlines_table_drop,
    countries_table_drop
]
