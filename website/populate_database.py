b = {1: "the",	21: "at",	41: "there",	61: "some",	81: "my",
2: "of",	22: "be",	42: "use",	62: "her",	82: "than",
3: "and",	23: "this",	43: "an",	63: "would",	83: "first",
4: "a",	24: "have",	44: "each",	64: "make",	84: "water",
5: "to",	25: "from",	45: "which",	65: "like",	85: "been",
6: "in",	26: "or",	46: "she",	66: "him",	86: "call",
7: "is",	27: "one",	47: "do",	67: "into",	87: "who",
8: "you",	28: "had",	48: "how",	68: "time",	88: "oil",
9: "that",	29: "by",	49: "their",	69: "has",	89: "its",
10: "it",	30: "word",	50: "if",	70: "look",	90: "now",
11: "he",	31: "but",	51: "will",	71: "two",	91: "find",
12: "was",	32: "not",	52: "up",	72: "more",	92: "long",
13: "for",	33: "what",	53: "other",	73: "write",	93: "down",
14: "on",	34: "all",	54: "about",	74: "go",	94: "day",
15: "are",	35: "were",	55: "out",	75: "see",	95: "did",
16: "as",	36: "we",	56: "many",	76: "number",	96: "get",
17: "with",	37: "when",	57: "then",	77: "no",	97: "come",
18: "his",	38: "your",	58: "them",	78: "way",	98: "made",
19: "they",	39: "can",	59: "these",	79: "could",	99: "may",
20: "I",	40: "said",	60: "so",	80: "people",	100: "part"}
# s = []
# for x in b.values():
#     balls.append(x)
# print(s)

a = ['the', 'at', 'there', 'some', 'my', 'of', 'be', 'use', 'her', 'than', 'and', 'this', 'an', 'would', 'first', 'a', 'have', 'each', 'make', 'water', 'to', 'from', 'which', 'like', 'been', 'in', 'or', 'she', 'him', 'call', 'is', 'one', 'do', 'into', 'who', 'you', 'had', 'how', 'time', 'oil', 'that', 'by', 'their', 'has', 'its', 'it', 'word', 'if', 'look', 'now', 'he', 'but', 'will', 'two', 'find', 'was', 'not', 'up', 'more', 'long', 'for', 'what', 'other', 'write', 'down', 'on', 'all', 'about', 'go', 'day', 'are', 'were', 'out', 'see', 'did', 'as', 'we', 'many', 'number', 'get', 'with', 'when', 'then', 'no', 'come', 'his', 'your', 'them', 'way', 'made', 'they', 'can', 'these', 'could', 
'may', 'I', 'said', 'so', 'people', 'part']

def import100words(db):
    for word in (a):
        db.session.add(Word(data=word))