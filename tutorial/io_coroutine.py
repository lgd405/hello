#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = ''
    while True:
        n = yield r
        if not n :
            r = '...[CONSUMER] DO Noting ...'
            return
        n = n*n
        print('....[CONSUMER] Consuming %s...' % n)

        # if n != 4 :
        #    r = '...[CONSUMER] do nothing...'
        #    return
        
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)