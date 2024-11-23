local N, M = io.read():match("(%d+) (%d+)")
N = tonumber(N)
M = tonumber(M)

local campus = {}
local reachable = {}

local ix = 0 
local iy = 0


for i = 1, N do
	campus[i] = io.read()
	reachable[i] = {}

	if campus[i]:find("I") then
		ix = campus[i]:find("I", 1)
		iy = i
	end
end
reachable[N + 1] = {}

local peoples = 0

local function dfs(y, x)
	if x < 1 or x > M or y < 1 or y > N then
		return
	end
	if campus[y]:sub(x, x) == "X" then
		return
	end
	reachable[y][x] = true
	peoples = peoples + (campus[y]:sub(x, x) == "P" and 1 or 0)

	if x - 1 >= 1 and not reachable[y][x - 1] then
		dfs(y, x - 1)
	end

	if not reachable[y][x + 1] then
		dfs(y, x + 1)
	end 

	if y - 1 >= 1 and not reachable[y - 1][x] then
		dfs(y - 1, x)
	end

	if not reachable[y + 1][x] then
		dfs(y + 1, x)
	end
end

dfs(iy, ix)

if (peoples == 0) then
	print("ㅜㅜ")
else
	print(peoples)
end
