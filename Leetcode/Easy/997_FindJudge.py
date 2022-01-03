class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        In-degree: how much a person is trusted by others.
        Out-degree: how much that person trusts.
            indegree - outdegree = n - 1
        """
        #print(f"People:{n}")
        # How much trust them - how much they trust (should equal `n-1`)
        degrees = [0]*(n+1) # people aren't 0-indexed, so `n+1`, ignore degrees[0]...
    
        # If only 1 person, and no trusting going on... that's the judge!
        if n == 1 and not trust:
            return 1
    
    
        for trusting, trusted in trust:
            #print(f"Person {trusting} trusts {trusted}.")
            # Another person they trust (outdegree)
            degrees[trusting] -= 1
            # This person is trusted (indegree)
            degrees[trusted] += 1
        #print(degrees[1:])
        
        return degrees.index(n-1) if (n-1) in degrees else -1
            
        
        
        
"""

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
  The town judge trusts nobody.
  Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
      You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

"""
            
            
"""
We need a single value assigned to each person, instead of having a 
"trusted" & "trusting" list, then re-looping a bunch after going through `trust`.
  - The Judge should be trusted by (n-1) people (all but himself).
    - His score should be (n-1): +1 for all people that trust him, except himself.
  - Other people can be trusted, but not universally like the Judge. They also cannot trust anyone themselves!
   
indegree - outdegree = n-1
    how much they are trusted - how much they trust = total-1
    
The only one that can achieve the above is the JUDGE.
  - If everybody trusts Person A, but they themselves trust someone, they won't have a (n-1) score, but (n-2)...
            
4 people
The judge must be : 3 - 0 = 4-1
                        3=3
                        trusted by 3 - trusts 0 = 3
                        
            
"""       
