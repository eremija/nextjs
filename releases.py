import urllib.request, json, os 

with urllib.request.urlopen("https://api.github.com/repos/eremija/nextjs/releases") as url:
    data = json.loads(url.read().decode())
    git_tag = data[0]["tag_name"]

os.environ["CIRCLE_TAG"]=str(git_tag)
print(os.environ["CIRCLE_TAG"])
