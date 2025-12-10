function sendSignal(){
    console.log('Help')
}

/* we havent run this 1000 times */
while(i < 1000){
    sendSignal();
    //i = i+1;
    //i += 1;
    i++;
}

let result = 0;

let j = 1;

while (j <= 10) {
    result = result + j;
    console.log(result);
    j++;
}

console.log(result);



let fuel = 1000;
let distance = 0;

while(fuel > 0) {
    distance ++;

    if(distance >= 100 && distance < 200)

    

    if (distance == 500) {
        continue;

    }

    fuel --;

    if (distance == 500) {
        break;

    }
}

console.log(distance, fuel);



let population = 100;

// population = population * 1.05;
// population *= 1.05;

let i = 0;
while (i < 10) {
    population *= 1.05;
    i++
}


for(let i = 0; i < 10; i++){
    population *=1.05;
}

console.log(population);


let database = ['turtle', 'cat', 'dog', 'bird'];
console.log(database);
console.log(databas.length);

let animal = database[1];
console.log(animal);

datdabase[0] = 'dinosaur';
console.log(database);

let last = database [database.length - 1];
console.log (last);

database.push('lizard');
console.log(database)

database.pop();
console.log(database);

let scores = [10, 20, 10];

let p = 0;
while(p < scores.length) {
    score[p]++;
    i++
}

console.log(scores);

for(p = 0; p < scores.length; i++) {
    scores[i]++;
}

console.log

scores.forEach(function(entry, index){
    console.log(entry, index);
    scores[p]++
});
console.log(scores);

scores.forEach(function(entry, index){
    scores[p]++
});
console.log(scores);

let catalog = [{
    title: 'Js for beginners',
    author: 'josh',
    copies: 1
}]

catalog.forEach(function(entry, index){
    if(entry.author == 'zenva'){
        entry.copies++;
    }
})

console.log(catalog);

let a = [[1, 2, 3], [4, 5, 6., 7]]
console.log(a[0][1]);

a[1][2] = 100;

console.log(a[1][2]);

let terrains = [
    ['desert', 'desert', 'grass', 'grass']
    ['desert', 'desert', 'grass', 'grass'],
    ['desert', 'desert', 'grass', 'grass'],
    ['desert', 'desert', 'grass', 'grass']
];