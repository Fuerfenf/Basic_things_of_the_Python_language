"""
this code explain how recursive search in tree info by tag
"""

html_dom = {
    'html': {
        'head': {
            'title': 'title first'
        },
        'body': {
            'h2': 'h2 tag',
            'div': 'div block',
            'p': 'paragraph block',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, tree_sub in tree.items():
        if isinstance(tree_sub, dict):
            result = find_element(tree=tree_sub, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result


result_out = find_element(tree=html_dom, element_name='head')
print(result_out)