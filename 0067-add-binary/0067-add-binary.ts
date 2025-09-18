function addBinary(a: string, b: string): string {
    
    const maxLength = Math.max(a.length, b.length);

    a = a.padStart(maxLength, "0") 
    b = b.padStart(maxLength, "0") 

    let retenu = 0
    const result: string[] = []

    for (let i = maxLength - 1; i >=0; i--)
    {
        let bitA = a[i] === "1" ? 1 : 0;
        let bitB = b[i] === "1" ? 1 : 0;

        let sum = bitA + bitB + retenu

        result.push((sum % 2).toString())
        retenu = sum >= 2 ? 1 : 0
        
    }

    if (retenu ===1)
        {
            result.push("1")
        }

        return result.reverse().join("")


};