#!/usr/bin/env python

import os, optparse, re, subprocess

class StackFrame():
    def __init__(self, inputLine = None, address = None, filename = None, sourceLineNum = None, sourceCode = None):
        self.inputLine = inputLine
        self.address = address
        self.filename = filename
        self.sourceLineNum = sourceLineNum
        self.sourceCode = sourceCode

def Main():
    parser = optparse.OptionParser()
    
    parser.add_option('-c', '--callstack', dest = 'callstack', metavar = 'CALLSTACK', help = 'use CALLSTACK as the name of the callstack file')
    parser.add_option('-l', '--libfile',   dest = 'libfile',   metavar = 'LIBFILE',   help = r'use LIBFILE for symbols e.g. libunity.sym.so')
    #parser.add_option('-s', '--source',    dest = 'source',    metavar = 'SOURCE',    help = r'use SOURCE directory for Unity source code e.g. f:\dev\pluto\unity ')
    (options, args) = parser.parse_args()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
        
    if options.callstack == None or options.libfile == None:
        parser.print_help()
        return 1
    
    # Now open the file with the callstack
    lines = open(options.callstack, 'rt').read().splitlines()

    regexpList = []
    regexpList.append(re.compile(r'at lib[a-z]+\.0x((?:[0-9a-f]+))',        re.I)) # Match text like "at libunity.0x3c2ca4(Native Method)"
    regexpList.append(re.compile(r'at lib[a-z]+\.((?:[0-9a-f]+))',          re.I)) # Match text like "at libunity.003c2ca4(Native Method)"
    regexpList.append(re.compile(r'lib[a-z]+\.so\s+\+\s+0x((?:[0-9a-f]+))', re.I)) # Match text like "libunity.so + 0x396b3c"
    regexpList.append(re.compile(r'\s*#[0-9]+\s+pc\s+((?:[0-9a-f]+))',      re.I)) # Match text like "#03 pc 003d4530"
    regexpList.append(re.compile(r'\d+\s+lib[a-z]+\.((?:[0-9a-f]+))',       re.I)) # Match text like "1       libunity.006da5d0"
    
    # This stackList array will eventually contain 0:line number in input file, 1:code address, 2:Code info
    stackList = []
    
    # Find hex addresses on the input
    for i in range(0, len(lines)):
        line = lines[i]
        match = None
        if not 'libunity.' in line:
            continue

        for regexp in regexpList:
            match = regexp.search(line)
            if match:
                break
        
        if match:
            address = int(match.group(1), 16)
            stackList.append(StackFrame(i, address))
    
    # Run these addresses through the addr2line tool:
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    addr2line = os.path.join(scriptDir, 'tools', 'msys32', 'bin', 'addr2line.exe')
    args = [addr2line, '-C', '-f', '-p', '-e', options.libfile]
    for s in stackList:
        args += ['{:x}'.format(s.address)]
    output = ''
    if len(stackList) > 0:
        output = GetOutput(args, echo = False)
    codeinfo = output.splitlines()
    
    for i in range(0, len(codeinfo)):
        stackList[i].sourceCode = codeinfo[i]


    # Add the extra information onto the input lines:
    for stack in stackList:
        i = stack.inputLine
        if stack.sourceCode != None:
            lines[i] += ' ' + stack.sourceCode.strip()
    
    # Finally output all of the new annotated lines:
    for line in lines:
        print(line)
    
    return 0

# Run a command using subprocess and get the output
def GetOutput(args, cwd = None, echo = True):
    if echo:
        if cwd != None:
            print('GetOutput: ' + subprocess.list2cmdline(args) + ' in ' + cwd)
        else:
            print('GetOutput: ' + subprocess.list2cmdline(args))

    stdout, stderr = subprocess.Popen(args, stdout = subprocess.PIPE, cwd = cwd).communicate()
    return stdout

if __name__ == '__main__':
    exit(Main())
