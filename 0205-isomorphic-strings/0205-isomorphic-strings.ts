function isIsomorphic(s: string, t: string): boolean {
    
    const dico1 = new Map<string, string>();
    const dico2 = new Map<string, string>();
    
    if (s.length != t.length)
        return false
    
    for ( let i = 0; i<= s.length; i++)
    {
        if(dico1.has(s[i]) && dico1.get(s[i]) !== t[i])
        {
            return false
        }
        if (dico2.has(t[i]) && dico2.get(t[i]) !== s[i])
        {
            return false
        }
        
        dico1.set(s[i], t[i])
        dico2.set(t[i], s[i])
        
    }
    return true

};