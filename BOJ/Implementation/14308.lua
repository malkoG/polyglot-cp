local T = tonumber(io.read())

local matrix = {}
local counter = {}
local function init_matrix(R, C)
	for i = 1, R do
		matrix[i] = {}
		counter[i] = {}
		for j = 1, C do
			matrix[i][j] = 0
			counter[i][j] = 0
		end
	end
end

local empty = function(R, C)
	for i = 1, R do
		for j = 1, C do
			matrix[i][j] = 0
			counter[i][j] = 0
		end
	end
end

local fill = function(_r, _c, K)
	for i = 1, K do
		local x, y = io.read("*n", "*n")
		matrix[x + 1][y + 1] = 1
	end
end

local scan = function(R, C)
	for i = 1, R do
		for j = 1, C do
			if (matrix[i][j] == 0) then
				counter[i][j] = 1
				if (i > 1 and j > 1) then
					-- min of values of left, top and top-left
					counter[i][j] = math.min(counter[i - 1][j], counter[i][j - 1], counter[i - 1][j - 1]) + 1
				end
			end
		end
	end
end

local print_matrix = function(R, C)
	for i = 1, R do
		for j = 1, C do
			io.write(matrix[i][j], " ")
		end
		io.write("\n")
	end
end



init_matrix(3000, 3000)
for i = 1, T do
	local R, C, K = io.read("*n", "*n", "*n")

	empty(R, C)
	fill(R, C, K)
	scan(R, C)

	local count = 0 
	for i = 1, R do
		for j = 1, C do
			if (counter[i][j]) then
				count = count + counter[i][j]
			end
		end
	end

	print("Case #" .. i .. ": " .. count)
end
