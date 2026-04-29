let database = ["turtle", "cat", "dog", "bird"];
console.log(database)
console.log(database.length)

let animal = database[3];
console.log(animal);

database[0] = "dino";
console.log(database)
console.log(database[0])

let last = database[database.length - 1]
console.log(last)

database.push("lizard");
console.log(database);

database.pop();
console.log(database)