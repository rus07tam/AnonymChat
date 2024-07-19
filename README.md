# AnonymChatBot

AnonymChatBot is a Telegram bot that allows users to anonymously chat with each other.
Main features:
1. Full anonymity. The bot does not have an admin panel for reading chats or for deanonymization
2. Support message replies. If user A wants to make a replay of user B's message. Then the bot itself will be able to pass the required reply_to_message_id in `message.copy_to()`
3. Support message reactions. The bot can synchronize the reactions that users have set between chats
4. No DB. The bot is not using any database, and all data is stored in States.
5. Work in groups (beta). Anonymous chat works in groups, but the chat will not be for the whole group, but for the user who started the chat

## Project Structure

```
├── config.py
├── bot_init.py
├── states.py
├── handlers
│ ├── start.py
│ ├── search.py
│ ├── cancel.py
│ ├── stop.py
│ └── message.py
├── main.py
└── README.md
```


- `config.py`: Contains configuration constants such as the API token.
- `bot_init.py`: Initializes the bot and dispatcher.
- `states.py`: Defines the user states using finite state machines (FSM).
- `handlers/`: Directory containing modules for each command handler.
  - `start.py`: Handles the `/start` command.
  - `search.py`: Handles the `/search` command.
  - `cancel.py`: Handles the `/cancel` command.
  - `stop.py`: Handles the `/stop` command.
  - `message.py`: Handles messages when the user is in a conversation.
  - `message_reactiob.py`: Synchronizes message reactions between users.
- `main.py`: The main script entry point that starts the bot.

## Setup

### Prerequisites

- Python 3.7 or higher
- [Aiogram](https://docs.aiogram.dev/en/latest/)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/chat-bot.git
   cd chat-bot
   ```
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set token in `config.py`:
   ```python
    API_TOKEN = 'YOUR_API_TOKEN_HERE'
    ```