#!/usr/bin/env python
import sys, os

def print_help():
    print 'Usage: %s GAE_SDK_PATH output.db'%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_help()
        sys.exit(-1)
    gae_path = os.path.expanduser(sys.argv[1])
    outfile = sys.argv[2]
    cmd = [sys.executable, os.path.join(gae_path, 'appcfg.py'),
            'download_data',
            '--application=s~teamplayquest',
            '--url=http://teamplayquest.appspot.com/_ah/remote_api',
            '--filename=%s'%outfile]
    os.execlp(cmd[0], *cmd)
