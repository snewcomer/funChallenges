defmodule Codewars.EvilOdious do
  def evil?(n) do
    count = 
      ~r/1/
      |> Regex.scan(Integer.to_string n, 2)
      |> length
    "It's #{if rem(count, 2) == 0, do: "Evil", else: "Odious"}!"
  end
end

# or longer version

defmodule Codewars.EvilOdious do
  import Integer, only: [is_even: 1, to_string: 2]
  def evil?(n) do
    to_string(n, 2)
    |> String.replace("0", "")
    |> String.split("")
    |> Enum.reduce(%{}, &count/2)
    |> isEven
  end
  defp count(num, acc) do
    Map.update(acc, num, 1, &(&1 + 1))
  end
  defp isEven(obj) do
    if(is_even(obj["1"])) do
      "It's Evil!"
    else
      "It's Odious!"
    end
  end
end
