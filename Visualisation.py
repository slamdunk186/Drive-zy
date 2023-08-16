import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
# wn.setup(1920, 1080)
alex.fillcolor("blue")
alex.speed(10)
alex.hideturtle()



def clear(ball):
    loop = 15
    ball.speed(10)
    while (loop > 0):
        loop -= 1
        # clearing the turtle work
        ball.clear()

        # updating the screen
        wn.update()

        # forward motion by turtle object
        ball.forward(60)


def ngon(n):
    turtles = []
    alex.penup()
    alex.right(90)
    alex.forward(90)
    alex.left(90)
    for i in range(n):
        turtles.append(turtle.Turtle())
    for i in range(n):
        alex.forward(100)
        alex.left(360 / n)
        P = alex.pos()
        turtles[i].penup()
        turtles[i].goto(P)
        turtles[i].fillcolor('blue')
        turtles[i].begin_fill()
        turtles[i].shape("circle")
        turtles[i].end_fill()
        #turtles[i].hideturtle()

    return turtles

def solve():
    n = int(input())
    m = int(input())
    vehicles = ngon(n)
    graph = []
    out_deg = []
    vis = []
    rev_graph = []
    for i in range(n):
        graph.append([])
        rev_graph.append([])
        vis.append(False)
        out_deg.append(0)
    for i in range(m):
        u, v = input().split()
        u = int(u)
        v = int(v)
        graph[u].append(v)
        rev_graph[v].append(u)
        pos1 = vehicles[u].pos()
        pos2 = vehicles[v].pos()
        alex.penup()
        alex.goto(pos1)
        alex.pendown()
        alex.goto(pos2)
        alex.penup()

    alex.penup()
    for i in range(n):
        alex.goto(vehicles[i].pos())
        
        alex.back(40)
        alex.write(i, font=("Cooper Black", 25, "italic"))

    q = []
    q.append(0)
    while (len(q) > 0):
        u = q.pop()
        print(u)
        vis[u] = True
        for v in graph[u]:
            if (vis[v] == False):
                q.append(v)

        out_deg[u] = len(graph[u])

    cnt = 0
    while (cnt < n):
        for i in range(n):
            if (out_deg[i] == 0):
                print("Vehicle " +str(i) + " is instructed to move") 
                clear(vehicles[i])
                for j in rev_graph[i]:
                    out_deg[j] -= 1

                out_deg[i] = 100000000000
                cnt += 1


solve()
wn.mainloop()
