import feedparser
import re

TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


d1 = feedparser.parse('https://ondem.libsyn.com/rss')
for entry in d1.entries:
    if 'ONDE Política' in str(entry.title):
        # texto = entry.title + "\n" + entry.link + '\n' + entry.subtitle + '\n' + entry.id
        texto = entry.content.text.strip()
        print(remove_tags(str(texto)))
        break
