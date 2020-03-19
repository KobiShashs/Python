def sort_anagrams(list_of_strings):
    res = []
    from itertools import groupby
    return [list(group) for key,group in groupby(sorted(list_of_strings,key=sorted),sorted)]


    return res

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
#[['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]