
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

#optimal # of edits between S and T

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    # TODO -  implement memoization

    slen, tlen = (len(S), len(T))

    MED = [[0 for m in range(tlen + 1)] for n in range(slen + 1)]

    for o in range(len(S) +1):
      for p in range(len(T) + 1):
        if o == 0:
          MED[o][p] = p
        elif p == 0:
          MED[o][p] = o
        elif S[o-1] == T[p-1]:
          MED[o][p] = MED[o-1][p-1]
        else:
          MED[o][p] = 1 + min(MED[o][p-1], MED[o-1][p], MED[o-1][p-1])
    
    return MED[-1][-1]

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment


    slen, tlen = (len(S), len(T))
  
    MED = [[0 for m in range(tlen)] for n in range(slen)]

    for o in range(len(S)):
      for p in range(len(T)):
        if o == 0:
          MED[o][p] = p
        elif p == 0:
          MED[o][p] = o
        elif S[o-1] == T[p-1]:
          MED[o][p] = MED[o-1][p-1]
        else:
          MED[o][p] = 1 + min(MED[o][p-1], MED[o-1][p], MED[o-1][p-1])
    
 
    aline_s = ""
    aline_t = ""
  
    if len(S) == 0:
      aline_s = '-' * len(T)
      return aline_s, T

    if len(T) == 0:
      aline_t = '-' * len(S)
      return S, aline_t


    if S[0] == T[0]:
      aline_s = (S[0]+ fast_align_MED(S[1:], T[1:])[0])
      aline_t = (T[0]+ fast_align_MED(S[1:], T[1:])[1])


    addchar = fast_MED(S, T[1:])
    delchar = fast_MED(S[1:], T)
    replace = fast_MED(S[1:], T[1:])

    if min(addchar, delchar, replace) == addchar: #and addchar != replace:
      aline_s = ('-'+ fast_align_MED(S, T[1:])[0])
      aline_t = (T[0]+ fast_align_MED(S, T[1:])[1])

    if min(addchar, delchar, replace) == delchar: #and delchar != replace:
      aline_s = (S[0]+ fast_align_MED(S[1:], T)[0])
      aline_t = ('-'+ fast_align_MED(S[1:], T)[1])

    if min(addchar, delchar, replace) == replace:
      aline_s = (S[0]+ fast_align_MED(S[1:], T[1:])[0])
      aline_t = (T[0]+ fast_align_MED(S[1:], T[1:])[1])

    return aline_s, aline_t

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])


