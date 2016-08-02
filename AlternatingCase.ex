defmodule Codewars.StringUtils do
  def alter_case(str) do
    String.split(str, "")
    |> Enum.map(fn(letter) -> case(letter) end)
    |> Enum.join("")
  end
  defp case(letter) do
    if(String.match?(letter, ~r/[a-z]/)) do
      String.upcase(letter)
    else
      String.downcase(letter)
    end
  end
end

# other
defmodule Codewars.StringUtils do
  def alter_case(str) do
    str
    |> String.graphemes
    |> Enum.map(&switch_case/1)
    |> Enum.join
  end
  
  defp switch_case(grapheme) do
    cond do
      upcase?(grapheme) -> String.downcase(grapheme)
      downcase?(grapheme) -> String.upcase(grapheme)
      true -> grapheme
    end
  end
  
  defp downcase?(grapheme) do
    String.downcase(grapheme) == grapheme 
  end
  
  defp upcase?(grapheme) do
    String.upcase(grapheme) == grapheme 
  end
end
