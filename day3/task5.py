import os

def os_file_manager():
    """
         OS File Manager
    """
    while True:
        # Step 1: Ask user for a directory path
        directory = input("Enter a directory path: ").strip()

        # Step 2: Validate path
        if not os.path.isdir(directory):
            print(" Invalid directory. Try again.")
            continue

        # Step 3: Create "backup" folder if not exists
        backup_dir = os.path.join(directory, "backup")
        if not os.path.exists(backup_dir):
            os.mkdir(backup_dir)

        copied_count = 0

        # Step 4: Copy all .txt files into backup
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                src = os.path.join(directory, filename)
                dst = os.path.join(backup_dir, filename)

                # Copy manually (read + write)
                with open(src, "r") as src_file:
                    content = src_file.read()
                with open(dst, "w") as dst_file:
                    dst_file.write(content)

                copied_count += 1

