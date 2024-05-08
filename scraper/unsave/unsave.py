import csv
import praw
import math

def main():
    # reddit = praw.Reddit(
    #         user_agent = True, 
    #         client_id = "Cd_SO772htrNoxOClPHGKA", 
    #         client_secret = "nP7t5Lbt80BfBzTia9iQiW3wKlRWbw", 
    #         username = "Artistic-Benefit5275",
    #         password = "V4s4_H:CURTpn!B"
    #     )
    
    # with open('./scripts/unsave/saved_list.csv', mode='r') as file:
    #     reader = csv.reader(file)
    #     count = 1
    #     for reddit_id in reader:
    #         reddit.submission(id=reddit_id[0]).unsave()
    #         print(f"[{count}] Unsaving... {reddit_id[0]}")
    #         count += 1
    cat = "meow"
    print(cat[:math.floor(len(cat)/2)])
    print(cat[math.floor(len(cat)/2):])
    
if __name__ == "__main__":
    main()