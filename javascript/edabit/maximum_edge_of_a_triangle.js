/*
# Maximum Edge of a Triangle

Create a function that finds the maximum range of a triangle 's third edge.

## Examples
* nextEdge(8, 10)➞ 17
* nextEdge(5, 7)➞ 11
* nextEdge(9, 2)➞ 10

## Notes
(side1 + side2) - 1 = maximum range of third edge.
All given triangles have side lengths that are positive integers.
Don 't forget to return the result.

Source:
https: //edabit.com/challenge/nhXofMMyrowMyr9Nv
*/
function nextEdge(side1, side2) {
    return (side1 + side2) - 1;
}


/**
 * Run sample nextEdge functions, print results to console.log.
 */
console.log(nextEdge(5, 4) == 8)
console.log(nextEdge(8, 3) == 10)
console.log(nextEdge(7, 9) == 15)
console.log(nextEdge(10, 4) == 13)
console.log(nextEdge(7, 2) == 8)