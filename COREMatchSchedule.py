""" Match schedule imported from TBA before competition. Use scraping program found at
    https://github.com/core2062/TBAScraper to quickly get this data that is
    formatted correctly,
    Format: red team1, red team2, red team3, blue team1, blue team3, blue team3 """

SCHEDULE = [
    (1,2,3,4,5,6),#1 pass 1
    (7,8,9,10,11,12), #2
    (13,14,15,16,17,18), #3
    (1,2,3,4,5,6), #4
    (7,8,9,10,11,12), #5
    (13,14,15,16,17,18), #6 STOP pass 17
    (1,2,3,4,5,6), #7
    (7,8,9,10,11,12), #8
    (13,14,15,16,17,18), #9
    (1,2,3,4,5,6), #10
    (7,8,9,10,11,12), #11
    (13,14,15,16,17,18) #12
]
