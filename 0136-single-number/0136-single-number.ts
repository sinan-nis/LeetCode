function singleNumber(nums: number[]): number {

    if (nums.length === 1) return nums[0];

    for (let i=0; i < nums.length; i++){
        let alreadyIn: boolean = false;

        for (let j=0; j< nums.length;j++){

            if(i === j) continue;

            if (nums[i] === nums[j]){
                alreadyIn = true;
                break;
            }
            
        }
        if(!alreadyIn) return nums[i];
    }
};