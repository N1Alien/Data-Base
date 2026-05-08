import sqlite3
import db_content_checker

empty_db = db_content_checker.check_for_tables("climate_data.db")


# Create connection to the climate database
def get_connection():
    """Returns a connection to the climate_data.db database"""
    conn = sqlite3.connect('climate_data.db')
    return conn

# Example usage and verification
if __name__ == "__main__":
    if empty_db:
        print("Database is empty. Please create the database before using this class.")
        exit()
    conn = get_connection()
    
    # Query stations
    print("Stations:")
    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    for row in result:
        print(row)
    
    print("\nMeasurements:")
    result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
    for row in result:
        print(row)
    
    # Get summary statistics
    print("\nDatabase Summary:")
    stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
    measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
    print(f"Total stations: {stations}")
    print(f"Total measurements: {measurements}")
    
    conn.close()
