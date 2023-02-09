#/bin/sh

STATION_ID_TORONTO=51459
STATION_ID_VANCOUVER=51442

mkdir -p data/toronto/
mkdir -p data/vancouver/

# fetch toronto intl a data
for year in `seq 2013 2022`;
do
  for month in `seq 1 1`;
  do
    echo $year $month
    wget \
      --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${STATION_ID_TORONTO}&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" \
      -P "./data/toronto/"
  done;
done

# fetch vancouver intl a data
for year in `seq 2013 2022`;
do
  for month in `seq 1 1`;
  do
    echo $year $month
    wget \
      --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${STATION_ID_VANCOUVER}&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" \
      -P "./data/vancouver/"
  done;
done
