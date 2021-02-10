from gelbooru import Comment

"""posts = Post.search_tags(tq.Options(tq.Or("fox_ears", "kitsune"), rating=tq.InvRating.questionable,
                                     sort=tq.SortTypes.random))

posts[0].get_image().show()"""

print([x.body for x in Comment.search(id=5876129)])