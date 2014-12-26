from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR

# run the shell as a subprocess:
p = Popen("java -cp /home/rostunov/workspace/malt_wrapper/malt.jar org.maltparser.server.Main", shell=True, stdin=PIPE, stdout=PIPE, stderr = PIPE)
# p = Popen(['python', 'shell.py'],
#         stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
# wrap p.stdout with a NonBlockingStreamReader object:
nbsr = NBSR(p.stdout)
# issue command:
p.stdin.write('command\n'.encode('utf-8'))
# get the output
while True:
    output = nbsr.readline(0.1)
    # 0.1 secs to let the shell output the result
    if not output:
        print ('[No more data]')
        break
    print (output)


# for i in range(0,100):
#     p.stdin.write('command\n'.encode('utf-8'))
#     # get the output
#     while True:
#         output = nbsr.readline(0.1)
#         # 0.1 secs to let the shell output the result
#         if not output:
#             print ('[No more data]')
#             break
#         print (output)
#     i=i+1