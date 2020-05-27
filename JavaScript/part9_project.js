var fname = prompt("Enter your first name: ")
var lname = prompt("Enter your last name: ")
var height = prompt("Enter your height in cms: ")
var pet = prompt("Enter your pet name: ")

var flag = false
if(fname[0] === lname[0]){
    if(height >= 170){
        if(pet[pet.length()] === 'y')
            flag = true
    }
}

if(flag){
    console.log("Hello Their")
}