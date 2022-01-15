import feedparser
import json
get_url = input(" what is the url? :")
url = feedparser.parse(get_url)

try:
    posts = url.feed
    posts_details = {"title": url.feed.title,
                     "link": url.feed.link}
    post_list = []
    for post in posts:
        temprorary = dict()
        try:
            temprorary["title"] = post.title
            temprorary["link"] = post.link
            temprorary["author"] = post.author
            temprorary["time_published"] = post.published
            temprorary["tags"] = [tag.term for tag in post.tags]
            temprorary["authors"] = [author.name for author in post.authors]
            temprorary["summary"] = post.summary
        except:
            pass
        
        
        post_list.append(temprorary)
    print(json.dumps(post_list,indent=2))
    print(post_list)
except:
    posts = url.entries

    posts_details = {"title": url.feed.title,
                     "link" : url.feed.link   }
    post_list = []
    for post in posts:
        temprorary = dict()
        try:
            temprorary["title"] = post.title
            temprorary["link"] = post.link
            temprorary["author"] = post.author
            temprorary["time_published"] = post.published
            temprorary["tags"] = [tag.term for tag in post.tags]
            temprorary["authors"] = [author.name for author in post.authors]
            temprorary["summary"] = post.summary
        except:
            pass
        
        
        post_list.append(temprorary)
    print(json.dumps(post_list, indent=2))
    print(post_list)


