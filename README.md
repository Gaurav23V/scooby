# Scooby - Terminal-based AI Assistant

Scooby is a Python-based CLI assistant that provides an interactive chat experience in your terminal. It features conversation history, streaming responses, and image handling capabilities.

<div align="center">
  <img src="sample/Screenshot from 2024-12-26 01-17-24.png" alt="Scooby Terminal Assistant" width="600"/>
</div>

## Features

- **Command-line Interface**: Launch Scooby directly from your terminal
- **Streaming Responses**: See AI responses appear in real-time with a typing effect
- **Conversation History**: Maintains context across conversations using SQLite
- **Session Management**: Each conversation has a unique session ID
- **Colored Output**: Distinguishes between user and assistant messages
- **Image Support**: Share images through terminal commands (coming soon)
- **Note**: By default using latest gpt-4o. You can switch as you wish.

## File Structure

- `scooby.py`: Main entry point using Click framework
- `ui.py`: Handles the conversation interface and streaming responses
- `api.py`: Manages OpenAI API interactions
- `db.py`: SQLite database operations for conversation history
- `image_handler.py`: Image processing utilities
- `run_scooby.sh`: Bash script to launch the application

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- GitHub account (for API token)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Gaurav23V/scooby
cd scooby
```

2. Install required packages:
```bash
pip install openai click rich colorama pillow
```

3. Set up environment variables:
Create a file named `env_variables.sh` in your home directory:
```bash
#!/bin/bash
export ENDPOINT="https://models.inference.ai.azure.com"
export GITHUB_TOKEN="your-github-token"
```

4. Make the script executable:
```bash
chmod +x ~/env_variables.sh
chmod +x run_scooby.sh
```

5. Add to your `.bashrc` or `.zshrc`:
```bash
alias scooby='~/path/to/run_scooby.sh'
```

## Getting a GitHub Token (Must have Github Pro)

1. Go to GitHub.com and log in
2. Click your profile picture → Settings
3. Scroll to "Developer settings" → "Personal access tokens"
4. Generate fine-grained token
5. Select necessary scopes
6. Copy the generated token
7. Add it to your `env_variables.sh` file

## Usage

1. Start Scooby:
```bash
scooby
```

2. Chat naturally with the assistant
3. Exit the conversation:
```
see ya scooby
```

## Key Commands

- Type `scooby` to start the assistant
- Use `see ya scooby` to exit
- Press `Ctrl+C` for emergency exit

## Database Structure

The conversation history is stored in SQLite with the following schema:
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    role TEXT,
    content TEXT
)
```

## Troubleshooting

If Scooby doesn't start:
1. Check if environment variables are set correctly
2. Verify Python installation
3. Ensure all dependencies are installed
4. Check file permissions of run_scooby.sh

If you get API errors:
1. Verify your GitHub token
2. Check internet connection
3. Ensure endpoint URL is correct

## Future Features

- Image sharing capabilities
- Code syntax highlighting
- Conversation export
- Custom themes