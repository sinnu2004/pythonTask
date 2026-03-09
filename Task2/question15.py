def angle(M):
    return M*30

H = int(input("Enter the hour hand :"))
M = int(input("Enter the minute hand :"))
diff = abs(H-M)

print(angle(diff))