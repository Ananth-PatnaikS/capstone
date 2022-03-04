create_airport = """
CREATE TABLE IF NOT EXISTS public.airport (
    iata_code    VARCHAR,
    name         VARCHAR,
    type         VARCHAR,
    local_code   VARCHAR,
    coordinates  VARCHAR,
    city         VARCHAR,
    elevation_ft FLOAT,
    continent    VARCHAR,
    iso_country  VARCHAR,
    iso_region   VARCHAR,
    municipality VARCHAR,
    gps_code     VARCHAR
);
"""

drop_airport = "DROP TABLE IF EXISTS airport;"

airports_insert =("""
INSERT INTO airport (iata_code, name, type, local_code, coordinates, city, elevation_ft, continent, \
    iso_country, iso_region, municipality, gps_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
create_demographic = """
CREATE TABLE IF NOT EXISTS public.demographic (
    city                   VARCHAR,
    state                  VARCHAR,
    media_age              FLOAT,
    male_population        NUMERIC,
    female_population      NUMERIC,
    total_population       NUMERIC,
    num_veterans           NUMERIC,
    foreign_born           NUMERIC,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  NUMERIC
);
"""
drop_demographic = "DROP TABLE IF EXISTS demographic;"
demographic_insert = """
INSERT INTO demographic (city, state, media_age, male_population, female_population, total_population, \
num_veterans, foreign_born, average_household_size, state_code, race, count) VALUES (%s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s)"""
create_immigration = """
CREATE TABLE IF NOT EXISTS immigration (
    cicid    FLOAT PRIMARY KEY,
    year     FLOAT,
    month    FLOAT,
    cit      FLOAT,
    res      FLOAT,
    iata     VARCHAR(3),
    arrdate  FLOAT,
    mode     FLOAT,
    addr     VARCHAR,
    depdate  FLOAT,
    bir      FLOAT,
    visa     FLOAT,
    count    FLOAT,
    dtadfile VARCHAR,
    entdepa  VARCHAR(1),
    entdepd  VARCHAR(1),
    matflag  VARCHAR(1),
    biryear  FLOAT,
    dtaddto  VARCHAR,
    gender   VARCHAR(1),
    airline  VARCHAR,
    admnum   FLOAT,
    fltno    VARCHAR,
    visatype VARCHAR
);
"""

drop_immigration = "DROP TABLE IF EXISTS immigration;"

immigrations_insert = ("""
INSERT INTO immigration (cicid, year, month, cit, res, iata, arrdate, mode, addr, depdate, bir, visa, count, dtadfile, \
entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, admnum, fltno, visatype) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""")

create_temperature = """
CREATE TABLE IF NOT EXISTS temperature (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

temperatures_insert = ("""
INSERT INTO temperature (timestamp, average_temperature, average_temperature_uncertainty, city, country, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

drop_temperature = "DROP TABLE IF EXISTS weather;"

drop_table_queries = [drop_airport, drop_demographic, drop_immigration, drop_temperature]
create_table_queries = [create_airport, create_demographic, create_immigration, create_temperature]