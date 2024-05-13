from app_flask import create_app, db

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)

@app.cli.command("create-db")
def create_db_command():
    """Creates the database tables."""
    db.create_all()
    print('Created Database!')
