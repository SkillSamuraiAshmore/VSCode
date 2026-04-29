//function hourToMinutes(hours) {
//  let result = hours * 60;
//  console.log(result);
//  return result;
//}

//let a = hourToMinutes(10);
//let b = hourToMinutes(20);
//console.log(a);
//console.log(b);

//let dayToHours = function(days) {
//  return days * 24;
//}

//let c = dayToHours(7);
//console.log(c);

let balance = 100;
let stock = 8;
let price = 5;
let quantity = 8;

function sellitem(quantity) {
  if(quantity <= stock) {
    stock = stock - quantity;
    balance = balance + (price * quantity);
    console.log("Purchase successful!");
    console.log("Remaining stock: " + stock);
    console.log("New balance: " + balance);
  }
  else {
    console.log("Purchase failed: Not enough stock.");
  }
}