# Last updated: 20/11/2025, 20:05:20
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #hmm intervals hmmm 
        # 2 numbers from each interval 
        #minimise number of intervals basically 
        #each interval has atleast two numbers start and end 
        #so i need to combine intervals till they become disjoint / or a single number be the joining them 
        # combining means intersection ie 
        #keep on interesecting as long as u have 2 numbers ? 
        #but intersection in waht order ? 
        #say i sort it by end 
        #so teh first set i get is the one whihc ends earliest so if i have to pick two numbers form this set 
        #its optimal to pick end , end-1 
        #its just greedy based on end? 
        #looks easy and looks correct why is this porblem rate dhard 
        intervals.sort(key=lambda x:(x[1]))
        #sorted based on end 
        print(intervals)
        chosen=set() 
        #i porbbaly wont need this lets see 
        count=0 
        #so to start i want start>end so first interval gets both of its things chosen 
        #ie 
        E=-1
        E2=-2 

        #after writing for loop i am realising it maybe better if i sort based on start ascending after end ascending 
        #but tbh shouldnt make a differnce
        #the fix is simple track last two max numbers and boom it is fixed , then what order u sort start wouldnt matter tooo 
        #E and E2 repeesent max2 nos in picked essentaillu 
        #with E>E2
        for start,end in intervals: 
            #let capital E be the last chosen end 
            if start<=E2:
                #full intersection
                pass
            elif start<E:
                #betwwen E2 and E both exclusive 
                #one intersection with E is guaranteed
                if E==end:
                    E2=end-1 
                    count+=1
                    continue
                E2=end
                E,E2=E2,E
                count+=1
            elif start==E:
                #E was already in picked set so pick one more number 
                #ah when i picked E here i didnt pick E-1 ,so my invariant didnt hold  just need to fix , still pretty close hehe given i thought it this was fast and its uspposed to be hard 
                E2=E
                E=end
                count+=1
                
            else:
                count+=2 
                E=end
                E2=end-1 
            print(E,E2,count)
        return(count)

#so i need two numbers hmmm lets do it yayy shoudl be easy 