
import pexpect

child = pexpect.spawn("echo myworld")

print(child.expect(["Hello","welcome", "Myworld"]))

