import twint

c = twint.Config()
c.Username = 'doutorheitor'
c.Search = 'armenia'

twint.run.Search(c)
