import rocktree_server

server = rocktree_server.RockTreeServer("data", 10)
server.spawn_server(("localhost", 3434))
