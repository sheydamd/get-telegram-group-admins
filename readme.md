# Save Telegram Group Admins List with Python (python-telegram-bot)

This script uses the python-telegram-bot library (async version) and asyncio to fetch the list of administrators of a Telegram group when the bot starts and saves it into a file named admins.txt.
---
## Install the library:
`bash`
- install venv by using:
python -m venv .venv
    - .venv\Scripts\activate

- pip install python-telegram-bot
## How to Use?

1. Get your bot token from BotFather and replace the TOKEN variable in the script:
    - TOKEN = "your_bot_token_here"

2. Set your target group's numeric ID (usually starts with -100):

    - GROUP_ID = -100----

3. Run the script:
`bash`
python your_script.py

4. After running, a file named admins.txt will be created, containing the list of admins in this format:
    - FirstName LastName @username (user_id)
