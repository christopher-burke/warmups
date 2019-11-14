/*
Minutes to Seconds

Write a function that takes an integer minutes and converts it to seconds.

Source:
https: //edabit.com/challenge/8q54MKnRrm89pSLmW
*/

function convert(minutes) {
    return minutes * 60
}

/**
 * Run sample convert functions, print results to console.log.
 */
console.log(convert(6) == 360)
console.log(convert(4) == 240)
console.log(convert(8) == 480)
console.log(convert(60) == 3600)