#!/usr/bin/python3
"""HandyHaversacks.py
    Author: Bissallah Ekele - bAe
    Date: 06/09/2021
    Description: Processing colored luggages.
"""
import re

class Color_Tree:
    "Tree of colored bags."    
    
    head = None
    tail = None

    def __init__(self):
        """Default Cstr."""
        # Sentinels
        Color_Tree.head = Color_Tree.Color_Node()
        Color_Tree.tail = Color_Tree.Color_Node()

        Color_Tree.head.children.append(Color_Tree.tail)
        Color_Tree.tail.children.append(Color_Tree.head)

    # TODO: Make scope private
    def get_child_nodes(self, children):
        """Extract child-node properties."""
        child_nodes = []
        for child in children:
            child_weight = child[0:1]
            child_color = child[2:-4]
            child_node = self.Color_Node(child_color, child_weight)
            child_nodes.append(child_node)

        return child_nodes

    def insert(self, parent_color, children):
        """Create node of parent and children and place in tree if root,
            Link child nodes to parent if not root.
        """
        parent_found = False
        
        child_nodes = self.get_child_nodes(children)

        # if sentinel has no child
        if Color_Tree.tail in Color_Tree.head.children:
            parent_found = True
            Color_Tree.head.children.remove(Color_Tree.tail)
            new_root = self.Color_Node.from_node_with_children(parent_color, 1, child_nodes)
            new_root.parent = Color_Tree.head
            Color_Tree.head.children.append(new_root)
            Color_Tree.tail.children.remove(Color_Tree.head)
            for child_node in new_root.children:
                child_node.parent = new_root
                Color_Tree.tail.children.append(child_node)
        else:
            # Search for parent (Breadth First Search - Level Order Traversal)
            queue = [Color_Tree.head]
            while queue:
                curr = queue.pop(0)
                # if parent present, place new-children at all found-leaves
                if curr.color == parent_color:
                    parent_found = True
                    curr.children = self.get_child_nodes(children)
                    for node in curr.children:
                        node.parent = curr
                    if curr in Color_Tree.tail.children and child_nodes:
                        Color_Tree.tail.children.remove(curr)
                        for node in curr.children:
                            Color_Tree.tail.children.append(node)
                    
                for child in curr.children:
                    queue.append(child)

        # if parent absent - another root node has been encountered
        # Make parent node with children
        # map head-sentinel to parent
        if not parent_found:
            parent_found = True
            new_root = self.Color_Node.from_node_with_children(parent_color, 1, child_nodes)
            new_root.parent = Color_Tree.head
            Color_Tree.head.children.append(new_root)
            for child_node in new_root.children:
                child_node.parent = new_root
                Color_Tree.tail.children.append(child_node)
        
        return Color_Tree.head

    def display(self):
        queue = [Color_Tree.head]
        print("Sentinel: {sentinel}".format(sentinel=Color_Tree.head))
        while queue:
            if Color_Tree.tail in queue:
                break
            curr = queue.pop(0)
            print("Parent: {parent_node} Children: [".format(parent_node=curr))
            for child in curr.children:
                print("{child_node}".format(child_node=child))
                queue.append(child)
            print("]")

    def count_parents(self, bag_color):
        # Psuedocode
        # Perform Tail-up Level-Order Traversal - BFS
        # If node-color in set
        # Place node-parent-color in set
        # return size of set
        
        queue = Color_Tree.tail.children
        found_bags = {bag_color,}
        while queue:
            curr = queue.pop(0)
            if  curr.parent.color:
                queue.append(curr.parent)
            if curr.color in found_bags and curr.parent.color:
                found_bags.add(curr.parent.color)
        print(found_bags)
        return len(found_bags) - 1



    class Color_Node:
        """A colored-bag node."""

        def __init__(self, color=None, weight=0):
            """Generic Cstr - Create new node without children."""
            self.parent = None
            self.color = color
            self.weight = weight
            self.children = []  

        @classmethod
        def from_node_with_children(cls, color, weight, child_nodes):
            """Generic Cstr - Create new node with children (before tail sentinel)."""
            new_node = cls(color, weight)
            new_node.children = child_nodes

            return new_node

        def __repr__(self):
            """Node string representation."""
            return "Node({color}, {weight})".format(color=self.color, weight=self.weight)
  

def build_color_tree(rules):
    color_tree = Color_Tree()
    parent_regex = r"[a-z\s]+contain"
    child_regex = r"\d[a-z\s]+bag"
    
    for rule in rules:
        parent = re.search(parent_regex, rule).group()
        parent_color = parent[:-13]
        children = re.findall(child_regex, rule)

        _ = color_tree.insert(parent_color, children)

    return color_tree

def main():
    test_input = r".\test_input.txt"
    puzzle_input = "puzzle_input.txt"

    file_name = test_input

    color_tree = None
    with open(file_name) as f:
        rules  = f.read().splitlines()
        color_tree = build_color_tree(rules)
    
    # color_tree.display()
    print(color_tree.count_parents("shiny gold"))

if __name__ == "__main__":
    main()