from flask import Flask

app = Flask(__name__)

from recsys.algorithm.factorize import SVD

filename = "/Users/zhanghengyang/PycharmProjects/pyrecsys_test_flask/static/movie_data/ratings.dat"


"""
######ratings.dat
  UserID::MovieID::Rating::Timestamp

- UserIDs range between 1 and 6040
- MovieIDs range between 1 and 3952
- Ratings are made on a 5-star scale (whole-star ratings only)
- Timestamp is represented in seconds since the epoch as returned by time(2)
- Each user has at least 20 ratings

"""

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/rec")
def rectest():


    svd = SVD()
    svd.load_data(filename, sep="::", format={"col":0, "row":1, "value":2, "ids": int})




if __name__ == '__main__':
    #app.run()
    #import os
    #print os.getcwd()
    import time
    start_time = time.time()

    svd = SVD()
    data = svd.load_data(filename, sep="::", format={"col":0, "row":1, "value":2, "ids": int})
    K = 100
    svd.compute(k=K, min_values=10, pre_normalize=None, mean_center=True, post_normalize=True, savefile=None)
    #print data
    #r = svd.predict(200, 1, MIN_VALUE=0, MAX_VALUE=5.0)
    r = svd.recommend(1, n=10, only_unknowns=True, is_row=False )
    print r


    time_consumed = time.time() - start_time
    print time_consumed