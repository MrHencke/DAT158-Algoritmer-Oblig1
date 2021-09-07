def BMMatch(Text, Pattern): 
    m = len(Pattern)
    n = len(Text)
    i = m-1
    j = m-1
    comparisons = 0

    while  i <= n-1:
        comparisons +=1
        if Pattern[j] == Text[i]:
            if j == 0:
                return "Found the given pattern in index: {} after {:.2f} comparisons per character".format(i, comparisons/n)
            else:
                i-=1
                j-=1
        else:
            i = i+m - min(j, 1 + last(Text[i], Pattern))
            j = m-1
    
    return "There is no substring in T matching P"

def last(Character, Pattern):
    return Pattern.find(Character)


if __name__ == '__main__':    
    Text = "minoritetsladningsbærerdiffusjonskoeffisientmålingsapparaturet var med fylkestrafikksikkerhetsutvalgssekretariatslederfunksjonene på tur i dag, de tenkte på onomatopoetikon"
    Pattern = "lederfunk"
    print(BMMatch(Text, Pattern))    