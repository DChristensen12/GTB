#!/bin/bash
if [ ! -f .env ]; then
  echo "❌ .env file not found! Please create one from .env.example"
  exit 1
fi

echo "⬇Downloading all GTB raw datasets..."

python src/data_ingest/global_population.py
python src/data_ingest/global_parks.py
python src/data_ingest/global_sentinel.py
python src/data_ingest/heat_pollution.py
python src/data_ingest/sea_level_rise.py

echo "All data downloaded to data/raw/ :D"
