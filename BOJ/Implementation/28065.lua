local n = tonumber(io.read())

local solution = "1"
local val = 1
local sign = 1

for i = n - 1, 1, -1 do
	val = val + i * sign
	solution = solution .. " " .. val
	sign = sign * -1
end


print(solution)
