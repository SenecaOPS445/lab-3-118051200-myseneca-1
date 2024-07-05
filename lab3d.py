#!/usr/bin/env python3

# Author ID: 118051200

'''
import subprocess


def free_space():
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(['awk', '{print $4}'], stdin=grep_process.stdout, stdout=subprocess.PIPE)
    awk_output, _ = awk_process.communicate()

    # Decode the output from bytes to string and strip any leading or trailing whitespace
    decoded_output = awk_output.decode('utf-8').strip()

    # Print the formatted output
    print(decoded_output)

if __name__ == '__main__':
    free_space()

    '''


import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p_grep = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p_awk = subprocess.Popen(['awk', '{print $4}'], stdin=p_grep.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Communicate with the process and get the retrieve its output (stdout)
    output = p_awk.communicate()

    # Convert stdout to a string and strip off the newline characters
    return output[0].strip()


if __name__ == '__main__':
    print(free_space())