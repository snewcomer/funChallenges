# next_item([1, 2, 3, 4, 5, 6, 7], 3) #=> 4   take index and return humber after
defmodule NextBigThing do
  def next_item([], _item), do: nil
  def next_item([item, next | _rest], item), do: next
  def next_item([_any | rest], item), do: next_item(rest, item)
end
