import sqlite3
import db_content_checker

empty_db = db_content_checker.check_for_tables("climate_data.db")

class ClimateDB:
    def __init__(self, db_name="climate_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def update_record(self, table_name, record_id, **kwargs):
        """Update a record by ID in specified table"""
        fields = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [record_id]
        self.cursor.execute(f"UPDATE {table_name} SET {fields} WHERE id = ?", values)
        self.conn.commit()
        print(f"Record {record_id} in {table_name} updated successfully")
    
    def delete_record(self, table_name, record_id):
        """Delete a record by ID from specified table"""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        self.conn.commit()
        print(f"Record {record_id} from {table_name} deleted successfully")
    
    def delete_by_location_name(self, table_name, location_name):
        """Delete all records for a location name from specified table"""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (location_name,))
        self.conn.commit()
        print(f"All records for {location_name} deleted from {table_name}")
    
    def delete_by_column_value(self, table_name, column_name, value):
        """Delete all records with a specific column value from specified table"""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name} = ?", (value,))
        self.conn.commit()
        print(f"All records with {column_name} = {value} deleted from {table_name}")

    def close(self):
        self.conn.close()

# Examples
if __name__ == "__main__":
    if empty_db:
        print("Database is empty. Please create the database before using this class.")
        exit()
    db = ClimateDB()
    
    # Update records in both tables
    db.update_record("stations", 3, name="Bangkok")
    db.update_record("measurements", 3, precip=9000)
    
    # Delete from specific tables
    db.delete_record("stations", 1)
    db.delete_record("measurements", 1)
    
    # Delete by location from both tables
    db.delete_by_location_name("stations", "PEARL CITY")
    db.delete_by_column_value("measurements", "precip", 0)
    
    db.close()
