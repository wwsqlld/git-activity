import requests
import matplotlib.pyplot as plt
import pandas as pd



def get_github_user_data(username: str) -> str:
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    if response.status_code == 200:
        data  = response.json()
        graf = dict(
            watched = 0,
            created = 0,
            pushed = 0,
            comment = 0,
            watchedpull = 0
        )
           
        for event in data:
            if event['type'] == 'CreateEvent':
                graf['created'] += 1
            elif event['type'] == 'PushEvent':
                graf['pushed'] += 1
            elif event['type'] == 'WatchEvent':
                graf['watched'] += 1
            elif event['type'] == 'IssueCommentEvent':
                graf['comment'] += 1
            elif event['type'] == 'PullRequestReviewEvent':
                graf['watchedpull'] += 1 

        graf_ser = pd.Series(graf)
        graf_ser.plot(kind='bar')
        plt.title(f"GitHub User Activity for {username}")
        plt.xlabel("Activity Type")
        plt.ylabel("Count")
        plt.show() 
        return f"The User {username} has created {graf['created']} repositories, pushed {graf['pushed']} times and watched {graf['watched']} repositories. The user has commented {graf['comment']} times. The user has watched {graf['watchedpull']} pull requests."
        
    else:
        return None



def main():
    x = input("Enter github username: ")
    print(get_github_user_data(x))



if __name__ == "__main__":
    main()
