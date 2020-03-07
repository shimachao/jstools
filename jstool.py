# js 代码反混淆工具

"""
Usage:
    js_tool dename (--infile <infilename>) [--outfile <outfilename>]

Options:
    -h,--help  输出帮助信息
    --version  查看版本
    -i --infile  指定输入文件
    -o --outfile  指定输出文件
"""

import re
import sys

from docopt import docopt

names = ['这里填入名称表']


def replace16(match) -> str:
    return f"'{names[int(match.group(1), 16)]}'"


def cli():
    args = docopt(__doc__)
    if args['dename']:
        handle_dename(args['<infilename>'], args['<outfilename>'])


def handle_dename(infile, outfile):
    in_fp = open(file=infile, mode="r", encoding="utf8")
    
    if outfile is None or len(outfile) == 0:
        out_fp = sys.stdout
    else:
        out_fp = open(file=outfile, mode='w', encoding='utf8')
    pattern = re.compile(r'names\[(0x[\dabcde]*)\]')
    
    out_fp.write(pattern.sub(repl=replace16, string=in_fp.read()))
    in_fp.close()
    if out_fp != sys.stdout:
        out_fp.close()


if __name__ == '__main__':
    cli()
