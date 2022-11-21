from sklearn import datasets

datasets.fetch_20newsgroups(data_home = "data/raw", subset = "all", shuffle = True, remove = ("headers", "footers", "quotes"))



