import newspaper

news_paper = newspaper.build(u'http://counterpunch.com')

for article in news_paper.articles:
    article.download()
    article.parse()
    article.nlp()
    print(">" + article.title + "\n" + article.summary + "\n")
