
function bubbleSort(arr){
    len = arr.length
    for(i=0;i<len;i++){
        for(j=0;j<(len-i-1);j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    console.log(arr)
}

var arr = [234, 43, 55, 63, 5, 6, 235, 547];
bubbleSort(arr);
