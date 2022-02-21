import sys
from tkinter import Text, ttk

import feedparser
import pyperclip
from ttkthemes import ThemedTk


def Stalker(evento=None):
    conteudo.configure(state='normal')
    conteudo.delete('1.0', 'end')

    if combo.get() == 'Todos':
        d = feedparser.parse('https://medium.com/feed/@heitorloureiro')
        texto1 = d.entries[0].title + '\n' + d.entries[0].link

        d1 = feedparser.parse('https://ondem.libsyn.com/rss')
        for entry in d1.entries:
            if 'ONDE Política' in str(entry.title):
                texto2 = entry.title + '\n' + entry.link
                break

        d2 = feedparser.parse(
            'https://www.youtube.com/feeds/videos.xml?channel_id=UCagwwqpZie4J4cXerPfO1bw'
        )
        for entry in d2.entries:
            texto3 = entry.title + '\n' + entry.link

        texto4 = texto1 + '\n' + texto2 + '\n' + texto3
        conteudo.insert('1.0', texto4)

    if combo.get() == 'Blog':
        d = feedparser.parse('https://medium.com/feed/@heitorloureiro')
        texto = d.entries[0].title + '\n' + d.entries[0].link
        conteudo.insert('1.0', texto)

    if combo.get() == 'Podcast':
        d1 = feedparser.parse('https://ondem.libsyn.com/rss')
        for entry in d1.entries:
            if 'ONDE Política' in str(entry.title):
                texto = entry.title + '\n' + entry.link
                conteudo.insert('1.0', texto)
                break

    if combo.get() == 'Youtube':
        d2 = feedparser.parse(
            'https://www.youtube.com/feeds/videos.xml?channel_id=UCagwwqpZie4J4cXerPfO1bw'
        )
        for entry in d2.entries:
            texto = entry.title + '\n' + entry.link
            conteudo.insert('1.0', texto)
    conteudo.configure(state='disabled')


def sair():
    sys.exit(0)


def copia():
    texto = conteudo.get(1.0, 'end')
    pyperclip.copy(texto)


# janela = Tk()
janela = ThemedTk(theme='arc')
janela.title('Heitor Stalker 0.1')
janela.geometry('870x470')

frame = ttk.Frame()
conteudo = Text(frame)


values = ['Blog', 'Podcast', 'Youtube', 'Todos']

combo = ttk.Combobox(frame, values=values)
combo['state'] = 'readonly'
combo.set('Blog')

botao = ttk.Button(frame, text='Stalqueie', command=Stalker)
butao = ttk.Button(frame, text='Sair', command=sair)
butao_copia = ttk.Button(frame, text='Copiar', command=copia)


botao.grid(row=0, column=1, padx=4)
butao.grid(row=1, column=1)
butao_copia.grid(row=1, column=3)
combo.grid(row=0, column=0, pady=4)
conteudo.grid(row=1, column=0, padx=4)
frame.pack()

janela.mainloop()
