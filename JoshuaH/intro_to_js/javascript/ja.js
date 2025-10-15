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


let player = {
    health: 100,
    fun: 0,
    eatApple: function() {
        console.log('eat apple');

        //this.health = this.health + 10
        this.health += 10;

        console.log(this.health);
    }
};

player.eatApple();
console.log(player);