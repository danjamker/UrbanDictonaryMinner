import urllib, json
from collections import deque

queue = deque(["bruh"])
li = []
base_url = "http://api.urbandictionary.com/v0/define?term=%s"

if __name__ == '__main__':

    with open("data-4.json", mode='a') as f:
        count = 0
        while len(queue) > 0:
            word_q = queue.pop()
            print base_url % word_q.encode('utf-8')
            try:
                response = urllib.urlopen(base_url % word_q.encode('utf-8'))
                data = json.loads(response.read())
                json.dump(data, f)
                f.write("\n")
                for w in data["tags"]:
                    if w not in li:
                        queue.append(w.encode('utf-8'))
                        print("    --- "+ w)
                        li.append(w.encode('utf-8'))
            except Exception as e:
                print e