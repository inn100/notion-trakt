import os
import tmdbsimple as tmdb

# ... 现有代码 ...

def get_movie_detail(movie_id):
    movie = tmdb.Movies(movie_id)
    return movie.info(language="zh", append_to_response="images")

# 添加获取电视剧信息的函数
def get_tv_detail(tv_id):
    tv = tmdb.TV(tv_id)
    return tv.info(language="zh", append_to_response="images")
