import psycopg2
from psycopg2 import sql

def create_tables():
    """Create tables in PostgreSQL database"""
    commands = (
        """
        CREATE TABLE videos (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            transcription TEXT NOT NULL,
            tags VARCHAR(255)
        )
        """,
    )
    conn = None
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword host=yourhost")
        cur = conn.cursor()
         # Print and execute each command to create tables
        for command in commands:
            print(f"Executing command: {command}")
            cur.execute(command)
        # Close communication with PostgreSQL database server
        cur.close()
        # Commit all the changes
        conn.commit()
        print("All tables are created successfully")
    # If any error occurs
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # Close the connection
            conn.close()

if __name__ == '__main__':
    create_tables()
