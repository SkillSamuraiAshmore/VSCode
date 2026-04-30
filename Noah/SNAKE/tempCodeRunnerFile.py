def move_left():
  x = player.xcor()
  x = max(x - playerspeed, -280)
  player.setx(x)