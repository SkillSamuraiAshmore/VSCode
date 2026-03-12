let player = {
  Health: 100, 
  Fun: 0,
  eatApple: function() {
    console.log("Eat apple")
    this.Health = this.Health + 10;
    console.log(this.Health)
  },
  eatcandy: function() {
    console.log("Eat candy")
    this.Fun += 10;
    this.Health -= 5;
  },
  Play: function() {
    console.log("Play")
    this.Fun += 20;
    this.Health += 5;
  }
};

console.log(player);

player.eatApple();
player.eatcandy();
player.Play();
console.log(player.Health);
console.log(player.Fun);