function strStr(haystack: string, needle: string): number {
    const n = haystack.length;
    const m = needle.length;
    let index = 0

    if (m === 0) return 0;
    if (m > n) return -1;

    for (let i = 0; i<= n - m; i++)
    {
        let valid = true

        for (let j = 0; j < m; j++)
        {
            if (haystack[i + j] !== needle[j])
            {
                valid = false
                break 
            }
        }
        
        if(valid) return i 
    }

    return -1

    
}
