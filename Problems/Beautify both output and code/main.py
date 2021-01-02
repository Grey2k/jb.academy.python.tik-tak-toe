username = input()
title = input()

print('http://example.com/{username}/desirable/{title}/profile'.format(
    username=username, title=title
))
