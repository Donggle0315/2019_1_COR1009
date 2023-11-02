def makeTree(treeInfo):
    dictTree = {}
    for i in range(1, len(treeInfo) - 1):
        if dictTree.get(treeInfo[i]) is not None:
            dictTree[treeInfo[i]].append(i)
        else:
            dictTree[treeInfo[i]] = [i]
    return dictTree

def findParent(nid, dictTree):
    parent = -1
    for i in dictTree:
        if nid in dictTree[i]:
            parent = i
            break
    return parent

nodebase = [-1, 0, 1, 1, 2, 2, 2]
node = makeTree(nodebase)
print("7개의 노드가 존재하는 트리입니다.")
print()
while True:
    nodeinput = input("노드 번호 입력: ")
    nodeinput = int(nodeinput)
    if nodeinput < 0:
        print()
        print("***** 프로그램 종료")
        break
    elif nodeinput == 0:
        print("노드 번호 0은 부모 노드가 없는 루트 노드입니다.")
    else:
        print("노드 번호 {}의 부모 노드 번호는 {}입니다.".format(nodeinput, findParent(nodeinput, node)))
    print()

    
