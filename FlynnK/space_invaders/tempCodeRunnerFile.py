for invader in invaderList:
                y = invader.ycor()
                y = y - 25
                invader.sety(y)

        if invader.distance(bullet) < 15:
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            x = random.randint(-200, 200)
            y = random.randint(100, 200)
            invader.setposition(x, y)

            score += 10
        
        if invader.distance(player) < 15:
            player.hideturtle()
            invader.hideturtle()
            print("your score was: ", score)
