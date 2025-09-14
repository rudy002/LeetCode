function mySqrt(x: number): number {
    
    let result = 0

    for(let i = 0; i<= x; i++)
    {
        if(i*i <= x)
            result = i
        else
            break
    }

    return result
};