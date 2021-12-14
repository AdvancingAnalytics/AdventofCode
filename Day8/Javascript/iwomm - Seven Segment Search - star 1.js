fs = require('fs')

const input = fs.readFileSync('./input.txt', 'utf-8');
let inputData = input.split('\n');

let signalArr = [];
let outputArr = [];

function collectDigits(inputData) {
    for (let i=0; i < inputData.length; i++) {
        let [signal, output] = inputData[i].split(' | ');

        let signalDigits = signal.split(' ').map(item => item.trim());
        let outputDigits = output.split(' ').map(item => item.trim());
    
        signalArr.push(...signalDigits);
        outputArr.push(...outputDigits);
    }
}

function retrieveCount(arr, uniqueLen) {
    return arr.filter(x => x.length === uniqueLen).length
}

collectDigits(inputData);

// one uses unique number of segments: 2
let count1 = retrieveCount(outputArr, 2);

// four uses unique number of segments: 4
let count4 = retrieveCount(outputArr, 4);

// seven uses unique number of segments: 3
let count7 = retrieveCount(outputArr, 3);

// eight uses unique number of segments: 7
let count8 = retrieveCount(outputArr, 7);

console.log('Total occurences of digits 1, 4, 7 & 8: ' + (count1 + count4 + count7 + count8));
