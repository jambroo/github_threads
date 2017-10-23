import requests
import threading
import os

class GithubRequestThread:
    def __init__(self, username):
        self.username = username

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        r = requests.get('https://api.github.com/users/%s' % self.username)
        result = r.json()

        print("RESULT: "+result["name"])
        print("RESULT: "+result["location"])


threads = [
    GithubRequestThread(os.environ["GITHUB_USER_1"]),
    GithubRequestThread(os.environ["GITHUB_USER_2"])
]

print("INFO: All threads are started")

for thread in threads:
  print("INFO: Waiting for user '%s' request." % thread.username)
  thread.thread.join()

print("INFO: All threads completed")
