🚀 Tesla Stock & News SMS Notifier 📈
This Python project fetches the latest news and financial data about Tesla using the News API and Alpha Vantage API, respectively. It sends updates via SMS using the Twilio API whenever significant changes in Tesla's stock price occur.


✨ Features

📰 Retrieves Tesla-related news headlines and descriptions from News API.
💹 Fetches daily stock price data for Tesla (TSLA) from Alpha Vantage API.
📊 Compares stock price changes between consecutive days and calculates percentage change.
✉️ Sends customized SMS notifications with stock updates and relevant news articles using Twilio.


📂 Project Structure

call_apinews(): 📰 Fetches Tesla-related news from News API.
call_teslas(): 💹 Retrieves Tesla's stock price data from Alpha Vantage API.
send_messages(): ✉️ Sends SMS notifications via Twilio API combining stock data and news.


🛠️ Prerequisites

🐍 Python 3.7 or higher


🔑 Active accounts and API keys for:

Twilio API
News API
Alpha Vantage API


🔒 Environment Variables

This project makes use of environment variables to securely store sensitive information such as API keys and authentication credentials. Using environment variables ensures security and allows for easy configuration across environments.

Required Variables:

ACCOUNT_SID: Twilio Account SID
AUTH_TOKEN: Twilio Auth Token
(Optional) Other secrets, if needed for future extensions.
Example .env File:
Create a file named .env in the root directory and add the following lines:

env
Copiar código
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
How Environment Variables Are Used:
In the code, environment variables are accessed using the os module:

python
Copiar código
import os

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
This approach ensures sensitive information is not hard-coded into the source files.

💡 Note: If you're unfamiliar with environment variables, don't worry—this project helped me learn how to create and use them securely. It's an essential skill in programming that I'm continuing to develop!

📦 Installation
Clone the repository:

bash
Copiar código
git clone https://github.com/Ronaldwm89/Tesla-Stock-News-AlertBOT
cd tesla-stock-news-sms
Create a virtual environment and activate it:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install the required dependencies:

bash
Copiar código
pip install -r requirements.txt
Set up your environment variables in a .env file as described above.

▶️ Usage
Run the script to fetch Tesla updates and send SMS notifications:

bash
Copiar código
python script_name.py

📝 Learning Note
While building this project, I learned how to securely manage sensitive data using environment variables and integrate multiple APIs. This is part of my ongoing journey to improve my Python skills and create more robust applications.

📜 License
This project is licensed under the MIT License. Feel free to use or modify it.

📬 Contact
If you have any questions or suggestions, feel free to reach out via GitHub.


















# Tesla Stock & News SMS Notifier BOT

This Python project fetches the latest news and financial data about Tesla using the **News API** and **Alpha Vantage API**, respectively. It sends updates via SMS using the **Twilio API** whenever significant changes in Tesla's stock price occur.

---

## Features
- Retrieves Tesla-related news headlines and descriptions from News API.
- Fetches daily stock price data for Tesla (TSLA) from Alpha Vantage API.
- Compares stock price changes between consecutive days and calculates percentage change.
- Sends customized SMS notifications with stock updates and relevant news articles using Twilio.

---

## Project Structure
- **`call_apinews()`**: Fetches Tesla-related news from News API.
- **`call_teslas()`**: Retrieves Tesla's stock price data from Alpha Vantage API.
- **`send_messages()`**: Sends SMS notifications via Twilio API combining stock data and news.

---

## Prerequisites
- Python 3.7 or higher
- Active accounts and API keys for:
  - [Twilio API](https://www.twilio.com/)
  - [News API](https://newsapi.org/)
  - [Alpha Vantage API](https://www.alphavantage.co/)

---

## Environment Variables
This project makes use of **environment variables** to securely store sensitive information such as API keys and authentication credentials. Using environment variables ensures security and allows for easy configuration across environments.

### Required Variables:
- `ACCOUNT_SID`: Twilio Account SID
- `AUTH_TOKEN`: Twilio Auth Token
- (Optional) Other secrets, if needed for future extensions.

### Example `.env` File:
Create a file named `.env` in the root directory and add the following lines:
```env
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
```

### How Environment Variables Are Used:
In the code, environment variables are accessed using the `os` module:
```python
import os

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
```
This approach ensures sensitive information is not hard-coded into the source files.

If you're unfamiliar with environment variables, don't worry—this project helped me learn how to create and use them securely. It's an essential skill in programming that I'm continuing to develop!

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tesla-stock-news-sms.git
   cd tesla-stock-news-sms
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables in a `.env` file as described above.

---

## Usage
Run the script to fetch Tesla updates and send SMS notifications:
```bash
python script_name.py
```

---

## Learning Note
While building this project, I learned how to securely manage sensitive data using environment variables and integrate multiple APIs. This is part of my ongoing journey to improve my Python skills and create more robust applications.

---

## License
This project is licensed under the MIT License. Feel free to use or modify it.

---

## Contact
If you have any questions or suggestions, feel free to reach out via [GitHub](https://github.com/yourusername).
