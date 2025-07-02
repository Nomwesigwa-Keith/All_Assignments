# Post Automation Agent for X.com (Twitter)

import tweepy
import schedule
import time
import random
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(level=logging.INFO, filename='x_post_log.txt', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# X.com API credentials (Replace with your actual credentials)
API_KEY = 'c1zwLwArnqY9XjfOlJusR0Q01'
API_KEY_SECRET = 'b2CfCZ23XuVMPHwBPbuZ2FgJCQbzMj8FBhu0PtNWgZviOrelo6'
ACCESS_TOKEN = '1434620781405822982-3XMIXlpIZMYlpYCZU9QDGy0RtBjyrc'
ACCESS_TOKEN_SECRET = 'bKcXwGCTAVQukH5xp6npkXhHYjYtiTCZiR0I5DLCZm56B'

# Authenticate with X.com API
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Predefined list of daily messages
messages = [
    "Monday motivation: Start strong, stay consistent. #MondayMotivation",
    "Tuesday tip: The secret to long-term success is daily progress. #TuesdayThoughts",
    "Wednesday Wisdom: Are you halfway through your goals or halfway stuck? Reset. #MidweekMotivation",
    "Thursday thoughts: Be thankful for the progress, even if it’s small. #ThankfulThursday",
    "Friday Fun! Celebrate your wins, big or small. You’ve earned it. #FridayFeeling",
    "Saturday vibes: Reflect, recharge, and read something inspiring. #SelfCare",
    "Sunday reset: Plan your week with purpose. Success begins with a solid plan. #SundayVibes"
]

# Mapping weekday index to message
day_to_message = {
    0: messages[0],  # Monday
    1: messages[1],
    2: messages[2],
    3: messages[3],
    4: messages[4],
    5: messages[5],
    6: messages[6]   # Sunday
}

def post_message_on_x(message):
    """
    Posts a message to X.com using Tweepy API.
    """
    try:
        status = api.update_status(status=message)
        logging.info(f"Posted successfully: {message}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Posted: {message}")
        return status
    except Exception as e:
        logging.error(f"Failed to post message: {e}")
        print(f"Error posting message: {e}")
        return None

def daily_post_job():
    """
    Posts a daily message based on the current day of the week.
    """
    weekday = datetime.now().weekday()
    message = day_to_message.get(weekday)
    if message:
        post_message_on_x(message)

# Schedule the job to run every day at 9:00 AM
schedule.every().day.at("23:30").do(daily_post_job)

# Run the scheduler loop
if __name__ == "__main__":
    print("AI Post Agent started. Waiting to post daily messages...")
    post_message_on_x("✅ Test message from my bot! #HelloWorld")  # <- Move here
    while True:
        schedule.run_pending()
        time.sleep(60)

post_message_on_x("✅ Test message from my bot! #HelloWorld")


#graded assignment(40): create a function to post a message on X.com(SOCIAL MEDIA) using AI agent post script using python
