
from sqlalchemy import create_engine, inspect

def check_for_tables(db_name):
    engine = create_engine(f'sqlite:///{db_name}')
    inspector = inspect(engine)
    
    tables = inspector.get_table_names()
    
    if len(tables) > 0:
        return False
    else:
        return True



