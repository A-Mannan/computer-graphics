import os
import subprocess
import sys

lIBRARIES = [
    "lGL",
    "lGLU",
    "lglut",
    "lglfw",
    "lXrandr",
    "lXxf86vm",
    "lXi",
    "lXinerama",
    "lX11",
    "lrt",
    "ldl",
    "lSDL2",
    "lSDL2_mixer",
]


def compile_and_execute_cpp_file(file_path):
    file_name = os.path.splitext(file_path)[0]
    executable_name = f"./{file_name}"
    command = f"g++ {file_path} -o {executable_name} {' '.join(['-' + lib for lib in lIBRARIES])}"

    try:
        subprocess.run(command, shell=True, check=True)
        subprocess.run(executable_name, shell=True, check=True)
        os.remove(executable_name)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")


def main():
    if len(sys.argv) < 2:
        print("Please provide the filename as a command-line argument.")
        sys.exit(1)

    cpp_file_path = sys.argv[1]
    compile_and_execute_cpp_file(cpp_file_path)


if __name__ == "__main__":
    main()
