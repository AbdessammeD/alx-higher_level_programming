#!/usr/bin/python3
"""Module that reads a text file and prints it to stdout"""

def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as f:
        f.reads()
