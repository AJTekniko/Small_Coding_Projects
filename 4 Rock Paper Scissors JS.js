const rock = "💎";
const paper = "📰";
const scissors = "✂";

const gameImages = [rock, paper, scissors];

let user = Number(prompt(`What do you choose?
Type 0 for Rock, 1 for Paper or 2
for Scissors.`));

//print user image
if (user >= 0 && user <= 2){
    console.log(gameImages[user]);
}

//Create random value and print computer image
let computer = Math.floor(Math.random() * 3);
console.log(gameImages[computer]);

//Compare user choise to computer choice
if (user >= 3 || user < 0){
    console.log(`You did not select a valid option.
Game over`);
}
else if (user == 0 && computer == 2){
    console.log("You win!");
}
else if (user == 2 && computer == 0){
    console.log("You lose!");
}
else if (user < computer){
    console.log("You lose!");
}
else if (user > computer){
    console.log("You win!");
}
else if (user == computer){
    console.log("It's a draw");
}
