from pubsub import *
from pprint import pprint
from itertools import islice
from heapq import merge

post_message('alicja', 'Python is cool!')
post_message('marcelo', 'Python é foda!')
post_message('elizete', 'What is Python?')
post_message('marcelo', 'Jestem silny')
post_message('marcelo', 'Jeste byke')
post_message('marcelo', '#python is cool')
post_message('ala', 'learning #python')
post_message('trudy', 'monty #python')
post_message('lilj', 'programming with #python')

follow('marcelo', followed_user='alicja')
follow('alicja', followed_user='marcelo')
follow('murilo', followed_user='marcelo')

if __name__ == '__main__':
    # pprint(posts)
    # pprint(user_posts['marcelo'])

    # pprint(followers)

    # pprint(list(islice(user_posts['marcelo'], 2)))

    # pprint(posts_for_user('marcelo', limit=1))

    pprint(search('#python'))