from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genres_dicts = defaultdict(dict)
    
    for i in range(len(genres)):
        genres_dicts[genres[i]][i] = plays[i]
        
    genres_dicts = dict(sorted(genres_dicts.items(), key=lambda item: sum(item[1].values()), reverse=True))
    
    for id, genres_dict in genres_dicts.items():
        sorted_genres = sorted(genres_dict.items(), key=lambda item: (item[1], -item[0]), reverse=True)
        for i in range(min(2, len(sorted_genres))):
            answer.append(sorted_genres[i][0])
    
    return answer