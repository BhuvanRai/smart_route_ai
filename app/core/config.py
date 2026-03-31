
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Use the credentials from your friend's config file
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://bkv:globalsupplychain@15.206.160.22:5432/supplychain")

# Map tracking/traffic/weather API keys
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY", "DPKc8wTW9olXLIUPZt3r4jmh5P6caGXX")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "a2226e1a74aa4136b2162252262803")

# psycopg2 needs pure postgresql connection string, removing the "+psycopg2" part if present
def get_psycopg2_url(url: str) -> str:
    if url.startswith("postgresql+psycopg2://"):
        return url.replace("postgresql+psycopg2://", "postgresql://", 1)
    return url

PSYCOPG2_URL = get_psycopg2_url(DATABASE_URL)

def get_db_connection():
    """
    Returns a new psycopg2 connection.
    Make sure to close the connection after using it.
    """
    conn = psycopg2.connect(PSYCOPG2_URL, cursor_factory=RealDictCursor)
    return conn
