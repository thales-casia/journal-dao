from math import floor

class IReview():
  reviewerID: int
  rating: int

  def __init__(self, reviewerID:int, rating:int) -> None:
    self.reviewerID = reviewerID
    self.rating = rating
  def __hash__(self) -> int:
    return self.reviewerID

class IDistribution():
  id: int
  token: int

  def __init__(self, id:int, token:int) -> None:
    self.id = id
    self.token = token
  def __hash__(self) -> int:
    return self.id


class ArticleDAO:
  _distribution:set[IDistribution] = set()
  _articleID = 0
  _authors = set()
  _reviewers = set()


  def __init__(self, articleID:int, authors:set[int]):
    self._articleID = articleID
    self._authors = authors
  def review(self, reviews:set[IReview]):
    token = 0
    for review in reviews:
      token += review.rating
      self._distribution.add(IDistribution(review.reviewerID, (6 - review.rating) * 100))
    author_len = len(self._authors)

    token = token * 100
    weight = dict()
    weight_len = 0
    for i, author in enumerate(self._authors):
      n = author_len - i
      weight[i] = n
      weight_len += n
    for i, author in enumerate(self._authors):
      self._distribution.add(IDistribution(author, floor(token * (weight[i] / weight_len))))


article = ArticleDAO(1, {1,2,3})
article.review({IReview(reviewerID=11, rating=5), IReview(reviewerID=12, rating=4)})

print(article)
