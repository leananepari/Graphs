import random
from util import Stack, Queue 

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        total = num_users * avg_friendships / 2
        # Add users
        for i in range(0, 10):
          self.add_user('name')
        # Create friendships
        while total > 0:
          user = random.randint(1, num_users - 1)
          friend = random.randint(1, num_users - 1)
          if user != friend and friend not in self.friendships[user] and user not in self.friendships[friend]:
            self.add_friendship(user, friend)
            total -= 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        queue = Queue()

        queue.enqueue(user_id)

        while queue.size() > 0:
          vertex = queue.dequeue()

          if vertex not in visited:

            if vertex == user_id:
              visited[vertex] = [vertex]
            elif user_id in self.friendships[vertex] and vertex not in visited:
              visited[vertex] = [user_id, vertex]
            else:
              connections = self.friendships[vertex]
              path = []
              for c in connections:
                if c in visited:
                  if len(path) == 0:
                    path = visited[c].copy()
                  else:
                    if len(path) > len(visited[c]):
                      path = visited[c].copy()
              path.append(vertex)
              copy = path.copy()
              visited[vertex] = copy
              path = []

            for next_vert in self.friendships[vertex]:
                queue.enqueue(next_vert)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    # s = set()
    # s.add(5)
    # s.add(7)
    # s.add(8)
    # for i in s:
    #   print(i)
 