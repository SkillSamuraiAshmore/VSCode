let player = {
  age: 25, 
  name: "Place_holder",
  isActive: true,
  outfit: {
    color: "blue",
    size: "M",
    cost: 100,
    secondhand: false
  }
};

console.log(player);

player.isActive = false;
console.log(player.isActive);
console.log(player.outfit.cost);

player.outfit.size = "XXXXXL";
console.log(player);