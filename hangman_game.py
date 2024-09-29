import tkinter as tk
from tkinter import messagebox
import random
import time

# Word list for the game
words = ['abuse', 'accident',  'activist', 'actor', 'administration', 'admit', 'adult', 'advertise', 'advise', 'afraid', 'agency', 'aggression', 'agriculture','airplane', 'airport','ambassador', 'amend', 'ammunition', 'amount', 'anarchy', 'ancestor', 'ancient', 'anger', 'animal', 'anniversary', 'announce', 'another', 'answer', 'apologize', 'archeology',  'arrest', 'artillery', 'assist', 'astronaut', 'astronomy', 'asylum', 'atmosphere', 'attach', 'attack', 'attempt', 'attend', 'attention', 'automobile', 'autumn', 'available', 'average', 'avoid', 'awake', 'award', 'balance', 'balloon', 'ballot', 'barrier', 'battle', 'behavior', 'behind', 'biology', 'blind', 'boycott', 'brain', 'brave', 'bread', 'break', 'breathe', 'bridge', 'brief', 'bright', 'bring', 'broadcast', 'brother', 'brown', 'budget', 'build', 'building', 'bullet', 'burst', 'business', 'cabinet', 'camera', 'campaign', 'cancel', 'cancer', 'candidate', 'capital', 'capture', 'career', 'careful', 'carry', 'catch', 'cause', 'ceasefire', 'celebrate', 'center', 'century', 'ceremony', 'chairman', 'champion', 'chance', 'change', 'charge', 'chase', 'cheat', 'cheer', 'chemicals', 'chemistry', 'chief', 'child', 'children', 'choose', 'circle', 'citizen', 'civilian', 'civil', 'rights', 'claim', 'clash', 'class', 'clean', 'clear', 'clergy', 'climate', 'climb', 'clock', 'close', 'cloth', 'clothes', 'cloud', 'coalition', 'coast', 'coffee', 'collapse', 'collect', 'college', 'colony', 'color', 'combine', 'command', 'comment', 'committee', 'common', 'communicate', 'community', 'company', 'compare', 'compete', 'complete', 'complex', 'compromise', 'computer', 'concern', 'condemn', 'condition', 'conference', 'confirm', 'conflict', 'congratulate', 'Congress', 'connect', 'conservative', 'consider', 'constitution', 'contact', 'contain', 'container', 'continent', 'continue', 'control', 'convention', 'cooperate', 'correct', 'corruption', 'cotton', 'count', 'country', 'court', 'cover', 'crash', 'create', 'creature', 'credit', 'crime', 'criminal', 'crisis', 'criticize', 'crops', 'cross', 'crowd', 'crush', 'culture', 'curfew', 'current', 'custom', 'customs', 'damage', 'dance', 'danger', 'daughter', 'debate', 'decide', 'declare', 'decrease', 'defeat', 'defend', 'deficit', 'define', 'degree', 'delay', 'delegate', 'demand', 'democracy', 'demonstrate', 'denounce', 'depend', 'deplore', 'deploy', 'depression', 'describe', 'desert', 'design', 'desire', 'destroy', 'detail', 'detain', 'develop', 'device', 'dictator', 'different', 'difficult', 'dinner', 'diplomat', 'direct', 'direction', 'disappear', 'disarm', 'disaster', 'discover', 'discrimination', 'discuss', 'disease', 'dismiss', 'dispute', 'dissident', 'distance', 'divide', 'doctor', 'document', 'dollar', 'donate', 'double', 'dream', 'drink', 'drive', 'drown', 'during', 'early', 'earth', 'earthquake', 'ecology', 'economy', 'education', 'effect', 'effort', 'either', 'elect', 'electricity', 'embassy', 'embryo', 'emergency', 'emotion', 'employ', 'empty', 'enemy', 'energy', 'enforce', 'engine', 'engineer', 'enjoy', 'enough', 'enter', 'environment', 'equal', 'equipment', 'escape', 'especially', 'establish', 'estimate', 'ethnic', 'evaporate', 'event', 'every', 'evidence', 'exact', 'examine', 'example', 'excellent', 'except', 'exchange', 'excuse', 'execute', 'exercise', 'exile', 'exist', 'expand', 'expect', 'expel', 'experience', 'experiment', 'expert', 'explain', 'explode', 'explore', 'export', 'express', 'extend', 'extra', 'extraordinary', 'extreme', 'extremist', 'factory', 'false', 'family', 'famous', 'father', 'favorite', 'federal', 'female', 'fence', 'fertile', 'field', 'fierce', 'fight', 'final', 'financial', 'finish', 'fireworks', 'first', 'float', 'flood', 'floor', 'flower', 'fluid', 'follow', 'force', 'foreign', 'forest', 'forget', 'forgive', 'former', 'forward', 'freedom', 'freeze', 'fresh', 'friend', 'frighten', 'front', 'fruit', 'funeral', 'future', 'gather', 'general', 'generation', 'genocide', 'gentle', 'glass', 'goods', 'govern', 'government', 'grain', 'grass', 'great', 'green', 'grind', 'ground', 'group', 'guarantee', 'guard', 'guerrilla', 'guide', 'guilty', 'happen', 'happy', 'harvest', 'headquarters', 'health', 'heavy', 'helicopter', 'hijack', 'history', 'holiday', 'honest', 'honor', 'horrible', 'horse', 'hospital', 'hostage', 'hostile', 'hotel', 'house', 'however', 'human', 'humor', 'hunger',  'husband', 'identify', 'ignore', 'illegal','independent', 'individual', 'industry', 'infect', 'inflation', 'influence', 'inform', 'information', 'inject', 'injure', 'innocent', 'insane', 'insect', 'inspect', 'instead', 'instrument', 'insult', 'intelligence', 'intelligent', 'intense', 'interest', 'interfere', 'international', 'Internet', 'intervene', 'invade', 'invent', 'invest', 'investigate', 'invite', 'involve', 'island', 'issue', 'jewel', 'joint', 'judge', 'justice',  'knowledge',  'laboratory', 'language', 'large', 'laugh', 'launch', 'learn', 'leave', 'legal', 'legislature', 'letter', 'level', 'liberal', 'light', 'lightning', 'limit', 'liquid', 'listen', 'literature', 'little', 'local', 'lonely', 'loyal', 'machine', 'magazine', 'major', 'majority', 'manufacture', 'march', 'market', 'marry', 'material', 'mathematics', 'matter', 'mayor', 'measure', 'media', 'medicine', 'member', 'memorial', 'memory', 'mental', 'message', 'metal', 'method', 'microscope', 'middle', 'militant', 'military', 'militia', 'mineral', 'minister', 'minor', 'minority', 'minute', 'missile', 'missing', 'mistake', 'model', 'moderate', 'modern', 'money', 'month', 'moral', 'morning', 'mother', 'motion', 'mountain', 'mourn', 'movement', 'movie', 'murder', 'music', 'mystery', 'narrow', 'nation', 'native', 'natural', 'nature', 'necessary', 'negotiate', 'neighbor', 'neither', 'neutral', 'never', 'night', 'noise', 'nominate', 'normal', 'north', 'nothing', 'nowhere', 'nuclear', 'object', 'observe', 'occupy', 'ocean', 'offensive', 'offer', 'office', 'officer', 'official', 'often', 'operate', 'opinion', 'oppose', 'opposite', 'oppress', 'orbit', 'organize', 'overthrow', 'paint', 'paper', 'parachute', 'parade', 'pardon', 'parent', 'parliament', 'partner', 'party', 'passenger', 'passport', 'patient',  'people', 'percent', 'perfect', 'perform', 'period', 'permanent', 'permit', 'person', 'persuade', 'physical', 'physics', 'picture', 'pilot', 'planet', 'plant', 'plastic', 'please', 'plenty', 'point', 'poison', 'police', 'policy', 'politics', 'pollute', 'popular', 'population', 'position', 'possess', 'possible', 'postpone', 'poverty', 'power', 'praise', 'predict', 'pregnant', 'present', 'president', 'press', 'pressure', 'prevent', 'price', 'prison', 'private', 'prize', 'probably', 'problem', 'process', 'produce', 'profession', 'professor', 'profit', 'program', 'progress', 'project', 'promise', 'propaganda', 'property', 'propose', 'protect', 'protest', 'prove', 'provide', 'public', 'publication', 'publish', 'punish', 'purchase', 'question', 'quick', 'quiet', 'radar', 'radiation', 'radio', 'railroad', 'raise', 'reach', 'react', 'ready', 'realistic', 'reason', 'reasonable', 'rebel', 'receive', 'recent', 'recession', 'recognize', 'record', 'recover', 'reduce', 'reform', 'refugee', 'refuse', 'register', 'regret', 'reject', 'relations', 'release', 'religion', 'remain', 'remains', 'remember', 'remove', 'repair', 'repeat', 'report', 'represent', 'repress', 'request', 'require', 'rescue', 'research', 'resign', 'resist', 'resolution', 'resource', 'respect', 'responsible', 'restaurant', 'restrain', 'restrict', 'result', 'retire', 'return', 'revolt', 'right', 'river', 'rocket', 'rough', 'round', 'rubber', 'rural', 'sabotage', 'sacrifice', 'sailor', 'satellite', 'satisfy', 'school', 'science', 'search', 'season', 'second', 'secret', 'security', 'seeking', 'seize', 'Senate', 'sense', 'sentence', 'separate', 'series', 'serious', 'serve', 'service', 'settle', 'several', 'severe', 'shake', 'shape', 'share', 'sharp', 'sheep', 'shell', 'shelter', 'shine', 'shock', 'shoot', 'short', 'should', 'shout', 'shrink', 'sickness', 'signal', 'silence', 'silver', 'similar', 'simple', 'since', 'single', 'sister', 'situation', 'skeleton', 'skill', 'slave', 'sleep', 'slide', 'small', 'smash','smoke', 'smooth', 'social', 'soldier', 'solid', 'solve', 'sound', 'south', 'space', 'speak', 'special', 'speech', 'split', 'sport', 'spread', 'spring', 'square', 'stand', 'start', 'starve', 'state', 'station', 'statue', 'steal', 'steam', 'steel', 'stick', 'stone', 'store', 'storm', 'story', 'stove', 'straight', 'strange', 'street', 'stretch', 'strike', 'strong', 'structure', 'struggle',   'submarine', 'substance', 'substitute', 'subversion', 'succeed', 'sudden', 'suffer', 'sugar', 'suggest', 'suicide', 'summer', 'supervise', 'support', 'surprise', 'surrender', 'survive', 'suspect', 'suspend', 'swallow', 'swear', 'sweet', 'sympathy', 'system', 'target', 'taste', 'teach', 'technical', 'technology', 'telephone', 'telescope', 'television', 'temperature', 'temporary', 'tense', 'terrible', 'territory', 'terror', 'terrorist', 'thank', 'theater', 'theory', 'there', 'these', 'thick', 'thing', 'think', 'third', 'threaten', 'through', 'throw', 'tired', 'today', 'together', 'tomorrow', 'tonight', 'torture','tradition', 'traffic', 'tragic', 'train', 'transport', 'transportation', 'travel', 'treason', 'treasure', 'treat', 'treatment', 'treaty', 'trial', 'tribe', 'trick', 'troops', 'trouble', 'truce', 'truck', 'understand', 'unite', 'universe', 'university', 'unless', 'until', 'urgent', 'usual', 'vacation', 'vaccine', 'valley', 'value', 'vegetable', 'vehicle', 'version', 'victim', 'victory', 'video', 'village', 'violate', 'violence', 'visit', 'voice', 'volcano', 'volunteer', 'wages', 'waste', 'watch', 'water', 'wealth', 'weapon', 'weather', 'welcome', 'wheel', 'window', 'winter', 'withdraw', 'witness', 'wonderful', 'world','wreckage','yesterday']
word_list=[x.upper() for x in words]
# Hangman stages images (will be placeholder for drawing parts)
hangman_stages = [
    ''' 
      +---+
          |
          |
          |
         ===
    ''',
    ''' 
      +---+
      O   |
          |
          |
         ===
    ''',
    ''' 
      +---+
      O   |
      |   |
          |
         ===
    ''',
    ''' 
      +---+
      O   |
     /|   |
          |
         ===
    ''',
    ''' 
      +---+
      O   |
     /|\\  |
          |
         ===
    ''',
    ''' 
      +---+
      O   |
     /|\\  |
     /    |
         ===
    ''',
    ''' 
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    '''
]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry('650x700')
        self.root.config(bg='#f0f7f7')
        
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Title label
        title = tk.Label(self.root, text="Hangman Game", font=('Courier', 24, 'bold'), bg='#f7f7f7', fg='#333')
        title.pack(pady=20)

        # Hangman display area
        self.hangman_canvas = tk.Canvas(self.root, width=400, height=200, bg='#f7f7f7', bd=0, highlightthickness=0)
        self.hangman_canvas.pack(pady=20)

        # Word display area
        self.word_display = tk.Label(self.root, text="", font=('Helvetica', 20, 'bold'), bg='#f7f7f7')
        self.word_display.pack(pady=10)

        # Entry for letter guess
        self.guess_entry = tk.Entry(self.root, font=('Helvetica', 16), width=5)
        self.guess_entry.pack(pady=10)
        
        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, font=('Helvetica', 16), bg='#333', fg='#fff')
        self.guess_button.pack(pady=10)

        # Lives and score
        self.status_label = tk.Label(self.root, text="", font=('Helvetica', 16), bg='#f7f7f7', fg='#333')
        self.status_label.pack(pady=20)

        # Reset button
        reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=('Helvetica', 16), bg='#555', fg='#fff')
        reset_button.pack(pady=20)

    def reset_game(self):
        self.word = random.choice(word_list)
        print(self.word)
        self.word_display.config(text="_ " * len(self.word))
        self.guessed_word = ['_' for _ in self.word]
        self.lives = 6
        self.update_hangman()
        self.status_label.config(text=f"Lives: {self.lives}")

    def check_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a valid letter.")
            return

        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[idx] = guess
            self.word_display.config(text=" ".join(self.guessed_word))
        else:
            self.lives -= 1

        self.update_hangman()

        if "_" not in self.guessed_word:
            self.end_game("🎉🎊 Congratulations! 🎊🎉, You Win!")

        elif self.lives == 0:
            self.end_game(f"Game Over😿! The word was {self.word}.")

    def update_hangman(self):
        # Update the hangman drawing and lives left
        self.hangman_canvas.delete("all")
        self.hangman_canvas.create_text(200, 100, text=hangman_stages[6 - self.lives], font=('Courier', 20), fill='#333')
        self.status_label.config(text=f"Lives: {self.lives}")

    def end_game(self, message):
        # Clear the canvas and display the celebration message
        self.hangman_canvas.delete("all")
        self.hangman_canvas.create_text(200, 100, text=message, font=('Helvetica', 14, 'bold'), fill='green')
        
        # Change the background color
        self.root.config(bg='#d1ffd1')

        # Reset the game after a 4 seconds
        self.root.after(4000, self.reset_game) 

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()