import argparse
from urllib import request, error
import json

event_json = None

parser = argparse.ArgumentParser(
    prog='GitHub User Activity',
    description='This CLI app fetches the latest GitHub user activity.'
)

parser.add_argument('user_name')
args = parser.parse_args()

url = f'https://api.github.com/users/{args.user_name}/events'

try:
   response = request.urlopen(url)   
except error.HTTPError as e:
    print(f'HTTP Error: {e.code} {e.reason}')
except error.URLError as e:
    print(f'URL Error: {e.reason}')
else:
    body = response.read()    
    event_json = json.loads(body.decode('utf-8')) 

if event_json is not None:
    for event in event_json:

        event_type = event['type']
        repo_name = event['repo']['name']
        payload = event['payload']
        datetime = event['created_at']

        if event_type == 'CommitCommentEvent':
            print(f'Commented commit in {repo_name}')
    
        elif event_type == 'CreateEvent':
            ref_type = payload['ref_type']
            print(f"Created {ref_type} in {repo_name} at {datetime}")

        elif event_type == 'DeleteEvent':
            ref_type = payload['ref_type']
            print(f"Deleted {ref_type} in {repo_name} at {datetime}")

        elif event_type == 'DiscussionEvent':
            print(f"Discussion created in {repo_name} at {datetime}")

        elif event_type == 'ForkEvent':
            forkee = payload['forkee']['full_name']
            print(f"Forked {forkee} at {datetime}")

        elif event_type == 'GollumEvent':
            page_name = payload['pages[][page_name]']
            print(f"Created or update the {page_name}")

        elif event_type == 'IssueCommentEvent':
            action = payload['action']
            print(f"{action.capitalize()} a comment issue in {repo_name} at {datetime}")
    
        elif event_type == 'IssuesEvent':
            action = payload['action']
            print(f"{action.capitalize()} a issue in {repo_name} at {datetime}")
    
        elif event_type == 'MemberEvent':
            action = payload['action']
            user_member = payload['member']
            print(f"{action.capitalize()} {user_member} in {repo_name} at {datetime}")
    
        elif event_type == 'PublicEvent':
            print(f"Made public the {repo_name} at {datetime}")

        elif event_type == 'PullRequestEvent':
            action = payload['action']
            print(f"{action.capitalize()} a pull request in {repo_name} at {datetime}")
    
        elif event_type == 'PullRequestReviewEvent':
            action = payload['action']
            print(f"{action.capitalize()} a pull request review in {repo_name} at {datetime}")

        elif event_type == 'PullRequestReviewCommentEvent':
            action = payload['action']
            print(f"{action.capitalize()} a comment pull request review in {repo_name} at {datetime}")

        elif event_type == 'PushEvent':
            repository_id = payload['repository_id']        
            print(f'Pushed to {repo_name} at {datetime}')

        elif event_type == 'ReleaseEvent':
            action = payload['action']
            print(f'{action.capitalize()} in {repo_name} at {datetime}')
            
        elif event_type == 'WatchEvent':
            action = payload['action']
            print(f'{action.capitalize()} {repo_name} at {datetime}')
            

        

        