package main

type TrieNode struct {
	children map[rune]*TrieNode
	end      bool
}

func newTrieNode() *TrieNode {
	return &TrieNode{children: make(map[rune]*TrieNode)}
}

type Trie struct {
	root *TrieNode
}

func Constructor() Trie {
	return Trie{root: newTrieNode()}
}

func (t *Trie) Insert(word string) {
	curr := t.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			curr.children[c] = newTrieNode()
		}
		curr = curr.children[c]
	}
	curr.end = true
}

func (t *Trie) Search(word string) bool {
	curr := t.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}
	return curr.end
}

func (t *Trie) StartsWith(prefix string) bool {
	curr := t.root
	for _, c := range prefix {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}
	return true
}