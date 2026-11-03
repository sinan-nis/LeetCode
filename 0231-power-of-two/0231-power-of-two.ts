function isPowerOfTwo(n: number): boolean {
    if(Number.isInteger(Math.log2(n))) return true;
    return false;
};