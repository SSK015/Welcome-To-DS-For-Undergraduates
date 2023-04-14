import threading
import time


def run(readfile, writefile):
    file = open(readfile)
    write = open(writefile, 'w')
    count_dict = {}
    for line in file:
        line = line.strip()
        word, count = line.split(',', 1)
        try:
            count = int(count)
        except ValueError:
            continue
        if word in count_dict.keys():
            count_dict[word] = count_dict[word] + count
        else:
            count_dict[word] = count

    count_dict = sorted(count_dict.items(), key=lambda x: x[0], reverse=False)
    for key, v in count_dict:
        write.write("{},{}\n".format(key, v))


if __name__ == '__main__':
    start = time.perf_counter()
    t1 = threading.Thread(target=run('shuffle01', 'reduce01'), args=("t1",))
    t2 = threading.Thread(target=run('shuffle02', 'reduce02'), args=("t2",))
    t3 = threading.Thread(target=run('shuffle03', 'reduce03'), args=("t3",))
    # start = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    print("t1 cost %s s" % (time.perf_counter() - start))
    t2.join()
    print("t2 cost %s s" % (time.perf_counter() - start))
    t3.join()
    print("t3 cost %s s" % (time.perf_counter() - start))
