function binaryGap(number){
   const binaryValues = number.toString(2)
   let currentGap = 0
   let maximumGap = 0

    for(i=0; i<binaryValues.length; i++){
        if(binaryValues[i] === "0"){
            currentGap++
        }else{
            if(currentGap>maximumGap){
                maximumGap = currentGap
            }
            currentGap = 0
        }
    }
    console.log(`the maximum gap is ${maximumGap}`)
}
binaryGap(529)