"""psit"""
import json
def node(node_map, node_first):
    """elegant"""
    node_can_links = run_node(node_map, [node_first], [node_first])
    print(sorted(set(node_can_links)))
 
def run_node(node_map, node_parent, node_can_links):
    """elegant"""
    while node_parent:
        node_child = [i for i in node_map[node_parent.pop()] if i not in node_can_links]
        node_can_links += node_child
        node_parent += node_child
    return node_can_links
 
node(json.loads(input().replace("'", '"')), input())
