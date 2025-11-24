let letters = [];
for (let i = 97; i < 123; i++) {
  letters.push(String.fromCharCode(i));
}
for (let i = 65; i < 91; i++){
  letters.push(String.fromCharCode(i));
}

let symbols = [];
for (let i = 33; i < 48; i++) {
    symbols.push(String.fromCharCode(i));
}
for (let i = 58; i < 65; i++) {
    symbols.push(String.fromCharCode(i));
}
for (let i = 91; i < 97; i++) {
    symbols.push(String.fromCharCode(i));
}
for (let i = 123; i < 127; i++) {
    symbols.push(String.fromCharCode(i));
}

let nums = [];
for (let i = 48; i < 58; i++) {
  nums.push(String.fromCharCode(i));
}

console.log(`Welcome to the Password Generator!`)
let numLetters = Number(prompt(`How many letters would you like in your password?`))

let numSymbols = Number(prompt(`How many symbols?`))

let numNumbers = Number(prompt(`How many numbers?`))

let passwordList = [];

function shuffle(array){
    let currentIndex = array.length;

    while (currentIndex != 0){
        let randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
}

for (let i = 0; i < numLetters; i++){
    shuffle(letters);
    passwordList.push(letters[i]);
}

for (let i = 0; i < numSymbols; i++){
    shuffle(symbols);
    passwordList.push(symbols[i]);
}

for ( let i = 0; i < numNumbers; i++){
    shuffle(nums);
    passwordList.push(nums[i]);
}

shuffle(passwordList);

let password = "";
for (let i = 0; i < passwordList.length; i++){
    password += passwordList[i]
}

console.log(`Your password:
${password}`)
