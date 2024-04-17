
from rich.console import Console
import subprocess
import os

console = Console()
root = "/kaggle/working/"

output_tar = os.path.join(root, output_name) + ".tar"
compressed_output = output_tar + ".lz4"

with open(output_tar, 'w'):  
    pass

asd = [
    (f"tar -cvf {output_tar} -C {root} {directory}", "Archiving Folder"),
    (f"lz4 {output_tar} {compressed_output}", "Compressing Archive")
]

with console.status(f"[bold green]Compressing...") as status:
    try:
        for command, description in asd:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    console.log(f"[bold blue]{description}[/] completed")
                else:
                    console.log(f"[bold red]Failed[/] to [bold blue]{description}[/]\nError log:\n{result.stderr}")
        os.remove(output_tar)        
    except:
            print("gayass there's an error")

print(f"Compression Success. \n{compressed_output}")