import newspaper

cnn_paper = newspaper.build(u'http://counterpunch.com')

for article in cnn_paper.articles:
    article.download()
    article.parse()
    article.nlp()
    print(">" + article.title + "\n" + article.summary + "\n")