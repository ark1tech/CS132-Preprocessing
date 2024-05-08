import praw
import csv
import time
from datetime import datetime, timedelta

def main():
    reddit = praw.Reddit(
            user_agent = True, 
            client_id = "Cd_SO772htrNoxOClPHGKA", 
            client_secret = "nP7t5Lbt80BfBzTia9iQiW3wKlRWbw", 
            username = "Artistic-Benefit5275",
            password = "V4s4_H:CURTpn!B"
        )
    
    # SCRAPE
    
    subreddit = reddit.subreddit("AntiworkPH")
    count = 1
    with open('top.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "Content Type",
            "Title", 
            "Content", 
            "Upvotes Count",
            "Comments Count", 
            "Upvote Ratio",
            "Flair",
            "Permalink",
            "Reddit ID"
        ])
        for submission in subreddit.top(time_filter = "all", limit = 1000):

            time.sleep(1)

            if submission.saved:
                print(f"❌ Skipped (Already scraped) ~ https://www.reddit.com/{submission.permalink}")
                continue
            if (not submission.is_self):
                if (submission.is_original_content) and submission.score <= 10:
                    print(f"❌ Skipped (High-Context) ~ https://www.reddit.com/{submission.permalink}")
                    continue
                else: 
                    if submission.domain == "v.redd.it": content_type = "Video"
                    elif submission.domain == "i.redd.it": content_type = "Image"
                    else: content_type = "Unknown"
            if datetime.fromtimestamp(submission.created_utc) >= datetime.now() - timedelta(days=10):
                print(f"❌ Skipped (Date {datetime.fromtimestamp(submission.created_utc)}) ~ https://www.reddit.com/{submission.permalink}")

            print(f"[{count}] 🤖 (Top) Scraping ~ https://www.reddit.com/{submission.permalink}")
            writer.writerow([
                f"{datetime.fromtimestamp(submission.created_utc)}",
                f"{"Text-only" if submission.is_self else content_type}",  
                f"{submission.title}", 
                f"{submission.selftext}", 
                f"{submission.score}", 
                f"{submission.num_comments}", 
                f"{submission.upvote_ratio}", 
                f"{submission.link_flair_text}",
                f"https://www.reddit.com/{submission.permalink}",
                f"{submission.id}"
            ])
            submission.save()
            count += 1
            if count == 3000: 
                break

if __name__ == "__main__":
    main()