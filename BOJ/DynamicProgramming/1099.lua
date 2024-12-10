local sentence = io.read()
local N = tonumber(io.read())
local words = {}

for i=1, N do
  words[i] = io.read()
end

table.sort(words, function(a, b)
  return #a < #b
end)

local INF = 100000000

local dp = {}
---  3d dp
for i=1, 60 do
  dp[i] = {}
  for j=1, 60 do
	dp[i][j] = INF
  end
end

local function get_cost(word, left, right)
  local pattern = sentence:sub(left, right)
  local word_counter = {}
  local pattern_counter = {}
  local len = #word

  local result = 0

  for i=1, len do 
	word_counter[word:sub(i, i)] = (word_counter[word:sub(i, i)] or 0) + 1 
	pattern_counter[pattern:sub(i, i)] = (pattern_counter[pattern:sub(i, i)] or 0) + 1 
  end

  for k, v in pairs(word_counter) do
	if pattern_counter[k] ~= v then
	  return INF
    end
  end

  for i=1, len do 
	if word:sub(i, i) ~= pattern:sub(i, i) then
	  result = result + 1
	end
  end

  -- print(word, left, right, result)

  return result
end

local function solve(left, right)
  if left > right then 
	return INF
  end
  if dp[left][right] ~= INF then
	return dp[left][right]
  end

  local result = INF 

  local costs = {}
  for i=1, N do
	local word = words[i]
	local cost = get_cost(word, left, left + #word - 1)
	costs[#word] = math.min((costs[#word] or INF), cost)
  end

  for len, cost in pairs(costs) do 
	if len == right - left + 1 then
	  result = math.min(result, cost)
	else 
	  result = math.min(result, cost + solve(left + len, right))
	end
  end


  dp[left][right] = result
  return result
end

local result = INF
result = math.min(result, solve(1, #sentence))
if result == INF then
  print(-1)
else
  print(result)
end
