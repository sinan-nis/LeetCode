function missingNumber(nums: number[]): number {
    
        let counter: number = 0;
        nums.sort((a: number, b: number): number => a - b);
        for (const num of nums){
            if (num === counter){
                counter++;
            }
            else{
                return counter;
            }
           
            
        }
            return nums.length;
};