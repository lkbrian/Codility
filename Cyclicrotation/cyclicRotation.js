function cyclicRotation(Array,K){
    for(i=0;i<K;i++){
        let number = Array.pop()
        Array.unshift(number)
    }
    console.log(Array)
}
cyclicRotation([1,2,3,4,5],3)