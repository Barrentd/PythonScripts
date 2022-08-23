
from ast import main
import shutil
import os
import zipfile
import re

def extract_file( zf, info, extract_dir ):
    zf.extract( info.filename, path=extract_dir )
    print(info.external_attr)

def compress_file(output_dir):
    with zipfile.ZipFile(output_dir+'.zip', mode="w") as archive:
        for file in os.listdir(output_dir):
            if os.path.isfile(os.path.join(output_dir, file)):
                print("file",file)
                archive.write(os.path.join(output_dir, file),file)
            else:
                print("none", file)
                for root, dirs, files in os.walk(str(output_dir)+'/'+str(file)):
                    for file in files:
                        fold = re.sub('^.*\/', '', root)
                        archive.write(os.path.join(root, file),fold+'/'+file)
                    for directory in dirs:
                        fold = re.sub('^.*\/', '', root)
                        archive.write(os.path.join(root, directory),fold)

def main():

    num = 1
    zip = '654a8f6b-a13f-4091-88e9-20433fe0ab00.zip'
    output_dir = str(num)+'654a8f6b-a13f-4091-88e9-20433fe0ab00'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with zipfile.ZipFile(zip, 'r') as zf:
        for info in zf.infolist():
            print("info",info)
            extract_file( zf, info, output_dir )

    for file in os.listdir(output_dir):
        if os.path.isfile(os.path.join(output_dir, file)):
            src= str(output_dir)+'/'+str(file)
            dst = str(output_dir)+'/'+str(num)+str(file)
            shutil.copyfile(src, dst)
            os.remove(str(output_dir)+'/'+str(file))

    compress_file(output_dir)
    shutil.rmtree(output_dir)


if __name__ == "__main__":
    main()