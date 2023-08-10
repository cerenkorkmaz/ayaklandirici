import os,sys
import subprocess
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    paths = []

    for path_element in root.findall(".//Path"):
        path = path_element.text
        paths.append(path)

    return paths

def parse_file_path(file_path):
    directory_path, file_name = os.path.split(file_path)
    return directory_path, file_name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("bat dosyasında .xml verildiğine emin olun")
        sys.exit(1)

    print("AYAKLANDIRICI ÇALIŞTI")
        
    xml_file = sys.argv[1]
    paths = parse_xml(xml_file)

    dirs = []
    files = []
    for i in range (len(paths)):
        mDir , mFile = parse_file_path(paths[i])
        dirs.append(mDir)
        files.append(mFile)

    pids=[]
    for i in range (len(paths)):
        try:
            os.chdir(dirs[i])
            if files[i].endswith('.bat'):
                pids.append(subprocess.Popen(files[i], creationflags=subprocess.CREATE_NEW_CONSOLE).pid)
            else:
                pids.append(subprocess.Popen(files[i]).pid)
        except:
            print("Yanlış ya da eksik dosya yolu: " + files[i])

    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)

    argv = " ".join(str(item) for item in pids)    
    subprocess.run(["python" , "Terminator.py"] + [argv], creationflags=subprocess.CREATE_NO_WINDOW)

