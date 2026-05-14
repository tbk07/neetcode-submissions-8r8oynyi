type TrieNode struct {
    children map[rune]*TrieNode
    end      bool
}

func newTrieNode() *TrieNode {
    return &TrieNode{children: make(map[rune]*TrieNode)}
}

type PrefixTree struct {
    root *TrieNode
}

func Constructor() PrefixTree {
    return PrefixTree{root: newTrieNode()}
}

func (this *PrefixTree) Insert(word string) {
    curr := this.root
    for _, c := range word {
        if _, ok := curr.children[c]; !ok {
            curr.children[c] = newTrieNode()
        }
        curr = curr.children[c]
    }
    curr.end = true
}

func (this *PrefixTree) Search(word string) bool {
    curr := this.root
    for _, c := range word {
        if _, ok := curr.children[c]; !ok {
            return false
        }
        curr = curr.children[c]
    }
    return curr.end
}

func (this *PrefixTree) StartsWith(prefix string) bool {
    curr := this.root
    for _, c := range prefix {
        if _, ok := curr.children[c]; !ok {
            return false
        }
        curr = curr.children[c]
    }
    return true
}