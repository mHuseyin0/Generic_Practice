print("xde" .. "xxd")

-- Comment
--[[
--  Multiline comment
--]]

-- nil (correspons to null), number, string, boolean, table (corresponds to arrays) are data types

local a = 5

print(a .. " is a type of " .. type(a))

local strNum = "22"

print(strNum + 5)
print(tonumber(strNum) + 5)
print(math.random())
print(string.len(strNum))

local age = 15
local isValid = false

if age > 18 and isValid then
	print("Passed.")
elseif age > 18 then
	print("You are not valid.")
else
	print("You are younger than 18.")
end

for i = 1, 3, 1 do
	for j = 1, 3, 1 do
		print("i: " .. i .. " j: " .. j)
	end
end

print("age:")
while age < 18 do
	print(age)
	age = age + 1
end
print()
print("x:")
local x = 0
repeat
	x = x + 1
	print(x)
until x == 10

print("\nInput:")
local input = io.read()

print("input: " .. input)

-- table, coroutine and os modules are also useful
-- some kind of OOP is also available
os.execute("firefox")
