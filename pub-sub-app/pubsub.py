from collections import deque, defaultdict
from itertools import islice
import time
from typing import NamedTuple, Deque, DefaultDict, Set, Optional, List
from heapq import merge
from sys import intern 

User = str
Timestamp = Optional[float]
Post = NamedTuple('Post', [('timestamp', float), ('user', str), ('text', str)])

posts = deque()                         # type: Deque[Post]
user_posts = defaultdict(deque)         # type: DefaultDict[User, Deque[Post]]

following = defaultdict(set)               # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)               # type: DefaultDict[User, Set[User]]

def post_message(user: User, text: str, timestamp: Timestamp=None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()

    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    user = intern(user)
    return list(islice(user_posts[user], limit))

def posts_for_user(user: User, limit: Optional[int]=None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user]
                        for followed_user in following[user]], reverse=True)
    return list(islice(relevant, limit))


def search(phrase: str, limit: Optional[int]=None) -> List[Post]:
    # Todo: add pre-indexing to the posts to speed up searches
    return list(islice((post for post in posts if phrase in post.text), 3))
