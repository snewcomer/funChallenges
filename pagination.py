class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self._my_list = collection
      self._num_per = items_per_page
      self._length = len(collection)

  # returns the number of items within the entire collection
  def item_count(self):
      return self._length

  # returns the number of pages
  def page_count(self):
      a_num = self._length % self._num_per
      if a_num == 0:
        return self._length / self._num_per
      else:
        return max((a_num // self._num_per), 1) + (self._length // self._num_per)

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      twod = self.twoDArray()
      try:
        test = twod[page_index]
        if self._num_per == 1 and ((self._length == 1 and page_index == 0) or self.page_count() == page_index):
          return 0
        else:
          return len(test)

      except IndexError:
        if page_index <= -1:
          return self._num_per
        else:
          return -1


  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      twod = self.twoDArray()
      if self._length <= item_index or item_index < 0:
        return -1
      i = 0
      acc = 0
      while True:
          a_num = self.page_item_count(i)
          acc += a_num
          if acc <= item_index:
              i += 1
          else:
              break;
      return i

  def twoDArray(self):
      twod = []
      a = 0
      length = len(self._my_list)
      while a < length:
          new = []
          for i in range(self._num_per):
              if a == length -1:
                  new.append(self._my_list[a])
                  a += 1
                  break;
              else:
                  new.append(self._my_list[a])
                  a += 1
          twod.append(new)
      return twod
