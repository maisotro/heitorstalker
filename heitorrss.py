import feedparser
import fire
import pyperclip


def blog():
    d = feedparser.parse('https://medium.com/feed/@heitorloureiro')
    return d.entries[0].title + '\n' + d.entries[0].link


def podcast():
    d1 = feedparser.parse('https://ondem.libsyn.com/rss')
    for entry in d1.entries:
        if 'ONDE Política' in str(entry.title):
            return entry.title + '\n' + entry.link
            break


def youtube():
    d2 = feedparser.parse(
        'https://www.youtube.com/feeds/videos.xml?channel_id=UCagwwqpZie4J4cXerPfO1bw'
    )
    for entry in d2.entries:
        return entry.title + '\n' + entry.link


def bot():
    # medium
    a = blog()
    c = podcast()
    d = youtube()

    a = (
        '*#######--Heitor Stalker 1.0--#######*\n\n\n *Ultimo post do Blog* \n'
        + str(a)
        + '\n*Ultimo episodio do podcast* \n'
        + str(c)
        + '\n*Ultimo video no youtube* '
        + str(d)
    )
    pyperclip.copy(a)


fire.Fire()
