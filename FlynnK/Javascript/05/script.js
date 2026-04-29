let item = "engines";

//if(item != "engine") {
//  console.log("not engine!")
//}

//let score = 60;
//if(score >= 60) {
//  console.log("pass");
//}

//else if(score <= 20) {
//  console.log("fail");
//}

//let isEngine = item == "engine";
//console.log(isEngine);


let balance = 9;
let itemPrice = 10;

if(balance >= itemPrice) {
  console.log("purchased item");
  balance -= itemPrice;
  console.log("balance: " + balance);
}

else if(balance < itemPrice) {
  console.log("not enough money");
}