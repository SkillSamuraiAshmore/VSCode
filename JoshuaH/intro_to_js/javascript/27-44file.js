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