let distance = 50;
let fuel = 25;
let distanceCondition = distance <= 200 && distance > 100;
let isEngineWorking = false;

if(!isEngineWorking || distance > 200) {
  console.log("won't make it");
}

else if(distance > 200) {
  console.log("won't make it");
}

else if(distanceCondition && fuel >= 100) {
  console.log("you will make it");
}

else if(distance <= 100 && fuel >= 25) {
  console.log("you will make it");
}