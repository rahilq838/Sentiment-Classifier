
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt",'r') as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(string):
    for letter in string:
        if letter in punctuation_chars:
            string=string.replace(letter,'')
    return string 

def get_neg(sentence):
    neg_count=0
    sentence=sentence.split(" ")
    for wrd in sentence:
        wrd=strip_punctuation(wrd)
        if wrd.lower() in negative_words:
            neg_count+=1
    return neg_count

def get_pos(sentence):
    pos_count=0
    sentence=sentence.split(" ")
    for wrd in sentence:
        wrd=strip_punctuation(wrd)
        if wrd.lower() in positive_words:
            pos_count+=1
    return pos_count

with open("project_twitter_data.csv") as tData:
    listOfTweetsData=tData.readlines()
    resultData=open("resulting_data.csv",'w')
    for row in listOfTweetsData:
        if row!=row[0]:
            tweetData=row.split(',')
            print(tweetData)
            resultData.write('{},{},{},{},{}\n'.format(tweetData[1].strip(),tweetData[2].strip(),get_pos(tweetData[0]),get_neg(tweetData[0]),'') )
        else:
            resultData.write("Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score")

    resultData.close()