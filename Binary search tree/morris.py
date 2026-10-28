def morris_inorder(root):
    result = []
    cur = root

    while cur:
        if not cur.left:
            # No left subtree: visit and go right
            result.append(cur.val)
            cur = cur.right
        else:
            # Find inorder predecessor (rightmost in left subtree)
            pred = cur.left
            while pred.right and pred.right is not cur:
                pred = pred.right

            if pred.right is None:
                # First time here: create thread, go left
                pred.right = cur
                cur = cur.left
            else:
                # Thread exists: left subtree is done
                pred.right = None      # remove thread
                result.append(cur.val) # visit
                cur = cur.right
    return result






def morris_preorder(root):
    result, cur = [], root
    while cur:
        if not cur.left:
            result.append(cur.val)
            cur = cur.right
        else:
            pred = cur.left
            while pred.right and pred.right is not cur:
                pred = pred.right
            if pred.right is None:
                result.append(cur.val)   # visit on first arrival
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                cur = cur.right
    return result
