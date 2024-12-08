local C, R = io.read("*n", "*n")
local matrix = {}
local visited = {}
local B = 0
local W = 0

io.read()

for r = 1, R do
	matrix[r] = {}
	local row = io.read("*l")
	visited[r] = {}
	for c = 1, C do 
		matrix[r][c] = row:sub(c, c)
		visited[r][c] = false
	end
end

local function get_area(r, c, color) 
	if r < 1 or r > R or c < 1 or c > C or visited[r][c] or matrix[r][c] ~= color then
		return 0
	end
	visited[r][c] = true
	return 1 + get_area(r - 1, c, color) + get_area(r + 1, c, color) + get_area(r, c - 1, color) + get_area(r, c + 1, color)
end

for r = 1, R do
	for c = 1, C do
		if not visited[r][c] then
			local area = get_area(r, c, matrix[r][c])
			if matrix[r][c] == "B" then
				B = B + area * area
			else
				W = W + area * area
			end
		end
	end
end

io.write(W, " ", B)
