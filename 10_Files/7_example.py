COMMA = ", "
points=" "
nba_input_file=open(r"c:\Python\nba.txt","r")
for row in nba_input_file:
    current = row.split(COMMA)[1]
    points+=current
nba_input_file.close();
print(points)

points_file = open(r"c:\Python\nba_res.txt","w")
points_file.write(points)
points_file.close