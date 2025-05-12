import requests 


def get_github_user_data(username: str) -> str:
    url = f"https://api.github.com/users/{username}/events/public"
    response = requests.get(url)
    if response.status_code == 200:
        data  = response.json()
        watched = 0
        created = 0
        pushed = 0
        for event in data:
            if event['type'] == 'CreateEvent':
                created += 1
            elif event['type'] == 'PushEvent':
                pushed += 1
            elif event['type'] == 'WatchEvent':
                watched += 1
        return f"The User {username} has created {created} repositories, pushed {pushed} times and watched {watched} repositories."
    else:
        return None



def main():
    x = input("Enter github username: ")
    print(get_github_user_data(x))











if __name__ == "__main__":
    main()
