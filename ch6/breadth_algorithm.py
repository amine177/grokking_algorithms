from collections import deque


def person_is_seller(p):
    return p in ["claire", "thon", "jhonny"]


def search(g, s):

    search_queue = deque()
    search_queue += graph[s]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("{} is a mango seller".format(person))
                return True
            else:
                search_queue += g[person]
    return False


if __name__ == "__main__":

    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = ["you"]
    graph["thom"] = []
    graph["johnny"] = []

    search(graph, "you")
