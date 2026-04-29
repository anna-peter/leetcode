from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = Counter()
        outputdomains = []

        # split out the count 
        # count how many times discuss.leetcode.com -> counts['discuss.leetcode.com'] 
        # count leetcode.com -> counts['leetcode.com']
        # count .com -> counts['.com']
        for domain in cpdomains: 
            count, url = domain.split(" ") # split out the count and url
            # update count to count every occurrence
            count = int(count)
            fragments = url.split( ".") # -> ['discuss', 'leetcode', 'com'] or [ 'leetcode', 'com']
            for i in range(len(fragments)):  # to get the length of arr cant do arr.len()
                url_to_add = ".".join(fragments[i:])
                print(url_to_add)
                
                counts[url_to_add] += count # add the count we saw to that url
                
        for url, url_count in counts.items():           
            outputdomains.append(f"{url_count} {url}")
        
        print(outputdomains)
        return outputdomains




        
        