import subprocess

folder_path= input("Listelemek istediğiniz klasör yolunu girin: ")


result= subprocess.run(["ls", folder_path], capture_output=True, text=True)

print("Output: " , result.stdout)
print("Error: ", result.stderr)