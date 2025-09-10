let player = {age: 99, name:'ABC', isActive: true};

console.log(player);

console.log(player.name);
console.log(player.['name']);

player .isActive = false;
console.log(player);

player.health = 100;
console.log(player);

delete player.health
console.log(player)