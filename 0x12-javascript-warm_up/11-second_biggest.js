#!/usr/bin/node

// // This function sorts the array in descending order
// function sort(arr) {
//   let n = arr.length;
//   let swap = false;

//   for (let i = 0; i < n; i++){
//     for (let j = i + 1; j < n; j++){
//       if (parseInt(arr[j]) > parseInt(arr[i])) {
//         temp = arr[j]; arr[j] = arr[i]; arr[i] = temp;
//         swap = true;
//       }
//     }
//     if (swap === false) {
//       return arr;
//     }
//     swap = false;
//   }
//   return arr;
// }

// // This function returns the second member of the sorted array
// function max2(arr) {
//   let a = sort(arr);
//   n = a.length;
//   if (n === 0 || n === 1) return 0;
//   return a[1];
// }

// arr = process.argv.slice(2);
// console.log(max2(arr));

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => b - a);
  console.log(args[1]);
}
