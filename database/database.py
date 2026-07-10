import sqlite3


class AlertDatabase:

    def __init__(self, db_name="sentinelx.db"):
        self.connection = sqlite3.connect(db_name)

        self.create_table()


    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            type TEXT,

            source_ip TEXT,

            attempts INTEGER,

            severity TEXT,

            status TEXT DEFAULT 'OPEN',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            mitre_id TEXT,

            mitre_name TEXT,

            tactic TEXT

        )
        """

        self.connection.execute(query)
        self.connection.commit()


    def insert_alert(self, alert):

        query = """
        INSERT INTO alerts
        (type, source_ip, attempts, severity, mitre_id, mitre_name, tactic)

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        self.connection.execute(
            query,
            (
                alert["type"],
                alert["source_ip"],
                alert["attempts"],
                alert["severity"],
                alert["mitre_id"],
                alert["mitre_name"],
                alert["tactic"]
            )
        )

        self.connection.commit()


    def get_alerts(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM alerts"
        )

        return cursor.fetchall()
    
