# Telegram Game Bot

This repository contains a Telegram bot that connects to a game. The bot allows users to start and play the game directly from Telegram.

## Prerequisites

- Python 3.8 or higher
- A Telegram bot token from @BotFather
- `venv` for creating a virtual environment
- The required Python packages listed in `requirements.txt`

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/telegram-game-bot.git
cd telegram-game-bot
```
### Step 2: Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Create a .env file 
```
BOT_TOKEN=your-telegram-bot-token
```
### Run the bot 
```
python main.py
```
