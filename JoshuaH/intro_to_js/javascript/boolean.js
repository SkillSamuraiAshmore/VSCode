// let distance = 250;
// let fuel = 100;
// let distanceCondition = distance <= 200 && distance >= 100;
// let isEngineBroken = true
// let isEngineFunctioning = false;

// if (!isEngineFunctioning || distance > 200) {
//     console.log('wont make it')
// }

// else if(distance = 200) {
//     console.log('wont make it');
// }

// else if(distanceCondition && fuel >=100) {
// console.log('you will make it')
// }

// else if(distance < 100 && fuel >= 25) {
//     console.log('you will make it')
// }

// console.log(a);
function hourToMinutes(hours) {
    let result = hours * 60;
    console.log(hours);
    return result;
}

let a = hourToMinutes(10);
let b = hourToMinutes(20);

let dayToHours = function(days) {
    return days * 24;
}

let c = dayToHours(1);
console.log(c);

//variables declaration 
let balance = 100;
let stock = 50;
let price = 5;
let quantity = 8;

function sellitem (quantity){
//1. check if we have stock 
if (quantity <= stock) {
    //rediuce stock increase balance
    //stock = stock - quantity 
    stock -= quantity;

    //balance = balance + price * quantity 
    balance += price * quantity 

    console.log('purchase completed, balance', balance, stock)}
    else{
    console.log('not enough stock')
}
}

sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)

