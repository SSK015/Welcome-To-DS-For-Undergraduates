
import threading
import time


def run(instream):
    file = open(instream)
    write1 = open('shuffle01', 'a')
    write2 = open('shuffle02', 'a')
    write3 = open('shuffle03', 'a')
    for line in file:
        line = line.strip()
        word, count = line.split(',', 1)
        bucket = hash(word) % 3 # 使用哈希算法得到bucket编号
        if bucket == 0:
            write1.write("{},{}\n".format(word, count))
        elif bucket == 1:
            write2.write("{},{}\n".format(word, count))
        else:
            write3.write("{},{}\n".format(word, count))


if __name__ == '__main__':
    start = time.perf_counter()
    t1 = threading.Thread(target=run('map01'), args=("t1",))
    t2 = threading.Thread(target=run('map02'), args=("t2",))
    t3 = threading.Thread(target=run('map03'), args=("t3",))
    t4 = threading.Thread(target=run('map04'), args=("t4",))
    t5 = threading.Thread(target=run('map05'), args=("t5",))
    t6 = threading.Thread(target=run('map06'), args=("t6",))
    t7 = threading.Thread(target=run('map07'), args=("t7",))
    t8 = threading.Thread(target=run('map08'), args=("t8",))
    t9 = threading.Thread(target=run('map09'), args=("t9",))
    # start = time.perf_counter()
    # t1 = threading.Thread(target=run('combiner1'), args=("t1",))
    # t2 = threading.Thread(target=run('combiner2'), args=("t2",))
    # t3 = threading.Thread(target=run('combiner3'), args=("t3",))
    # t4 = threading.Thread(target=run('combiner4'), args=("t4",))
    # t5 = threading.Thread(target=run('combiner5'), args=("t5",))
    # t6 = threading.Thread(target=run('combiner6'), args=("t6",))
    # t7 = threading.Thread(target=run('combiner7'), args=("t7",))
    # t8 = threading.Thread(target=run('combiner8'), args=("t8",))
    # t9 = threading.Thread(target=run('combiner9'), args=("t9",))
    # start = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

    t1.join()
    print("t1 cost %s s" % (time.perf_counter() - start))
    t2.join()
    print("t2 cost %s s" % (time.perf_counter() - start))
    t3.join()
    print("t3 cost %s s" % (time.perf_counter() - start))
    t4.join()
    print("t4 cost %s s" % (time.perf_counter() - start))
    t5.join()
    print("t5 cost %s s" % (time.perf_counter() - start))
    t6.join()
    print("t6 cost %s s" % (time.perf_counter() - start))
    t7.join()
    print("t7 cost %s s" % (time.perf_counter() - start))
    t8.join()
    print("t8 cost %s s" % (time.perf_counter() - start))
    t9.join()
    print("t9 cost %s s" % (time.perf_counter() - start))
