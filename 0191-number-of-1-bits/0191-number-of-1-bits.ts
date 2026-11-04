function hammingWeight(n: number): number {
    const str: string = n.toString(2);
    let counter: number = 0;
    for (const bits of str) {
        if (bits === "1") counter++;
    }
    
    return counter;
};