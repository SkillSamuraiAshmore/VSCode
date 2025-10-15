let player = {
    age: 99,
    name: 'ABC',
    isActive: true,
    outfit: {
        color: 'blue',
        size: 'M',
        cost: 100, 
        isNew: true,
    }
};

console.log(player);

console.log(player.name);
console.log(player['name']);

player.health = 100;
console.log(player);

delete player.health;
console.log(player);

console.log(player.outfit.color)

player.outfit.size = 'S';
console.log(player);


// implement methods for player object
let player = {
  health: 100,
  fun: 0,
  play: function() {
    this.fun += 10;
  },
  eat: function(food) {
    if(food == 'apple') {
      this.health += 10;
    }
    else if(food == 'candy') {
      this.health -= 5;
      this.fun += 5;
    }
  }
  
};

// execute methods
player.play();
console.log(player);

player.eat('apple');
console.log(player);

player.eatApple();
console.log(player);