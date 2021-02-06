import xml.etree.ElementTree as ET
import requests
"""
with open("out1.txt", "w", encoding="utf-8") as f:
    for page_id in range(100, 200):
        print(page_id)
        f.write(requests.get("https://gelbooru.com/index.php?page=dapi&s=tag&q=index&orderby=count&pid=" + str(page_id)).text)

a=0
with open("out.txt", "r") as f1:
    with open("out1.txt", "r") as f2:
        with open("out2.txt", "w") as f3:
            for i in f1.readlines() + f2.readlines():
                if "type=\"4\"" in i:
                    f3.write(i)
                    print(a := a + 1)

with open("out2.txt", "r") as f1:
    with open("out3.txt", "w") as f2:
        for i in f1.readlines():
            f2.write(i.split("name=\"")[1].split("\"")[0] + "\n")


def url_builder(tag):
    return "https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=solo%20"+tag

with open("out3.txt", "r") as f1:
    with open("out6.txt", "w", encoding="utf-8") as f2:
        for i in f1.readlines()[3439:]:
            try:
                f2.write(requests.get(url_builder(i.strip("\n").replace("-", "%2D"))).text.split("\n")[1])
                print(i)
            except IndexError:
                print("error: ", i)
"""
class Post:
    count = 0
    badcount = 0
    badlist = []

    def __init__(self):
        self.charname = None
        self.chareye = None
        self.charhair = None
        self.id = None

    def commatisize(self):

        if not (self.charname and self.chareye and self.charhair):
            #print("missingerror:{}; id:{}".format(self.charname, self.id))
            Post.badcount = Post.badcount + 1
            return

        Post.count = Post.count + 1

        return "{}, {}, {}, {}\n".format(self.charname, self.chareye, self.charhair, self.id)

    def updatename(self, name):
        if self.charname:
            #print("\tnamedupeerror:{}; id{}; tags{},{}".format(self.charname, self.id, self.charname, name))
            Post.badlist.append(self.charname + "+" + name)
            return 0
        self.charname = name

    def updateid(self, id):
        if self.id:
            #print("\tiddupeerror:{}; id{}; tags{},{}".format(self.charname, self.id, self.id, id))
            return 0
        self.id = id

    def updateeye(self, eye):
        if self.chareye:
            #print("\teyedupeerror:{}; id{}; tags{},{}".format(self.charname, self.id, self.chareye, eye))
            return 0
        self.chareye = eye

    def updatehair(self, hair):
        if self.charhair:
            #print("\thair-dupeerror:{}; id{}; tags{},{}".format(self.charname, self.id, self.charhair, hair))
            return 0
        self.charhair = hair


f = open("finalout.csv", "w")
f.write("Name, Eye, Hair, PostID\n")

colors = [x.strip() for x in open("colors.txt").readlines()]
char_tags = [x.strip() for x in open("out3.txt").readlines()]

for post in open("out4.txt", encoding='utf-8').read().split(">"):

    if not post:
        continue

    p = Post()

    tags = post.split("tags=\"")[1].strip().split("\"")[0].split(" ")
    id = int(post.split("id=\"")[2].split("\"")[0])

    p.updateid(id)

    for i in tags:
        if i in char_tags:
            p.updatename(i)

    for i in tags:
        if "eyes" in i and (a := i.split("_eyes")[0]) in colors:
            p.updateeye(a)
        elif "hair" in i and (a := i.split("_hair")[0]) in colors:
           p.updatehair(a)

    p.commatisize()

print(Post.count, Post.badcount)

