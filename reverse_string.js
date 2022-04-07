
function reverse_string(str){
const arr = []

for(let i=str.length;i>=0;i--){
  arr.push(str[i])
}
return arr.join("")
}

console.log(reverse_string("sagar"))