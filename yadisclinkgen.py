import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", required=False, action='store_true', help="test direct links whether they are valid")
args = parser.parse_args()

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    link='https://getfile.dokpub.com/yandex/get/'

    if os.path.exists('input.txt'):
        with open(input_file, 'r') as inputf, open(output_file, 'w') as outputf:
            f = 0
            for line in inputf.readlines():
                outputf.writelines(link+line)
                f+=1
            
        inputf.close()
        outputf.close()

        if args.test:
            test_links()

        print("============================")
        print("[SUCCESS] %i links generated" % f)
        print("============================")

    else:
        print("===========================")
        print("[ERROR] No input.txt found!")
        print("===========================")

def test_links():
    output_file = "output.txt"

    with open(output_file, 'r') as outputf:
        lines = [line.strip('\n') for line in outputf]
        for link in lines:
            response = requests.get(link)
            if response.status_code == 200:
                print(link, "\t [VALID LINK]")
            else:
                print(link, "\t [INVALID LINK]")
                    
    outputf.close()

if __name__ == "__main__":
    main()