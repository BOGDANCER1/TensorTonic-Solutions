import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3

        self.id_to_word[0] = self.pad_token
        self.id_to_word[1] = self.unk_token
        self.id_to_word[2] = self.bos_token
        self.id_to_word[3] = self.eos_token
        
        uniques = set()

        for text in texts:
            words = text.split()
            uniques.update(words)

        for i, word in enumerate(uniques, start=4):
            self.word_to_id[word] = i
            self.id_to_word[i] = word

        self.vocab_size = len(self.word_to_id)
        
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        answer = []
        # answer.append(self.word_to_id[self.bos_token])

        for word in text.split():

            answer.append(self.word_to_id.get(word, self.word_to_id[self.unk_token]))
        
        # answer.append(self.word_to_id[self.eos_token])

        return answer

    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        output = []

        for id in ids:
                output.append(self.id_to_word.get(id, self.unk_token))

        return " ".join(output)
