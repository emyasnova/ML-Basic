from homework_04 import file_tools

# Create a file
file = file_tools.File("example.txt", 1024, "2023-01-01", "user")

# Create a cloud file
cloud_file = file_tools.FileCloud("example_cloud.txt", 1024, "2023-01-01", "user", "AWS")

# Create a server file
server_file = file_tools.FileServer("example_server.txt", 1024, "2023-01-01", "user", "localhost")

# Create a storage file
storage_file = file_tools.FileStorage("example_storage.txt", 1024, "2023-01-01", "user", "local")
