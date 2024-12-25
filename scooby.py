import click
import db
import ui
import api

@click.command()
def main():
  # Initialize database connection
  db.init_db()
  # Start the conversation loop
  ui.conversation_loop()

if __name__ == "__main__":
  main()