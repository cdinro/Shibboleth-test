from subprocess import PIPE, Popen
import re

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def geturl(url, Flag=False):
        cmd = "curl -kv -s \"%s\" 2>&1" % url
        out = cmdline(cmd)
        if Flag:
                urls = re.findall(r'href=[\'"]?([^\'" >]+)', out)
                return urls[0]
        else:
                m = re.search("< Location: (.+?)\n", out)
                return m.group(1).strip()


idp1 = geturl("https://your_service_provider.com/secure", True)
idp2 = geturl(idp1)
out = cmdline("curl -s -kv -d \"j_username=test1&j_password=qwe123&_eventId_proceed=submit\" \"%s\" 2>&1" % idp2)

if out.find("SAMLResponse"):
        print "Success"
else:
        print "Failure"
