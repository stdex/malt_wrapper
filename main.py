from subprocess import Popen, PIPE
import errno
import sys

p1 = Popen("java -cp /home/rostunov/workspace/malt_wrapper/malt.jar org.maltparser.server.Main", shell=True, stdin=PIPE, stdout=PIPE)
print (p1.stdout.read())

p1.stdin.write("123")
result = p1.stdout.read()
print (result)
p1.wait()

p1.stdin.write("123")
result = p1.stdout.read()
print (result)
p1.wait()

# for x in range(100):
#     line = 'Line number %d.\n' % x
#     try:
#         p1.stdin.write(line)
#         print (p1.stdout.read())
#     except IOError as e:
#         if e.errno == errno.EPIPE or e.errno == errno.EINVAL:
#             # Stop loop on "Invalid pipe" or "Invalid argument".
#             # No sense in continuing with broken pipe.
#             break
#         else:
#             # Raise any other error.
#             raise

# while True:
#     inline = p.stdout.readline()
#     if not inline:
#         break
#
# sys.stdout.write(inline)
# sys.stdout.flush()

# subprocess_cmd = 'java -jar /home/rostunov/workspace/malt_wrapper/malt.jar -a covnonproj -c test123 -F /home/rostunov/workspace/neuro/malt_prj/malt/resource/data/convnonprd_small_with_outputcolumn.xml -l liblinear -lx /home/rostunov/workspace/neuro/maltparser/predict -if /home/rostunov/workspace/neuro/malt_prj/malt/resource/data/Roma_model.xml -i /home/rostunov/workspace/neuro/malt_prj/malt/resource/data/inp_Lc_Rc_test.csv -m parse -o out_test.txt -li true -cs true'
# proc = Popen(
#     subprocess_cmd,
#     stdout=PIPE, stderr=PIPE
# )
# proc.wait()
# res = proc.communicate()  # получить tuple('stdout res', 'stderr res')
# print(proc.stdout.read())
# if proc.returncode:
#     print (res[1])
# print ('result:', res[0])

