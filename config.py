import secrets

SECRET_KEY = secrets.token_hex(16)
SQLALCHEMY_DATABASE_URI = 'postgres://teachinginbinary:3OGuBhuYBPGkd1Xkv6nd23iqe73k91vT@dpg-cp0pgm021fec7388mkn0-a.oregon-postgres.render.com/library_db_pl7g'