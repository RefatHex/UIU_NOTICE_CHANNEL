#  UIU Notices

This Telegram bot is designed to provide United International University (UIU) notices to users automatically. It fetches notices from the UIU website and sends them to users at regular intervals.

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pipenv:
    ```bash
    pipenv install
    ```
4. Replace `<TOKEN>` in the `TOKEN.py` file with your Telegram bot token.
5. Run the bot script:
    ```bash
    pipenv run python your_script_name.py
    ```

## Features

- **Start Command**: `/start` - Initializes the bot and activates the auto-update feature.
- **Author Command**: `/author` - Provides information about the author of the bot.
- **Auto Update**: The bot automatically fetches the latest notice from the UIU website and sends it to users.
- **Error Handling**: The bot includes error handling to log and handle any exceptions that may occur during its operation.

## Usage

1. Start the bot by sending the `/start` command.
2. You will start receiving updates on 'UIU_Notice_Bot' channel.
3. Use the `/author` command to know more about the author of the bot.

## Notice Scraper

The bot fetches notices from the UIU website using web scraping techniques. It scrapes the website periodically to check for new notices.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.


## Contributors

- [Author's GitHub Profile](https://github.com/refathex)


