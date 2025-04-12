"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    i=0
    while i<len(paragraphs):
        if not select(paragraphs[i]):
            paragraphs.remove(paragraphs[i])
            continue
        i=i+1
    if k<len(paragraphs):
        return paragraphs[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def f(a):
        c=remove_punctuation(a)
        d=lower(c)
        e=split(d)
        for m in topic:
            for n in e:
                if m==n:
                    return True
        return False
    return f
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    if typed=='' and source=='':
        return 100.0
    elif typed==''and source!='':
        return 0.0
    elif typed!=''and source=='':
        return 0.0
    else:
        k=0.0
        a=len(typed_words)
        b=len(source_words)
        if a>=b:
            for i in range(b):
                if typed_words[i]==source_words[i]:
                    k=k+1
            return 100*k/a
        else:
            for i in range(a):
                if typed_words[i]==source_words[i]:
                    k=k+1
            return 100*k/a
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed)/5*60/elapsed
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    def f(typed_word, word_list, diff_function, limit):
        for i in word_list:
            if diff_function(typed_word,i,limit)<=limit:
                return True
        return False
    if f(typed_word, word_list, diff_function, limit):
        a=diff_function(typed_word,word_list[0],limit)
        p=word_list[0]
        for i in word_list:
            if typed_word==i:
                return i
            b=diff_function(typed_word,i,limit)
            if a>b:
                p=i
                a=diff_function(typed_word,i,limit)
        return p
    else:
        return typed_word
    # END PROBLEM 5


def sphinx_fixes(typed, source, limit):#这种消消乐要牢记，一样的就除掉，每次就可以只比较第一个
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if limit<0:
        return limit+1
    elif typed==source:
        return 0
    elif len(typed)==0 and len(source)!=0:
        return len(source)
    elif len(typed)!=0 and len(source)==0:
        return len(typed)
    elif typed[0]==source[0]:
        return sphinx_fixes(typed[1:], source[1:], limit)
    else:
        return 1+sphinx_fixes(typed[1:], source[1:], limit-1)
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):#有limit的限制，如果执行次数超过limit就不会再执行，就简单了
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.
    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # BEGIN PROBLEM 7
    if limit<0:#属于是没认真读题，人家都说了不能超过最大限制,甚至上一题都没看
        return limit+1
    if start==goal:
        return 0
    elif len(start)==0 and len(goal)!=0:
        return len(goal)
    elif len(start)!=0 and len(goal)==0:
        return len(start)
    elif start[0]==goal[0]:
        return minimum_mewtations(start[1:],goal[1:],limit)
    else:
        add=1+minimum_mewtations(start,goal[1:],limit-1)
        remove=1+minimum_mewtations(start[1:],goal,limit-1)
        substitude=1+minimum_mewtations(start[1:],goal[1:],limit-1)
        return min(add,remove,substitude)
        
    # END PROBLEM 7


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    p=0
    for i in range(len(typed)):
        if typed[i]==prompt[i]:
            p=p+1
        else:
            break
    upload({'id':user_id,'progress':p/len(prompt)})
    return p/len(prompt)
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a game data, which contains a list of 
    words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    q=[]
    for k in range(len(times_per_player)):
        p=[]
        for a in range(len(times_per_player[k])-1):
            p=p+[times_per_player[k][a+1]-times_per_player[k][a]]
        q=q+[p]
    return game(words,q)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    # lists of indices for each player and each word
    player_indices = range(len(get_all_times(game)))
    word_indices = range(len(get_all_words(game)))
    # BEGIN PROBLEM 10
    q=[]
    for a in range(len(get_all_times(game))):
        p=[]
        for b in range(len(get_all_words(game))):
            n=get_all_times(game)[0][b]
            s=0
            k=0
            while k<len(get_all_times(game))-1:
                if n>get_all_times(game)[k+1][b]:
                    n=get_all_times(game)[k+1][b]
                    s=k+1
                k=k+1
            if a==s:
                p=p+[get_all_words(game)[b]]
        q=q+[p]
    return q

    
    # END PROBLEM 10


def game(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), \
        'words should be a list of strings'
    assert all([type(t) == list for t in times]),\
        'times should be a list of lists'
    assert all([isinstance(i, (int, float))for t in times for i in t]), \
        'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), \
        'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(game, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(game["words"]), \
        "word_index out of range of words"
    return game["words"][word_index]


def time(game, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game["words"]), "word_index out of range of words"
    assert player_num < len(game["times"]), \
        "player_num out of range of players"
    return game["times"][player_num][word_index]


def get_all_words(game):
    """A selector function for all the words in the game"""
    return game["words"]


def get_all_times(game):
    """A selector function for all typing times for all players"""
    return game["times"]


def game_string(game):
    """A helper function that takes in a game dictionary and returns a string representation of it"""
    return f"game({get_all_words(game)}, {get_all_times(game)})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = choose(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
