var redDoorE1 = document.querySelector("#r");
var greenDoorE1 = document.querySelector("#g");
var blueDoorE1 = document.querySelector("#b");

redDoorE1.addEventListener("click", checkDoor);
greenDoorE1.addEventListener("click", checkDoor);
blueDoorE1.addEventListener("click", checkDoor);

function checkDoor(e) {
    var clickedDoor = e.target;
    console.log(clickedDoor.id);

    if (clickedDoor.id === "r") {
        console.log("You clicked the red door.");
    }

    else if (clickedDoor.id === "g") {
        console.log("You clicked the green door.");
    }
    else {
        console.log("You clicked the blue door.");
    }
}








//function checkDoor(e) {
//    console.log(e.target);
//    console.log(e.type);
//}